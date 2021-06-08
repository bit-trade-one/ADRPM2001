import board
import neopixel

pixels = neopixel.NeoPixel( board.D18 , 2, brightness=0.1 )

pixels[0] = ( 0, 255,   0 )
pixels[1] = ( 0,   0, 255 )

pixels.show()
