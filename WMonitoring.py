from PyQt5 import QtWidgets,uic
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF
import sys

class WMonitoring(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(WMonitoring,self).__init__()
        uic.loadUi("ui/w_monitoring.ui",self)

        self.line_chart = QLineSeries(self) 
       
        # set data to line chart
        # Pattern = QPointF(x,y)
        self.line_chart.append(QPointF(1654937365,1))

        # chart instance
        self.chart = QChart()
        self.chart.addSeries(self.line_chart) # add line to graph
        self.chart.createDefaultAxes()

        # hide legend
        self.chart.legend().hide()
        # show chart view
        self.chart_view = QChartView(self.chart)
        self.setCentralWidget(self.chart_view)
        self.show()


app = QtWidgets.QApplication(sys.argv)
main = WMonitoring()
sys.exit(app.exec_())
