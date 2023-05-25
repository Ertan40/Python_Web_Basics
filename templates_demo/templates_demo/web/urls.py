from django.urls import path

from templates_demo.web.views import index, redirect_to_home, about

urlpatterns = (
     path('', index, name='index'),
     path('go-to-home/', redirect_to_home, name="redirect_to_home"),
     path('about/', about, name="about"),
)