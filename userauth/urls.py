from django.urls import path
from .views import signup,home,login,logout,upload,likes




urlpatterns = [
    path("",home),
    path("signup/",signup,name="signup"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path('upload',upload,name='upload'),
    path('like-post/<str:id>',likes,name='like-post'),
]
