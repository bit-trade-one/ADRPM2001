import pigpio
import time

LED_PIN = 14
LED_TIME= 1

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )

while True:
	pi.write( LED_PIN, pigpio.LOW )
	time.sleep( LED_TIME )
	pi.write( LED_PIN, pigpio.HIGH )
	time.sleep( LED_TIME )



