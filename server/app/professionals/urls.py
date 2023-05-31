from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.professionals import api

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('professionals', api.ProfessionalsViewSet,basename="professionals")


# The API URLs are now determined automatically by the router.
urlpatterns =[ 
              path('', include(router.urls),name='professionals'), 
              
              ]