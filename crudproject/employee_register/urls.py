from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), #localhost:p/employee; GET and POST requests for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), # GET and POST requests for update operaiton
    path('delete/<int:id>/', views.employee_delete, name="employee_delete"),
    path('list/',views.employee_list, name='employee_list') #localhost:p/employee/list; GET requests to retrieve and display all records
]
