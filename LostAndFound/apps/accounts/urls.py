from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.user_login , name="user_login"),
    path('register/',views.user_register,name="user_register"),
    path('forgotPass/',views.forgotPass,name="forgotPass"),
    path('mailVerification/',views.mailVerification,name="mailVerification"),

]