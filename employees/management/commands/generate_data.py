from django.core.management.base import BaseCommand
from employees.models import Department, Employee
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate fake data for departments and employees'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = []

        # Create 25 departments
        for i in range(5):
            parent = None
            for j in range(5):
                department = Department.objects.create(
                    name=f'Department {i}-{j}',
                    parent=parent
                )
                departments.append(department)
                parent = department

        # Create 50000 employees
        for _ in range(50000):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_this_decade(),
                salary=random.uniform(30000, 120000),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated data'))
