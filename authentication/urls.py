from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('logout/', logout, name='logout'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('otp_verify/', otp_verify, name='otp_verify'),
    # path('resend_otp/', resend_otp, name='resend_otp'),
]
