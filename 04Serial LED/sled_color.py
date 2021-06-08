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

while ( True ):
	value = adc.get_value( READ_CH )

	sel = int( value / 1023 * 7 )
	if ( sel == 7 ):
		sel = 6

	pixels[ 0 ] = ( lcolor[ sel ][ 1 ], lcolor[ sel ][ 0 ], lcolor[ sel ][ 2 ] )
	pixels[ 1 ] = ( lcolor[ sel ][ 1 ], lcolor[ sel ][ 0 ], lcolor[ sel ][ 2 ] )
	pixels.show()

	print( "Section :" , sel , "   Volume :", value )

	time.sleep( 0.2 )
