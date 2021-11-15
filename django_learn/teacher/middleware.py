from django.http import HttpResponseForbidden


def simple_middleware(get_response):  # 参数名不可更改
    print('初始化设置1')

    def middleware(request):
        # 只有谷歌浏览器才让访问
        user_agent = request.META['HTTP_USER_AGENT']
        if not 'chrome' in user_agent.lower():
            return HttpResponseForbidden()

        print("处理请求前执行的代码1")
        response = get_response(request)
        print("处理请求后执行的代码2")
        return response

    return middleware


class SimpleMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        print('初始化设置2')

    def __call__(self, request):
        print("处理请求前执行的代码3")
        response = self.get_response(request)
        print("处理请求后执行的代码4")
        return response

