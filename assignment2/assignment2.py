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

