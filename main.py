import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit ,QGroupBox, QPushButton,QTableWidget, QHeaderView
from PySide6 import QtCore
from PySide6.QtGui import QFont



class CRUD(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450,500)


        Cdr_1 = QGroupBox(self)
        Cdr_1.setGeometry(10,10,430,160)
        Cdr_1.setTitle("Datos de contacto")
       
        self.nombre = QLineEdit(Cdr_1)
        self.nombre.setGeometry(80,30,320,20)

        self.empleo = QLineEdit(Cdr_1)
        self.empleo.setGeometry(80,60,320,20)

        self.email = QLineEdit(Cdr_1)
        self.email.setGeometry(80,90,320,20)

        text = QLabel(Cdr_1)
        text.setText("Nombre")
        text.setGeometry(30,30,50,20)


        text_1 = QLabel(Cdr_1)
        text_1.setText("Empleo")
        text_1.setGeometry(30,60,50,20)

        text_2 = QLabel(Cdr_1)
        text_2.setText("Email")
        text_2.setGeometry(30,90,50,20) 


        btn_borra = QPushButton("Borrar",Cdr_1)
        btn_borra.setGeometry(90,120,100,25)

       

        btn_nuevo = QPushButton("Nuevo",Cdr_1)
        btn_nuevo.setGeometry(200,120,90,25)
        btn_nuevo.clicked.connect(self.add_guest)

        btn_modificar = QPushButton("Modificar",Cdr_1)
        btn_modificar.setGeometry(300,120,100,25)


       
        #Esto es la QTableWidget Esto es la tabla con sus columan y row con la geometria #
        self.tableta = QTableWidget(self)
        self.tableta.setGeometry(10,180,430,300)
        self.tableta.setColumnCount(3)
        self.tableta.setHorizontalHeaderLabels(["Nombre","Empleo","Email"])

      
        #----------------------------------------------------------- Estilo del Table ------------------------------------------------------------------------------------------# 

        #Color de la tableta nomas #
        fnt = QFont()
        fnt.setPointSize(10)
        fnt.setBold(True)
     

        #tableta vertical
        ver = QHeaderView(QtCore.Qt.Vertical, self.tableta)
        self.tableta.setVerticalHeader(ver)
        ver.setFont(fnt)



        # Esto Es para que las Column ocupen toda la tabla #
        headerView = QHeaderView(QtCore.Qt.Horizontal, self.tableta)
        self.tableta.setHorizontalHeader(headerView)
        headerView.setSectionResizeMode(2, QHeaderView.Stretch)
        headerView.setSectionsClickable(True)
        headerView.setFont(fnt)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    def add_guest(self):
        rowPosition = self.tableta.rowCount()
        self.tableta.insertRow(rowPosition)

        nombre = self.nombre.text()
        traba = self.empleo.text()
        Gmai = self.email.text()


App=QApplication(sys.argv)
window = CRUD()
window.show()
App.exec_()