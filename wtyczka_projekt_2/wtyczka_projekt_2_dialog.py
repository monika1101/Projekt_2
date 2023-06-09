# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaProjekt2Dialog
                                 A QGIS plugin
 Wtyczka liczy różnicę wysokości i pole powierzchni pomiędzy wskazanymi punktami.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Monika Palęga, Paulina Pluta
        email                : monika.palega.stud@pw.edu.pl, paulina.pluta.stud@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_projekt_2_dialog_base.ui'))


class WtyczkaProjekt2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaProjekt2Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
