import os
import subprocess

from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt


def afficheDoc():
    fichier = os.path.join(os.path.dirname(__file__), "altibonne.pdf")
    if not os.path.isfile(fichier):
        afficheerreur("La documentation est introuvable", "Information")
    else:
        subprocess.Popen(['start', '', fichier], shell=True)

def afficheerreur(text, titre="titre"):
    msg = QMessageBox()

    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", QMessageBox.YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", QMessageBox.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True



