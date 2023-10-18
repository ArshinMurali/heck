from . import views
from django.urls import path
app_name='tasks'
urlpatterns = [
    path('task_1/',views.task_1, name='task_1'),

]