import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, 
                             QAction, QFileDialog, QMessageBox, QStatusBar,
                             QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto")
        self.setGeometry(100, 100, 800, 600)

        # CSS
        self.setStyleSheet("""
            QTextEdit {
                background-color: #e9f1f7;
                font-family: 'Comic Sans MS';
                font-size: 16px;
            }

            QAction {
                font-size: 14px;
                color: #333;
            }
            
            QLineEdit:focus { 
                border: 1px solid #0078d7;
                background-color: #f7fbff;
            }
        """)

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escribe aquí tu texto...")

    def crear_menus(self):
        # Obtener la barra de menús
        menubar = self.menuBar()
        
        # Crear menú Archivo
        menu_archivo = menubar.addMenu('&Archivo')
        menu_editar = menubar.addMenu('&Editar')
        menu_ayuda = menubar.addMenu('&Ayuda')
        
        # ARCHIVO - NUEVO
        accion_nuevo = QAction('&Nuevo', self)
        accion_nuevo.setShortcut(QKeySequence.New)  # Ctrl+N
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        menu_archivo.addAction(accion_nuevo)

        # ARCHIVO - ABRIR
        accion_abrir = QAction('&Abrir', self)
        accion_abrir.setShortcut(QKeySequence.Open)  # Ctrl+O
        accion_abrir.triggered.connect(self.abrir_archivo)
        menu_archivo.addAction(accion_abrir)

        # ARCHIVO - GUARDAR
        accion_guardar = QAction('&Guardar', self)
        accion_guardar.setShortcut(QKeySequence.Save)  # Ctrl+S
        accion_guardar.triggered.connect(self.guardar_archivo)
        menu_archivo.addAction(accion_guardar)

        # ARCHIVO - SALIR
        accion_salir = QAction('&Salir', self)
        accion_salir.setShortcut(QKeySequence.Quit)  # Ctrl+Q
        accion_salir.triggered.connect(self.salir)
        menu_archivo.addAction(accion_salir)

        # EDITAR - CORTAR
        accion_cortar = QAction('&Cortar', self)
        accion_cortar.setShortcut(QKeySequence.Cut)  # Ctrl+X
        accion_cortar.triggered.connect(self.editor.cut)
        menu_editar.addAction(accion_cortar)
        
        # EDITAR - COPIAR
        accion_copiar = QAction('&Copiar', self)
        accion_copiar.setShortcut(QKeySequence.Copy)  # Ctrl+C
        accion_copiar.triggered.connect(self.editor.copy)
        menu_editar.addAction(accion_copiar)

        # EDITAR - PEGAR
        accion_pegar = QAction('&Pegar', self)
        accion_pegar.setShortcut(QKeySequence.Paste)  # Ctrl+V
        accion_pegar.triggered.connect(self.editor.paste)
        menu_editar.addAction(accion_pegar)

        # AYUDA - ACERCA DE
        accion_acerca = QAction('&Acerca', self)
        accion_acerca.triggered.connect(self.acerca_de)
        menu_ayuda.addAction(accion_acerca)

    def nuevo_archivo(self):
        respuesta = QMessageBox.question(self, 'Nuevo archivo','¿Desea guardar los cambios?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
            self.editor.clear()
        elif respuesta == QMessageBox.No:
            self.editor.clear()
    
    def abrir_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos de texto (*.txt)')
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')
    
    def guardar_archivo(self):
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if archivo:
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write(self.editor.toPlainText())
                    QMessageBox.information(self, 'Guardado', f'Archivo guardado correctamente')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo guardar el archivo:\n{e}')


    def acerca_de(self):
        # Mostrar información del programa
        QMessageBox.information(self, 'Acerca de', 'Editor de Texto v1.0\n\nCreado con PyQt5\nPara aprender desarrollo de interfaces.')
    
    def salir(self):
        # Preguntar si desea guardar antes de salir
        respuesta = QMessageBox.question(self, 'Salir', '¿Desea guardar los cambios antes de salir?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
        elif respuesta == QMessageBox.No:
            self.close()

    def crear_barra_estado(self):
        # Crear y configurar barra de estado
        self.statusBar().showMessage('Listo')
        # Conectar eventos del editor para mostrar información
        self.editor.cursorPositionChanged.connect(self.actualizar_cursor)
    def actualizar_cursor(self):
        cursor = self.editor.textCursor()
        linea = cursor.blockNumber() + 1
        columna = cursor.columnNumber() + 1
        self.statusBar().showMessage(f'Línea: {linea}, Columna: {columna}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorTexto()
    editor.crear_menus()
    editor.crear_barra_estado()
    editor.show()
    sys.exit(app.exec_())