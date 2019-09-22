from common.utils import crypt_utils
from bright import settings

row_data = [
    {
        'username': 'admin',
        'password': crypt_utils.md5('admin', settings.APP_SALT),
        'cellphone': '13966660426',
        'email': 'admin@wesoft.com'
    }
]
