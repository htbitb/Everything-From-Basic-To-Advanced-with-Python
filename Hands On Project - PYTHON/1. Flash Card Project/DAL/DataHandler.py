import pandas as pd

class DataHandler:
    def __init__(self, to_learn_path, original_path):
        self.to_learn_path = to_learn_path
        self.original_path = original_path
        self.to_learn = self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv(self.to_learn_path)
        except FileNotFoundError:
            original_data = pd.read_csv(self.original_path)
            return original_data.to_dict(orient="records")
        else:
            return data.to_dict(orient="records")

    def remove_known_card(self, card):
        self.to_learn.remove(card)
        self.save_data()

    def save_data(self):
        data = pd.DataFrame(self.to_learn)
        data.to_csv(self.to_learn_path, index=False)