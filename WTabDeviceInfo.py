from PyQt5 import QtWidgets,uic
import sys

class WTabDeviceInfo(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(WTabDeviceInfo,self).__init__()
        uic.loadUi("ui/w_tab_device_info.ui",self)
