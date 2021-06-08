import pigpio
import time
from cls381 import cls381

CLS381_ADDR = 0x53
LED_PIN = 19

pi = pigpio.pi()
I2C_CH = 1

color_sensor = cls381( pi, I2C_CH, CLS381_ADDR )

color_sensor.set_mode( color_sensor.COLOR_MODE )

pi.set_mode( LED_PIN, pigpio.OUTPUT )
pi.write( LED_PIN, pigpio.HIGH )


count = 0;

while( count < 10 ):
    sum_r = 0
    sum_g = 0
    sum_b = 0

    i = 0
    while( i < 10 ):
        ( red, green, blue, ir ) = color_sensor.get_color()

        sum_r = sum_r + red
        sum_g = sum_g + green
        sum_b = sum_b + blue

        i = i + 1
        time.sleep( 0.1 )

    nor_red = int( sum_r / 10 )
    nor_green = int( sum_g / 10 )
    nor_blue = int( sum_b / 10 )

    print( "Red :", nor_red, "  Green :", nor_green, "  Blue :", nor_blue )

    time.sleep( 0.5 )
    count = count + 1

pi.write( LED_PIN, pigpio.LOW )

