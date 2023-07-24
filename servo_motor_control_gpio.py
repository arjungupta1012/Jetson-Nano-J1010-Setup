import Jetson.GPIO as GPIO
import time

servo_pin = 18  # The GPIO pin connected to the servo motor
frequency = 50  # PWM frequency (Hz)
angle_min = 0  # Minimum angle (in degrees)
angle_max = 180  # Maximum angle (in degrees)
duty_cycle_min = 2.5  # Minimum duty cycle for the servo motor (in %)
duty_cycle_max = 12.5  # Maximum duty cycle for the servo motor (in %)

def angle_to_duty_cycle(angle):
    # Map the angle value to the duty cycle range
    duty_cycle = ((angle - angle_min) / (angle_max - angle_min)) * (duty_cycle_max - duty_cycle_min) + duty_cycle_min
    return duty_cycle

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, frequency)
    pwm.start(0)
    return pwm

def set_angle(pwm, angle):
    duty_cycle = angle_to_duty_cycle(angle)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)  # Give the servo some time to move to the desired angle

def cleanup(pwm):
    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        pwm = setup()

        while True:
            # Move the servo motor to 0 degrees
            set_angle(pwm, 0)
            time.sleep(1)

            # Move the servo motor to 90 degrees
            set_angle(pwm, 90)
            time.sleep(1)

            # Move the servo motor to 180 degrees
            set_angle(pwm, 180)
            time.sleep(1)

    except KeyboardInterrupt:
        cleanup(pwm)

