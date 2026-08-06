import webbrowser

from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt

def afficheDoc():
    webbrowser.open("https://ignf.github.io/altibonne-qgis-plugin/")

def afficheerreur(text, titre="titre"):
    msg = QMessageBox()

    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    msg.exec()

def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)

    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", QMessageBox.ButtonRole.YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", QMessageBox.ButtonRole.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True
    return None



