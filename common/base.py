import uuid
from django.db import models
from django.db.models.query import QuerySet
import json
import datetime


class BaseModel(models.Model):
    """模型抽象基类"""

    # id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, verbose_name='主键')
    id = models.AutoField(primary_key=True, editable=False, verbose_name='主键', help_text='主键')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    modified_date = models.DateTimeField(null=True, auto_now=True, verbose_name='更新时间', help_text='更新时间')
    is_active = models.BooleanField(default=True, verbose_name='是否可用', help_text='是否可用')
    desc = models.CharField(null=True, max_length=512, verbose_name='备注信息', help_text='备注信息')

    class Meta:
        abstract = True

    def json(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        obj = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                obj[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                obj[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                obj[attr] = getattr(self, attr)
                if isinstance(obj[attr], models.Model):
                    obj[attr] = {'id': obj[attr].id}
        return obj


class BaseJsonMessage:
    """Json回复格式基类"""

    @staticmethod
    def instance(success=False, message=None, data=None):
        params = dict(success=success)
        if message:
            params.update(message=message)
        if data:
            if isinstance(data, QuerySet):
                temp = []
                for _ in data:
                    temp.append(_.json())
                data = temp
            if isinstance(data, models.Model):
                data = data.json()
            if isinstance(data, str):
                data = json.loads(data)
            params.update(data=data)
        return params
