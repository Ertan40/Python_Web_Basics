from django import forms

from softuni_exam.web.models import Profile, Event


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'profile_picture', 'password')
        widgets = {
            'email': forms.TextInput(),
            'profile_picture': forms.URLInput(),
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(attrs={'placeholder': '....'})}


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def __hidden_fields(self):
        for name, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Event.objects.all().delete()
            self.instance.delete()
        return self.instance


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class EventDeleteForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'



