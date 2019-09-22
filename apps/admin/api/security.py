from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.admin.models import User
from common.utils import jwt_utils


class ApiLoginViewBackend(ModelBackend):
    """
    API User Login
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(cellphone=username) | Q(email=username), is_superuser=True, is_staff=True, is_active=True)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except User.DoesNotExist:
            return None


class LoginView(APIView):
    """
    User Login
    """

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(Q(username=username) | Q(cellphone=username) | Q(email=username), is_active=True)
            if user.check_password(password):
                return Response(jwt_utils.create_jwt_token(user), status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass
        else:
            return Response({'success': False, 'message': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
