# HX711
HX_DT = 'G9'
HX_SCK = 'G10'
HX_SCALE = 50
HX_TARE = 0

# TTN Node IDs
DEV_EUI = '<DEV_EUI>'
APP_EUI = '<APP_EUI>'
APP_KEY = '<APP_KEY>'

# Debug
DEBUG_LED = True
DEBUG_CON = True

# LoRa setup
LORA_FREQUENCY = 868100000
LORA_DR = 5   # DR_5

# Prefix of each packet
PKT_PREFIX = b'PKT #'

# Sleep time in packet send
SLEEP_MAIN = 600

# Low Energy config
DIS_WIFI = True
DIS_BLE = True
HEARTBEAT = False

# LED color
LED_OFF = 0x000000
GREEN = 0x007f00
YELLOW = 0x7f7f00
RED = 0x7f0000
BLUE = 0x00007f
