import csv
from faker import Faker

fake = Faker()

name = fake.name()
email = fake.email()
# print(f"fake name :{fake.name()}")
# print(f"fake country : {fake.country()}")

users = [[fake.name(), fake.email()] for x in range(50)]

print(users)

# Write data into csv file
with open("users.CSV", "w", encoding="UTF-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Email'])
    csv_writer.writerows(users)
