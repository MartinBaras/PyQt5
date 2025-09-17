import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
                             QPushButton, QTextEdit, QComboBox, QMessageBox,
                             QGroupBox, QListWidget, QListWidgetItem, QSplitter)
from PyQt5.QtCore import Qt

class SistemaDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Docentes")
        self.setGeometry(100, 100, 800, 600)
        
        # Archivo donde se guardarán los datos
        self.archivo_datos = "docentes.txt"
        
        # Configurar interfaz
        self.configurar_interfaz()
        self.cargar_datos()
        
        # CSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
                           
            QLabel {
                font-family: "Comic Sans MS";    
            }
            QGroupBox {
                font-weight: bold;
                font-family: "Comic Sans MS"; 
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                font-family: "Comic Sans MS"; 
                left: 10px;
                padding: 0 10px 0 10px;
                color: #495057;
            }
            QPushButton {
                background-color: #007bff;
                font-family: "Comic Sans MS"; 
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
            QLineEdit, QComboBox {
                font-family: "Comic Sans MS"; 
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #007bff;
            }
            QListWidget {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
        """)

    def configurar_interfaz(self):
        # Widget central con división
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal horizontal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Crear splitter para dividir la pantalla
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Panel izquierdo: Formulario y botones
        panel_izquierdo = self.crear_panel_formulario()
        splitter.addWidget(panel_izquierdo)
        
        # Panel derecho: Lista y detalles
        panel_derecho = self.crear_panel_lista()
        splitter.addWidget(panel_derecho)
        
        # Configurar proporciones del splitter
        splitter.setSizes([400, 600])

    def crear_panel_formulario(self):
        """Crear el panel con el formulario de datos"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Crear grupo de formulario
        grupo_form = QGroupBox("Datos del Docente")
        form_layout = QGridLayout()
        
        # LEGAJO
        self.legajo_edit = QLineEdit()
        self.legajo_edit.setPlaceholderText("Ej: DOC001")
        form_layout.addWidget(QLabel("Legajo:"), 0, 0)
        form_layout.addWidget(self.legajo_edit, 0, 1)

        # NOMBRE
        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Ej: Martin")
        form_layout.addWidget(QLabel("Nombre:"), 1, 0)
        form_layout.addWidget(self.nombre_edit, 1, 1)

        # APELLIDO
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Ej: Baras")
        form_layout.addWidget(QLabel("Apellido:"), 2, 0)
        form_layout.addWidget(self.apellido_edit, 2, 1)

        # DNI
        self.dni_edit = QLineEdit()
        self.dni_edit.setPlaceholderText("Ej: 12552153")
        form_layout.addWidget(QLabel("DNI:"), 3, 0)
        form_layout.addWidget(self.dni_edit, 3, 1)

        # EMAIL
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Ej: mb15215@gmail.com")
        form_layout.addWidget(QLabel("Email:"), 4, 0)
        form_layout.addWidget(self.email_edit, 4, 1)

        # TELEFONO
        self.telefono_edit = QLineEdit()
        self.telefono_edit.setPlaceholderText("Ej: 3462-921452")
        form_layout.addWidget(QLabel("Telefono:"), 5, 0)
        form_layout.addWidget(self.telefono_edit, 5, 1)

        # MATERIA
        self.materia_combo = QComboBox()
        self.materia_combo.addItems(["Matematicas", "Tecnologia", "Software", "Hardware", "Taller"])
        form_layout.addWidget(QLabel("Materia:"), 6, 0)
        form_layout.addWidget(self.materia_combo, 6, 1)

        # CATEGORIA
        self.categoria_combo = QComboBox()
        self.categoria_combo.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])
        form_layout.addWidget(QLabel("Categoría:"), 7, 0)
        form_layout.addWidget(self.categoria_combo, 7, 1)
        
        grupo_form.setLayout(form_layout)
        layout.addWidget(grupo_form)
        
        # Crear grupo de botones
        grupo_botones = QGroupBox("Acciones")
        botones_layout = QVBoxLayout()
        
        # AGREGAR
        self.btn_agregar = QPushButton("Agregar Docente")
        self.btn_agregar.clicked.connect(self.agregar_docente)
        botones_layout.addWidget(self.btn_agregar)

        # BUSCAR
        self.btn_buscar = QPushButton("Buscar Docente")
        self.btn_buscar.clicked.connect(self.buscar_docente)
        botones_layout.addWidget(self.btn_buscar)

        # MODIFICAR
        self.btn_modificar = QPushButton("Modificar Docente")
        self.btn_modificar.clicked.connect(self.modificar_docente)
        botones_layout.addWidget(self.btn_modificar)

        # ELIMINAR
        self.btn_eliminar = QPushButton("Eliminar Docente")
        self.btn_eliminar.clicked.connect(self.eliminar_docente)
        botones_layout.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)
        botones_layout.addWidget(self.btn_limpiar)
        
        #GRUPO BOTONES
        grupo_botones.setLayout(botones_layout)
        layout.addWidget(grupo_botones)
        
        widget.setLayout(layout)
        return widget

    def cargar_datos(self):
        # Verificar si existe el archivo
        if not os.path.exists(self.archivo_datos):
            return
        
        # Leer líneas del archivo
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if linea.strip():  # Ignorar líneas vacías
                        datos = linea.strip().split('|')
                        if len(datos) == 8:  # Verificar que tenga todos los campos
                            self.agregar_a_lista(datos)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al cargar datos:\n{e}')
            
    def guardar_datos(self):
        # Obtener todos los elementos de la lista
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for i in range(self.lista_docentes.count()):
                    item = self.lista_docentes.item(i)
                    datos = item.data(Qt.UserRole)  # Datos completos guardados en el item
                    linea = '|'.join(datos) + '\n'
                    archivo.write(linea)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al guardar datos:\n{e}')
            
    def agregar_docente(self):
        # Validar campos obligatorios
        if not self.legajo_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El legajo es obligatorio')
            return
    
        # Verificar que el legajo no exista
        legajo = self.legajo_edit.text().strip()
        if self.buscar_por_legajo(legajo):
            QMessageBox.warning(self, 'Error', 'Ya existe un docente con ese legajo')
            return
        
        # Recopilar datos del formulario
        datos = [
            self.legajo_edit.text().strip(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_combo.currentText(),
            self.categoria_combo.currentText()
        ]
        
        # Agregar a la lista y guardar
        self.agregar_a_lista(datos)
        self.guardar_datos()
        self.limpiar_formulario()
        QMessageBox.information(self, 'Éxito', 'Docente agregado correctamente')

    def crear_panel_lista(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Crear área de búsqueda
        busqueda_layout = QHBoxLayout()
        busqueda_layout.addWidget(QLabel("Buscar:"))
        self.busqueda_edit = QLineEdit()
        self.busqueda_edit.setPlaceholderText("Buscar por apellido, nombre o legajo...")
        self.busqueda_edit.textChanged.connect(self.filtrar_lista)
        busqueda_layout.addWidget(self.busqueda_edit)
        layout.addLayout(busqueda_layout)
        
        # Crear lista de docentes
        self.lista_docentes = QListWidget()
        self.lista_docentes.itemClicked.connect(self.mostrar_detalles)
        layout.addWidget(self.lista_docentes)
        
        # Crear área de detalles
        grupo_detalles = QGroupBox("Detalles del Docente Seleccionado")
        self.detalles_text = QTextEdit()
        self.detalles_text.setReadOnly(True)
        self.detalles_text.setMaximumHeight(200)
        detalles_layout = QVBoxLayout()
        detalles_layout.addWidget(self.detalles_text)
        grupo_detalles.setLayout(detalles_layout)
        layout.addWidget(grupo_detalles)

        widget.setLayout(layout)
        return widget
    
    def agregar_a_lista(self, datos):
        # Crear texto para mostrar en la lista
        texto_item = f"{datos[2]}, {datos[1]} ({datos[0]})"  # Apellido, Nombre (Legajo)
        item = QListWidgetItem(texto_item)
        item.setData(Qt.UserRole, datos)  # Guardar datos completos
        self.lista_docentes.addItem(item)
 
    def filtrar_lista(self):
        # Obtener texto de búsqueda
        texto_busqueda = self.busqueda_edit.text().lower()
        
        # Mostrar/ocultar items según coincidencia
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            # Buscar en legajo, nombre y apellido
            coincide = (texto_busqueda in datos[0].lower() or  # legajo
                       texto_busqueda in datos[1].lower() or   # nombre
                       texto_busqueda in datos[2].lower())     # apellido
            item.setHidden(not coincide)
        pass
    
    def mostrar_detalles(self, item):
        # Obtener datos del item seleccionado
        datos = item.data(Qt.UserRole)
        """indice_materias=0
        materias=["Legajo","Nombre","Apellido","DNI","Email","Teléfono","Materia","Categoría"]
        for e in datos:
            indice_materias=indice_materias+1
            print(materias[indice_materias-1], e)"""
        detalles = f"""
        Legajo: {datos[0]}
        Nombre: {datos[1]}
        Apellido: {datos[2]}
        DNI: {datos[3]}
        Email: {datos[4]}
        Teléfono: {datos[5]}
        Materia: {datos[6]}
        Categoría: {datos[7]}
        """
        self.detalles_text.setPlainText(detalles)

    def buscar_docente(self):
        # Pedir legajo a buscar
        legajo = self.legajo_edit.text().strip()
        if not self.legajo_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'Ingrese un legajo para buscar')
            return
        
        # Buscar en la lista y seleccionar
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0].lower() == legajo.lower():
                self.lista_docentes.setCurrentItem(item)
                self.mostrar_detalles(item)
                return
        
        QMessageBox.information(self, 'No encontrado', f'No se encontró docente con legajo: {legajo}')
    
    def buscar_por_legajo(self, legajo):
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0] == legajo:
                return item
        return None

    def modificar_docente(self):
        # Verificar que hay un elemento seleccionado
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para modificar')
            return
        
        # Cargar datos en el formulario
        datos = item_actual.data(Qt.UserRole)
        self.legajo_edit.setText(datos[0])
        self.nombre_edit.setText(datos[1])
        self.apellido_edit.setText(datos[2])
        self.dni_edit.setText(datos[3])
        self.email_edit.setText(datos[4])
        self.telefono_edit.setText(datos[5])
        self.materia_combo.setCurrentText(datos[6])
        self.categoria_combo.setCurrentText(datos[7])
        
        # Cambiar botón "Agregar" por "Actualizar"
        self.btn_agregar.setText("Actualizar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(lambda: self.actualizar_docente(item_actual))
    
    def actualizar_docente(self, item):
        if not item:
            QMessageBox.warning(self, "Error", "No se seleccionó ningún docente para actualizar.")
            return

        # Obtener nuevos datos desde el formulario
        nuevos_datos = [
        self.legajo_edit.text().strip(),
        self.nombre_edit.text().strip(),
        self.apellido_edit.text().strip(),
        self.dni_edit.text().strip(),
        self.email_edit.text().strip(),
        self.telefono_edit.text().strip(),
        self.materia_combo.currentText(),
        self.categoria_combo.currentText()
        ]

        # Validar campos básicos
        if not nuevos_datos[0]:
            QMessageBox.warning(self, "Error", "El campo Legajo es obligatorio.")
            return

        # Actualizar visualmente el texto que se muestra en la lista
        texto_item = f"{nuevos_datos[2]}, {nuevos_datos[1]} ({nuevos_datos[0]})"
        item.setText(texto_item)

        # Actualizar los datos ocultos asociados al item
        item.setData(Qt.UserRole, nuevos_datos)

        # Guardar todo nuevamente en el archivo
        self.guardar_datos()
        QMessageBox.information(self, "Éxito", "Docente actualizado correctamente.")

    def eliminar_docente(self):
        # Verificar selección
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para eliminar')
            return
        # Pedir confirmación
        datos = item_actual.data(Qt.UserRole)
        respuesta = QMessageBox.question(self, 'Confirmar eliminación',
                                       f'¿Está seguro de eliminar a {datos[1]} {datos[2]}?',
                                       QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
        # Eliminar de la lista y guardar
            row = self.lista_docentes.row(item_actual)
            self.lista_docentes.takeItem(row)
            self.guardar_datos()
            QMessageBox.information(self, 'Éxito', 'Docente eliminado correctamente')
            
    def limpiar_formulario(self):
        # Limpiar todos los campos
        self.legajo_edit.clear()
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.email_edit.clear()
        self.telefono_edit.clear()
        self.categoria_combo.setCurrentIndex(0)
        self.categoria_combo.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sistema = SistemaDocentes()
    sistema.show()
    sys.exit(app.exec_())
