from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from accounts.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #Django Administration
    path("mgmt/", admin.site.urls),
]
