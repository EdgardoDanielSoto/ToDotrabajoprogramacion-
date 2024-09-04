from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QMessageBox
from PySide6.QtCore import Qt
from ui_app_tareas import Ui_tareas
import logotareas_rc

class Tareas(QWidget, Ui_tareas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo")

        self._scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self._scroll_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    def boton_agregar_clicked(self):
        texto_tarea = self.ingreso_texto_tarea.toPlainText()
        if len(texto_tarea) > 55:
            self.mostrar_advertencia("La tarea no puede exceder los 55 caracteres.")
        elif texto_tarea:
            self._scroll_layout.addWidget(QCheckBox(texto_tarea))
            self.ingreso_texto_tarea.clear()

    def boton_modificar_clicked(self):
        nuevo_texto = self.ingreso_texto_tarea.toPlainText()
        if nuevo_texto:
            for lista in range(self._scroll_layout.count()):
                widget = self._scroll_layout.itemAt(lista).widget()
                if QCheckBox and widget.isChecked():
                    widget.setText(nuevo_texto)
                    widget.setChecked(False)
            self.ingreso_texto_tarea.clear()

    def boton_eliminar_clicked(self):
        for lista in range(self._scroll_layout.count()):
            item = self._scroll_layout.itemAt(lista)
            if item is not None:
                widget = item.widget()
                if  QCheckBox and widget.isChecked():
                    self._scroll_layout.removeWidget(widget)
                    widget.deleteLater()

    def boton_completar_clicked(self):
        for lista in range(self._scroll_layout.count()):
            widget = self._scroll_layout.itemAt(lista).widget()
            if QCheckBox and widget.isChecked():
                fuente = widget.font()
                fuente.setStrikeOut(True)
                widget.setFont(fuente)

    def mostrar_advertencia(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)


