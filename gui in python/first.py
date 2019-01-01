from tkinter import * 
g = Tk()
g.title('First')
#size of the gui window 500x500 is size and 0 +0 is the loaction
g.geometry('500x500+0+0')
#add label
#pack is the class of label it show label
mylabel1 = Label(text='First text',fg='blue').place(x=200,y=200)
mylabel2 = Label(text='second text').place(x=200,y=300)



#button

btn1 = Button(text='Submit',fg='red',bg='green').pack()













#for ourtput
g.mainloop()

















