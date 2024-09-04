import sys
from PySide6.QtWidgets import QApplication
from app_tareas import Tareas

aplicacion = QApplication(sys.argv)

ventana = Tareas()
ventana.show()

aplicacion.exec()