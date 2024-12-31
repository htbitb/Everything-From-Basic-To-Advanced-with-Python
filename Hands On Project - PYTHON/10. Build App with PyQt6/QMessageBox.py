from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Coffee Maker")
        self.setGeometry(100,100,400,400)
        
        self.button = QPushButton(self)
        self.button.setGeometry(150,80,200,40)
        self.button.clicked.connect(self.show_message)
        
    def show_message(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Message Box Title")
        msg.setText("This is a simple QMessage Box")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        
        
        result = msg.exec()
        if result == QMessageBox.StandardButton.Ok:
            print("Ok button clicked")
        else:
            print("Cancel button clicked")

# Create the application from above class
# Q application is used to manage applications resources and the event loop
app = QApplication(sys.argv)
 
# craete an instance of the window
window = Window()
 
# Show method needs to be called to show the created window on screen
window.show()
 
#Start the event loop, use sys.exit to close the program.
sys.exit(app.exec())