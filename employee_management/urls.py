from django.contrib import admin
from django.urls import include, path
from base.views import home

urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
]
