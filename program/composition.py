# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:32:29 2018

@author: Madhav
"""

class marsrocket():
    def __init__ (self,name,distance,maker):
        self.rocket= Rocket(name, distance)
        self.maker=  maker
    
    def getprint(self):
        return ("%kouch nahi%," (self.rocket.name, self.maker))
    
    
if  __name__ == "__main__" :    
    z= marsrocket("ptna","madhav","ISRO")
    print(z.getprint())
        