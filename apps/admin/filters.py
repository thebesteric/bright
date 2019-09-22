import django_filters as filters
from apps.admin import models


class UserFilter(filters.rest_framework.FilterSet):
    """
    用户过滤类
    """

    is_superuser = filters.BooleanFilter('is_superuser', lookup_expr='exact', label='超级管理员', help_text='超级管理员')
    is_staff = filters.BooleanFilter('is_staff', lookup_expr='exact', label='是否管理员', help_text='是否管理员')
    date_joined = filters.DateFilter('date_joined', lookup_expr='contains', label='创建日期', help_text='创建日期')

    class Meta:
        model = models.User
        fields = ['is_superuser', 'is_staff', 'date_joined']
