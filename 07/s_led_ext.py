import board
import neopixel

pixels = neopixel.NeoPixel( board.D18 , 10 )

pixels[0] = (0, 64, 0)
pixels[1] = (64, 0, 0)
pixels[2] = (0, 0, 64)
pixels[3] = (0, 64, 0)
pixels[4] = (64, 0, 0)
pixels[5] = (0, 0, 64)
pixels[6] = (0, 64, 0)
pixels[7] = (64, 0, 0)
pixels[8] = (0, 0, 64)
pixels[9] = (64, 64, 64)

pixels.show()
