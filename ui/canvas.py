from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget


class Canvas(QWidget):

    def __init__(self):

        super().__init__()

        self.setMouseTracking(True)

        self.setFocusPolicy(Qt.StrongFocus)

        self.cursor_pos = QPointF(0, 0)

    # --------------------------------------------

    def mouseMoveEvent(self, event):

        self.cursor_pos = event.position()

        self.update()

    # --------------------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        # Background

        painter.fillRect(
            self.rect(),
            QColor(35, 35, 35)
        )

        # ---------------- Grid ----------------

        painter.setPen(QColor(55, 55, 55))

        step = 25

        for x in range(0, self.width(), step):

            painter.drawLine(
                x,
                0,
                x,
                self.height()
            )

        for y in range(0, self.height(), step):

            painter.drawLine(
                0,
                y,
                self.width(),
                y
            )

        # ---------------- Axis ----------------

        painter.setPen(QColor(160, 70, 70))

        painter.drawLine(
            0,
            self.height() // 2,
            self.width(),
            self.height() // 2,
        )

        painter.setPen(QColor(70, 180, 70))

        painter.drawLine(
            self.width() // 2,
            0,
            self.width() // 2,
            self.height(),
        )

        # ======================================
        # CrossHair
        # ======================================

        painter.setPen(
            QPen(
                QColor(0, 255, 255),
                1,
            )
        )

        x = self.cursor_pos.x()

        y = self.cursor_pos.y()

        painter.drawLine(
            int(x),
            0,
            int(x),
            self.height(),
        )

        painter.drawLine(
            0,
            int(y),
            self.width(),
            int(y),
        )