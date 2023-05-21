from django.shortcuts import render
from django.http import HttpRequest

from mysite.tasks.models import Task
#mysite.tasks.views.py

# def index(request):
#     return http.HttpResponse("Ok")
def show_all_tasks(request):
    all_tasks = Task.objects.order_by('id').all()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)

    return http.HttpResponse(result)

def index(request):
    all_tasks = Task.objects \
        .order_by('id') \
        .all()
    context = {
        'title': 'The tasks app',
        'tasks': all_tasks
    }
    return render(request, 'index.html', context)