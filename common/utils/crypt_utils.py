"""
加密解密工具类
@project: bright
@file: .py
@ide: PyCharm
@auth: Eric Joe
@email: whatisjava@hotmail.com
@build: 2019/9/10 13:31
@info:
"""

import hashlib


def md5(str_val, salt=''):
    """md5 加密"""
    m = hashlib.md5()
    m.update((str_val + salt).encode())
    return m.hexdigest()
