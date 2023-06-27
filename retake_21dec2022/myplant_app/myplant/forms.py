from django import forms

from myplant_app.myplant.models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }


class ProfileCreateForm(ProfileBaseForm):
    ...

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'profile_picture': forms.URLInput(),
        }

# class ProfileDeleteForm(ProfileBaseForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.hidden_fields()
#
#     def __hidden_fields(self):
#         for (name, field) in self.fields.items():
#             field.widget = forms.HiddenInput()
#
#     def save(self, commit=True):
#         if commit:
#             Plant.objects.all().delete()
#             self.instance.delete()
#         return self.instance


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        widgets = {
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput(),

        }


class PlantCreateForm(PlantBaseForm):
    ...


class PlantEditForm(PlantBaseForm):
    ...


class PlantDeleteForm(PlantBaseForm):
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
