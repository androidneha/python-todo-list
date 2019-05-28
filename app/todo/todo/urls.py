from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from todo_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
]
