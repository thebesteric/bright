from apps.admin.api.common import pagination, fields, viewsets
from apps.admin.models import Role, RoleMenu, RoleAction
from apps.admin.serializers import role_serializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class RoleViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        角色列表
    create:
        创建角色
    destroy:
        删除角色
    retrieve:
        获取角色详情
    update:
        更新角色
    """

    queryset = Role.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = role_serializer.RoleSerializer
    pagination_class = pagination.StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ip']
    ordering_fields = fields.BASE_ORDERING_FIELDS


class RoleMenusViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        角色菜单
    create:
        创建角色菜单
    destroy:
        删除角色菜单
    retrieve:
        获取角色菜单详情
    update:
        更新角色菜单
    """

    queryset = RoleMenu.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = role_serializer.RoleMenuSerializer


class RoleActionsViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        角色行为
    create:
        创建角色行为
    destroy:
        删除角色行为
    retrieve:
        获取角色行为详情
    update:
        更新角色行为
    """

    queryset = RoleAction.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = role_serializer.RoleActionSerializer
