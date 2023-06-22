from django.shortcuts import render, redirect

from notes_app.notes.forms import ProfileForm, NoteCreateForm, NoteEditForm, NoteDeleteForm
from notes_app.notes.models import Note, Profile


def get_user():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return False
def index(request):
    user = get_user()
    if not user:
        if request.method == 'GET':
            form = ProfileForm()
        else:
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)

    context = {
        'notes': Note.objects.all(),
    }
    return render(request, 'home-with-profile.html', context)

def add_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()

    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)



def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)

def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        note.delete()
        return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)

def note_details(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)

def profile(request):
    notes_count = Note.objects.count()
    user = Profile.objects.get()

    context = {
        'notes_count': notes_count,
        'user': user,
    }
    return render(request, 'profile.html', context)



def delete_profile(request, pk):
    user = Profile.objects.filter(pk=pk).get()
    Note.objects.all().delete()
    user.delete()
    return redirect('index')