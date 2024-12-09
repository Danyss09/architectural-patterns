import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected successfully")
    client.publish("test/topic", "Hello World, my name is Daniela Cáceres!")

client.on_connect = on_connect
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
