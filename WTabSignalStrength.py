from PyQt5 import QtWidgets,uic
import analoggaugewidget

class WTabSignalStrength(QtWidgets.QMainWindow):
    def __init__(self):
        super(WTabSignalStrength,self).__init__()
        uic.loadUi("ui/w_tab_signal_info.ui",self)
        self.SetupGauge()

    def SetupGauge(self):
        self.signal_gauge.units = "dBm"
        self.signal_gauge.setScalaCount(10)
        self.signal_gauge.setEnableValueText(False)
        self.signal_gauge.setEnableScaleText(False)
