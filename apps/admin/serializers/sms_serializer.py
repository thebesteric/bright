"""
短信序列化
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-16 10:16
@info: 
"""
import re
from datetime import datetime
from datetime import timedelta

from django.contrib.auth import get_user_model

from apps.admin.api.common import serializers
from apps.admin.models import VerifyCode
from bright.settings import REGEX

User = get_user_model()


class VerifyCodeSerializer(serializers.ModelSerializer):
    """
    短信验证码
    """

    class Meta:
        model = VerifyCode
        fields = "__all__"


class SmsCodeSendSerializer(serializers.Serializer):
    """
    短信
    """

    cellphone = serializers.CharField(max_length=11, required=True, help_text='手机号')
    description = serializers.CharField(max_length=256, default=None, help_text='描述', required=False)

    def validate_cellphone(self, cellphone):
        """
        验证手机号码
        :param cellphone:
        :return:
        """

        # 验证手机号码是否合法
        if not re.match(REGEX['CELLPHONE'], cellphone):
            raise serializers.ValidationError('手机号码格式非法')

        # 手机号码是否已经注册
        if User.objects.filter(cellphone=cellphone).count():
            raise serializers.ValidationError('手机号码已经存在')

        # 验证发送频率
        one_minute_age = datetime.now() - timedelta(minutes=1)
        if VerifyCode.objects.filter(cellphone=cellphone, created_date__gt=one_minute_age).count():
            raise serializers.ValidationError('请勿频繁发送短信')

        return cellphone
