from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.count = 0
        
    def initUI(self):
        
        self.setWindowTitle("My First PyQt window")
        self.setGeometry(0,0,400,400)
        
        #
        name_label = QLabel(self)
        name_label.setText("Enter your name")
        name_label.move(60, 10)
        
        self.name = QLineEdit(self)
        # name.resize(20,20)
        self.name.move(60,50)  
        
        #new code added to create a button
        button = QPushButton(self)
        button.setText("Add")
        button.move(100, 70)
        button.clicked.connect(self.buttonCLicked)
        
        
        self.result_label = QLabel(self)
        self.result_label.setFixedSize(150, 20)
        self.result_label.move(60, 120)
        
    def carinfo(self):
        with open("10. Build App with PyQt6\car.png"):
            image_label = QLabel(self)
            pixmap = QPixmap('10. Build App with PyQt6\car.png')
            image_label.setPixmap(pixmap)
            image_label.move(50,0)
        #car name
        name_label = QLabel(self)
        name_label.setText("My Car")
        name_label.setFont(QFont("Arial",20))
        name_label.move(170, 170)
        
        #Engine Spec
        engine_label = QLabel(self)
        engine_label.setText("Engine Capacity: 4L TFSI")
        engine_label.setFont(QFont("Arial",16))
        engine_label.move(20, 210)
        
        #Feature
        feature_label = QLabel(self)
        feature_label.setText("Feature: ABS, EBD, ADAS")
        feature_label.setFont(QFont("Arial",16))
        feature_label.move(20, 240)
        
        #Model
        model_label = QLabel(self)
        model_label.setText("Models: 2.2 Petro, 1.8 Diesel")
        model_label.setFont(QFont("Arial",16))
        model_label.move(20, 270)
        
        #Pricing
        pricing_label = QLabel(self)
        pricing_label.setText("Pricing: $80.000")
        pricing_label.setFont(QFont("Arial",16))
        pricing_label.move(20, 300)

    def buttonCLicked(self):
        self.result_label.setText("Your Name is:" + self.name.text())
            
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())