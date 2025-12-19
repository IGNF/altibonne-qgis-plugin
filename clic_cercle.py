from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtCore import Qt

class CercleClickable(QGraphicsEllipseItem):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.setFlags(QGraphicsEllipseItem.ItemIsSelectable | QGraphicsEllipseItem.ItemIsFocusable)
        self.setAcceptHoverEvents(True)  # facultatif pour hover
        self.setAcceptedMouseButtons(Qt.LeftButton)  # accepter clic gauche

    def mousePressEvent(self, event):
        print("Cercle cliqué !")
        super().mousePressEvent(event)

    def hoverEnterEvent(self, event):
        print("survol cercle")
        self.setCursor(Qt.PointingHandCursor)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(event)