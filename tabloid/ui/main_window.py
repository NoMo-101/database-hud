from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView

class UIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabloid")
        self.resize(1200, 800)

        self.scene = QGraphicsScene()

        self.view = QGraphicsView(self.scene)

        self.setCentralWidget(self.view)

        self.scene.addText("Ui is working")
        