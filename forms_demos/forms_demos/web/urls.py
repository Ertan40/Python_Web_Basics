# web\urls.py
from forms_demos.web.views import index, model_form_view
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    # path('model_form/', model_form_view, name='model form'),
    path('model_form/<int:pk>/', model_form_view, name='model form'),
]