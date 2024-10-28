from django.contrib import admin
from .models import Department, Position, User


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(User)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'position', 'date_joined', 'is_active')
    list_filter = ('department', 'position', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
