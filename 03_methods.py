# regularmethods VS classmethods VS staticmethods

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    #alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('wi', 'fon', 50000)
emp_2 = Employee('example', 'user', 60000)


'''
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.23)
# classmethod changes class variable so it is visible for each instance
emp_1.set_raise_amt(1.23) # same effect as above

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
'''

# checking staticmethod
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))