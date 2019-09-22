from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    标准分页参数设置
    """
    page_size = 20
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 200


class LargeResultsSetPagination(PageNumberPagination):
    """
    大数据分页参数设置
    """
    page_size = 50
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 1000
