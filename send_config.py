import mqtt


mqtt_publisher = mqtt.Publisher("/homeassistant/sensor/masterbath/state", "tanukimario.mushroomkingdom")
mqtt_publisher.send_config_message()
