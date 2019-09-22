import datetime

from django.db.models import Q
from django.http import HttpResponse

from apps.admin.models import DenyIP, DenyAccount


class RequestDenyFilterMiddleware:
    """请求地址过滤（访问拒绝）中间件类"""

    # 拒绝的IP地址池，如果需要可以从数据库读取
    DENY_IPS = []
    DENY_ACCOUNT = []

    def __init__(self, get_response):
        # 程序启动时执行, 只执行一次
        self.get_response = get_response
        self.reload_addr()

    def __call__(self, request):
        # 中间件执行开始
        response = self.get_response(request)
        # 中间件执行结束
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """视图函数调用之前会调用"""
        # 请求实际函数前执行
        remote_ip = request.META['REMOTE_ADDR']
        account = request.user.__str__()
        # print('FROM: (%s, %s), %s' % (remote_ip, account, request))

        global DENY_IPS
        if remote_ip in DENY_IPS:
            return HttpResponse('<h1>IP访问被拒绝</h1>')

        global DENY_ACCOUNT
        if account in DENY_ACCOUNT:
            return HttpResponse('<h1>IP访问被拒绝</h1>')

        # TODO 记录日志

    def process_exception(self, request, exception):
        # 程序异常时执行
        return HttpResponse(exception.args[0])

    @staticmethod
    def reload_addr():
        """重新加载地址"""
        global DENY_IPS
        DENY_IPS = [_.ip for _ in DenyIP.objects.filter(Q(open_date__gt=datetime.datetime.now()) | Q(open_date__isnull=True), is_active=True)]

        global DENY_ACCOUNT
        DENY_ACCOUNT = [_.user.__str__() for _ in DenyAccount.objects.filter(Q(open_date__gt=datetime.datetime.now()) | Q(open_date__isnull=True), is_active=True)]
