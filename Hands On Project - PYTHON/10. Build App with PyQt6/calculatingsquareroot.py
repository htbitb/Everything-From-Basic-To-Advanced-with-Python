import sys
import math
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QMessageBox,QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("Coffee Maker")
        self.setGeometry(100, 100, 400, 150)  # Increased the window width
 
        self.number_label = QLabel("Enter a number:", self)
        self.number_label.move(20, 20)
        
        self.number_input = QLineEdit(self)
        self.number_input.move(200, 20)
 
        self.calculate_button = QPushButton("Find Root", self)
        self.calculate_button.move(200, 60)
 
        self.result_label = QLabel("Result:", self)
        self.result_label.move(20, 100)
 
        self.calculate_button.clicked.connect(self.calculate_square_root)
 
    def calculate_square_root(self):
        try:
            number = float(self.number_input.text())
            if number >= 0:
                square_root = math.sqrt(number)
                if square_root.is_integer():
                    self.result_label.setText(f"Square Root: {square_root:.4f}")
                else:
                    QMessageBox.warning(self, "Not a Perfect Square", "The number is not a perfect square.")
            else:
                QMessageBox.warning(self, "Invalid Input", "Number must be non-negative.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
 
        
 
# Create the application from above class
# Q application is used to manage applications resources and the event loop
app = QApplication(sys.argv)
 
# craete an instance of the window
window = Window()
 
# Show method needs to be called to show the created window on screen
window.show()
 
#Start the event loop, use sys.exit to close the program.
sys.exit(app.exec())