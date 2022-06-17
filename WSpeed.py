from PyQt5 import QtWidgets, uic
from datetime import date
import json
import sys
import analoggaugewidget
import mqtt

class WSpeed(QtWidgets.QMainWindow):
    def __init__(self):
        super(WSpeed,self).__init__()
        uic.loadUi("ui/w_speed.ui",self)
        self.InitGauge()

        self.mc = mqtt.MqttClient()
        # mqtt client instance
        self.client,self.msg = self.mc.ConnectToMqttBroker()
        self.client.on_connect = self.OnConnectBrokerAndSubscribe
        self.client.on_message = self.SubscirbeMessagePayload
        self.lbl_message.setText(self.msg)
        
    # define gauge
    def InitGauge(self):
        self.gauge_widget.units = "Km/h"
        self.gauge_widget.setEnableValueText(True)
        self.gauge_widget.updateValue(int(10))

    def OnConnectBrokerAndSubscribe(self,client, userdata, flags, rc):
        if rc == 0:
            self.lbl_message.setText("Connected to MQTT Broker!")
        else:
            self.lbl_message.setText("Failed to connect mqtt broker")
        
        client.subscribe("/device/sync/time")
        client.subscribe("/device/resp/tracking/111")
    def SubscirbeMessagePayload(self,client, userdata, message):
        if message.topic == "/device/sync/time":
            strMessage = message.payload.decode("utf-8")
            jsonMessage = json.loads(strMessage)
            self.lbl_date.setText(jsonMessage["date"])
            self.lbl_time.setText(jsonMessage["time"])
        elif message.topic == "/device/resp/tracking/111":
            strMessage = message.payload.decode("utf-8")
            jsonMessage = json.loads(strMessage)
            self.gauge_widget.updateValue(jsonMessage["speed"])
            if jsonMessage["is_recorded"] == True:
                self.lbl_status_val.setText(jsonMessage["status"])
            else:
                self.lbl_status_val.setText(jsonMessage["status"])
            
            temp = str(jsonMessage["temp"])
            self.lbl_temp.setText("Temp: {0} C".format(temp))
            self.lbl_lat.setText("Lat: {0}".format(
                str(jsonMessage["lat"])
            ))
            self.lbl_long.setText("Lng: {0}".format(
                str(jsonMessage["long"])
            ))
            self.lbl_signal.setText("Signal: {0} dBm".format(
                str(jsonMessage["signal"])
            ))