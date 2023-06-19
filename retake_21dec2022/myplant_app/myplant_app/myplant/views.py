from django.shortcuts import render, redirect

from myplant_app.myplant.forms import ProfileCreateForm, ProfileEditForm, PlantCreateForm, PlantEditForm, PlantDeleteForm
from myplant_app.myplant.models import Profile, Plant


# Create your views here.
def get_user():
    try:
        user = Profile.objects.get()
        return True
    except Profile.DoesNotExist:
        return False

def index(request):
    context = {
        'logged': get_user()
    }
    return render(request, 'common/home-page.html', context)

def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'logged': get_user(),
    }
    return render(request, 'profile/create-profile.html', context)
def profile_details(request):
    user = Profile.objects.get()
    count_stars = Plant.objects.count()
    if count_stars == 0:
        count_stars = 0
    else:
        count_stars = range(count_stars if count_stars <= 3 else 3)
    context = {
        'user': user,
        'logged': get_user(),
        'count_stars': count_stars,
    }
    return render(request, 'profile/profile-details.html', context)

def profile_edit(request):
    user = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileEditForm(instance=user)
    else:
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'logged': get_user(),
        'form': form,
        'user': user,
    }
    return render(request, 'profile/edit-profile.html', context)


# def profile_delete(request): with form
#     user = Profile.objects.get()
#     if request.method == 'GET':
#         form = ProfileDeleteForm(instance=user)
#     else:
#         form = ProfileDeleteForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'logged': get_user(),
#         'form': form,
#     }
#     return render(request, 'profile/delete-profile.html', context)


def profile_delete(request):
    if request.method == "POST":
        Profile.objects.all().delete()
        Plant.objects.all().delete()
        return redirect('index')

    context = {
        'logged': get_user(),
    }
    return render(request, 'profile/delete-profile.html', context)

def catalogue(request):
    plants = Plant.objects.all()
    logged = get_user()

    context = {
        'plants': plants,
        'logged': logged,
    }
    return render(request, 'common/catalogue.html', context)



def plant_create(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'plant/create-plant.html', context)

def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'logged': get_user(),
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'plant': plant,
        'form': form,
    }
    return render(request, 'plant/edit-plant.html', context)

def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'form': form,
        'plant': plant,
    }
    return render(request, 'plant/delete-plant.html', context)