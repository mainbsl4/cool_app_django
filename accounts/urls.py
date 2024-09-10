from django.urls import path
from .views import amne_e

urlpatterns = [

    # path('accounts/', ),
    path('amne_e/', amne_e, name='amne_e'),

    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('accounts/password_reset/
]
