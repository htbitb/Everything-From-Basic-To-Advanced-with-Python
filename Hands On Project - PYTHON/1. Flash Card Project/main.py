from tkinter import *
from APP.AppControler import FlashCardApp
from DAL.DataHandler import DataHandler
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

class FlashCardUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flash Card App")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.canvas = Canvas(width=800, height=526)
        self.card_front_img = PhotoImage(file='DAL/images/card_front.png')
        self.card_back_img = PhotoImage(file='DAL/images/card_back.png')
        self.card_bkg = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cross_image = PhotoImage(file='DAL/images/wrong.png')
        self.unknown_button = Button(image=self.cross_image, highlightthickness=0, command=self.next_card)
        self.unknown_button.grid(row=1, column=0)
        self.check_image = PhotoImage(file='DAL/images/right.png')
        self.known_button = Button(image=self.check_image, highlightthickness=0, command=self.is_known)
        self.known_button.grid(row=1, column=1)

    def set_app(self, app):
        self.app = app

    def display_card(self, card, language, text_color, background_image):
        self.canvas.itemconfig(self.card_title, text=language, fill=text_color)
        self.canvas.itemconfig(self.card_word, text=card[language], fill=text_color)
        self.canvas.itemconfig(self.card_bkg, image=background_image)

    def next_card(self):
        self.app.next_card()

    def is_known(self):
        self.app.is_known()

    def run(self):
        self.app.next_card()
        self.window.mainloop()

# Initialize components
data_handler = DataHandler("DAL/data/words_to_learn.csv", "DAL/data/french_words.csv")
flash_card_ui = FlashCardUI()
flash_card_app = FlashCardApp(data_handler, flash_card_ui)

# Start the UI
flash_card_ui.run()
