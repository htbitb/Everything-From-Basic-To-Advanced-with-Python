import sys
import math
from PyQt6.QtWidgets import QVBoxLayout, QWidget,QApplication,QHBoxLayout,QLabel,QPushButton,QLineEdit,QMessageBox,QMainWindow
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(0,0,400,150)
        
        layout = QGridLayout(self)
        self.setLayout(layout)
        
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display,0,0,1,4)
        
        
        
        # number button created
        self.buttons = [QPushButton(str(i)) for i in range(10)]
        for i, button in enumerate(self.buttons):
            row, col = divmod(i,3)
            layout.addWidget(button, row+1, col)
        for button in self.buttons:
            button.clicked.connect(self.number_clicked)
        
        # operator button created
        operators = ["+", "-", "*", "/"]
        self.operator_buttons = [QPushButton(i) for i in operators]
        for i, operator_but in enumerate(self.operator_buttons):
            layout.addWidget(operator_but, i+1, 3)
        # Now add these oeperator buttons to the layout below
        for button in self.operator_buttons:
            button.clicked.connect(self.operator_clicked)
        
        #clear button
        self.clear_button = QPushButton("C")
        self.clear_button.clicked.connect(self.clear)
        
        #equal button
        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.calculate)
        
        #Add = and C button
        layout.addWidget(self.clear_button,4,2)
        layout.addWidget(self.equals_button,4,1)
        
        # Create three variables, current input, previous input and current operator
        self.current_input = "0"
        self.current_operator =""
        self.previous_operator=""
    
    def number_clicked(self):
        digit = self.sender().text()
        
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self.display.setText(str(self.current_input))
        
    def operator_clicked(self):
        operator = self.sender().text()
        
        if self.current_operator == "":
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input="0"
        else:
            # call the calculate method here
            #Same as above
            self.calculate()
            self.previous_input = self.current_input
            self.current_operator = operator
            self.current_input = "0"
    
    def calculate(self):
        if self.current_operator=="+":
            result = str(float(self.previous_input)+float(self.current_input))
        elif self.current_operator=="-":
            result = str(float(self.previous_input)-float(self.current_input))
        elif self.current_operator=="*":
            result = str(float(self.previous_input)*float(self.current_input))
        elif self.current_operator=="/":
            if self.current_input=="0":
                result="Error"
            else:
                result = str(float(self.previous_input)/float(self.current_input))
        else:
            result=self.current_input
        self.display.setText(result)
        self.current_input=result
        self.current_operator=""
    
    def clear(self):
        self.display.setText("0")
        self.current_input = "0"
        self.current_operator =""
        self.previous_operator=""
        
app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())