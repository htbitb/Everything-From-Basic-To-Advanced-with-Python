from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QCheckBox
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Coffee Maker")
        self.setGeometry(0,0,400,400)
        
        #total cost of drink
        self.cost = 0
        
        label = QLabel(self)
        label.setText("Choose your options")
        label.move(20,20)
        
        #add checkbox 
        sugar_check = QCheckBox(self)
        sugar_check.setText("Sugar ($ 0.5)")
        sugar_check.move(20,40)
        sugar_check.toggled.connect(self.sugar_checked)
        
        milk_check = QCheckBox(self)
        milk_check.setText("milk ($ 1)")
        milk_check.move(20,60)
        milk_check.toggled.connect(self.milk_checked)
        
        #label
        self.label = QLabel(self)
        self.label.setText("Total cost: $0")
        self.label.resize(200,20)
        self.label.move(20,90)
    
    def sugar_checked(self, checked):
        if checked:
            self.cost += 0.5
            self.label.setText(f"Total cost: ${str(self.cost)}")
        else:
            self.cost -= 0.5
            self.label.setText(f"Total cost: ${str(self.cost)}")
    
    def milk_checked(self, checked):
        if checked:
            self.cost += 1
            self.label.setText(f"Total cost: ${str(self.cost)}")
        else:
            self.cost -= 1
            self.label.setText(f"Total cost: ${str(self.cost)}")
        
        
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())