from PyQt5 import QtWidgets, uic
import qdarktheme
import sys
import WSpeed

class WMain(QtWidgets.QMainWindow):
    def __init__(self):
       super(WMain, self).__init__()
       # load ui
       uic.loadUi("ui/w_main.ui", self)

       # stacked widget
       self.stack =  QtWidgets.QStackedWidget()
       self.speed_page = WSpeed.WSpeed()
       self.stack.addWidget(self.speed_page)

       # default stacked
       self.stack.setCurrentIndex(0)
       self.show()

app = QtWidgets.QApplication(sys.argv)
main = WMain()
app.setStyleSheet(qdarktheme.load_stylesheet())
sys.exit(app.exec_())
