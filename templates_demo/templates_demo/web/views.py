from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Student: {self.name},  age: {self.age}"


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Ertan', 40),
        'student_info': Student('Meryem', 10).get_info(),
        'now': datetime.now(),
        'students': ['Pesho', 'Pesho', 'Gosho', 'Meri', 'Mimi'],
        # 'students': []
        'values': list(range(1, 20)),
    }
    return render(request, 'index.html', context)

def redirect_to_home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')