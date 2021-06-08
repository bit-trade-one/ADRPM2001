import pigpio
import time
import math

class cls381:
    AMBIENT_MODE = 0x02
    COLOR_MODE = 0x06
    def __init__( self, pi, ch, addr ):
        self.pi = pi
        self.ch = ch
        self.addr = addr
        self.i2c = self.pi.i2c_open( self.ch, self.addr )

        self.norma_red   = 40000
        self.norma_green = 60000
        self.norma_blue  = 40000
        self.bright = 1
        time.sleep(1)

    def set_mode( self, mode ):
        if ( mode == self.COLOR_MODE ):
            self.pi.i2c_write_byte_data( self.i2c, 0x00, self.COLOR_MODE )
        else:
            self.pi.i2c_write_byte_data( self.i2c, 0x00, self.AMBIENT_MODE )

    def get_ambient( self ):
        ( count, value )= self.pi.i2c_read_i2c_block_data( self.i2c, 0x0d, 3 )
        light = ( value[ 2 ] << 16 ) + ( value[ 1 ] << 8 ) + value[ 0 ]

        return( light )

    def set_normalize( self, r, g, b ):
        self.norma_red   = r
        self.norma_green = g
        self.norma_blue  = b

    def set_bright( self, val ):
        self.bright = val

    def get_color( self ):
        ( count, value )= self.pi.i2c_read_i2c_block_data( self.i2c, 0x0d, 3 )
        green = ( value[ 2 ] << 16 ) + ( value[ 1 ] << 8 ) + value[ 0 ]

        ( count, value )= self.pi.i2c_read_i2c_block_data( self.i2c, 0x10, 3 )
        red = ( value[ 2 ] << 16 ) + ( value[ 1 ] << 8 ) + value[ 0 ]

        ( count, value )= self.pi.i2c_read_i2c_block_data( self.i2c, 0x13, 3 )
        blue = ( value[ 2 ] << 16 ) + ( value[ 1 ] << 8 ) + value[ 0 ]

        ( count, value )= self.pi.i2c_read_i2c_block_data( self.i2c, 0x0a, 3 )
        ir = ( value[ 2 ] << 16 ) + ( value[ 1 ] << 8 ) + value[ 0 ]

        return( red, green, blue, ir )

    def rgb_hsv( self, r, g, b ):
        mx = max( r, g, b )
        mn = min( r, g, b )

        df = mx - mn

        if( mx == mn):
            h = 0
        elif( mx == r ):
            h = ( 60 * ( ( g - b ) / df ) + 360 ) % 360
        elif( mx == g ):
            h = ( 60 * ( ( b - r ) / df ) + 120 ) % 360
        elif( mx == b ):
            h = ( 60 * ( ( r - g ) / df ) + 240 ) % 360

        if( mx == 0 ):
            s = 0
        else:
            s = df / mx
        v = mx

        return( h, s, v )

    def disc_color( self ):
        ( red, green, blue, ir ) = self.get_color()
        n_red = red / self.norma_red * self.bright
        n_green = green / self.norma_green * self.bright
        n_blue = blue / self.norma_green * self.bright

        if ( n_red > 1 or n_green > 1 or n_blue > 1 ):
            return ( -1, "Out Range" )
            print( "Out of Range for Brightness. Change BRIGHT value.")
        
        ( h, s, v ) = self.rgb_hsv( n_red, n_green, n_blue )

        if( h >= 0 and h < 60 ):
            color_no = 1
            color_name = "Red"

        if( h >= 60 and h < 180 ):
            color_no = 2
            color_name = "Green"

        if( h >= 180 and h < 300 ):
            color_no = 3
            color_name = "Blue"

        if( h >= 300 and h <= 360 ):
            color_no = 1
            color_name = "Red"
        
        return( color_no, color_name )


