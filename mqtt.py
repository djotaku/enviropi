"""Publish state via MQTT."""

import logging
import paho.mqtt.publish as publish

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(asctime)s - %(message)s")

class Publisher():
    """A class that will take care of publishing MQTT messages.

    :param channel: The channel that the messages will be published on.
    :param server: The MQTT server messages will be sent to.
    """
    def __init__(self, channel, server):
        self.channel = channel
        self.server = server
        self.client_id = "bathroompi"

    def publish(self, message) -> bool:
        """Publish message to MQTT server.

        :param message: the message to publish.
        """

        try:
            publish.single(self.channel, message, hostname=self.server, client_id=self.client_id)
            return True
        except:
            logging.error("Server DNS issue.")
            return False
