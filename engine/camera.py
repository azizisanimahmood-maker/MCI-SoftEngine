from PySide6.QtCore import QPointF


class Camera:

    def __init__(self):

        self.zoom = 1.0

        self.offset = QPointF(0.0, 0.0)

    # --------------------------------

    def zoom_in(self):

        self.zoom *= 1.10

    # --------------------------------

    def zoom_out(self):

        self.zoom /= 1.10

    # --------------------------------

    def pan(self, dx, dy):

        self.offset += QPointF(dx, dy)