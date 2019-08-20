# method - function associated with class
'''
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# each instance is unique

emp_1.first = 'wi'
emp_1.last = 'fon'
emp_1.email = 'wi.fon@company.com'
emp_1.pay = 50000

emp_2.first = 'example'
emp_2.last = 'user'
emp_2.email = 'example.user@company.com'
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)
'''
# in such way class features are unused
# make it better
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('wi', 'fon', 50000)
emp_2 = Employee('example', 'user', 60000)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
# instead of this we can use method in class

print(emp_1.fullname())
emp_1.fullname()
print(Employee.fullname(emp_1))