from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from user.views import RegisterView, ActiveView, LoginView, UserInfoView, UserOrderView, AddressView, LogoutView

urlpatterns = [
    path('', UserInfoView.as_view(), name='user'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LoginView.as_view(), name='logout'),
    path('active/<str:token>', ActiveView.as_view(), name='active'),

    path('order', UserOrderView.as_view(), name='order'),
    path('address', AddressView.as_view(), name='address')
]
