from django import forms

from notes_app.notes.models import Note, Profile

class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'



class NoteCreateForm(NoteBaseForm):
    ...


class NoteEditForm(NoteBaseForm):
    ...


class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()


    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'