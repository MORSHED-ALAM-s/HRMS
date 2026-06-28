from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, unique=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        db_table = "HR_COMPANY"

    def __str__(self):
        return self.company_name
class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        db_column="COMPANY_ID"
    )

    branch_name = models.CharField(max_length=150)
    address = models.TextField(blank=True)

    class Meta:
        db_table = "HR_BRANCH"

    def __str__(self):
        return self.branch_name
        
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "HR_DEPARTMENT"

    def __str__(self):
        return self.dept_name
    
class Designation(models.Model):
    desig_id = models.AutoField(primary_key=True)

    desig_name = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        db_table = "HR_DESIGNATION"

    def __str__(self):
        return self.desig_name


class Employee(models.Model):
    emp_no = models.CharField(
        max_length=20,
        primary_key=True,
        verbose_name="Employee No"
    )

    full_name = models.CharField(
        max_length=100,
        verbose_name="Full Name"
    )

    father_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    mobile = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )
    company = models.ForeignKey(
    Company,
    on_delete=models.PROTECT,
    db_column="COMPANY_ID",
    related_name="employees"
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.PROTECT,
        db_column="BRANCH_ID",
        related_name="employees"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        db_column="DEPT_ID",
        related_name="employees"
    )
    
    designation = models.ForeignKey(
    Designation,
    on_delete=models.PROTECT,
    db_column="DESIG_ID",
    related_name="employees"
)

    joining_date = models.DateField()

    basic_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "HR_EMPLOYEE"
        ordering = ["emp_no"]

    def __str__(self):
        return f"{self.emp_no} - {self.full_name}"
    
   