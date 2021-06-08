import pigpio
import time
import neopixel
import board
from sht31 import sht31

SHT31_ADDR = 0x45

LED_NUM = 10
HUMI_PLACE = 0
TEMP_PLACE = 1
BAR_LED_NUM = LED_NUM - 2

RED = 0
GREEN = 1
BLUE = 2

pi = pigpio.pi()
I2C_CH = 1

pixels = neopixel.NeoPixel( board.D18 , 10 )

weather_sensor = sht31(pi, I2C_CH, SHT31_ADDR )

i = 0
while( i < LED_NUM ):
	pixels[ i ] = ( 0x00, 0x00, 0x00 )
	i = i + 1

pixels.show()

temp_color = [ [ 0x00, 0x00, 0x7f ],
               [ 0x00, 0x48, 0x7f ],
               [ 0x00, 0x7f, 0x6c ],
               [ 0x00, 0x7f, 0x24 ],
               [ 0x24, 0x7f, 0x00 ],
               [ 0x6c, 0x7f, 0x00 ],
               [ 0x7f, 0x48, 0x00 ],
               [ 0x7f, 0x00, 0x00 ] ]

humi_color = [ [ 0x7f, 0x7f, 0x00 ],
               [ 0x54, 0x7f, 0x00 ],
               [ 0x2a, 0x7f, 0x00 ],
               [ 0x00, 0x7f, 0x00 ],
               [ 0x00, 0x7f, 0x2a ],
               [ 0x00, 0x7f, 0x54 ],
               [ 0x00, 0x7f, 0x7f ],
               [ 0x00, 0x54, 0x7f ],
               [ 0x00, 0x2a, 0x7f ],
               [ 0x00, 0x00, 0x7f ] ]

while ( True ):
	( temp, humi ) = weather_sensor.read_sensor()
	print( "Temp:" , temp , "C Humi:", humi, "%" )

	sel = int( temp / 5 ) + 1
	if( temp < 0 ):
		sel = 0
	if( temp >= 35 ):
		sel = 7

	pixels[ TEMP_PLACE ] = ( temp_color[ sel ][ GREEN ], temp_color[ sel ][ RED ], temp_color[ sel ][ BLUE ] )

	target = 0
	while ( target < BAR_LED_NUM ):
		if( target < sel ):
			pixels[ target + 2 ] = ( temp_color[ sel ][ RED ], temp_color[ sel ][ GREEN ], temp_color[ sel ][ BLUE ] )
		else:
			pixels[ target + 2 ] = ( 0x00, 0x00, 0x00 )
		target = target + 1


	sel = int( humi / 10)
	if( sel == 10 ):
		sel = 9

	pixels[ HUMI_PLACE ] = ( humi_color[ sel ][ GREEN ], humi_color[ sel ][ RED ], humi_color[ sel ][ BLUE ] )

	pixels.show()

	time.sleep( 1 )
