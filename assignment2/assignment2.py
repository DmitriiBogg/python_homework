import csv
import traceback

#Q2
def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}" for trace in trace_back]
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")
        if str(e):
            print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

# Q3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

#Q4
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

#Q5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Q6
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

#Q7
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

sort_by_last_name()
print(employees)

#Q8
def employee_dict(row):
    result = {}
    for i, key in enumerate(employees["fields"]):
        if key != "employee_id":
            result[key] = row[i]
    return result

print(employee_dict(employees["rows"][0]))

#Q9
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)
    return result

print(all_employees_dict())
# Questions 2 to 9 are like an Excel table, so pretty simple. Though, again, there are a lot of new information, so brain is going crazy))

#Q10
import os

def get_this_value():
    return os.environ.get("THISVALUE")

#Q11 
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("fire boll")
print(custom_module.secret)

#Q12
def read_minutes():
    def read_file(filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            fields = next(reader)
            rows = [tuple(row) for row in reader]
        return {"fields": fields, "rows": rows}

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes() # forget about it first time ))

# The structure is similar to how employees before.
#  Are we convert it to a tuple so that it can be put into a set? I'm still a bit slow and confused with this.

#Q13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
print(minutes_set)

#Q14
from datetime import datetime

def create_minutes_list():
    as_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), as_list))
    return converted

minutes_list = create_minutes_list()
print(minutes_list)

#Q15
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    formatted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))

    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"]) 
        writer.writerows(formatted)  

    return formatted

write_sorted_list()
# Q14-15 is challenge. I understand the logic and how it should be. It's just the syntax that's new, I think.
# Actually, if we ignore the new syntax and its rules, it's pretty simple and intuitively clear.
