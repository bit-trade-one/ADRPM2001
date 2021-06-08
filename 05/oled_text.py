#import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = None
I2C_ADDR = 0x3c

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 16

disp = Adafruit_SSD1306.SSD1306_128_32( rst=RST, i2c_address=I2C_ADDR )

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

draw = ImageDraw.Draw( image )

jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

draw.text( ( 5, 0 ), "基本パーツ", font=jpfont, fill=255 )
draw.text( ( 22, 16 ), "配線済みボード", font=jpfont, fill=255 )

disp.image(image)
disp.display()



