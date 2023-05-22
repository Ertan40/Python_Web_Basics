from django.urls import path
from departments_app.departments.views import show_departments, show_departments_by_id, redirect_to_first_department, \
    show_not_found, index

urlpatterns = [
    path('', index),
    path('<int:department_id>/', show_departments_by_id, name='show departments'),
    path('int/<int:department_id>/', show_departments),
    path('redirect/', redirect_to_first_department),
]

# urlpatterns = [
#     #/departments/
#     path('', show_departments),
#     #/departments/{department_id}/
#     path('<department_id>/', show_departments),
#     path('int/<int:department_id>/', show_departments),
#
# ]

# paths = (
#     '',
#     '<department_id>/',
#     'int/<int:department_id>/',
# )
#
# urlpatterns = [path(url, sample_view) for url in paths]

# urlpatterns = ()
# urlpatterns += (path('', sample_view),)
# urlpatterns += (path('<department_id>/', sample_view),)
# urlpatterns += (path('int/<int:department_id>/', sample_view),)