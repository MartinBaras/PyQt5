import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                             QRadioButton, QButtonGroup, QComboBox, QCheckBox, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario") # Establecer titulo de ventana.
        self.setGeometry(100, 100, 400, 300) # Establecer geometria de ventana (Posicion y tamaño)
        layout = QGridLayout() # Organiza los widgets en filas y columnas
        self.setLayout(layout) # Aplicar Grid Layout a la ventana

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

        #SUBTITULO
        self.subtitulo = QLabel("Formulario de Registro") # Crear etiqueta
        layout.addWidget(self.subtitulo,0,0,0,0) # Agregar etiqueta a la ventana
        self.subtitulo.setAlignment(Qt.AlignHCenter) # Alinear etiqueta al centro hacia arriba
        self.subtitulo.setFont(QFont("Arial", 16, QFont.Bold)) # Establecer fuente "Arial", Tamaño 16, Negrita

        #NOMBRE
        self.nombre = QLabel("Nombre:") # Crear etiqueta
        layout.addWidget(self.nombre,1,0) # Agregar etiqueta a la ventana

        self.inputbox_nombre = QLineEdit() # Crear QLineEdit/Inputbox
        layout.addWidget(self.inputbox_nombre,1,1) # Agregar inputbox a la ventana
        
        #EMAIL
        self.email = QLabel("Email:")
        layout.addWidget(self.email,2,0)

        self.inputbox_email = QLineEdit()
        layout.addWidget(self.inputbox_email,2,1)
        
        #CONTRASEÑA
        self.contraseña = QLabel("Contraseña:")
        layout.addWidget(self.contraseña,3,0)

        self.inputbox_contraseña = QLineEdit()
        layout.addWidget(self.inputbox_contraseña,3,1)
        self.inputbox_contraseña.setEchoMode(QLineEdit.Password) # Oculta el texto del input box.

        #GENERO
        self.genero = QLabel("Genero:")
        layout.addWidget(self.genero,4,0)

        self.genero_masculino = QRadioButton("Masculino")
        layout.addWidget(self.genero_masculino,4,1)

        self.genero_femenino = QRadioButton("Femenino")
        layout.addWidget(self.genero_femenino,4,2)

        grupo_botones = QButtonGroup()
        grupo_botones.addButton(self.genero_masculino)
        grupo_botones.addButton(self.genero_femenino)

        #PAIS
        self.pais = QLabel("Pais:") # Crear etiqueta
        layout.addWidget(self.pais,5,0) # Agregar etiqueta a la ventana

        self.comboboxpais = QComboBox() # QComboBox permite elegir una opción de una lista desplegable.
        layout.addWidget(self.comboboxpais,5,1)

        self.comboboxpais.addItems(["Argentina", "Chile", "México", "Colombia", "Bolivia"])

        #TERMINOS Y CONDICIONES
        self.terminos = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.terminos,6,1)

        #VALIDACION
        self.validacion = QPushButton("Registrarse")
        layout.addWidget(self.validacion,7,1)
        self.validacion.clicked.connect(self.validar_datos)

    def validar_datos(self):
        if not self.inputbox_nombre.text().strip() or not self.inputbox_email.text().strip() or not self.inputbox_contraseña.text().strip():
            QMessageBox.warning(self,"Error", "Rellena los campos")
        elif self.terminos.isChecked()==False: # Chequea el estado del QPushButton
            QMessageBox.warning(self,"Error", "Acepte terminos y condiciones")
        else:
            QMessageBox.information(self, "Exito", "Registro exitoso")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())