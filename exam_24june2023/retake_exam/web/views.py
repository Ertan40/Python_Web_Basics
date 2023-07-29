from django.shortcuts import render, redirect

from retake_exam.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm
from retake_exam.web.models import Profile, Fruit


def get_user():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return False


def index(request):
    context = {'logged': get_user()}
    return render(request, 'common/index.html', context)


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {'fruits': fruits, 'logged': get_user()}
    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    logged = get_user()
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': logged}
    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    logged = get_user()
    context = {'logged': logged, 'fruit': fruit}
    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': get_user(), 'fruit': fruit}
    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': get_user(), 'fruit': fruit}
    return render(request, 'fruit/delete-fruit.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': get_user()}
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    user = Profile.objects.get()
    full_name = None
    total_posts = Fruit.objects.count()
    if total_posts > 0:
        total_posts = total_posts
    else:
        total_posts = 0
    if user.first_name and user.last_name:
        full_name = f'{user.first_name} {user.last_name}'
    elif user.first_name:
        full_name = f'{user.first_name}'
    elif user.last_name:
        full_name = f'{user.last_name}'

    context = {'logged': get_user(), 'full_name': full_name, 'total_posts': total_posts, 'user': user}
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
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


def delete_profile(request):
    if request.method == "POST":
        Profile.objects.all().delete()
        Fruit.objects.all().delete()
        return redirect('index')

    context = {
        'logged': get_user(),
    }
    return render(request, 'profile/delete-profile.html', context)


# def delete_profile(request): with form
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
