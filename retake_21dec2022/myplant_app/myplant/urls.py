from django.urls import path

from myplant_app.myplant.views import index, profile_create, catalogue, profile_details, profile_edit, profile_delete, \
    plant_create, plant_details, plant_edit, plant_delete

urlpatterns = [
    path('', index, name='index'),
    path('profile/create/', profile_create, name='profile create'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/delete/', profile_delete, name='profile_delete'),
    path('create/', plant_create, name='plant create'),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('edit/<int:pk>/', plant_edit, name='plant edit'),
    path('delete/<int:pk>/', plant_delete, name='plant delete'),
]