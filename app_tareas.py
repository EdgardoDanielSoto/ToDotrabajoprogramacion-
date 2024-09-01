from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox
from PySide6.QtCore import Qt
from ui_app_tareas import Ui_tareas

class Tareas(QWidget, Ui_tareas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo")

        self._scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self._scroll_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.boton_agregar.clicked.connect(self.tarea_ingresada)
        self.boton_modificar.clicked.connect(self.modificar_tarea)
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)
        self.boton_completada.clicked.connect(self.completar_tarea)

    def tarea_ingresada(self):
        texto_tarea = self.ingreso_texto_tarea.toPlainText()
        if texto_tarea:
            nueva_tarea = QCheckBox(texto_tarea)
            self._scroll_layout.addWidget(nueva_tarea)
            self.ingreso_texto_tarea.clear()

    def modificar_tarea(self):
        nuevo_texto = self.ingreso_texto_tarea.toPlainText()
        if nuevo_texto:
            for i in range(self._scroll_layout.count()):
                widget = self._scroll_layout.itemAt(i).widget()
                if isinstance(widget, QCheckBox) and widget.isChecked():
                    widget.setText(nuevo_texto)
                    break
            self.ingreso_texto_tarea.clear()

    def eliminar_tarea(self):
        for i in range(self._scroll_layout.count()):
            widget = self._scroll_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                self._scroll_layout.removeWidget(widget)
                widget.deleteLater()
                break

    def completar_tarea(self):
        for i in range(self._scroll_layout.count()):
            widget = self._scroll_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                font = widget.font()
                font.setStrikeOut(True)
                widget.setFont(font)

