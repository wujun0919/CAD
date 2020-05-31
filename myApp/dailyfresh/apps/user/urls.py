from django.urls import path, re_path
from user.views import RegisterView, ActiveView, LoginView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('active/<str:token>', ActiveView.as_view(), name='active')
]
