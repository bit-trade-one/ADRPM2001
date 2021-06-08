import pigpio

SERVO_PIN = 5

PULSE = 1500

pi = pigpio.pi()

pi.set_servo_pulsewidth( SERVO_PIN, PULSE )

