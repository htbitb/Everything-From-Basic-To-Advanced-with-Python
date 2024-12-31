import sys
import math
from PyQt6.QtWidgets import QGridLayout, QWidget,QApplication,QHBoxLayout,QLabel,QPushButton,QLineEdit,QMessageBox,QMainWindow
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("Coffee Maker")
        self.setGeometry(100, 100, 400, 150)  # Increased the window width
 
    
        # Create widgets
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
 
        # Create a grid layout and set it as the layout for the window
        layout = QGridLayout()
        self.setLayout(layout)
    
        # Add widgets to the layout at specific positions
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)
        layout.addWidget(button1, 1, 0)
        layout.addWidget(button2, 1, 1)
        layout.addWidget(button3, 1, 2)
 
# Create the application from above class
# Q application is used to manage applications resources and the event loop
app = QApplication(sys.argv)
 
# craete an instance of the window
window = Window()
 
# Show method needs to be called to show the created window on screen
window.show()
 
#Start the event loop, use sys.exit to close the program.
sys.exit(app.exec())