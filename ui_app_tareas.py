# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_tareas.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QTextEdit, QWidget)

class Ui_tareas(object):
    def setupUi(self, tareas):
        if not tareas.objectName():
            tareas.setObjectName(u"tareas")
        tareas.resize(350, 450)
        tareas.setMinimumSize(QSize(350, 450))
        tareas.setMaximumSize(QSize(350, 450))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        tareas.setFont(font)
        tareas.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-top-color: rgb(36, 31, 49);\n"
"gridline-color: rgb(36, 31, 49);")
        self.Encabezado = QLabel(tareas)
        self.Encabezado.setObjectName(u"Encabezado")
        self.Encabezado.setGeometry(QRect(90, 0, 161, 41))
        font1 = QFont()
        font1.setFamilies([u"Roboto Light"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        self.Encabezado.setFont(font1)
        self.boton_agregar = QPushButton(tareas)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setGeometry(QRect(10, 140, 331, 25))
        font2 = QFont()
        font2.setFamilies([u"Roboto Light"])
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(True)
        self.boton_agregar.setFont(font2)
        self.boton_agregar.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"\n"
"")
        self.boton_modificar = QPushButton(tareas)
        self.boton_modificar.setObjectName(u"boton_modificar")
        self.boton_modificar.setGeometry(QRect(10, 410, 89, 25))
        self.boton_modificar.setFont(font2)
        self.boton_modificar.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"\n"
"")
        self.boton_eliminar = QPushButton(tareas)
        self.boton_eliminar.setObjectName(u"boton_eliminar")
        self.boton_eliminar.setGeometry(QRect(250, 410, 89, 25))
        self.boton_eliminar.setFont(font2)
        self.boton_eliminar.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"")
        self.pregunta_quehacer = QLabel(tareas)
        self.pregunta_quehacer.setObjectName(u"pregunta_quehacer")
        self.pregunta_quehacer.setGeometry(QRect(80, 40, 191, 31))
        font3 = QFont()
        font3.setFamilies([u"Roboto Light"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setUnderline(True)
        self.pregunta_quehacer.setFont(font3)
        self.ingreso_texto_tarea = QTextEdit(tareas)
        self.ingreso_texto_tarea.setObjectName(u"ingreso_texto_tarea")
        self.ingreso_texto_tarea.setGeometry(QRect(10, 70, 331, 61))
        self.ingreso_texto_tarea.setStyleSheet(u"*{\n"
"    border-radius: 10px;\n"
"    border: 0.5px solid gray;\n"
"padding: 5px;\n"
"}\n"
"")
        self.area_de_lista = QScrollArea(tareas)
        self.area_de_lista.setObjectName(u"area_de_lista")
        self.area_de_lista.setGeometry(QRect(10, 170, 331, 231))
        self.area_de_lista.setStyleSheet(u"*{\n"
"    border-radius: 10px;\n"
"    border: 0.5px solid gray;\n"
"padding: 5px;\n"
"background-color: rgb(46, 194, 126);\n"
"}")
        self.area_de_lista.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 319, 219))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.area_de_lista.setWidget(self.scrollAreaWidgetContents)
        self.boton_completada = QPushButton(tareas)
        self.boton_completada.setObjectName(u"boton_completada")
        self.boton_completada.setGeometry(QRect(120, 410, 111, 25))
        self.boton_completada.setFont(font2)
        self.boton_completada.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"\n"
"")

        self.retranslateUi(tareas)

        QMetaObject.connectSlotsByName(tareas)
    # setupUi

    def retranslateUi(self, tareas):
        tareas.setWindowTitle(QCoreApplication.translate("tareas", u"ToDo", None))
        self.Encabezado.setText(QCoreApplication.translate("tareas", u"Lista de Tareas", None))
        self.boton_agregar.setText(QCoreApplication.translate("tareas", u"Agregar", None))
        self.boton_modificar.setText(QCoreApplication.translate("tareas", u"Modificar", None))
        self.boton_eliminar.setText(QCoreApplication.translate("tareas", u"Eliminar", None))
        self.pregunta_quehacer.setText(QCoreApplication.translate("tareas", u"\u00bfQue hay que hacer?", None))
        self.ingreso_texto_tarea.setPlaceholderText(QCoreApplication.translate("tareas", u"Ingrese aqu\u00ed la tarea", None))
        self.boton_completada.setText(QCoreApplication.translate("tareas", u"Completada", None))
    # retranslateUi

