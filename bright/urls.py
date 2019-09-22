"""bright URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('tinymce/', include(('tinymce.urls', 'tinymce'))),  # Rich text
    path('docs/', include_docs_urls(title='Bright API Docs')),  # Documents
    path('api/admin/', include(('apps.admin.urls', 'admin'))),  # Admin API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Rest framework
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # static
