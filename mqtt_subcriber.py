# on the broker side
import paho.mqtt.client as mqtt
import requests

BOT_TOKEN = "your_bot_token_here"
USER_ID = "your_user_id_here"
MQTT_BROKER = "broker_ip_here"
MQTT_TOPIC = "sim/alerts/"


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {"chat_id": USER_ID, "text": msg}
    requests.get(url, params=params)
    
    
def on_receive(client, userdata, message):
    msg = message.payload.decode()
    print(f"Received message: {msg}")
    send_telegram(msg)
    
client = mqtt.Client()
client.on_message = on_receive
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)
client.loop_forever()