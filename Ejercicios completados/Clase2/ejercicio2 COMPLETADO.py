import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDateEdit,
                             QRadioButton, QSpinBox, QPushButton, QMessageBox, QButtonGroup)
from PyQt5.QtCore import Qt, QDate

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 350)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        #CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #e9f1f7;
            }

            QLineEdit {
                background-color: #fff;
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
                           
            QDateEdit {
                background-color: white;
                border: 1px solid gray;
                border-radius: 4px;
                padding: 3px;
            }
            QSpinBox {
                background-color: white;
                border: 1px solid gray;
                border-radius: 4px;
                padding: 3px;
            }
        """)

        #SUBTITULO
        self.lblSubtitulo = QLabel("Formulario de Compra")
        self.layout.addWidget(self.lblSubtitulo,0,0,0,0)
        self.lblSubtitulo.setAlignment(Qt.AlignHCenter)
        self.lblSubtitulo.setStyleSheet("QLabel { font-size: 16pt; font-style: bold; }")

        #NOMBRE
        self.lblNombre = QLabel("Nombre:")
        self.layout.addWidget(self.lblNombre,1,0)
        self.inputbox_nombre = QLineEdit()
        self.layout.addWidget(self.inputbox_nombre,1,1)

        #APELLIDO
        self.lblApellido = QLabel("Apellido:")
        self.layout.addWidget(self.lblApellido,2,0)
        self.inputbox_Apellido = QLineEdit()
        self.layout.addWidget(self.inputbox_Apellido,2,1)

        #DNI
        self.lblDNI = QLabel("DNI:")
        self.layout.addWidget(self.lblDNI,3,0)
        self.inputbox_DNI = QLineEdit()
        self.layout.addWidget(self.inputbox_DNI,3,1)

        #ORIGEN
        self.lblOrigen = QLabel("Origen:")
        self.layout.addWidget(self.lblOrigen,4,0)
        self.combobox_origen = QComboBox()
        self.combobox_origen.addItems(["Argentina","Chile","Mexico"])
        self.layout.addWidget(self.combobox_origen,4,1)

        #DESTINO
        self.lblDestino = QLabel("Destino:")
        self.layout.addWidget(self.lblDestino,5,0)
        self.combobox_destino = QComboBox()
        self.combobox_destino.addItems(["Argentina","Chile","Mexico"])
        self.layout.addWidget(self.combobox_destino,5,1)

        #FECHA
        self.lblFecha = QLabel("Fecha de vuelo:")
        self.layout.addWidget(self.lblFecha,6,0)
        self.date_editFecha = QDateEdit() # QDateEdit permite seleccionar una fecha.
        self.layout.addWidget(self.date_editFecha,6,1)

        #CLASE
        self.lblClase = QLabel("Clase:")
        self.layout.addWidget(self.lblClase,7,0)
        self.turista = QRadioButton("Turista")
        self.layout.addWidget(self.turista,7,1)
        self.ejecutiva = QRadioButton("Ejecutiva")
        self.layout.addWidget(self.ejecutiva,8,1)

        self.grupo_botones = QButtonGroup()
        self.grupo_botones.addButton(self.turista)
        self.grupo_botones.addButton(self.ejecutiva)

        #CANTIDAD DE PASAJEROS
        self.lblCantidad = QLabel("Cantidad pasajeros:")
        self.layout.addWidget(self.lblCantidad,9,0)
        self.spinbox_pasajeros = QSpinBox() # Permite seleccionar una cantidad
        self.spinbox_pasajeros.setMinimum(1) # Aplica minimo "1" como numero en el QSpinBox
        self.spinbox_pasajeros.setMaximum(10) # Aplica maximo "10" como numero en el QSpinBox
        self.layout.addWidget(self.spinbox_pasajeros,9,1)
        
        #CONFIRMACION
        self.btnConfirmacion = QPushButton("Comprar")
        self.layout.addWidget(self.btnConfirmacion,10,0,1,2)
        self.btnConfirmacion.clicked.connect(self.validacionDatos)
    
    def validacionDatos(self):
        #Verificar si todos los campos estan rellenados
        self.fecha_actual = QDate.currentDate()
        self.fecha_actual = self.fecha_actual.toString()
        if not self.inputbox_nombre.text().strip() or not self.inputbox_Apellido.text().strip() or not self.inputbox_DNI.text().strip():
            QMessageBox.warning(self,"Error", "Rellena los campos")    
        #Verificar que el origen y el destino sean distintos
        elif self.combobox_origen.currentText() == self.combobox_destino.currentText():
            QMessageBox.warning(self,"Error", "No se permite mismo origen y destino")
        #Verificar fecha
        elif self.date_editFecha.date().toString() < self.fecha_actual:
            QMessageBox.warning(self,"Error", "La fecha no puede ser hoy")
        #Verificar que se haya seleccionado una clase
        elif self.grupo_botones.checkedButton() is None:
            QMessageBox.warning(self,"Error", "Seleccione una clase")
        #Compra exitosa
        else:
            QMessageBox.information(self, f"Compra exitosa", 
            f"Nombre: {self.inputbox_nombre.text()}\n"
            f"Apellido: {self.inputbox_Apellido.text()}\n"
            f"DNI: {self.inputbox_DNI.text().strip()}\n"
            f"ORIGEN: {self.combobox_origen.currentText()}\n"
            f"DESTINO: {self.combobox_destino.currentText()}\n"
            f"FECHA: {self.date_editFecha.text()}\n"
            f"CLASE: {self.grupo_botones.checkedButton().text()}\n"
            f"CANTIDAD: {self.spinbox_pasajeros.text()}\n") 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())