from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from apps.admin.api.common import fields, viewsets
from apps.admin.models import Action
from apps.admin.serializers import action_serializer


class ActionViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        行为、排序，分页，搜索
    create:
        创建行为
    destroy:
        删除行为
    retrieve:
        获取行为详情
    update:
        更新行为
    """

    queryset = Action.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = action_serializer.ActionSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'operate', 'desc']
    ordering_fields = fields.BASE_ORDERING_FIELDS
