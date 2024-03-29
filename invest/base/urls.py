from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns= [
    path('',  views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('about/', views.about, name="about" ),
    path('contact/', views.contact, name="contact"),
    path('plan/', views.plan, name="plan"),
    path('service/', views.service, name="service"),
    path('faq/', views.faq, name="faq"),
    # path('project/', views.project, name="project")


    path('reset_passsword/', auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"), name= "reset_password"),
    path('reset_passsword_sent/', auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"), name= "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset.form.html"), name= "password_reset_confirm"),
    path('reset_passsword_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset.done.html"), name= "password_reset_complete"),
    
]