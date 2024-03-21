from faker import Faker

fake = Faker()

# print(f"fake name : {fake.name()}")
# print(f"fake mail {fake.email()}")
# print(fake.country())
# print(fake.name())
# print(fake.text())
# print(fake.latitude(), fake.longitude())
# print(fake.url())



# print("***Spanish***")
# fake = Faker("es_ES")
# print(fake.name())
# print(fake.email())
# print(fake.country())
# print(fake.name())
# print(fake.latitude(), fake.longitude())


print("""Hindi Language""")
fake = Faker("hi_IN")
for i in range(0, 10):

    print(f"fake name :{fake.name()}")
    print(f"fake country : {fake.country()}")

