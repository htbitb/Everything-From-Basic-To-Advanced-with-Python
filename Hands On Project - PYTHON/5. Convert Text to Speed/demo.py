from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()


def textToSpeed():
    if button:
        text = entry.get()
        language = 'en'
        output = gTTS(text=text, lang=language,slow=False)
        output.save('output.mp3')
        
        os.system('start output.mp3')





entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text='Start', command=textToSpeed)
canvas.create_window(200,230,window=button)


# with open('./5. Convert Text to Speed/sample.txt', 'r') as re:
#     data = re.read()

# output = gTTS(text=data, lang='en',slow=False)
# output.save('output.mp3')

# os.system("start output.mp3")

root.mainloop()