from apps.admin.api.common import viewsets, mixins
from apps.admin.models import Organization
from apps.admin.serializers import orgz_serializer


class OrganizationViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        机构列表
    create:
        创建机构
    destroy:
        删除机构
    retrieve:
        获取机构详情
    update:
        更新机构
    """

    queryset = Organization.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = orgz_serializer.OrganizationSerializer


class OrganizationTreeViewSet(mixins.ListModelMixin, viewsets.GenericAuthViewSet):
    """
    list:
        机构树（递归）
    """

    queryset = Organization.objects.filter(is_active=True, parent__isnull=True).order_by('order')
    serializer_class = orgz_serializer.OrganizationTreeSerializer
