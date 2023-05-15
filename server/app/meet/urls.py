from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from . import api
from .views import MeetView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('meet', api.MeetViewSet,  basename="meet")


# The API URLs are now determined automatically by the router.
urlpatterns =[ 
              path('meet/',include(router.urls)),
              path('docs/', include_docs_urls(title='Meet API'))]