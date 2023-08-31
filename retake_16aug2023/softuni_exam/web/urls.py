from django.urls import path

from softuni_exam.web.views import home, dashboard, create_event, event_details, event_delete, event_edit, \
    create_profile, profile_details, edit_profile, delete_profile

urlpatterns = (

    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_event, name='create event'),
    path('details/<int:pk>/', event_details, name='event details'),
    path('edit/<int:pk>/', event_edit, name='event edit'),
    path('delete/<int:pk>/', event_delete, name='event delete'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)