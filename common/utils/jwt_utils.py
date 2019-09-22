"""
Json Web Token
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019/9/18 14:31
@info: 
"""
from rest_framework_jwt.settings import api_settings


def create_jwt_token(user):
    """
    创建 Json Web Token
    :param user:
    :return:
    """
    data = dict()
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    data['id'] = user.id
    data['name'] = user.username if user.username else user.cellphone
    data['token'] = jwt_encode_handler(payload)
    return data
