from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views
from apps.admin.api import *

router = DefaultRouter()

router.register('users', user.UserViewSet, base_name='users')
router.register('user/register', user.UserRegisterViewSet, base_name='user_register')
router.register('user/register/code', user.UserRegisterByCodeViewSet, base_name='user_register_by_code')
router.register('user/roles', user.UserRolesViewSet, base_name='user_roles')
router.register('user/organizations', user.UserOrganizationsViewSet, base_name='user_organizations')
router.register('user/groups', user.UserGroupsViewSet, base_name='user_groups')

router.register('organizations', organization.OrganizationViewSet, base_name='organizations')
router.register('organization/tree', organization.OrganizationTreeViewSet, base_name='organization_tree')

router.register('menus', menu.MenuViewSet, base_name='menus')
router.register('menu/tree', menu.MenuTreeView, base_name='menu_tree')

router.register('actions', action.ActionViewSet, base_name='actions')

router.register('groups', group.GroupViewSet, base_name='groups')
router.register('group/roles', group.GroupRoleViewSet, base_name='group_roles')
router.register('group/menus', group.GroupMenuViewSet, base_name='group_menus')
router.register('group/actions', group.GroupActionViewSet, base_name='group_actions')

router.register('roles', role.RoleViewSet, base_name='roles')
router.register('role/menus', role.RoleMenusViewSet, base_name='role_menus')
router.register('role/actions', role.RoleActionsViewSet, base_name='role_actions')

router.register('sms/codes', sms.VerifyCodeViewSet, base_name='sms_codes')
router.register('sms/code/send', sms.SmsCodeSendViewSet, base_name='sms_code_send')

router.register('deny/ips', deny.DenyIPViewSet, base_name='deny_ips')
router.register('deny/accounts', deny.DenyAccountViewSet, base_name='deny_accounts')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_jwt_token),  # API User Login Interface
    path('login/', security.LoginView.as_view()),  # User Login Interface
]
