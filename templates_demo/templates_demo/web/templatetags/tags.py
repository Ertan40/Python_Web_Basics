from django.template import Library

from templates_demo.web.views import Student

register = Library()

@register.simple_tag(name="student_info")
def show_student_info(student: Student):
    return f"Hi, my name is {student.name} and I am {student.age} - years old."


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    # current_course = Course.objects.filter(.......)
    context = {
        'url_names': args,
    }
    return context


# @register.inclusion_tag('tags/nav.html', name='app_nav', takes_context=True )
# def generate_nav(context, *args):
#     return {
#         'url_names': args,
#     }
#    in order to take context info
