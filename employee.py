class Employee:
    _count=0
    def __init__(self):
        Employee._count=Employee._count+1
    def display(self):
        print("The no. of employees:",Employee._count)

emp=Employee();
print(emp._count)
emp.display()


