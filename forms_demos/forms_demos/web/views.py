from django.shortcuts import render
from django import forms
from forms_demos.web.forms import PersonForm
from forms_demos.web.models import Person
# Create your views here.

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        # fields = ['name', 'last_name']
        exclude = ['last_name']
        widgets = {
            'name': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Your name',
                }
            ),
        }
        labels = {'name': 'Your custom name'}
        help_texts = {'age': 'Please fill your age'}

def index(request):
    name = None
    # people = Person.objects.all()
    # update_person = Person.objects.get(id=2)
    # form = PersonForm(instance=update_person)
    form = PersonForm()

    if request.method == "POST":# request.method = 'post':
        form = PersonForm(request.POST)
        # Validate the form
        # If valid cleans , fills cleaned_data dictionary
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(name=name)

            # Person.objects.create(**form.cleaned.data)
            # Person.objects.create(name=form.cleaned_data['your_name'],
            # age=form.cleaned_data['age'])
    # else:  # GET
    #     form = PersonForm()

    context = {
        'form': form,
        'name': name,
        # 'people': people,
    }
    return render(request, 'index.html', context)


# def model_form_view(request):
#
#     context = {
#         'model_form': PersonModelForm(),
#     }
#     return render(request, 'model_form.html', context)

def model_form_view(request, pk):  # update
    person = Person.objects.get(pk=pk)
    form = PersonModelForm(instance=person)
    if request.method == "POST":
        form = PersonModelForm(request.POST or None, instance=person)
        if form.is_valid():
            form.save()

    context = {
        'model_form': form,
        'person': person,
    }

    return render(request, 'model_form.html', context)

# def model_form_view(request):
    # person = Person.objects.get(id=1)
    # context = {'model_form': PersonModelForm(instance=person)}
    # form = PersonModelForm()
    # if request.method == "POST":
    #     form = PersonModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # context = {
    #     'model_form': form,
    # }

    # context = {
    #     'model_form': PersonModelForm(),
    # }

    # return render(request, 'model_form.html', context)

# def index(request):
#     name = None
#     if request.method == 'GET':
#         form = PersonForm()
#     else: # request.method = 'post':
#         form = PersonForm(request.POST)
#         print(request.POST)
#         form.is_valid()
#         name = form.cleaned_data['your_name']
#         Person.objects.create(name=name)
#     context = {
#         'form': form,
#         'name': name,
#     }
#     return render(request, 'index.html', context)