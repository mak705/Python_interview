class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@emailcom'
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))




# Two are instance of the employee class, contains data unique to each instance
emp_1 = Employee('mak','hus',80000)
emp_2 = Employee('TEST','user',66666)


print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

Employee.fullname(emp_2)
emp_2.fullname()



