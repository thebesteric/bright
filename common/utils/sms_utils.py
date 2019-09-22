"""
短信发送工具类
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019-09-10 22:41
@info: 
"""

import requests
import json
from bright.settings import SMS_CONFIG
import random


class SmsSender:

    def __init__(self, api_key=SMS_CONFIG['SMS_API_KEY']):
        self.api_key = api_key

    def send_message(self, cellphone, message):
        """
        发送单条短信
        :param cellphone:
        :param message:
        :return:
        """
        auth = ('api', self.api_key)
        data = {
            "mobile": cellphone,
            "message": message + SMS_CONFIG['SMS_SIGNATURE']
        }
        resp = requests.post("http://sms-api.luosimao.com/v1/send.json", auth=auth, data=data, timeout=3, verify=False)
        return json.loads(resp.content)

    @staticmethod
    def generate_code(num=4, seeds='1234567890'):
        """
        随机字符串
        :param num:
        :param seeds:
        :return:
        """
        random_arr = []
        for i in range(num):
            random_arr.append(random.choice(seeds))
        return ''.join(random_arr)


if __name__ == '__main__':
    # resp = SmsSender().send_message('13966660426', '测试短信')
    # print(resp)
    pass
