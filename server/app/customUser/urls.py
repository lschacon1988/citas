from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from . import api


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', api.CustomUserViewSet,  basename="users")


# The API URLs are now determined automatically by the router.
urlpatterns =[ 
              path('', include(router.urls),name='users'),               
              
              ]
    
    