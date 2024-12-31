import sys
import math
from PyQt6.QtWidgets import QVBoxLayout, QWidget,QApplication,QHBoxLayout,QLabel,QPushButton,QLineEdit,QMessageBox,QMainWindow
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("Coffee Maker")
        self.setGeometry(100, 100, 400, 150)  # Increased the window width
 
    
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
 
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(button1)
        hbox_1.addWidget(button2)
 
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(button3)
        hbox_2.addWidget(button4)
 
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
 
        self.setLayout(vbox)
 
# Create the application from above class
# Q application is used to manage applications resources and the event loop
app = QApplication(sys.argv)
 
# craete an instance of the window
window = Window()
 
# Show method needs to be called to show the created window on screen
window.show()
 
#Start the event loop, use sys.exit to close the program.
sys.exit(app.exec())
