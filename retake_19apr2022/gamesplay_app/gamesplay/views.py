from django.shortcuts import render, redirect

from gamesplay_app.gamesplay.forms import CreateProfileForm, EditProfileForm, CreateGameForm, EditGameForm, \
    DeleteGameForm
from gamesplay_app.gamesplay.models import Profile, Game


# Create your views here.

def get_user():
    user = Profile.objects.get()
    if user == 0:
        return False
    return True
def index(request):
    context = {
        'logged': get_user()
    }
    return render(request, 'common/home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)

def details_profile(request):
    user = Profile.objects.get()
    full_name = None
    count_games = Game.objects.count()
    if user.first_name and user.last_name:
        full_name = f'{user.first_name} {user.last_name}'
    elif user.first_name:
        full_name = f'{user.first_name}'
    elif user.last_name:
        full_name = f'{user.last_name}'

    if count_games > 0:
        games = Game.objects.all()
        count_rating = sum([x.rating for x in games]) / count_games
    else:
        count_rating = 0

    context = {
        'logged': get_user(),
        'full_name': full_name,
        'count_games': count_games,
        'count_rating': count_rating,
        'user': user,
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    user = Profile.objects.get()
    if request.method == 'GET':
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)

def delete_profile(request):
    if request.method == "POST":
        Profile.objects.all().delete()
        Game.objects.all().delete()
        return redirect('index')

    context = {
        'logged': get_user(),
    }
    return render(request, 'profile/delete-profile.html', context)

def dashboard(request):
    logged = get_user()
    games = Game.objects.all()
    context = {
        'logged': logged,
        'games': games,
    }
    return render(request, 'common/dashboard.html', context)

def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'logged': get_user(),
        'form': form,
         }

    return render(request, 'game/create-game.html', context)

def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
        'logged': get_user(),
    }
    return render(request, 'game/details-game.html', context)

def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'logged': get_user(),
        'form': form,
        'game': game,
    }
    return render(request, 'game/edit-game.html', context)

def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        # form = DeleteGameForm(request.POST, instance=game)
        # game.delete()
        # return redirect('dashboard')

    context = {
        'game': game,
        'form': form,
        'logged': get_user()
    }
    return render(request, 'game/delete-game.html', context)