import pigpio
import time
from sht31 import sht31

SHT31_ADDR = 0x45

pi = pigpio.pi()
I2C_CH = 1

weather_sensor = sht31(pi, I2C_CH, SHT31_ADDR )


while ( True ):
	( temp, humi ) = weather_sensor.read_sensor()

	print( "Temp:" , temp , "C Humi:", humi, "%" )

	time.sleep(1)
