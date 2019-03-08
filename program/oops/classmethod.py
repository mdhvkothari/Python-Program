class Employee:
    increment = 1.5
    def __init__(self,name,salary):
        self.name = name
        self.salary  = salary

    #when we don't use any class variable and instance variable then we use
    #we can't pass any argument in this function
    @staticmethod
    def static():
        print "ok"


    @classmethod
    #now we want to increase increment then we use @classmethod and it will pass cls instead to self
    def update(cls,amount):
        cls.increment = amount

    def increase(self):
        self.salary = self.salary*Employee.increment

one = Employee("mdhv",100000)
Employee.update(3)
one.increase()
print one.salary
Employee.static()
