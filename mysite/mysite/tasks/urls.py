#mysite.tasks.urls.py

from django.urls import path
from mysite.tasks.views import index, show_all_tasks

urlpatterns = (
    # localhosts:8000/tasks/
    path('', index),
    # localhosts:8000/tasks/all/
    path('all/', show_all_tasks),

)