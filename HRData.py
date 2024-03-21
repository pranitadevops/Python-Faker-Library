from faker import Faker
import random

fake = Faker()

# Generate fake sensor data
for _ in range(10):
    employee_id = fake.random_number(10)
    department = fake.random_element(elements=("IT", "Marketing"))
    hire_date = fake.date()
    print(f"employee_id:{employee_id},department :{department},hire_date:{hire_date}")
