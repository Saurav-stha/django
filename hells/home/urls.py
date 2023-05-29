from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("webDev",views.webDev,name='webDev'),
    path("appDev",views.appDev,name='appDev'),
    path("courses",views.courses,name='courses'),
    path("contact",views.contact,name="contact"),
    path("view",views.view,name="view"),
    path("edit",views.edit,name="edit"),
    path("faq",views.faq,name="faq"),
    path("pricing",views.pricing,name="pricing")
]