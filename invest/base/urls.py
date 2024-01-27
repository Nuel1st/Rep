from django.urls import path
from . import views


urlpatterns= [
    path('',  views.home, name="home"),
    path('login/', views.login, name="login"),
    path('about/', views.about, name="about" ),
    path('contact/', views.contact, name="contact"),
    path('plan/', views.plan, name="plan"),
    path('service/', views.service, name="service"),
    path('faq/', views.faq, name="faq"),
    # path('project/', views.project, name="project")

]