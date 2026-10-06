from django.contrib import admin
from .models import Department, Specialty, Teacher, HomePageInfo


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    search_fields = ('name', 'head')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'coordinator_name')
    list_filter = ('department',)
    search_fields = ('name', 'code', 'coordinator_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'academic_degree', 'department')
    list_filter = ('department', 'academic_degree')
    search_fields = ('full_name', 'position')


@admin.register(HomePageInfo)
class HomePageInfoAdmin(admin.ModelAdmin):
    list_display = ('faculty_name',)
