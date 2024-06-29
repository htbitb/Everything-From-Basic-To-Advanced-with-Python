import random

class FlashCardApp:
    def __init__(self, data_handler, ui):
        self.data_handler = data_handler
        self.ui = ui
        self.current_card = {}
        self.flip_timer = None
        self.ui.set_app(self)  # Inject self into the UI after creation
        self.next_card()

    def next_card(self):
        if self.flip_timer:
            self.ui.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.data_handler.to_learn)
        self.ui.display_card(self.current_card, "French", "black", self.ui.card_front_img)
        self.flip_timer = self.ui.window.after(3000, self.flip_card)

    def flip_card(self):
        self.ui.display_card(self.current_card, "English", "white", self.ui.card_back_img)

    def is_known(self):
        self.data_handler.remove_known_card(self.current_card)
        self.next_card()