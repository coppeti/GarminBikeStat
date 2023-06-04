from django.contrib import admin
from django.urls import path

from accounts.views import home, login_view

urlpatterns = [
    path('', login_view, name="home"),
    path("admin/", admin.site.urls),
]
