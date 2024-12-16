from tkinter import *
import qrcode
from PIL import ImageTk, Image
    
root = Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = qrcode.make(link)
    url.save(file_name, Scale= 2)
    Image.open(file_name)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)
canvas = Canvas(root, height="600", width="400")
canvas.pack()


app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_lable = Label(root, text="Link name")
link_lable = Label(root, text="Link")

canvas.create_window(200, 100, window=name_lable)
canvas.create_window(200, 160, window=link_lable)

name_entry = Entry(root)
link_entry = Entry(root)

canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 190, window=link_entry)

button = Button(text="Generate QR Code", command=generate)
canvas.create_window(200, 220,  window=button)

root.mainloop()