import subprocess

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QStyle


BUCKLE_STARTED_ICON = QIcon('icons/green-clak.svg')
BUCKLE_STARTED_TOOLTIP = 'Stop the noise'
BUCKLE_STOPPED_ICON = QIcon('icons/red-clak.svg')
BUCKLE_STOPPED_TOOLTIP = 'Make some noise'


class BuckleTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.start_buckle()
        self.activated.connect(self.on_tray_icon_activated)
        self.destroyed.connect(self.stop_buckle)

    @Slot(QSystemTrayIcon.ActivationReason)
    def on_tray_icon_activated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.toggle_noise()
    
    def toggle_noise(self):
        if self.buckle_process is None:
            self.start_buckle()
        else:
            self.stop_buckle()

    def start_buckle(self):
        self.setIcon(BUCKLE_STARTED_ICON)
        self.setToolTip(BUCKLE_STARTED_TOOLTIP)
        self.buckle_process = subprocess.Popen(['buckle', '-m', '0'])

    @Slot()
    def stop_buckle(self):
        self.setIcon(BUCKLE_STOPPED_ICON)
        self.setToolTip(BUCKLE_STOPPED_TOOLTIP)
        self.buckle_process.terminate()
        self.buckle_process = None
