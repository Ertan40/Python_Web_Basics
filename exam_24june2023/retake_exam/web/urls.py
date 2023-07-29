from django.urls import path

from retake_exam.web.views import index, dashboard, create_fruit, fruit_details, fruit_delete, fruit_edit, \
    create_profile, profile_details, edit_profile, delete_profile

urlpatterns = (

    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/details/', fruit_details, name='fruit details'),
    path('<int:pk>/edit/', fruit_edit, name='fruit edit'),
    path('<int:pk>/delete/', fruit_delete, name='fruit delete'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)