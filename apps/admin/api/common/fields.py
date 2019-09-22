BASE_ORDERING_FIELDS = ('id', 'created_date', 'modified_date', 'is_active')


def extends(*args):
    """
    合并返回新的排序字段
    :param args:
    :return:
    """
    ordering_fields = list(BASE_ORDERING_FIELDS)
    ordering_fields.extend(args)
    return ordering_fields
