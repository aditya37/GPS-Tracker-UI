from PyQt5 import QtWidgets, uic
import sys
import analoggaugewidget

class WSpeed(QtWidgets.QMainWindow):
    def __init__(self):
        super(WSpeed,self).__init__()
        uic.loadUi("ui/w_speed.ui",self)
        self.InitGauge()
    # define gauge
    def InitGauge(self):
        self.gauge_widget.units = "Km/h"
        self.gauge_widget.setEnableValueText(True)
        self.gauge_widget.updateValue(int(10))
        pass
