from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QLabel,
    QToolBar,
)

from ui.canvas import Canvas


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("MAS CAD Iran SoftEngine V1.0")

        self.resize(1600, 900)

        self.canvas = Canvas()

        self.setCentralWidget(self.canvas)

        self.create_toolbar()

        self.create_statusbar()

    # --------------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar("Main")

        toolbar.setMovable(False)

        self.addToolBar(Qt.TopToolBarArea, toolbar)

    # --------------------------------------------------------

    def create_statusbar(self):

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        # ------------------------------------------------

        self.lbl_ready = QLabel(" READY ")

        self.lbl_snap = QLabel(" SNAP:OFF ")

        self.lbl_grid = QLabel(" GRID:ON ")

        self.lbl_ortho = QLabel(" F8:OFF ")

        self.lbl_zoom = QLabel(" ZOOM:100% ")

        self.lbl_coord = QLabel(" X:0.000  Y:0.000 ")

        # ------------------------------------------------

        self.status.addWidget(self.lbl_ready)

        self.status.addPermanentWidget(self.lbl_snap)

        self.status.addPermanentWidget(self.lbl_grid)

        self.status.addPermanentWidget(self.lbl_ortho)

        self.status.addPermanentWidget(self.lbl_zoom)

        self.status.addPermanentWidget(self.lbl_coord)

    # --------------------------------------------------------

    def set_coordinates(self, x, y):

        self.lbl_coord.setText(

            f" X:{x:.3f}   Y:{y:.3f} "

        )

    # --------------------------------------------------------

    def set_ortho(self, state):

        if state:

            self.lbl_ortho.setText(" F8:ON ")

        else:

            self.lbl_ortho.setText(" F8:OFF ")