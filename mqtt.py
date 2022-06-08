"""Publish state via MQTT."""

import json
import logging
import paho.mqtt.publish as publish

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(asctime)s - %(message)s")

class Publisher():
    """A class that will take care of publishing MQTT messages.

    :param topic: The channel that the messages will be published on.
    :param server: The MQTT server messages will be sent to.
    """
    def __init__(self, topic, server):
        self.topic = topic
        self.server = server
        self.client_id = "bathroompi"

    def send_config_message(self):
        temperature_config = {
                "device_class":"temperature",
                "name": "Master Bath Temperature",
                "state_topic": self.topic,
                "unit_of_mesaurement": "F",
                "value_template": "{{value_json.temperature}}",
                "unique_id": "MASTER_BATH_TEMPERATURE",
                "device":{
                    "identifiers":["Bathroom Raspberry Pi"],
                    "name": "Bathroom Raspberry Pi",
                    "model": "Raspbery Pi Zero W",
                    "manufacturer": "Raspberry Pi Foundation"
                    }
                }
        humidity_config = {
                "device_class": "humidity",
                "name": "Master Bath Humidity",
                "state_topic": self.topic,
                "unit_of_measurement": "%",
                "value_template": "{{value_json.humidity}}",
                "unique_id": "MASTER_BATHER_HUMIDITY",
                "device": {
                    "identifiers": ["Bathroom Raspberry Pi"],
                    "name": "Bathroom Raspberry Pi",
                    "model": "Raspberry Pi Zero W",
                    "manufacturer": "Raspberry Pi Foundation"
                    }
                }
        light_sensor_config = {
                "device_class": "illuminance",
                "name": "Master Bath Illumination",
                "state_topic": self.topic,
                "unit_of_measurement": "lux",
                "value_template": "{{value_json.illumination}}",
                "unique_id": "MASTER_BATH_ILLUMINATION",
                "device": {
                    "identifiers": ["Bathroom Raspberry Pi"],
                    "name": "Bathroom Raspberry Pi",
                    "model": "Raspberry Pi Zero W",
                    "manufacturer": "Raspberry Pi Foundation"
                    }
                }

        topic_base = "homeassistant/sensor/masterbath"
        configs = [(json.dumps(temperature_config), f"{topic_base}T/config"),
                (json.dumps(humidity_config), f"{topic_base}H/config"),
                (json.dumps(light_sensor_config), f"{topic_base}L/config")]

        for config in configs:
            self.publish(config[0], config[1], retain=True)

    def publish(self, message, topic="", retain=False) -> bool:
        """Publish message to MQTT server.

        :param message: the message to publish.
        """
        if topic == "":
            topic = self.topic
        logging.debug(f"message = {message}")
        logging.debug(f"topic = {topic}")
        logging.debug(f"server = {self.server}")
        try:
            publish.single(topic, message, hostname=self.server, client_id=self.client_id)
            return True
        except Exception as e:
            logging.error(f"There was an error {e}")
            return False
