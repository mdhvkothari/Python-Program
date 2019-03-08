class Employee:
    increment = 1.5
    no_of_employee=0
    #__init__ is a constructor when we make a instance to the class then constructor will always call
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increase = 2
        Employee.no_of_employee += 1

    def increaseby2(self):
        self.salary = self.salary * self.increase
    #here self.increase first it will check if increase is in constructor if not present then it will go for class variabel
    def increaseby15(self):
    #if we use Employee.increase then this will direct use the Employee variabel
        self.salary = self.salary*Employee.increment
one = Employee("mdhv","kothari",50000)
print Employee.no_of_employee
two = Employee("chirag","singh",100000)
print Employee.no_of_employee

one.increaseby15()
print one.salary

one.increaseby2()
print one.salary

#for check all variable in class
print one.__dict__
print two.__dict__

#for class variabel
print Employee.__dict__
