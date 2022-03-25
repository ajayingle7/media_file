from django.urls import path
from .views import uploadView, showView



urlpatterns = [

    path("upload/", uploadView, name ="upload"),
    path("show/", showView, name= "show")



]