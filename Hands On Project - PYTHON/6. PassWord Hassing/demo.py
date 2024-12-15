from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$AGY1IC/lUmWGkCW1Fu/HGepA8qaAIO16K88Ljg1mDE/5i706mj9BS'
    entered_password = bytes(password, encoding='utf-8')
    
    if bcrypt.checkpw(entered_password, hash):
        print('Login Successful')
    else:
        print('Invalid Password')
        
root = Tk()
root.geometry("600x600")


password_entry = Entry()
password_entry.pack()
password_entry.get()
button = Button(text="validate", command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()





        