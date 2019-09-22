from apps.admin.api.common import viewsets
from apps.admin.models import Group, GroupRole, GroupMenu, GroupAction
from apps.admin.serializers import group_serializer


class GroupViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        群组列表
    create:
        创建群组
    destroy:
        删除群组
    retrieve:
        获取群组详情
    update:
        更新群组
    """
    queryset = Group.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = group_serializer.GroupSerializer


class GroupRoleViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        群组角色列表
    create:
        创建群组角色
    destroy:
        删除群组角色
    retrieve:
        获取群组角色详情
    update:
        更新群组角色
    """
    queryset = GroupRole.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = group_serializer.GroupRoleSerializer


class GroupMenuViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        群组菜单列表
    create:
        创建群组菜单
    destroy:
        删除群组菜单
    retrieve:
        获取群组菜单详情
    update:
        更新群组菜单
    """
    queryset = GroupMenu.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = group_serializer.GroupMenuSerializer


class GroupActionViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        群组菜单列表
    create:
        创建群组菜单
    destroy:
        删除群组菜单
    retrieve:
        获取群组菜单详情
    update:
        更新群组菜单
    """
    queryset = GroupAction.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = group_serializer.GroupActionSerializer
