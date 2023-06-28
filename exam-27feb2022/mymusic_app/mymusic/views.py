from django.shortcuts import render, redirect
from django.http import HttpResponse
from mymusic_app.mymusic.forms import ProfileCreateForm, AlbumEditForm, AlbumCreateForm, AlbumDeleteForm, \
    ProfileDeleteForm
from mymusic_app.mymusic.models import Profile, Album


# Create your views here.

def get_user():
    try:
        user = Profile.objects.get()
        return user
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_user()
    albums = Album.objects.all()
    if profile is None:
        return profile_create(request)
    context = {
        'albums': albums,
    }
    return render(request, 'common/home-with-profile.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'not_logged': True,
    }
    return render(request, 'common/home-no-profile.html', context)

def album_add(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)

def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album,
    }
    return render(request, 'album/album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = request.method(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)

    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/delete-album.html', context)

def profile_details(request):
    user = Profile.objects.get()
    count_albums = Album.objects.count()
    context = {
        'user': user,
        'count_albums': count_albums,
    }
    return render(request, 'profile/profile-details.html', context)

def profile_delete(request):
    user = get_user()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=user)
    else:
        form = ProfileDeleteForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'profile/profile-delete.html', context)