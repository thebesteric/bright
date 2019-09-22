import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bright.settings')

import django

django.setup()

from apps.admin.models import User, Menu, Organization, Role
from db_tools.data.user_data import row_data as user_data
from db_tools.data.menu_data import row_data as menu_data
from db_tools.data.orgz_data import row_data as orgz_data
from db_tools.data.role_data import row_data as role_data


def init_orgz():
    print('----- start organization import -----')
    for data in orgz_data:
        orgz = Organization()
        orgz.name = data['name']
        orgz.address = data['address']
        orgz.charge = data['charge']
        orgz.phone = data['phone']
        orgz.position = data['position']
        orgz.parent = data['parent']
        orgz.save()
    print('----- import organization succeed -----')


def init_user():
    print('----- start user import -----')
    for data in user_data:
        user = User()
        user.username = data['username']
        user.password = data['password']
        user.cellphone = data['cellphone']
        user.save()
    print('----- import user succeed -----')


def init_role():
    print('----- start role import -----')
    for data in role_data:
        role = Role()
        role.name = data['name']
        role.save()
    print('----- import role succeed -----')


def init_menu():
    print('----- start menu import -----')
    for data in menu_data:
        menu = Menu()
        menu.name = data['name']
        menu.icon = data['icon']
        menu.href = data['href']
        menu.is_outer = data['is_outer']
        menu.order = data['order']
        menu.parent_id = data['parent']
        menu.save()
    print('----- import menu succeed -----')


if __name__ == '__main__':
    # init_orgz()
    # init_menu()
    # init_user()
    # init_role()
    pass
