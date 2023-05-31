#admin.py
from django.contrib import admin

from models_demos.web.models import Employee, NullBlankDemo, Project, Department, Category


# The 'Employee' model is enabled in Django Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "level", "employee_department")
    # list_filter = ("level", "department", "first_name")
    search_fields = ("first_name", "last_name")

    
    def employee_department(self, obj):
        return obj.department.name

    fieldsets = (
        (
            "Personal_info",
        {
            'fields': ("first_name", "last_name", "age")
        }),
        ("Professional_info", {"fields": ("level", "years_of_experience")}),
        ("Company_info", {"fields": ("department", "works_full_time", "start_date")}),
    )

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(NullBlankDemo)
class NullBlankDemo(admin.ModelAdmin):
    pass

@admin.register(Department)
class Department(admin.ModelAdmin):
    ...

@admin.register(Project)
class Project(admin.ModelAdmin):
    ...

@admin.register(Category)
class Category(admin.ModelAdmin):
    ...