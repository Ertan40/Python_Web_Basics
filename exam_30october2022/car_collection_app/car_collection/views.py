from django.shortcuts import render, redirect
from django.db.models import Sum
from car_collection_app.car_collection.forms import ProfileCreateForm, CarCreateForm, CarEditForm, ProfileEditForm, \
    CarDeleteForm, ProfileDeleteForm
from car_collection_app.car_collection.models import Profile, Car
# Create your views here
def get_user():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return False


def index(request):
    context = {
        'logged': get_user()
    }
    return render(request, 'common/index.html', context)

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
    return render(request, 'profile/profile-create.html', context)

def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'car/car-create.html', context)

def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'logged': get_user(),
    }
    return render(request, 'car/car-edit.html', context)

def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'logged': get_user(),
        'car': car
    }
    return render(request, 'car/car-delete.html', context)

def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
        'logged': get_user(),
    }
    return render(request, 'car/car-details.html', context)

def catalogue(request):
    logged = get_user()
    count_cars = Car.objects.count()
    cars = Car.objects.all()
    context = {
        'logged': logged,
        'count_cars': count_cars,
        'cars': cars,
    }

    return render(request, 'common/catalogue.html', context)

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
        'form': form,
        'user': user,
        'logged': get_user(),
    }
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    user = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=user)
    else:
        form = ProfileDeleteForm(request.POST, instance=user)
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'logged': get_user(),
    }
    return render(request, 'profile/profile-delete.html', context)


def profile_details(request):
    user = Profile.objects.get()
    total_price = Car.objects.all().aggregate(Sum('price'))
    full_name = None
    if user.first_name and user.last_name:
        full_name = f"{user.first_name} {user.last_name}"
    elif user.first_name:
        full_name = f"{user.first_name}"
    elif user.last_name:
        full_name = f"{user.last_name}"
    context = {
        'logged': get_user(),
        'total_price': total_price['price__sum'],
        'full_name': full_name,
        'user': user,
    }
    return render(request, 'profile/profile-details.html', context)