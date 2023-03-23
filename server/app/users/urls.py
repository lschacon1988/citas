from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', api.UserViewSet,  basename="users")


# The API URLs are now determined automatically by the router.
urlpatterns = router.urls