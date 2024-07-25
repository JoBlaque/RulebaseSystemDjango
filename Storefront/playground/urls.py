from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#UrlConfig
urlpatterns =[
    path('hello/', views.say_hello),
    path("planner_api/", views.planner_api),
]