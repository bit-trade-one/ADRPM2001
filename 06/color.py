import pigpio
import time
from cls381 import cls381

CLS381_ADDR = 0x53

pi = pigpio.pi()
I2C_CH = 1

color_sensor = cls381( pi, I2C_CH, CLS381_ADDR )

color_sensor.set_mode( color_sensor.COLOR_MODE )

while True:
    ( red, green, blue, ir ) = color_sensor.get_color()
    print( "Red :", red, "  Green :", green, "  Blue :", blue, "  IR :", ir )

    time.sleep( 0.5 )


