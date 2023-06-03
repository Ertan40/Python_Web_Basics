from django.shortcuts import render, redirect

from models_demo.web.models import Employee, Department, Project

# Create your views here.
# def show_all_departments(request):
#     all_departments = Department.objects.all()
#     context = {'departments': all_departments}
#     return render(request, 'deparments.html', context)

def index(request):
    all_employees = Employee.objects.all()
    # all_employees = [ e for e in Employee.objects.all() if e.department_id = 1]
    all_employees2 = Employee.objects.filter(age__gt=30) \
        # .filter(first_name__endswith="n") \
        # .order_by('last_name', 'first_name')

    # all_employees2 = Employee.objects.filter(department__name="IT") \ # department.name
    #     .order_by('last_name', 'first_name')

    # 'get' returns a object not a QuerySet
    # 'get' returns a single object and throws error when multiple
    # 'get' is eager and doesnt return QuerySet
    # Employee.objects.get(level=Employee.LEVEL_SENIOR)
    all_departments = Department.objects.get(pk=1)
    # employee_with_id_one = get_object_or_404(Employee, pk=1)
    # try to get an employee with an id of 1;
    # if not - raise an Http404 exception;

    print(list(all_employees))
    print(list(Department.objects.all()))
    context = {
        'employees': all_employees,
        'employees2': all_employees2,
        'department': all_departments, # was departments
    }
    print(all_employees)
    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    # Project.objects.all().delete()  # deletes all projects
    # when 'restricted' this must be done explicitly
    # when 'Cascade' this is done implicitly
    # department_pk = 2
    # Employee.objects.filter(department_id=department_pk).delete() or
    # get_object_or_404(Employee, department_id=department_pk).delete()

    return redirect("index")


# def department_details(request, pk):
#     context = {
#         "department": get_object_or_404(Department, pk=pk),
#     }
#     return render(request, 'department-details.html', context)

def department_details(request, pk, slug):
    context = {
        "department": get_object_or_404(Department, pk=pk, slug=slug),
   ##   "department": Department.objects.filter(pk=pk, slug=slug),
    }
    return render(request, 'department-details.html', context)