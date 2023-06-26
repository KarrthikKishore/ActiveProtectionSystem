
def mqtt(a1,b1,a2,b2):
    import paho.mqtt.publish as publish

    MQTT_SERVER = "192.168.29.29"
    MQTT_PATH = "test_channel"
    import time
    while True:
         publish.single(MQTT_PATH, a1 , hostname=MQTT_SERVER) #send data continuously every 1 seconds
         publish.single(MQTT_PATH, b1 , hostname=MQTT_SERVER)
         time.sleep(1)


mqtt(1,2,3,4)