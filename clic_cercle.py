from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from qgis._core import QgsDistanceArea, QgsPointXY
from qgis.core import QgsCoordinateTransform, QgsProject
from qgis.gui import QgsVertexMarker


class CercleClickable(QGraphicsEllipseItem):
    def __init__(self, x, y, w, h,indice = None,entite_id = None,parent = None):
        super().__init__(x, y, w, h)
        self.setFlags(QGraphicsEllipseItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.LeftButton)  # accepter clic gauche
        self.indice = indice
        self.entite_id = entite_id
        self.parent = parent
        self.marker = None


    def mousePressEvent(self, event):
        # Projection du point vers le CRS du canvas
        src_crs = self.parent.layer.crs() if self.parent.layer else QgsProject.instance().crs()
        dest_crs = self.parent.iface.mapCanvas().mapSettings().destinationCrs()
        transform = QgsCoordinateTransform(src_crs, dest_crs, QgsProject.instance())
        point_canvas = transform.transform(self.entite_id)

        self.parent.dlg.pushButtonChangeZpoint.setEnabled(True)
        # self.lineedit_z_interpole.setText(str(self.z_interpole())
        self.parent.dlg.lineEditZInterpole.setText(str(self.z_interpole()))

        for m in self.parent.liste_markers:
            self.parent.iface.mapCanvas().scene().removeItem(m)
        self.parent.liste_markers.clear()

        self.marker = QgsVertexMarker(self.parent.iface.mapCanvas())
        self.marker.setColor(Qt.red)
        self.marker.setIconSize(10)
        self.marker.setIconType(QgsVertexMarker.ICON_CIRCLE)
        self.marker.setPenWidth(2)

        # Déplacer le marker vers le point cliqué
        self.marker.setCenter(point_canvas)
        # pour utilisation dans la class parent
        self.parent.point_clique = point_canvas

        self.parent.liste_markers.append(self.marker)

        self.parent.dlg.lineEditZpoint.setText(str(self.parent.list_z[self.indice]))
        super().mousePressEvent(event)

    def hoverEnterEvent(self, event):
        self.setCursor(Qt.CrossCursor)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        # self.lineedit_altitude.setText("")
        super().hoverLeaveEvent(event)

    def z_interpole(self):
        d = QgsDistanceArea()
        d.setSourceCrs(self.parent.layer.crs(), QgsProject.instance().transformContext())

        point_courant = QgsPointXY(float(self.parent.list_x[self.indice]), float(self.parent.list_y[self.indice]))
        # si on clique le premier point , le point d'avant n'existe pas
        try:
            point_avant = QgsPointXY(float(self.parent.list_x[self.indice-1]), float(self.parent.list_y[self.indice-1]))
        except:
            return None
        try:
            point_apres = QgsPointXY(float(self.parent.list_x[self.indice + 1]), float(self.parent.list_y[self.indice + 1]))
        except:
            return None
        distance_total = d.measureLine(point_avant, point_apres)
        distance_avant = d.measureLine(point_avant, point_courant)

        if distance_total != 0:
            z = float(self.parent.list_z[self.indice-1]) + (distance_avant / distance_total) * (float(self.parent.list_z[self.indice+1]) - float(self.parent.list_z[self.indice-1]))
        else:
            z = float(self.parent.list_z[self.indice-1])

        # 1 chiffre apres la virgule
        return round(z, 1)