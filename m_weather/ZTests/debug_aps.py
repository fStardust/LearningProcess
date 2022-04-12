# -*- coding: utf-8 -*-
import logging

import faust
import ujson
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

# 这里使用mongodb做为持久化任务存储
mongo_jobstore = MongoDBJobStore(
    database="apscheduler_job",
    collection="job",
    client=MongoClient("127.0.0.1", 27017)
)

init_scheduler_options = {
    "jobstores": {
        "default": mongo_jobstore  # 默认持久化存储器
    },
    "executors": {
        'default': ThreadPoolExecutor(20)  # 20个线程的线程池
    },
    "job_defaults": {
        'coalesce': False,  # 是否合并执行
        'max_instances': 3  # 最大实例数
    }
}
scheduler = BackgroundScheduler(**init_scheduler_options)
scheduler.start()

app = faust.App(
    'app_name',
    broker='kafka://{}'.format("127.0.0.1:9092"),
    topic_partitions=3,
)

test_app = app.topic("topic_name", value_serializer=ujson)


@app.agent(test_app)
async def testAgent(messages):
    async for message in messages:
        try:
            # flag 用于判断增、删、改操作
            flag = message.get("flag")
            # job_id 唯一标识，用于管理定时任务用
            job_id = message.get("job_id")
            if not flag or not job_id:
                continue
            # interval_time 这里用的时间间隔方式执行任务，这个是时间间隔的具体值
            interval_time = message.get("interval", 1)
            if flag == "add":
                # 新增任务
                if scheduler.get_job(job_id=job_id):
                    # 如果存在相同的ID任务，先删掉
                    scheduler.remove_job(job_id=job_id)
                # 添加任务
                scheduler.add_job(
                    func=task_func,  # 要执行的任务函数
                    trigger="interval",  # interval根据指定时间间隔执行定时任务
                    args=["arg1", "arg2"],  # task_func函数的参数
                    id=job_id,  # 任务ID，用于管理任务
                    misfire_grace_time=None,  # 当定时任务因为某些原因没能在指定时间执行时，通过这个参数觉得他是否还要执行
                    # 如果在应用程序初始化期间在持久作业存储中调度作业，则必须为该作业定义一个显式ID，并使用replace_existing=True，否则每次应用程序重新启动时都将获得该作业的新副本!
                    replace_existing=True,
                    minutes=interval_time,  # 指定几分钟执行一次
                )
            elif flag == "modify":
                # 修改任务
                # 通过这种方式修改好像有时会有问题，条件允许的话，可以像添加新任务那样，先把任务删了，再添加新的任务得了
                scheduler_trigger = scheduler._create_trigger(
                    trigger="interval",  # 指定新的执行任务方式，这里还是用的时间间隔
                    trigger_args={"minutes": interval_time}  # 多少分钟执行一次
                )
                scheduler.modify_job(
                    job_id=job_id,  # add_job时指定的job_id这里都是通过kafka读取的
                    trigger=scheduler_trigger,
                    args=["new_arg1", "new_arg2"],  # 函数参数在这里修改
                )
            elif flag == "remove":
                # 删除任务
                # job_id还是add_job添加的那个，这里都是通过kafka读取的
                scheduler.remove_job(job_id=job_id)
            else:
                logger.error(f"flag={flag}")
        except Exception as e:
            logger.error(e)
            continue


def task_func(arg1, arg2):
    # 定时任务的具体实现
    print(f"arg1 = {arg1}, arg2 = {arg2}")


if __name__ == "__main__":
    try:
        app.main()
    except:
        scheduler.shutdown()
