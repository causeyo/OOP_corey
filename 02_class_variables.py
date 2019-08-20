# instance variables VS class variables

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('wi', 'fon', 50000)

print(Employee.num_of_emps)

emp_2 = Employee('example', 'user', 60000)

print(emp_1.__dict__)
# namespace print

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
# raise amount attribute is not visible in instance

print(Employee.__dict__)
# raise amount attribute is not visible

emp_1.raise_amount = 1.12

print(emp_1.__dict__)
# # raise amount attribute is visible in instance now

print(Employee.num_of_emps)
