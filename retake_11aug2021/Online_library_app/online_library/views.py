from django.http import HttpResponse
from django.shortcuts import render, redirect

from Online_library_app.online_library.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from Online_library_app.online_library.models import Profile, Book


def get_user():
    try:
        user = Profile.objects.get()
        return user
    except Profile.DoesNotExist:
        return None
def index(request):
    user = get_user()
    books = Book.objects.all()
    if user:
        page = 'common/home-with-profile.html'
    else:
        page = 'common/home-no-profile.html'

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'user': user,
        'books': books,
    }
    return render(request, page, context)



def profile(request):
    user = Profile.objects.get()
    context = {
        'user': user
    }

    return render(request, 'profile/profile.html', context)
def add_book(request):
    user = Profile.objects.get()
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'book/add-book.html', context)

def edit_book(request, pk):
    user = Profile.objects.get()
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'user': user,
        'form': form,
        'book': book,
    }
    return render(request, 'book/edit-book.html', context)

def book_details(request, pk):
    user = Profile.objects.get()
    book = Book.objects.filter(pk=pk).get()
    context = {
        'user': user,
        'book': book,
    }
    return render(request, 'book/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')

def edit_profile(request):
    user = Profile.objects.get()
    if request.method == 'GET':
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'profile/edit-profile.html', context)

def delete_profile(request):
    user = Profile.objects.get()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=user)
    else:
        user.delete()
        Book.objects.all().delete()
        return redirect('index')

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)