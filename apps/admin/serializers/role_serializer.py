"""
角色序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-16 12:21
@info: 
"""

from rest_framework.validators import UniqueTogetherValidator

from apps.admin.api.common import serializers
from apps.admin.models import Role, RoleMenu, RoleAction, Menu, Action


class RoleSerializer(serializers.ModelSerializer):
    """
    角色
    """

    class Meta:
        model = Role
        fields = "__all__"


class RoleMenuSerializer(serializers.ModelSerializer):
    """
    角色菜单
    """

    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.filter(is_active=True), required=True)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(is_active=True), required=True)

    class Meta:
        model = RoleMenu
        validators = [UniqueTogetherValidator(queryset=RoleMenu.objects.all(), fields=('role', 'menu'), message='角色菜单已存在')]
        fields = ('id', 'role', 'menu')


class RoleActionSerializer(serializers.ModelSerializer):
    """
    角色行为
    """

    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.filter(is_active=True), required=True)
    action = serializers.PrimaryKeyRelatedField(queryset=Action.objects.filter(is_active=True), required=True)

    class Meta:
        model = RoleAction
        validators = [UniqueTogetherValidator(queryset=RoleAction.objects.all(), fields=('role', 'action'), message='角色菜单已存在')]
        fields = ('id', 'role', 'action')
