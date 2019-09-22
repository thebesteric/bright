"""
菜单序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-16 10:12
@info: 
"""
from apps.admin.api.common import serializers
from apps.admin.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    """
    菜单
    """

    class Meta:
        model = Menu
        fields = "__all__"


class MenuTreeSerializer(serializers.ModelSerializer):
    """
    菜单树
    """

    children = serializers.RecursiveField(many=True)

    class Meta:
        model = Menu
        fields = "__all__"
