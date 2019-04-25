
class employee:
    raise_amt=1.04
    def __init__ (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
   #    
       
       
a= employee("Madhav","Kothari",60000)
b= employee("Madv","Kthari",600000)
print(a.fullname())


class developer(employee):
     def __init__ (self,first,last,pay,program):
         employee.__init__(self,first,last,pay)#we don't need to again we class it from class employee
         self.program=program
     def program1(self):
         print(self.program)
     
#ingerit
a= developer("Madhav","Kothari",60000,'python')
b= developer("Madv","Kthari",600000,'python')
print(b.fullname())
b.program1()

