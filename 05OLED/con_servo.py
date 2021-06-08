import pigpio
import time
from mcp3002 import mcp3002

SERVO_PIN = 5
SERVO_R_MAX = 500
SERVO_L_MAX = 2500

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
	value = adc.get_value( READ_CH )
	pulse = int ( SERVO_L_MAX - ( 2000 / 1023 ) * value )

	pi.set_servo_pulsewidth( SERVO_PIN, pulse )

	print ( "Value :", value, "  Servo Pulse: ", pulse )

	time.sleep( 0.1 )


