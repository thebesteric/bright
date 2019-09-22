"""
行为序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019/9/18 15:32
@info: 
"""
from apps.admin.api.common import serializers
from apps.admin.models import Action


class ActionSerializer(serializers.ModelSerializer):
    """
    行为
    """

    class Meta:
        model = Action
        fields = '__all__'
