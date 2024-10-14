from tkinter import *
import ast
root = Tk()

display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
i = 0
class Control:
    # this function gets the number to be added and ads it to input
    def get_number(self, num):
        global i
        # insert the num at index i
        display.insert(i,num)
        # Increment the index
        i+=1
    
    def get_operation(self, operator):
        global i
        length = len(operator)
        display.insert(i,operator)
        i+=length
    
    def clear_all(self):
        display.delete(0, END)
    
    
    def calculate(self):
        entire_string = display.get()
        try:
            node = ast.parse(entire_string,mode="eval")
            result = eval(compile(node,'<string>','eval'))
            self.clear_all()
            display.insert(0, result)
        except Exception:
            self.clear_all()
            display.insert(0, "Error")
    
    
    def undo(self):
        entire_string = display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            self.clear_all()
            display.insert(0, new_string)
        else:
            self.clear_all()
            display.insert(0, "")