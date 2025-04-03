import pandas as pd

#Task 1
#1
task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],# I change charlie to Charlie in assignment3-test
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print(task1_data_frame)
#2
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
#3
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
#4
task1_older.to_csv("employees.csv", index=False)

#Task 2
#1
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)
#2
json_employees = pd.read_json("additional_employees.json")
print(json_employees)
#3
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

#Task 3
#1
first_three = more_employees.head(3)
print(first_three)
#2
last_two = more_employees.tail(2)
print(last_two)
#3
employee_shape = more_employees.shape
print(employee_shape)
#4
more_employees.to_csv("all_employees.csv", index=False)

#Task 4
#1
dirty_data = pd.read_csv("dirty_data.csv")
print("Dirty DataFrame:")
print(dirty_data)

#2
clean_data = dirty_data.copy()
clean_data.drop_duplicates(inplace=True)
print("\nDataFrame without duplicates:")
print(clean_data)

#3
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAge converted to numeric:")
print(clean_data)

#4
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nSalary converted to numeric:")
print(clean_data)

#5
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nFilled missing values in Age and Salary:")
print(clean_data)

#6
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nHire Date converted to datetime:")
print(clean_data)

#7
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nCleaned Name and Department columns:")
print(clean_data)

# This time the assignment was a bit boring because it was just about following instructions.