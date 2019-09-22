"""
机构序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 9/17/2019 6:26 PM
@info: 
"""

from apps.admin.api.common import serializers
from apps.admin.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """
    机构
    """

    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationTreeSerializer(serializers.ModelSerializer):
    """
    机构树
    """

    children = serializers.RecursiveField(many=True)

    class Meta:
        model = Organization
        fields = "__all__"
