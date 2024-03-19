from faker import Faker
import pandas as pd

fake = Faker()

names_with_prefix = []
records = 50

while len(names_with_prefix) < records:
    names_with_prefix.append("pt_"+fake.name())
data = {
    'Name': names_with_prefix,
    'Email': [fake.email() for _ in range(len(names_with_prefix))],
}
# Create a Pandas Dataframe
synthetic_data = pd.DataFrame(data)
print(synthetic_data)




