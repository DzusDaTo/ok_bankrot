from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def employee_count(self):
        return self.employee_set.count()

    def total_salary(self):
        return self.employee_set.aggregate(total_salary=models.Sum('salary'))['total_salary']

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to='photos/')
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('full_name', 'department')  # Уникальная связка "сотрудник-департамент"

    def __str__(self):
        return f"{self.full_name} - {self.position}"

