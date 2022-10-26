from rest_framework import routers
from django.urls import path, include

from users import views

simple_router = routers.SimpleRouter()
simple_router.register('location', views.LocationViewSet)

urlpatterns = [
   path('', include(simple_router.urls))
]

