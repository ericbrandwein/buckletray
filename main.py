import sys, signal


from PySide6.QtWidgets import QApplication
from buckletray import BuckleTray


if __name__ == '__main__':
    app = QApplication(sys.argv)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    tray = BuckleTray()
    tray.show()
    sys.exit(app.exec())