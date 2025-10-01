from employee import Employee, SalaryEmployee, HourlyEmployee, CommisionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:\n')
        for i in self.employees:
            print('Paycheck for', i.name, type(i), f'${i.calculate_paycheck():,.2f}')
        print('--------------------')


def main():
    my_company = Company()
    e1 = SalaryEmployee('Sarah', 20000)
    e2 = HourlyEmployee('Bob', 30, 15)
    e3 = CommisionEmployee('Jude', 52000, 4, 100)
    my_company.add_employee(e1)
    my_company.add_employee(e2)
    my_company.add_employee(e3)

    my_company.display_employees()

main()