import paho.mqtt.client as mqtt

# Función que se ejecuta cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code: {rc}")
    # Suscribirse al tema 'daniela/topic'
    client.subscribe("daniela/topic")

# Función que se ejecuta cuando se recibe un mensaje
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

# Crear una instancia del cliente MQTT usando la versión más reciente de MQTT (MQTTv5)
client = mqtt.Client(protocol=mqtt.MQTTv5)

# Asignar las funciones de callback
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker MQTT (en este caso, el broker público 'broker.hivemq.com')
client.connect("broker.hivemq.com", 1883, 60)

# Iniciar el bucle para mantener la conexión activa
client.loop_forever()
