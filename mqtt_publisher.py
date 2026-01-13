import psutil
import socket
import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "broker_ip_here"
THRESHOLD_GB = 3 # Memory usage threshold in GB

HOSTNAME = socket.gethostname()
MQTT_TOPIC = f"sim/alerts/"

def check_memory_usage():
    mem = psutil.virtual_memory()
    current_gb = mem.used / (1024**3)
    msg = ""
    if current_gb > THRESHOLD_GB:
        msg = f"Warning: High memory usage detected! on {HOSTNAME} Current usage is {current_gb:.2f} GB"
    else:
        msg = "0"
    return msg


client = mqtt.Client()

while True:
    msg = check_memory_usage()
    if msg != "0":
        client.connect(MQTT_BROKER, 1883, 60)
        client.publish(MQTT_TOPIC, msg)
        client.disconnect()
        time.sleep(60)
    time.sleep(10)


