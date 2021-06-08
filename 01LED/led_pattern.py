import pigpio
import time

LED_PIN = 14

pattern = [ 0.5, 0.5,
            0.5, 0.5,
            0.5, 1.5,
            0.5, 0.5,
            0.5, 0.5,
            0.5, 1.5,
            0.5, 0.5,
            0.5, 0.5,
            0.5, 0.5,
            0.5, 0.5,
            0.5, 0.5,
            0.5, 0.5,
            0.5, 3.0 ]

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )

pi.write( LED_PIN, pigpio.LOW )
time.sleep( 1 )

led_st = pigpio.LOW
for waittime in pattern:
	if ( led_st == pigpio.LOW ):
		led_st = pigpio.HIGH
	else:
		led_st = pigpio.LOW

	pi.write( LED_PIN, led_st )
	time.sleep( waittime )

pi.write( LED_PIN, pigpio.LOW )


