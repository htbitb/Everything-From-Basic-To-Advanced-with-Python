from tkinter import *
import ast
from module_control import * 

users = Control()

numbers =[1,2,3,4,5,6,7,8,9]
counter=0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root,text=button_text,width=2,height=2,command=lambda text=button_text: users.get_number(text))
        button.grid(row=x+2,column=y)
        counter+=1
 
#adding zero on row 5
button = Button(root,text="0",width=2,height=2,command=lambda:users.get_number(0))
button.grid(row=5,column=1)
 
 
#adding AC and = button
Button(root, text="AC",width=2,height=2,command=lambda:users.clear_all()).grid(row=5, column=0)
Button(root, text="=",width=2,height=2,command=lambda :users.calculate()).grid(row=5, column=2)
 
#adding the delete / undo button
Button(root, text="<-", width=2,height=2, command=lambda: users.undo()).grid(row=5, column=4)
 
#now column 3 is empty, lets fill it up with operations
count = 0
operations =['+','-','*','/','*3.14',"%","(","**",")","**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = Button(root,text=operations[count],width=2,height=2,command= lambda text=operations[count] : users.get_operation(text))
            count+=1
            button.grid(row=x+2,column=y+3)
 
root.mainloop()

