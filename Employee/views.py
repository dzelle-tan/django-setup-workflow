from django.shortcuts import render
from .forms import EmployeeForm

def employee_form(request):
    form = EmployeeForm()
    return render(request, 'Employee/employee_form.html', {'form': form})
