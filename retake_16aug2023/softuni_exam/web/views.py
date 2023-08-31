from django.shortcuts import render, redirect

from softuni_exam.web.forms import ProfileCreateForm, EventCreateForm, EventEditForm, EventDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from softuni_exam.web.models import Profile, Event


def get_user():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def home(request):
    context = {'logged': get_user()}
    return render(request, 'common/home-page.html', context)


def dashboard(request):
    events = Event.objects.all()
    context = {'events': events, 'logged': get_user()}
    return render(request, 'web/dashboard.html', context)


def create_event(request):
    logged = get_user()
    if request.method == 'GET':
        form = EventCreateForm()
    else:
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': logged}
    return render(request, 'web/event-create.html', context)


def event_details(request, pk):
    event = Event.objects.filter(pk=pk).get()
    logged = get_user()
    context = {'logged': logged, 'event': event}
    return render(request, 'web/events-details.html', context)


def event_edit(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EventEditForm(instance=event)
    else:
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': get_user(), 'event': event}
    return render(request, 'web/event-edit.html', context)


def event_delete(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EventDeleteForm(instance=event)
    else:
        form = EventDeleteForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': get_user(), 'event': event}
    return render(request, 'web/events-delete.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'logged': get_user()}
    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    user = Profile.objects.get()
    full_name = None
    total_events = Event.objects.count()

    if user.first_name and user.last_name:
        full_name = f'{user.first_name} {user.last_name}'
    elif user.first_name:
        full_name = f'{user.first_name}'
    elif user.last_name:
        full_name = f'{user.last_name}'

    context = {'logged': get_user(), 'full_name': full_name, 'total_events': total_events, 'user': user}
    return render(request, 'profile/profile-details.html', context)


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
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    user = Profile.objects.get()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=user)
    else:
        form = ProfileDeleteForm(request.POST, instance=user)
        form.save()
        return redirect('home')

    context = {
        'form': form,
        'logged': get_user(),
        'user': user,
    }
    return render(request, 'profile/profile-delete.html', context)
