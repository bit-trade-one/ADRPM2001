import time
import pigpio

SW1_PIN = 17

pi = pigpio.pi()

pi.set_mode( SW1_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW1_PIN, pigpio.PUD_DOWN )

while True:
	if( pi.read( SW1_PIN ) == pigpio.HIGH ):
		print("On.")
	else:
		print("Off.")

	time.sleep( 1 )


