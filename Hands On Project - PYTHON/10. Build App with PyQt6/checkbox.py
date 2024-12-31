from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QCheckBox
import sys
from PyQt6.QtGui import QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Check Box")
        self.setGeometry(0,0,400,400)
        
        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText("Sugar")
        sugar_checkbox.move(20,40)
        sugar_checkbox.toggled.connect(self.sugar_check)
    
    def sugar_check(self, checked):
        if checked:
            print("Sugar added")
        else:
            print("Sugar not added")
        
        
        
        
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())