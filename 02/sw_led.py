import time
import pigpio

SW1_PIN = 17
SW2_PIN = 4
LED_PIN = 14

duty = 0

pi = pigpio.pi()

pi.set_mode( SW1_PIN, pigpio.INPUT )
pi.set_mode( SW2_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW1_PIN, pigpio.PUD_DOWN )
pi.set_pull_up_down( SW2_PIN, pigpio.PUD_UP )

pi.set_mode( LED_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( LED_PIN, 50 )
pi.set_PWM_range( LED_PIN, 100 )
pi.set_PWM_dutycycle( LED_PIN, duty )

while True:
	if( pi.read( SW1_PIN ) == pigpio.HIGH ):
		while( pi.read( SW1_PIN ) == pigpio.HIGH ):
			time.sleep( 0.1 )
		while ( duty < 100 ):
			duty = duty + 1 
			pi.set_PWM_dutycycle( LED_PIN, duty )
			time.sleep( 0.01 )

	if( pi.read( SW2_PIN ) == pigpio.LOW ):
		while( pi.read( SW2_PIN ) == pigpio.LOW ):
			time.sleep( 0.1 )
		while ( duty > 0 ):
			duty = duty - 1 
			pi.set_PWM_dutycycle( LED_PIN, duty )
			time.sleep( 0.01 )

	time.sleep( 0.1 )


