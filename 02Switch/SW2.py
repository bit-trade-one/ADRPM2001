import time
import pigpio

SW2_PIN = 4

pi = pigpio.pi()

pi.set_mode( SW2_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW2_PIN, pigpio.PUD_UP )

while True:
	if( pi.read( SW2_PIN ) == pigpio.LOW ):
		print("On.")
	else:
		print("Off.")

	time.sleep( 1 )


