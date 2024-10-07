from django.shortcuts import render, redirect
from .forms import *

def homepage(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/')
    else:
        form = AddEmployeeForm()
    
    context = {
        'form': form,
    }

    return render(request, 'employee_form.html', context)