from paho.mqtt import client as mqtt

class MqttClient():

    def __init__(self,username="vps-mqtt",password="lymousin",port=1883,host="37.44.244.196"):
     
      self.username = username
      self.password = password
      self.port = port
      self.host = host

      # paho mqtt instance
      self.mqttClient = mqtt.Client()

    def ConnectToMqttBroker(self):
      if self.GetClientState() == True:
        return self.mqttClient,"Already connect to broker"
      else:
        self.mqttClient.username_pw_set(self.username,self.password)
        self.mqttClient.connect_async(self.host,self.port)
        self.mqttClient.loop_start()
        return self.mqttClient,"Connecting to mqtt broker"

    def GetClientState(self):
      return self.mqttClient.is_connected()