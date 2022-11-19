import sys
from PyQt5.QtWidgets import *

class basicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200,200,300,150)

        self.label1 = QLabel('bilangan 1')
        self.numberEdit1 = QLineEdit()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.numberEdit1)

        self.label2 = QLabel('bilangan 2')
        self.numberEdit2 = QLineEdit()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.numberEdit2)


        self.rbtn1= QRadioButton('Penjumlahan')
        self.rbtn1.setChecked(True)
        self.rbtn2= QRadioButton('Pengurangan')
        self.rbtn3= QRadioButton('Pembagian')
        self.rbtn4= QRadioButton('Perkalian')
        hbox3= QHBoxLayout()
        hbox3.addWidget(self.rbtn1)
        hbox3.addWidget(self.rbtn2)
        hbox3.addWidget(self.rbtn3)
        hbox3.addWidget(self.rbtn4)

        self.label3 = QLabel('Hasil')
        self.label4=QLineEdit(self)
        self.label4.setReadOnly(True)
        self.hasil=QPushButton("Calculate")
        self.hasil.clicked.connect(self.calcButtonProses)
            
        Vlayout= QVBoxLayout()
        Vlayout.addLayout(hbox1)
        Vlayout.addLayout(hbox2)
        Vlayout.addLayout(hbox3)
        Vlayout.addStretch()
        Vlayout.addWidget(self.label3)
        Vlayout.addWidget(self.label4)
        Vlayout.addWidget(self.hasil)
        self.setLayout(Vlayout)
        self.setWindowTitle('PyQt5 Radio Button Example')
        self.show()
    def calcButtonProses(self):
        a= float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())

        if self.rbtn1.isChecked():
            c=a+b
        
        elif self.rbtn2.isChecked():
            c=a-b


        elif self.rbtn3.isChecked():
            if b==0 or a==0:
                QMessageBox.information(self, 'informasi', 'Tidak bisa dibagi 0')
                c='inv'
            else:
                c=a/b
        elif self.rbtn4.isChecked():
            c=a*b

        self.label4.setText(str(c))

    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form=basicRadiobuttonExample()
    form.show()
    app.exec_()
        
        