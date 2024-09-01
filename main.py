import sys
from PySide6.QtWidgets import QApplication
from app_tareas import Tareas

app = QApplication(sys.argv)

window = Tareas()
window.show()

app.exec()