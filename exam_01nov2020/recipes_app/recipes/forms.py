from django import forms

from recipes_app.recipes.models import Recipe

class RecipeBaseFrom(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeCreateForm(RecipeBaseFrom):
    ...


class RecipeEditForm(RecipeBaseFrom):
    ...


class RecipeDeleteForm(RecipeBaseFrom):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'