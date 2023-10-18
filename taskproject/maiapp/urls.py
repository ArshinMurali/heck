from . import views
from django.urls import path
app_name='tasks'
urlpatterns = [
    path('task_ten/',views.task_ten, name='task_ten'),
    path('task_four/',views.task_four, name='task_four')

]