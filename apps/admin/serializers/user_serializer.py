"""
用户序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-16 9:49
@info: 
"""

import re
from datetime import datetime
from datetime import timedelta

from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from apps.admin.api.common import serializers
from apps.admin.models import User, UserRole, UserOrganization, UserGroup, Role, Organization, Group
from apps.admin.models import VerifyCode
from apps.admin.serializers import role_serializer, group_serializer, orgz_serializer
from bright.settings import REGEX


class UserSerializer(serializers.ModelSerializer):
    """
    用户
    """
    roles = role_serializer.RoleSerializer(many=True, required=False, read_only=True)
    groups = group_serializer.GroupSerializer(many=True, required=False, read_only=True)
    organizations = orgz_serializer.OrganizationSerializer(many=True, required=False, read_only=True)
    password = serializers.CharField(min_length=4, max_length=16, write_only=True, label='密码')

    def create(self, validated_data):
        """
        创建时设置密文密码
        :param validated_data:
        :return:
        """
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'cellphone', 'email', 'id_card', 'gender', 'avatar', 'birthday', 'roles', 'groups', 'organizations', 'desc', ]


class UserRoleSerializer(serializers.ModelSerializer):
    """
    用户角色
    """

    # 获取当前登录用户
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True), required=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.filter(is_active=True), required=True)

    class Meta:
        model = UserRole
        validators = [UniqueTogetherValidator(queryset=UserRole.objects.all(), fields=('user', 'role'), message='用户角色已存在')]
        fields = ('id', 'user', 'role')


class UserOrganizationSerializer(serializers.ModelSerializer):
    """
    用户机构
    """

    # 获取当前登录用户
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True), required=True)
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.filter(is_active=True), required=True)

    class Meta:
        model = UserOrganization
        validators = [UniqueTogetherValidator(queryset=UserOrganization.objects.all(), fields=('user', 'organization'), message='用户机构已存在')]
        fields = ('id', 'user', 'organization')


class UserGroupSerializer(serializers.ModelSerializer):
    """
    用户群组
    """

    # 获取当前登录用户
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True), required=True)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.filter(is_active=True), required=True)

    class Meta:
        model = UserGroup
        validators = [UniqueTogetherValidator(queryset=UserGroup.objects.all(), fields=('user', 'group'), message='用户群组已存在')]
        fields = ('id', 'user', 'group')


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    用户注册
    """

    username = serializers.CharField(min_length=4, max_length=18, allow_blank=False, allow_null=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户名已存在')],
                                     label='用户名', help_text='用户名')

    password = serializers.CharField(min_length=4, max_length=16, write_only=True, label='密码', help_text='密码')

    def create(self, validated_data):
        """
        创建时设置密文密码
        :param validated_data:
        :return:
        """
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, attrs):
        attrs['is_superuser'] = False
        return attrs

    class Meta:
        model = User
        fields = ['username', 'password', 'is_staff']


class UserRegisterByCodeSerializer(serializers.ModelSerializer):
    """
    用户注册（验证码）
    """

    cellphone = serializers.CharField(min_length=11, max_length=11, allow_blank=False, allow_null=False,
                                      validators=[UniqueValidator(queryset=User.objects.all(), message='手机号码已存在')],
                                      label='手机号码', help_text='手机号码')

    code = serializers.CharField(min_length=4, max_length=6, required=True, allow_blank=False, allow_null=False, write_only=True,
                                 label='验证码', help_text='验证码',
                                 error_messages={
                                     'blank': '请输入验证码',
                                     'required': '请输入验证码',
                                     'max_length': '验证码格式错误',
                                     'min_length': '验证码格式错误'
                                 })

    password = serializers.CharField(min_length=4, max_length=16, write_only=True, label='密码', help_text='密码')

    def create(self, validated_data):
        """
        创建时设置密文密码
        :param validated_data:
        :return:
        """
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_cellphone(self, cellphone):
        # 验证手机号码是否合法
        if not re.match(REGEX['CELLPHONE'], cellphone):
            raise serializers.ValidationError('手机号码格式非法')

        # 手机号码是否已经注册
        if User.objects.filter(cellphone=cellphone).count():
            raise serializers.ValidationError('手机号码已经存在')

        return cellphone

    def validate_code(self, code):
        cellphone = self.initial_data['cellphone']
        verify_codes = VerifyCode.objects.filter(cellphone=cellphone).order_by('-created_date')
        if verify_codes:
            last_verify_code = verify_codes[0]
            # 是否正确
            if code != last_verify_code.code:
                raise serializers.ValidationError('验证码错误')
            # 是否过期
            five_minute_age = datetime.now() - timedelta(minutes=5)
            if five_minute_age > last_verify_code.created_date:
                raise serializers.ValidationError('验证码已过期')
            return code

        raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['is_superuser'] = False
        # 默认手机号码就为用户名
        attrs['username'] = attrs['cellphone']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ['cellphone', 'password', 'code', 'is_staff']
