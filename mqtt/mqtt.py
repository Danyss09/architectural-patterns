from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import paho.mqtt.client as mqtt

# Configuración de Flask
app = Flask(__name__)

# Documento Swagger (OpenAPI)
swagger_document = {
    "openapi": "3.0.1",
    "info": {
        "title": "MQTT Hello API",
        "description": "API que documenta la funcionalidad MQTT para publicar mensajes en un topic.",
        "version": "1.0.0",
    },
    "servers": [
        {
            "url": "mqtt://broker.hivemq.com:1883",
            "description": "Broker público HiveMQ"
        }
    ],
    "paths": {
        "/publish": {
            "post": {
                "summary": "Publica un mensaje en un topic MQTT",
                "description": "Envía un mensaje al topic 'test/topic' usando el broker MQTT.",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "topic": {
                                        "type": "string",
                                        "example": "test/topic"
                                    },
                                    "message": {
                                        "type": "string",
                                        "example": "Hello World, my name is Daniela Cáceres!"
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Mensaje publicado exitosamente"
                    },
                    "400": {
                        "description": "Solicitud inválida"
                    }
                }
            }
        }
    }
}

# Configuración de Swagger UI
SWAGGER_URL = '/swagger'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    "/swagger.json",
    config={
        "app_name": "MQTT Hello API"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger_json():
    """Devuelve el documento Swagger en formato JSON."""
    return jsonify(swagger_document)

# Configuración MQTT
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    """
    Callback ejecutado al conectar con el broker MQTT.
    """
    if rc == 0:
        print("Conexión exitosa al broker MQTT")
    else:
        print(f"Error al conectar con el broker: {rc}")

client.on_connect = on_connect

@app.route('/publish', methods=['POST'])
def publish_message():
    """
    Endpoint para publicar un mensaje en el broker MQTT.
    """
    try:
        client.connect("broker.hivemq.com", 1883, 60)
        client.loop_start()
        client.publish("test/topic", "Hello World, my name is Daniela Cáceres!")
        return jsonify({"message": "Mensaje publicado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ejecutar servidor Flask
if __name__ == '__main__':
    print("Iniciando MQTT y servidor Flask...")
    app.run(port=4000, debug=True)
