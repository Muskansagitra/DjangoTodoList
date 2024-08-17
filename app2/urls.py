from django.contrib import admin
from django.urls import path
from app2 import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('todoadd/',views.todoadd,name="todoadd"),
    path ('completed/<int:id>',views.complete,name='completed'),
    path('delete/<int:id>',views.delete,name='delete'),
    

]
