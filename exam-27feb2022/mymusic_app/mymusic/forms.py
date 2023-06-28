from django import forms

from mymusic_app.mymusic.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age'
                })}


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()


    def __hidden_fields(self):
        for (name, field) in self.fields.items():
            field.widget = forms.HiddenInput()


    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance




class ProfileCreateForm(ProfileBaseForm):
    ...


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                }),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                })
        }

class AlbumCreateForm(AlbumBaseForm):
    ...



class AlbumEditForm(AlbumBaseForm):
    ...



class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()

    def __disabled_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance