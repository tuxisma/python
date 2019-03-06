class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname():
        return '{} {}'.format(self.first, self.last) #in order to get the full name, use self(used because works in each instance)

emp_1 = Employee('ismael', 'garcia', 45000)
emp_2 = Employee('yaneth', 'mendoza', 50000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())


