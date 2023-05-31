from django.db import models

from django.urls import reverse
# models.py
# Model fields == class attributes in Model classes
# ## Django ORM(Object-Relational Mapping) ##
# Employee.objects.all() # Select
# Employee.objects.create() # Insert
# Employee.objects.filter() # Select + Where
# Employee.objects.update() # Update

class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=15,
        unique=True,
    )
    dead_line = models.DateField()


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f"Id: {self.pk}; name: {self.name}"


class Employee(models.Model):
    LEVEL_JUNIOR = "Junior"
    LEVEL_REGULAR = "Regular"
    LEVEL_SENIOR = "Senior"
    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )
    # Var char(30) => strings with max length 30
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50, null=True)
    # Text => string with unlimited length
    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level',
    )
    age = models.IntegerField()
    years_of_experience = models.PositiveIntegerField()
    # adds 'UNIQUE' constraint
    email = models.EmailField(unique=True)
    photo = models.URLField(default='default-picture-url', blank=True)
    # if null=True with options , empty with checkbox
    works_full_time = models.BooleanField(null=True)
    start_date = models.DateField()
    review = models.TextField()
    # This will be automatically set on creation(insert)
    created_on = models.DateTimeField(
        auto_now_add=True,  #optional
    )
    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(auto_now=True)  #optional
    # one to many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        # on_delete=models.RESTRICT,
    )
    # many-to-many
    projects = models.ManyToManyField(
        Project,
        related_name='Employees',
        through='EmployeesProjects'
    )
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # self.id == self.pk
        return f'Id: {self.pk}; name: {self.fullname}'


class AccessCard(models.Model):
     employee = models.OneToOneField(
         Employee, on_delete=models.CASCADE,
         primary_key=True,
     )

class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
    )
    date_joined = models.DateField(
        auto_now_add=True,
    )


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True, # Form Validation
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )


