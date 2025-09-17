import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QDateEdit, QVBoxLayout, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #e9f1f7;
            }

            QLineEdit {
                background-color: #fff;
                font-family: 'Comic Sans MS';
                border: 1px solid gray;
                border-radius: 4px;
                padding: 4px;
            }
            
            QLineEdit:focus { 
                border: 1px solid #0078d7;
                background-color: #f7fbff;
            }
            
            QLabel {
                font-family: 'Comic Sans MS';
                font-size: 14px;
                color: #333;
            }
            
            QPushButton {
                background-color: #0078d7;
                color: white;
                border-radius: 6px;
                padding: 6px;
                font-weight: bold;
            }
            
            QPushButton:hover {
                background-color: #005fa3;
            }

            QDateEdit {
                background-color: #fff;
                border: 1px solid gray;
                border-radius: 4px;
                padding: 4px;
            }
        """)
        
        #Subtitulo
        self.lblSubTitulo=QLabel("Formulario de Afiliación")
        self.layout.addWidget(self.lblSubTitulo,0,0,1,2)
        self.lblSubTitulo.setAlignment(Qt.AlignHCenter)
        self.lblSubTitulo.setFont(QFont("Comic Sans", 20, QFont.Bold))

        #Nombre
        self.lblNombre = QLabel("Nombre:")
        self.layout.addWidget(self.lblNombre,1,0)
        self.lblNombre.setAlignment(Qt.AlignLeft)
        self.lblNombre.setFont(QFont("Comic Sans", 11, QFont.Bold))

        self.inputboxNombre = QLineEdit()
        self.layout.addWidget(self.inputboxNombre,1,1)

        #Apellido
        self.lblApellido = QLabel("Apellido:")
        self.layout.addWidget(self.lblApellido,2,0)
        self.lblApellido.setAlignment(Qt.AlignLeft)
        self.lblApellido.setFont(QFont("Comic Sans", 11, QFont.Bold))

        self.inputboxApellido = QLineEdit()
        self.layout.addWidget(self.inputboxApellido,2,1)

        #DNI
        self.lblDNI = QLabel("DNI:")
        self.layout.addWidget(self.lblDNI,3,0)
        self.lblDNI.setAlignment(Qt.AlignLeft)
        self.lblDNI.setFont(QFont("Comic Sans", 11, QFont.Bold))

        self.inputboxDNI = QLineEdit()
        self.layout.addWidget(self.inputboxDNI,3,1)

        #Fecha de nacimiento
        self.lblFechaNac = QLabel("Fecha de nacimiento:")
        self.layout.addWidget(self.lblFechaNac,4,0)
        self.lblFechaNac.setAlignment(Qt.AlignLeft)
        self.lblFechaNac.setFont(QFont("Comic Sans", 11, QFont.Bold))

        self.inputboxFechaNac = QDateEdit()
        self.layout.addWidget(self.inputboxFechaNac,4,1)

        #Salir
        self.btnSalirFormulario = QPushButton("Salir")
        self.layout.addWidget(self.btnSalirFormulario,5,0,1,2)
        self.btnSalirFormulario.setFont(QFont("Comic Sans", 11, QFont.Bold))
        self.btnSalirFormulario.clicked.connect(self.funcionSalir)

    def funcionSalir(self):
        exit()
        
class VentanaHerramientas(QWidget):
    def __init__(self, ventana_form):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        self.ventana_form=ventana_form
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #e9f1f7;
            }

            QLineEdit {
                background-color: #fff;
                font-family: 'Comic Sans MS';
                border: 1px solid gray;
                border-radius: 4px;
                padding: 4px;
            }
            
            QLineEdit:focus { 
                border: 1px solid #0078d7;
                background-color: #f7fbff;
            }
            
            QLabel {
                font-family: 'Comic Sans MS';
                font-size: 14px;
                color: #333;
            }
            
            QPushButton {
                background-color: #0078d7;
                color: white;
                border-radius: 6px;
                padding: 6px;
                font-weight: bold;
            }
            
            QPushButton:hover {
                background-color: #005fa3;
            }

            QCheckBox {
                font-size: 13px;
                color: #222;
            }

            QComboBox {
                background-color: white;
                border: 1px solid gray;
                border-radius: 4px;
                padding: 3px;
            }
        """)
        
        #Subtitulo
        self.lblSubTitulo=QLabel("Herramientas")
        self.layout.addWidget(self.lblSubTitulo)
        self.lblSubTitulo.setAlignment(Qt.AlignHCenter)
        self.lblSubTitulo.setFont(QFont("Comic Sans", 20, QFont.Bold))

        #Guardar
        self.btnGuardar = QPushButton("Guardar")
        self.layout.addWidget(self.btnGuardar)
        self.btnGuardar.setFont(QFont("Comic Sans", 11, QFont.Bold))
        self.btnGuardar.clicked.connect(self.funcionGuardar)
    
        #Abrir
        self.btnAbrir = QPushButton("Abrir")
        self.layout.addWidget(self.btnAbrir)
        self.btnAbrir.setFont(QFont("Comic Sans", 11, QFont.Bold))

        #Buscar
        self.btnBuscar = QPushButton("Buscar")
        self.layout.addWidget(self.btnBuscar)
        self.btnBuscar.setFont(QFont("Comic Sans", 11, QFont.Bold))

        #Salir
        self.btnSalirHerramientas = QPushButton("Salir")
        self.layout.addWidget(self.btnSalirHerramientas)
        self.btnSalirHerramientas.setFont(QFont("Comic Sans", 11, QFont.Bold))
        self.btnSalirHerramientas.clicked.connect(self.ventana_form.funcionSalir)

    def funcionGuardar(self):
        nombre = self.ventana_form.inputboxNombre.text().strip()
        apellido = self.ventana_form.inputboxApellido.text().strip()
        dni = self.ventana_form.inputboxDNI.text().strip()
        fecha_nac = self.ventana_form.inputboxFechaNac.date().toString("dd/MM/yyyy")
        if not nombre or not apellido or not dni:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
        else:
            QMessageBox.information(self,"Datos Guardados",f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nFecha Nacimiento: {fecha_nac}")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form)

    ventana_form.show()
    ventana_herr.show()
    sys.exit(app.exec_())