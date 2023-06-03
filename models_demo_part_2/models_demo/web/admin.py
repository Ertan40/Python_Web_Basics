from django.contrib import admin

from models_demo.web.models import Employee, NullBlankDemo, Department, Project, Category
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'seniority', 'works_full_time')
    list_filter = ('seniority', 'first_name', 'last_name')
    search_fields = ("first_name", "last_name")

    def employee_department(self, obj):
        return obj.department.name

    fieldsets = (
        (
            "Personal_info",
            {
                'fields': ("first_name", "last_name", "age")
            }),
        ("Professional_info", {"fields": ("seniority", "years_of_experience")}),
        ("Company_info", {"fields": ("department", "works_full_time", "start_date")}),
    )

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(NullBlankDemo)
class NullBlankDemo(admin.ModelAdmin):
    ...

@admin.register(Department)
class Department(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class Category(admin.ModelAdmin):
    ...

@admin.register(Project)
class Project(admin.ModelAdmin):
    ...