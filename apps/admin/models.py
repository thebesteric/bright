from django.contrib.auth.models import AbstractUser
from django.db import models
from django_mysql.models import JSONField

from common.base import BaseModel


class User(AbstractUser):
    """后台用户"""

    Gender = ((1, 'MALE'), (2, 'FEMALE'), (0, 'UNKNOWN'))

    cellphone = models.CharField(max_length=32, verbose_name='手机号', help_text='手机号码', unique=True, null=True)
    email = models.EmailField(verbose_name='电子邮件', help_text='电子邮箱', unique=True, null=True)
    id_card = models.CharField(max_length=32, verbose_name='身份证', help_text='身份证号', unique=True, null=True)
    gender = models.IntegerField(choices=Gender, default=0, verbose_name='性别', help_text='性别', null=True)
    avatar = models.ImageField(upload_to='avatar', verbose_name='头像', help_text='头像', null=True)
    birthday = models.DateField(verbose_name='出生日期', help_text='生日', null=True)
    configure = JSONField(verbose_name='用户配置', help_text='个人配置', null=True)
    desc = models.CharField(max_length=512, verbose_name='备注信息', help_text='描述', null=True)
    date_modified = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间', null=True)
    organizations = models.ManyToManyField('Organization', verbose_name='用户-机构', through='UserOrganization', help_text='组织机构')
    roles = models.ManyToManyField('Role', verbose_name='用户-角色', through='UserRole', help_text='角色')
    groups = models.ManyToManyField('Group', verbose_name='用户-组', through='UserGroup', help_text='群组')

    class Meta:
        db_table = 's_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username if self.username else self.cellphone


class Organization(BaseModel):
    """组织机构"""

    name = models.CharField(max_length=64, verbose_name='名称', help_text='名称',  unique=True)
    address = models.CharField(max_length=256, verbose_name='地址', help_text='地址', null=True)
    charge = models.CharField(max_length=64, verbose_name='负责人', help_text='负责人', null=True)
    phone = models.CharField(max_length=32, verbose_name='联系电话', help_text='电话号码', null=True)
    position = JSONField(verbose_name='经纬度', help_text='坐标', null=True)
    order = models.PositiveSmallIntegerField(default=0, verbose_name='排序', help_text='排序', null=True)
    parent = models.ForeignKey('self', related_name='children', verbose_name='父机构', help_text='父机构', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 's_organization'
        verbose_name = '机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserOrganization(BaseModel):
    """用户-机构"""

    user = models.ForeignKey('User', help_text='用户', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', help_text='机构', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_user_organization'
        verbose_name = '机构-用户'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'organization')


class UserRole(BaseModel):
    """用户-角色"""

    user = models.ForeignKey('User', help_text='用户', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', help_text='角色', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_user_role'
        verbose_name = '用户-角色'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'role')


class UserGroup(BaseModel):
    """用户-组"""

    user = models.ForeignKey('User', help_text='用户', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', help_text='群组', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_user_group'
        verbose_name = '用户-组'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'group')


class Menu(BaseModel):
    """菜单"""

    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称', unique=True)
    icon = models.CharField(max_length=32, verbose_name='图标', help_text='图标', null=True)
    url = models.CharField(max_length=128, verbose_name='地址', help_text='地址', null=True)
    is_outer = models.BooleanField(verbose_name='是否外链', help_text='是否外链', default=False)
    order = models.PositiveSmallIntegerField(verbose_name='排序', help_text='排序', null=True)
    parent = models.ForeignKey('self', related_name='children', verbose_name='父菜单', help_text='父菜单', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 's_menu'
        ordering = ['order']
        verbose_name = '菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Action(BaseModel):
    """行为"""

    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称', unique=True)
    operate = models.CharField(max_length=32, verbose_name='操作', help_text='操作')

    class Meta:
        db_table = 's_action'
        verbose_name = '行为'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Role(BaseModel):
    """角色"""

    name = models.CharField(max_length=64, verbose_name='名称', help_text='名称', unique=True)
    menus = models.ManyToManyField('Menu', through='RoleMenu', verbose_name='包含菜单', help_text='包含菜单')
    actions = models.ManyToManyField('Action', through='RoleAction', verbose_name='包含行为', help_text='包含行为')

    class Meta:
        db_table = 's_role'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class RoleMenu(BaseModel):
    """角色-菜单"""

    role = models.ForeignKey('Role', verbose_name='角色', help_text='角色', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', verbose_name='菜单', help_text='菜单', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_role_menu'
        verbose_name = '角色-菜单'
        verbose_name_plural = verbose_name
        unique_together = ('role', 'menu')


class RoleAction(BaseModel):
    """角色-行为"""
    role = models.ForeignKey('Role', verbose_name='角色', help_text='角色', on_delete=models.CASCADE)
    action = models.ForeignKey('Action', verbose_name='行为', help_text='行为', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_role_action'
        verbose_name = '角色-行为'
        verbose_name_plural = verbose_name
        unique_together = ('role', 'action')


class Group(BaseModel):
    """组"""

    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称', unique=True)
    roles = models.ManyToManyField('Role', through='GroupRole', verbose_name='包含角色', help_text='包含角色')
    menus = models.ManyToManyField('Menu', through='GroupMenu', verbose_name='包含菜单', help_text='包含菜单')
    actions = models.ManyToManyField('Action', through='GroupAction', verbose_name='包含行为', help_text='包含行为')

    class Meta:
        db_table = 's_group'
        verbose_name = '组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GroupRole(BaseModel):
    """组-角色"""

    group = models.ForeignKey('Group', verbose_name='群组', help_text='群组', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', verbose_name='角色', help_text='角色', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_group_role'
        verbose_name = '组-角色'
        verbose_name_plural = verbose_name
        unique_together = ('group', 'role')


class GroupMenu(BaseModel):
    """组-菜单"""

    group = models.ForeignKey('Group', verbose_name='群组', help_text='群组', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', verbose_name='菜单', help_text='菜单', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_group_menu'
        verbose_name = '组-菜单'
        verbose_name_plural = verbose_name
        unique_together = ('group', 'menu')


class GroupAction(BaseModel):
    """组-行为"""

    group = models.ForeignKey('Group', verbose_name='群组', help_text='群组', on_delete=models.CASCADE)
    action = models.ForeignKey('Action', verbose_name='行为', help_text='行为', on_delete=models.CASCADE)

    class Meta:
        db_table = 's_r_group_action'
        verbose_name = '组-行为'
        verbose_name_plural = verbose_name
        unique_together = ('group', 'action')


class DenyIP(BaseModel):
    """拒绝的 IP 地址"""

    ip = models.GenericIPAddressField(verbose_name='IP地址', help_text='IP地址')
    open_date = models.DateTimeField(verbose_name='解封时间', help_text='解封时间', null=True)

    class Meta:
        db_table = 's_deny_ip'
        verbose_name = 'IP黑名单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


class DenyAccount(BaseModel):
    """拒绝的 账号"""

    user = models.ForeignKey('User', verbose_name='用户', help_text='用户', on_delete=models.CASCADE)
    open_date = models.DateTimeField(verbose_name='解封时间', help_text='解封时间', null=True)

    class Meta:
        db_table = 's_deny_account'
        verbose_name = '账号黑名单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__()


class VerifyCode(BaseModel):
    """验证码"""

    code = models.CharField(max_length=6, verbose_name='验证码', help_text='验证码')
    cellphone = models.CharField(max_length=32, verbose_name='手机号', help_text='手机号')

    class Meta:
        db_table = 's_verify_code'
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
