from django.contrib import admin
from django.urls import path, include
from  imsyakApp.views import *
from  rest_framework import routers


router = routers.DefaultRouter()
router.register('Jadwal_Imsyak', jadwalViews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
