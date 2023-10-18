from . import views
from django.urls import path
app_name='tasks'
urlpatterns = [
    path('task_three/', views.task_three, name='task_three'),

]