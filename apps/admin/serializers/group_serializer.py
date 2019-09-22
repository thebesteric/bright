"""
群组序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 9/17/2019 5:39 PM
@info: 
"""

from apps.admin.api.common import serializers
from apps.admin.models import Group, GroupRole, GroupMenu, GroupAction, Role, Action, Menu
from rest_framework.validators import UniqueTogetherValidator


class GroupSerializer(serializers.ModelSerializer):
    """
    群组
    """

    class Meta:
        model = Group
        fields = "__all__"


class GroupRoleSerializer(serializers.ModelSerializer):
    """
    群组角色
    """

    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.filter(is_active=True), required=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.filter(is_active=True), required=True)

    class Meta:
        model = GroupRole
        validators = [UniqueTogetherValidator(queryset=GroupRole.objects.all(), fields=('group', 'role'), message='群组角色已存在')]
        fields = ('id', 'group', 'role')


class GroupMenuSerializer(serializers.ModelSerializer):
    """
    群组菜单
    """

    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.filter(is_active=True), required=True)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(is_active=True), required=True)

    class Meta:
        model = GroupMenu
        validators = [UniqueTogetherValidator(queryset=GroupMenu.objects.all(), fields=('group', 'menu'), message='群组角色已存在')]
        fields = ('id', 'group', 'menu')


class GroupActionSerializer(serializers.ModelSerializer):
    """
    群组行为
    """

    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.filter(is_active=True), required=True)
    action = serializers.PrimaryKeyRelatedField(queryset=Action.objects.filter(is_active=True), required=True)

    class Meta:
        model = GroupAction
        validators = [UniqueTogetherValidator(queryset=GroupAction.objects.all(), fields=('group', 'action'), message='群组行为已存在')]
        fields = ('id', 'group', 'action')
