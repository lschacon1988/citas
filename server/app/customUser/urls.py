from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from . import api, views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', api.CustomUserViewSet,  basename="users")


# The API URLs are now determined automatically by the router.
urlpatterns =[ 
              path('', include(router.urls),name='users'), 
              path('prueba/', views.Profile.get, name='prueba'),
              path('prueba2/', views.Profile.post, name='prueba2'),
              ]
    
    