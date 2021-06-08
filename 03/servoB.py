import pigpio

SERVO_PIN = 6

PULSE = 100

pi = pigpio.pi()

pi.set_servo_pulsewidth( SERVO_PIN, PULSE )

