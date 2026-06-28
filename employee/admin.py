
from django.contrib import admin
from .models import Company
from .models import Department, Designation, Employee

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_id", "company_name", "phone")
    search_fields = ("company_name",)

    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("dept_id", "dept_name")
    search_fields = ("dept_name",)


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ("desig_id", "desig_name")
    search_fields = ("desig_name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "emp_no",
        "full_name",
        "department",
        "designation",
        "joining_date",
        "basic_salary",
        "is_active",
    )

    search_fields = (
        "emp_no",
        "full_name",
    )

    list_filter = (
        "department",
        "designation",
        "is_active",
    )