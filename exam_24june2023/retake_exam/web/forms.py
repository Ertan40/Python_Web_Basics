from django import forms

from retake_exam.web.models import Profile, Fruit

# class ProfileBaseForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        labels = {'first_name': '', 'last_name': '', 'email': '', 'password': ''}

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'First Name'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
                  'image_url': 'Image URL', 'age': 'Age'}

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'image_url': forms.URLInput(),
            'age': forms.NumberInput(),
        }


# class ProfileDeleteForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__hidden_fields()
#
#     def __hidden_fields(self):
#         for (name, field) in self.fields.items():
#             field.widget = forms.HiddenInput()
#
#     def save(self, commit=True):
#         if commit:
#             Fruit.objects.all().delete()
#             self.instance.delete()
#         return self.instance


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {'name': '', 'image_url': '', 'description': '', 'nutrition': ''}

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition Info'}
            ),
        }

class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {'name': 'Name', 'image_url': 'Image URL', 'description': 'Description', 'nutrition': 'Nutrition'}


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description')
        labels = {'name': 'Name', 'image_url': 'Image URL', 'description': 'Description'}

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
            # field.widget.attrs['disabled'] = 'disabled'