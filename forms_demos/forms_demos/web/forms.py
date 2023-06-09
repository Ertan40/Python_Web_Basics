from django import forms

class PersonForm(forms.Form):
    your_name = forms.CharField(
        label="Your custom nice name",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your placeholder name',
                'class': 'form-control',
                'custom-attribute': 'custom-value'

            }
        )
    )
    age = forms.IntegerField(
        required=False,
        initial=18,
        help_text='Please fill your age',
    ) # then will be not required # because by defalut it is True
    last_name = forms.CharField(label="Add Last Name")

    # HOBBY_CHOICES = [
    #     (1, 'Football'),
    #     (2, 'Voleyball'),
    #     (3, 'Basketball'),
    # ]
    # hobby = forms.CharField(widget=forms.CheckboxSelectMultiple(
    #     choices=HOBBY_CHOICES,
    # ))
    # hobby2 = forms.CharField(widget=forms.Select(
    #     choices=HOBBY_CHOICES,
    # ))
    # is_happy = forms.BooleanField(required=False)

    # first_name = forms.CharField(label="Add First Name")
    # url_field = forms.URLField(initial='http://')
    # comment = forms.CharField(widget=forms.Textarea)
    #
    # email = forms.EmailField()
    # password = forms.CharField()
    # password2 = forms.CharField(widget=Forms.PasswordInput)