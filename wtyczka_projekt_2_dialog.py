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
        self.pushButton_pole.clicked.connect(self.pole)
        self.pushButton_wys.clicked.connect(self.deltaH)
        
    def pole(self):

        selected_features = self.mMapLayerComboBox.currentLayer().selectedFeatures()
        if len(selected_features) >= 3:
            x20 = []
            y20 = []
            i = 0
            for pkt in selected_features:
                   X = float(pkt['x2000'])
                   Y = float(pkt['y2000'])
                   x20.append(X)
                   y20.append(Y)
        sumx = []
        rozy = []
        for x, y in zip(x20, y20):
            if i>0:
                xi = x + xi1
                yi = y - yi1
                sumx.append(xi)
                rozy.append(yi)
            i =+1
            xi1 = x
            yi1 = y
        iloczyn = []
        for Xi, Yi in zip(sumx, rozy):
            il = Xi * Yi
            iloczyn.append(il)
        pola2 = sum(iloczyn)
        pole = pola2/2
        self.lineEdit.setText('Pole figury pomiędzy wybranymi punktami wynosi')
        self.label_wynik.setText(str(pole) + 'm2')
        # else :
        #     self.label_wynik.setText('Liczba punktów powinna być większa od 2')

            
        
    def deltaH(self):
        selected_features = self.mMapLayerComboBox.currentLayer().selectedFeatures()
        if len(selected_features) == 2:
            punkt1 = selected_features[0]
            punkt2 = selected_features[1]
            wysokosc1 = punkt1[H_PLEVRF2007NH]
            wysokosc2 = punkt2[H_PLEVRF2007NH]
            delta = wysokosc2 - wysokosc1
            self.lineEdit.setText('Przewyższenie pomiędzy punktami wynosi')
            self.label_wynik.setText(str(delta) + 'm')
                
        else :
            self.label_wynik.setText('Liczba punktów powinna wynosić 2')