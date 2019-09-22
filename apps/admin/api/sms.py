"""
短信 ViewSet
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-10 22:03
@info:
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.response import Response

from apps.admin.api.common import pagination, fields, viewsets, mixins
from apps.admin.models import VerifyCode
from apps.admin.serializers import sms_serializer
from common.utils.sms_utils import SmsSender


class SmsCodeSendViewSet(mixins.CreateModelMixin, viewsets.GenericAuthViewSet):
    """
    发送短信验证码
    """
    serializer_class = sms_serializer.SmsCodeSendSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cellphone = serializer.validated_data['cellphone']
        code = SmsSender.generate_code(4)
        sms_response = SmsSender().send_message(cellphone, '您的验证码为 %s, 请妥善保管' % code)
        if sms_response['error'] != 0:
            return Response(sms_response, status=status.HTTP_400_BAD_REQUEST)

        # 保存验证码
        VerifyCode(code=code, cellphone=cellphone, desc=serializer.validated_data['description']).save()

        return Response(sms_response, status=status.HTTP_201_CREATED)


class VerifyCodeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericAuthViewSet):
    """
    验证码，列表
    """

    queryset = VerifyCode.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = sms_serializer.VerifyCodeSerializer
    pagination_class = pagination.StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'cellphone', 'desc']
    ordering_fields = fields.BASE_ORDERING_FIELDS
