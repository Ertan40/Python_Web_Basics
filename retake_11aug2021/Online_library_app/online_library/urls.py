from django.urls import path, include

from Online_library_app.online_library.views import index, add_book, edit_book, book_details, profile, edit_profile, \
    delete_profile, delete_book

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)