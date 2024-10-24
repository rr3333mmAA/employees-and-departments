from django.shortcuts import render
from .models import Department


def department_tree(request):
    departments = Department.objects.filter(parent__isnull=True)

    context = {
        'departments': departments
    }
    return render(request, 'department_tree.html', context)
