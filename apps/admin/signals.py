from django.db.models import signals
from apps.admin.models import DenyIP, DenyAccount
from django.dispatch import receiver
from common.middleware import RequestDenyFilterMiddleware


@receiver(signals.post_save, sender=DenyIP)
def post_save_deny_ip(sender, instance=None, created=None, **kwargs):
    RequestDenyFilterMiddleware.reload_addr()


@receiver(signals.post_delete, sender=DenyIP)
def post_delete_deny_ip(sender, instance=None, created=None, **kwargs):
    RequestDenyFilterMiddleware.reload_addr()


@receiver(signals.post_save, sender=DenyAccount)
def post_save_deny_account(sender, instance=None, created=None, **kwargs):
    RequestDenyFilterMiddleware.reload_addr()


@receiver(signals.post_delete, sender=DenyAccount)
def post_delete_deny_account(sender, instance=None, created=None, **kwargs):
    RequestDenyFilterMiddleware.reload_addr()


def listener():
    pass
