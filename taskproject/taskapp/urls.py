from . import views
from django.urls import path
app_name='tasks'
urlpatterns = [
    path('',views.task, name='task'),
    path('login/',views.task_one, name='login'),
    path('register/',views.task_two, name='register'),
    path('form/', views.task_six, name='form'),



]
