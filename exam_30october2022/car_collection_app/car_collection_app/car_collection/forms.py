from django import forms

from car_collection_app.car_collection.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
        }

class ProfileCreateForm(ProfileBaseForm):
    ...


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hidden_fields()

    def __hidden_fields(self):
        for (name, field) in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'picture': forms.URLInput(),
        }

class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        # widgets = {
        #     'type': forms.TextInput(),
        #     'model': forms.TextInput(),
        #     'year': forms.NumberInput(),
        #     'image_url': forms.URLInput(),
        #     'price': forms.NumberInput(),
        #
        # }

class CarCreateForm(CarBaseForm):
    ...

class CarEditForm(CarBaseForm):
    ...

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()

    def __disabled_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance