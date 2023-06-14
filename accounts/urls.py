from django.urls import path


from .views import signup


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name="signup"),
    path('signup/', signup, name="signup"),
]
