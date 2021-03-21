from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('forms/',views.forms),
    path('resumedetails/<str:details>',views.resumedetails),
    path('signin/',views.signin),
    path('signout/',views.signout)
]