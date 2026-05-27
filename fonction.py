import webbrowser

from .mapping_version import *


def afficheDoc():
    webbrowser.open("https://ignf.github.io/altibonne-qgis-plugin/")

def afficheerreur(text, titre="titre"):
    msg = QMessageBox()

    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)

    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True



