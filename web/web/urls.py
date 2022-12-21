from base64 import urlsafe_b64decode
from pprint import pp
from django.contrib import admin
from django.urls import path, include
from ppomdm.views import index
from rest_framework import routers
import ppomdm.views

routers = routers.DefaultRouter()
routers.register("deals", ppomdm.views.DealViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include(routers.urls))
]
