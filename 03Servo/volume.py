import pigpio
import time
from mcp3002 import mcp3002

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    value = adc.get_value( READ_CH )
    ratio = round( value / 1023 * 100, 1  )
    volt = round( value / 1023 * 3.3, 2  )

    print ( "Value :", value, "  Volt : ", volt, "V  Ratio: ", ratio , "%" )

    time.sleep( 1 )


