from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Id: {self.pk}, name: {self.name}'

class Project(models.Model):
    name = models.CharField(max_length=30)

    code_name = models.CharField(max_length=15, unique=True)
    dead_line = models.DateField()

class Employee(models.Model):
    LEVEL_JUNIOR = "Junior"
    LEVEL_REGULAR = "Regular"
    LEVEL_SENIOR = "Senior"
    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.RESTRICT,
        null=True,
    )
    #many to many
    projects = models.ManyToManyField(Project)
    # projects = models.ManyToManyField(Project, through='EmployeesProjects')
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=40)

    email_address = models.EmailField(unique=True)
    works_full_time = models.BooleanField(null=True)
    seniority = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        default=LEVEL_JUNIOR,
        verbose_name='Seniority level',
    )
    age = models.IntegerField()
    years_of_experience = models.PositiveIntegerField()
    photo = models.URLField(default='default-picture-url', blank=True)
    start_date = models.DateField()
    review = models.TextField()
    # This will be automatically set on creation(insert)
    created_on = models.DateTimeField(
        auto_now_add=True,  #optional
    )
    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}, name: {self.full_name}/{self.seniority}'


class AccessCard(models.Model):
    employee = models.OneToOneField(to=Employee, on_delete=models.CASCADE,
                                    primary_key=True)


class Category(models.Model):
    name = models.CharField(max_length=15)

    parent_category = models.ForeignKey('Category', on_delete=models.RESTRICT,
                                        null=True, blank=True)

# class EmployeesProjects(models.Model):
#     employee_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)
#     project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)
#     date_joined = models.DateField(auto_now_add=True)
    # additional info
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