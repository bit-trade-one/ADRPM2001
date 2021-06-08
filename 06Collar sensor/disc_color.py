import pigpio
import time
from cls381 import cls381
from rgb_hsv import rgb_hsv

CLS381_ADDR = 0x53

NORMA_RED   = 40000
NORMA_GREEN = 60000
NORMA_BLUE  = 40000

BRIGHT = 1

pi = pigpio.pi()
I2C_CH = 1

color_sensor = cls381( pi, I2C_CH, CLS381_ADDR )

color_sensor.set_mode( color_sensor.COLOR_MODE )
color_sensor.set_normalize( NORMA_RED, NORMA_GREEN, NORMA_BLUE )
color_sensor.set_bright( BRIGHT )

SERVO_PIN = 5

while True:
    ( color_no, color_name ) = color_sensor.disc_color( )

    if ( color_no == -1 ):
        print( "Out of Range for Brightness. Change BRIGHT value.")
        break

    print( color_name )
    
    if ( color_no == 1 ):
        pi.set_servo_pulsewidth( SERVO_PIN, 2000 )
    elif( color_no == 2 ):
        pi.set_servo_pulsewidth( SERVO_PIN, 1500 )
    elif( color_no == 3 ):
        pi.set_servo_pulsewidth( SERVO_PIN, 1000 )

    time.sleep( 0.5 )


