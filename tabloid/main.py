import sys
from PyQt6.QtWidgets import QApplication
from tabloid.ui.main_window import UIWindow

app = QApplication(sys.argv)
window = UIWindow()
window.show()
sys.exit(app.exec())