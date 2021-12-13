from django.urls import path
from .views import (
    SignupView,
    PasswordView,
    AccountView,
    UserDeleteView,
    ActivateAccountView,
    purchaseview
)

urlpatterns = [
    path('sign-up/', SignupView, name='signup'),
    path('password/', PasswordView, name="password"),
    path('account/', AccountView, name="account"),
    path('delete-account/', UserDeleteView, name="delete-user"),
    path('activate-account/<str:token>/', ActivateAccountView, name="activate"),
    path('purchase/', purchaseview, name="purchase"),
]
