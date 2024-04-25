from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),  # Include app urls here
]
