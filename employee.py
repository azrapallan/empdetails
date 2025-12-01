import sys
def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Employee department: {department}\n"
        f"Salary: {salary}\n"
    )
    return result
if __name__=="__main__":
    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 55000

    print(employee_details(name, emp_id, department, salary))