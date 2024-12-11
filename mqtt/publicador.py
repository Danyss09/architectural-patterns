import paho.mqtt.client as mqtt

# Crear una instancia del cliente MQTT usando la versión más reciente de MQTT (MQTTv5)
client = mqtt.Client(protocol=mqtt.MQTTv5)

# Función que se ejecuta cuando el cliente se conecta al broker
# Ahora acepta 5 parámetros: client, userdata, flags, rc, and properties
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code: {rc}")
    # Publicar el mensaje en el tema 'daniela/topic'
    client.publish("daniela/topic", "Hello World, my name is Daniela Cáceres!")

# Asignar la función on_connect al cliente
client.on_connect = on_connect

# Conectar al broker MQTT (en este caso, el broker público 'broker.hivemq.com')
client.connect("broker.hivemq.com", 1883, 60)

# Iniciar el bucle para mantener la conexión activa
client.loop_forever()
