from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = "accounts"

urlpatterns=[
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('user/',views.home,name="home"),
    path('logout/',LogoutView.as_view(),name='logout'),

]
