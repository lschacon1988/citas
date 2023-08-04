
from app.customUser.views import Profile
from django.contrib import admin
from django.urls import include
from rest_framework.urls import path, views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .swagger_config import schema_view_local, schema_view_productions

schema_view = schema_view_local if settings.LOCAL_DEV else schema_view_productions


base_api_v1 = [
    path('', include('app.customUser.urls')),
    path('', include('app.professionals.urls')),
    path('', include('app.meet.urls')),
    path('', include('app.services.urls')),
]

base_view=[
    path('admin/', Profile.as_view(), name='admin'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_framework.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include(base_api_v1)),
    path('api/v1/', include(base_view)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
