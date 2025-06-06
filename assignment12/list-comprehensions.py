import pandas as pd

df = pd.read_csv("../csv/employees.csv")

# Task 3.1 
names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print(names)

# Task 3.2
names_with_e = [name for name in names if "e" in name]
print(names_with_e)
