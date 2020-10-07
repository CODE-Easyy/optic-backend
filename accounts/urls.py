from django.urls import path
from django.contrib.auth import views as auth_views
from .views import loginPage, logoutUser


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('reset-password/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password/password_reset.html'),
         name='reset_password'),
    path('reset-password-sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password/password_reset_done.html'),
         name='password_reset_complete'),

]