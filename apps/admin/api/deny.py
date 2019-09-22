from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from apps.admin.api.common import fields, viewsets
from apps.admin.models import DenyIP, DenyAccount
from apps.admin.serializers import deny_serializer


class DenyIPViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        IP黑名单列表、排序，分页，搜索
    create:
        创建IP黑名单
    destroy:
        删除IP黑名单
    retrieve:
        获取IP黑名单详情
    update:
        更新IP黑名单
    """

    queryset = DenyIP.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = deny_serializer.DenyIPSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ip']
    ordering_fields = fields.BASE_ORDERING_FIELDS


class DenyAccountViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        账号黑名单列表、排序，分页，搜索
    create:
        创建账号黑名单
    destroy:
        删除账号黑名单
    retrieve:
        获取账号黑名单详情
    update:
        更新账号黑名单
    """

    queryset = DenyAccount.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = deny_serializer.DenyAccountSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user']
    ordering_fields = fields.BASE_ORDERING_FIELDS
