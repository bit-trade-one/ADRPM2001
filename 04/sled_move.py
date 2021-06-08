import pigpio
import time
import neopixel
import board
from mcp3002 import mcp3002

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

LED_NUM = 2

MAX_SPEED = 0.01
MIN_SPEED = 1


pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

pixels = neopixel.NeoPixel( board.D18 , LED_NUM, brightness = 0.1 )

pixels[ 0 ] = ( 0x00, 0x00, 0x00 )
pixels[ 1 ] = ( 0x00, 0x00, 0x00 )
pixels.show()
time.sleep( 1 )

lcolor = [ [ 0xff, 0x00, 0x00 ],
           [ 0xff, 0xa1, 0x00 ],
           [ 0xff, 0xff, 0x00 ],
           [ 0x00, 0xff, 0x00 ],
           [ 0x00, 0xff, 0xff ],
           [ 0x00, 0x00, 0xff ],
           [ 0xff, 0x00, 0xff ] ]

sel0 = 0
while ( True ):
	value = adc.get_value( READ_CH )

	speed = ( MAX_SPEED - MIN_SPEED ) / 1023 * value + MIN_SPEED

	if ( sel0 == 7 ):
		sel0 = 6

	pixels[ 0 ] = ( lcolor[ sel0 ][ 1 ], lcolor[ sel0 ][ 0 ], lcolor[ sel0 ][ 2 ] )
	pixels[ 1 ] = ( lcolor[ sel0 ][ 1 ], lcolor[ sel0 ][ 0 ], lcolor[ sel0 ][ 2 ] )
	pixels.show()

	sel0 = sel0 + 1
	if ( sel0 == 7 ):
		sel0 = 0

	time.sleep( speed )
