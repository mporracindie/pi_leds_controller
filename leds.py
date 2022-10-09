# The Pins. Use Broadcom numbers.
RED_PIN   = 17
GREEN_PIN = 27
BLUE_PIN  = 22

import pigpio
import time
import os
import sys


bright = 255

def setLights(pin, brightness):
	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness)

def is_marco_home():
	hostname = "192.168.1.5" # Galaxy S20 FE
	response = os.system("ping -c 1 " + hostname)
	if response == 0:
		return True
	return False

def turn_leds_on():
	r = 255.0
	g = 36.0
	b = 226.0
	setLights(RED_PIN, r)
	setLights(GREEN_PIN, g)
	setLights(BLUE_PIN, b)

def turn_leds_off():
	r = 0.0
	g = 0.0
	b = 0.0
	setLights(RED_PIN, r)
	setLights(GREEN_PIN, g)
	setLights(BLUE_PIN, b)

pi = pigpio.pi() 

command = sys.argv[1]

if command == 'on':
	print('Turning lights on...')
	turn_leds_on()
elif command == 'off':
	print('Turning lights off...')
	turn_leds_off()
elif command == 'smart_on':
	if is_marco_home():
		turn_leds_on()
else:
	print('command unrecognised, turning lights off')
	turn_leds_off()

time.sleep(0.5)