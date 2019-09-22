"""
拒绝访问序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-16 11:16
@info: 
"""
from apps.admin.api.common import serializers
from apps.admin.models import DenyIP, DenyAccount


class DenyIPSerializer(serializers.ModelSerializer):
    """
    IP黑名单
    """

    open_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', label='解封时间', required=False)

    class Meta:
        model = DenyIP
        fields = '__all__'


class DenyAccountSerializer(serializers.ModelSerializer):
    """
    Account黑名单
    """

    open_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', label='解封时间', required=False)

    class Meta:
        model = DenyAccount
        fields = '__all__'
