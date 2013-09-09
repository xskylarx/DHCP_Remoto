# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sun Sep  8 14:30:45 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(245, 97)
        Form.setMinimumSize(QtCore.QSize(245, 97))
        Form.setMaximumSize(QtCore.QSize(245, 97))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/usuario.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.l_password = QtGui.QLabel(Form)
        self.l_password.setGeometry(QtCore.QRect(10, 45, 51, 16))
        self.l_password.setObjectName(_fromUtf8("l_password"))
        self.btn_aceptar = QtGui.QPushButton(Form)
        self.btn_aceptar.setGeometry(QtCore.QRect(50, 70, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/llave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_aceptar.setIcon(icon1)
        self.btn_aceptar.setAutoDefault(False)
        self.btn_aceptar.setFlat(False)
        self.btn_aceptar.setObjectName(_fromUtf8("btn_aceptar"))
        self.l_usuario = QtGui.QLabel(Form)
        self.l_usuario.setGeometry(QtCore.QRect(10, 13, 46, 13))
        self.l_usuario.setObjectName(_fromUtf8("l_usuario"))
        self.t_usuario = QtGui.QLineEdit(Form)
        self.t_usuario.setGeometry(QtCore.QRect(65, 10, 141, 20))
        self.t_usuario.setFrame(True)
        self.t_usuario.setObjectName(_fromUtf8("t_usuario"))
        self.btn_salir = QtGui.QPushButton(Form)
        self.btn_salir.setGeometry(QtCore.QRect(126, 70, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/salir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_salir.setIcon(icon2)
        self.btn_salir.setFlat(False)
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.t_password = QtGui.QLineEdit(Form)
        self.t_password.setGeometry(QtCore.QRect(65, 40, 141, 20))
        self.t_password.setFrame(True)
        self.t_password.setEchoMode(QtGui.QLineEdit.Password)
        self.t_password.setDragEnabled(True)
        self.t_password.setObjectName(_fromUtf8("t_password"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(210, 10, 21, 21))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("icons/usuario.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(208, 40, 21, 21))
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("icons/candado.png")))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.t_usuario, self.t_password)
        Form.setTabOrder(self.t_password, self.btn_aceptar)
        Form.setTabOrder(self.btn_aceptar, self.btn_salir)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "DHCP Remoto Login", None))
        self.l_password.setText(_translate("Form", "Password:", None))
        self.btn_aceptar.setToolTip(_translate("Form", "Accesar a la Aplicacion", None))
        self.btn_aceptar.setText(_translate("Form", "Continuar", None))
        self.l_usuario.setText(_translate("Form", "Usuario:", None))
        self.t_usuario.setToolTip(_translate("Form", "Nombre de Usuario", None))
        self.btn_salir.setToolTip(_translate("Form", "Salir de la aplicacion", None))
        self.btn_salir.setText(_translate("Form", "Salir", None))
        self.t_password.setToolTip(_translate("Form", "Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

