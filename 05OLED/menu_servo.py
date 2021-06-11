import Adafruit_SSD1306
import time
import pigpio
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SW1_PIN = 17
SW2_PIN = 4
SERVO_PIN = 5

pi = pigpio.pi()

pi.set_mode( SW1_PIN, pigpio.INPUT )
pi.set_mode( SW2_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW1_PIN, pigpio.PUD_DOWN )
pi.set_pull_up_down( SW2_PIN, pigpio.PUD_UP )

RST = None
I2C_ADDR = 0x3c

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 15

disp = Adafruit_SSD1306.SSD1306_128_32( rst=RST, i2c_address=I2C_ADDR )

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )
draw = ImageDraw.Draw( image )
jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')


SERVO_STOP_PULSE = 1480

LINE_1 = 0
LINE_2 = 16

menu_top = [ "速度選択",
             "回転方向選択",
             "パルス幅表示" ]

menu_speed = [ [ "停止", 0 ],
               [ "低速", 300 ],
               [ "中速", 500 ],
               [ "高速", 900 ] ]

menu_direct = [ [ "右回転", -1 ],
                [ "左回転", 1 ] ]

def disp_out( msg1, msg2 ):
    draw.rectangle( ( 0, 0, width, height ), fill = 0 )
    draw.text( ( 0, LINE_1 ), msg1 , font=jpfont, fill = 255 )
    draw.text( ( 0, LINE_2 ), msg2 , font=jpfont, fill = 255 )
    disp.image(image)
    disp.display()

def servo_speed():
    global speed
    sel = 0
    disp_out( menu_top[ select ], menu_speed[ sel ][ 0 ] )
    while True:
        if ( pi.read( SW1_PIN ) == pigpio.HIGH ):
            while( pi.read( SW1_PIN ) == pigpio.HIGH ):
                time.sleep( 0.3 )
        
            sel = sel + 1
            if ( sel >= len( menu_speed ) ):
                sel = 0
            disp_out( menu_top[ select ], menu_speed[ sel ][ 0 ] )
            time.sleep( 0.1 )

        if ( pi.read( SW2_PIN ) == pigpio.LOW ):
            while( pi.read( SW2_PIN ) == pigpio.LOW ):
                time.sleep( 0.1 )
            time.sleep( 0.3 )
            speed = menu_speed[ sel ][ 1 ]
            pulse = SERVO_STOP_PULSE + direct * speed
            pi.set_servo_pulsewidth( SERVO_PIN, pulse )
            print( pulse )
            break

    disp_out( menu_top[ select ], "" )
    return

def servo_direct():
    global direct
    sel = 0
    disp_out( menu_top[ select ], menu_direct[ sel ][ 0 ] )
    while True:
        if ( pi.read( SW1_PIN ) == pigpio.HIGH ):
            while( pi.read( SW1_PIN ) == pigpio.HIGH ):
                time.sleep( 0.3 )
        
            sel = sel + 1
            if ( sel >= len( menu_direct ) ):
                sel = 0
            disp_out( menu_top[ select ], menu_direct[ sel ][ 0 ] )
            time.sleep( 0.1 )

        if ( pi.read( SW2_PIN ) == pigpio.LOW ):
            while( pi.read( SW2_PIN ) == pigpio.LOW ):
                time.sleep( 0.1 )
            time.sleep( 0.3 )
            direct = menu_direct[ sel ][ 1 ]
            pulse = SERVO_STOP_PULSE +  ( direct * speed )
            pi.set_servo_pulsewidth( SERVO_PIN, pulse )
            print( direct, pulse )
            break

    disp_out( menu_top[ select ], "" )
    return

def disp_pulse():
    pulse = SERVO_STOP_PULSE +  ( direct * speed )
    mes_pulse = str( pulse ) + "μ秒"

    disp_out( "現在のパルス幅", mes_pulse )

    time.sleep( 5 )


select = 0
speed = 0
direct = 1

disp_out( menu_top[ select ], "" )
pi.set_servo_pulsewidth( SERVO_PIN, SERVO_STOP_PULSE )

while True:
    if ( pi.read( SW1_PIN ) == pigpio.HIGH ):
        while( pi.read( SW1_PIN ) == pigpio.HIGH ):
            time.sleep( 0.3 )
        
        select = select + 1
        if ( select >= len( menu_top ) ):
            select = 0
        disp_out( menu_top[ select ], "" )
        time.sleep( 0.1 )

    if ( pi.read( SW2_PIN ) == pigpio.LOW ):
        while( pi.read( SW2_PIN ) == pigpio.LOW ):
            time.sleep( 0.1 )
        time.sleep( 0.3 )
        if ( select == 0 ):
            servo_speed()
        elif ( select == 1 ):
            servo_direct()
        elif ( select == 2 ):
            disp_pulse()

        disp_out( menu_top[ select ], "" )
