from django import forms

from gamesplay_app.gamesplay.models import Profile, Game


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
        }


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
        # widgets = {
        #     'email': forms.EmailInput(),
        #     'age': forms.NumberInput(),
        #     'password': forms.PasswordInput(),
        #     'first_name': forms.TextInput(),
        #     'last_name': forms.TextInput(),
        #     'profile_picture': forms.URLInput(),
        # }


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class CreateGameForm(BaseGameForm):
    ...


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()


    def __disabled_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    # if you delete on views then no need for the below part
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class EditGameForm(BaseGameForm):
    ...