from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E1001\n"
        "Employee department: IT\n"
        "Salary: 55000\n"
    )

    assert employee_details("Alice", "E1001", "IT", 55000) == expected_output
