from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QMessageBox
from PySide6.QtCore import Qt
from ui_app_tareas import Ui_tareas

class Tareas(QWidget, Ui_tareas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo")

        self._scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self._scroll_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.boton_agregar.clicked.connect(self.__tarea_ingresada)
        self.boton_modificar.clicked.connect(self.__modificar_tarea)
        self.boton_eliminar.clicked.connect(self.__eliminar_tarea)
        self.boton_completada.clicked.connect(self.__completar_tarea)

    def __tarea_ingresada(self):
        texto_tarea = self.ingreso_texto_tarea.toPlainText()
        if len(texto_tarea) > 20:
            self.mostrar_advertencia("La tarea no puede exceder los 20 caracteres.")
        elif texto_tarea:
            self._scroll_layout.addWidget(QCheckBox(texto_tarea))
            self.ingreso_texto_tarea.clear()

    def mostrar_advertencia(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)

    def __modificar_tarea(self):
        nuevo_texto = self.ingreso_texto_tarea.toPlainText()
        if nuevo_texto:
            for lista in range(self._scroll_layout.count()):
                widget = self._scroll_layout.itemAt(lista).widget()
                if isinstance(widget, QCheckBox) and widget.isChecked():
                    widget.setText(nuevo_texto)
                    break
            self.ingreso_texto_tarea.clear()

    def __eliminar_tarea(self):
        for lista in range(self._scroll_layout.count()):
            widget = self._scroll_layout.itemAt(lista).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                self._scroll_layout.removeWidget(widget)
                widget.deleteLater()
                break

    def __completar_tarea(self):
        for lista in range(self._scroll_layout.count()):
            widget = self._scroll_layout.itemAt(lista).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                font = widget.font()
                font.setStrikeOut(True)
                widget.setFont(font)

