# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_projekt_2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WtyczkaProjekt2DialogBase(object):
    def setupUi(self, WtyczkaProjekt2DialogBase):
        WtyczkaProjekt2DialogBase.setObjectName("WtyczkaProjekt2DialogBase")
        WtyczkaProjekt2DialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(WtyczkaProjekt2DialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")

        self.retranslateUi(WtyczkaProjekt2DialogBase)
        self.button_box.accepted.connect(WtyczkaProjekt2DialogBase.accept) # type: ignore
        self.button_box.rejected.connect(WtyczkaProjekt2DialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WtyczkaProjekt2DialogBase)

    def retranslateUi(self, WtyczkaProjekt2DialogBase):
        _translate = QtCore.QCoreApplication.translate
        WtyczkaProjekt2DialogBase.setWindowTitle(_translate("WtyczkaProjekt2DialogBase", "Projekt 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WtyczkaProjekt2DialogBase = QtWidgets.QDialog()
    ui = Ui_WtyczkaProjekt2DialogBase()
    ui.setupUi(WtyczkaProjekt2DialogBase)
    WtyczkaProjekt2DialogBase.show()
    sys.exit(app.exec_())