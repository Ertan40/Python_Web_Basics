from django import forms

from Online_library_app.online_library.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }),
        }

class EditProfileForm(ProfileBaseForm):

    ...

class CreateProfileForm(ProfileBaseForm):

    ...

class DeleteProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()


    def __disabled_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            # field.widget.attrs['readonly'] = 'readonly'



class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'id': 'description',
                }),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image'
                }),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime...'
                }),
        }

class EditBookForm(BookBaseForm):
    ...

class AddBookForm(BookBaseForm):
    ...