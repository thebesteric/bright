from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response

from apps.admin.api.common import viewsets, mixins
from apps.admin.filters import UserFilter
from apps.admin.models import User, UserRole, UserOrganization, UserGroup
from apps.admin.serializers import user_serializer
from common.utils import jwt_utils


class UserViewSet(viewsets.ModelAuthViewSet):
    """
    list:
        用户列表、排序，分页，搜索
    create:
        创建用户
    destroy:
        删除用户
    retrieve:
        获取用户详情
    update:
        更新用户
    """
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = user_serializer.UserSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = UserFilter
    search_fields = ['username', 'cellphone', 'email']
    ordering_fields = ('id', 'date_joined', 'modified_date', 'is_active')


class UserRolesViewSet(viewsets.ModelAuthOwnerViewSet):
    """
    list:
        登录用户角色列表
    create:
        创建用户角色
    destroy:
        删除用户角色
    retrieve:
        获取用户角色详情
    update:
        更新用户角色
    """
    # permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    # authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    serializer_class = user_serializer.UserRoleSerializer

    # lookup_field = 'role_id'

    def get_queryset(self):
        return UserRole.objects.filter(user=self.request.user)


class UserOrganizationsViewSet(viewsets.ModelAuthOwnerViewSet):
    """
    list:
        登录用户机构列表
    create:
        创建用户机构
    destroy:
        删除用户机构
    retrieve:
        获取用户机构详情
    update:
        更新用户机构
    """
    serializer_class = user_serializer.UserOrganizationSerializer

    def get_queryset(self):
        return UserOrganization.objects.filter(user=self.request.user)


class UserGroupsViewSet(viewsets.ModelAuthOwnerViewSet):
    """
    list:
        登录用户群组列表
    create:
        创建用户群组
    destroy:
        删除用户群组
    retrieve:
        获取用户群组详情
    update:
        更新用户群组
    """
    serializer_class = user_serializer.UserGroupSerializer

    def get_queryset(self):
        return UserGroup.objects.filter(user=self.request.user)


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
        用户注册
    """
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = user_serializer.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        data = jwt_utils.create_jwt_token(user)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class UserRegisterByCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
        用户注册（验证码模式），默认手机号等于用户名
    """
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = user_serializer.UserRegisterByCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        data = jwt_utils.create_jwt_token(user)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
