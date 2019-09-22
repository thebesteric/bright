from apps.admin.api.common import viewsets, mixins
from apps.admin.models import Menu
from apps.admin.serializers import menu_serializer


class MenuViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        菜单列表
    create:
        创建菜单
    destroy:
        删除菜单
    retrieve:
        获取菜单详情
    update:
        更新菜单
    """

    queryset = Menu.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = menu_serializer.MenuSerializer


class MenuTreeView(mixins.ListModelMixin, viewsets.GenericAuthViewSet):
    """
    list:
        菜单树（递归）
    """

    queryset = Menu.objects.filter(is_active=True, parent__isnull=True).order_by('order')
    serializer_class = menu_serializer.MenuTreeSerializer
