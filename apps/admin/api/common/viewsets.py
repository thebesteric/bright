from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.admin.api.common import permissions, pagination


class AuthView(GenericAPIView):
    """
    Auth Permission
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    pagination_class = pagination.StandardResultsSetPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class AuthOwnerView(AuthView):
    """
    Auth Owner Permission
    PS: User just operate self item, Usually the model has attribute user
    """
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]


class GenericAuthViewSet(GenericViewSet, AuthView):
    """
    Generic Auth ViewSet
    """
    pass


class GenericAuthOwnerViewSet(GenericViewSet, AuthOwnerView):
    """
    Generic Auth Owner ViewSet
    """
    pass


class GenericAuthCacheViewSet(CacheResponseMixin, GenericAuthViewSet):
    """
    Generic Auth & Cache ViewSet
    PS: Cache acts on retrieve and list methods
    """
    pass


class GenericAuthOwnerCacheViewSet(CacheResponseMixin, GenericAuthOwnerViewSet):
    """
    Generic Auth Owner & Cache ViewSet
    PS: Cache acts on retrieve and list methods
    """
    pass


class ModelAuthViewSet(ModelViewSet, AuthView):
    """
    Model Auth ViewSet
    """
    pass


class ModelAuthOwnerViewSet(ModelViewSet, AuthOwnerView):
    """
    Model Auth Owner ViewSet
    """
    pass


class ModelAuthCacheViewSet(CacheResponseMixin, ModelAuthViewSet):
    """
    Model Auth & Cache ViewSet
    PS: Cache acts on retrieve and list methods
    """
    pass


class ModelAuthOwnerCacheViewSet(CacheResponseMixin, ModelAuthOwnerViewSet):
    """
    Model Auth Owner & Cache ViewSet
    PS: Cache acts on retrieve and list methods
    """
    pass
