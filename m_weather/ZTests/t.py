import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

print('django-apscheduler')

def job2(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name,time.strftime("%Y-%m-%d %H:%M:%S")))

# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")
# # 添加任务1
# # 每隔5s执行这个任务
# @register_job(scheduler,"interval", seconds=5,args=['王路'],id='job1')
# def job1(name):
#     # 具体要执行的代码
#     print('{} 任务运行成功！{}'.format(name,time.strftime("%Y-%m-%d %H:%M:%S")))

scheduler.add_job(job2,"interval",seconds=10,args=['王飞'],id="job2")


# 调度器开始运行
scheduler.start()