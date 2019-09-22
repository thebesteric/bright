from django.contrib.auth.decorators import login_required


class LoginRequiredMixin:
    """登录访问权限"""

    @classmethod
    def as_view(cls, **initkwargs):
        return login_required(super().as_view(**initkwargs))
