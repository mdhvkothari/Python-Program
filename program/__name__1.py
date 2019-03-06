import os


#when we import this file into another file then when we call about function then
#it will print all print statement
#for come up form this we use __name__ then we define main now in __name__2 print all this when we
#call main

def name():
    print("maddy")


def main():
        print(os.listdir("/"))
        print("My name is maddy")

print(__name__)

if(__name__=="__main__"):
    main()
