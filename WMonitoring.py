from PyQt5 import QtWidgets,uic
import sys

class WMonitoring(QtWidgets.QMainWindow):
    def __init__(self):
        super(WMonitoring,self).__init__()
        uic.loadUi("ui/w_monitoring.ui",self) 
        self.show()

app = QtWidgets.QApplication(sys.argv)
main = WMonitoring()
sys.exit(app.exec_())
