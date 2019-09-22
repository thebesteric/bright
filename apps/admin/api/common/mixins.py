from rest_framework.mixins import *


class CRUDModelMixin(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):
    """
    CRUD Mixin
    """
    pass
