from django.shortcuts import render, get_object_or_404
from faculty.models import Department, Specialty, HomePageInfo


def index(request):
    info = HomePageInfo.objects.first()
    return render(request, 'faculty/index.html', {'info': info})


def program_list(request):
    programs = Specialty.objects.select_related('department').all()
    return render(request, 'faculty/program_list.html', {'programs': programs})


def program_detail(request, pk):
    program = get_object_or_404(Specialty.objects.select_related('department'), pk=pk)
    # Розбиваємо дисципліни на список, якщо вони введені з нового рядка або через кому
    disciplines = [d.strip() for d in program.disciplines.replace('\n', ',').split(',') if d.strip()]
    return render(request, 'faculty/program_detail.html', {
        'program': program,
        'disciplines': disciplines
    })


def department_list(request):
    departments = Department.objects.prefetch_related('specialties').all()
    return render(request, 'faculty/department_list.html', {'departments': departments})


def department_detail(request, pk):
    department = get_object_or_404(
        Department.objects.prefetch_related('specialties', 'teachers'),
        pk=pk
    )
    return render(request, 'faculty/department_detail.html', {'department': department})