from rest_framework.serializers import *


class ModelSerializer(ModelSerializer):
    """
    模型基本序列化类
    """

    is_active = BooleanField(initial=True, required=False, help_text='是否可用', label='是否可用')
    created_date = DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    modified_date = DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')


class RecursiveField(Serializer):
    """
    递归字段
    """

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data
