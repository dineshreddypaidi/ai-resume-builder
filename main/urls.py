from django.contrib import admin
from django.urls import path,include
from apiv1.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello,name="welcome"),
    path('api/v1/',include('apiv1.urls')),
]
