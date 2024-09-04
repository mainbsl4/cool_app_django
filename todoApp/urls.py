from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("homepage/", views.homepage),
    path("homepage/<name>/", views.homepage),
    path("about/", views.about),
    path("contact/", views.contact),
]
