from django.urls import path
from users.views import UserLoginView, UserRegistrationView, UserProfileView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from users.views import UserRegistrationView, UserProfileView, EmailVerificationView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('verify/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='email_verification'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),

    ]