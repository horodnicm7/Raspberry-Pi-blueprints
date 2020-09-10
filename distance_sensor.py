#!/user/bin/python

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

def measure_distance(trigger_pin, echo_pin):
    """
    Computes the distance to a point, using the HC-SR04 sensor
    :param trigger_pin: GPIO pin number where the trigger is set
    :param echo_pin: GPIO pin number where the echo is set
    :return: a float number representing the distance in centimeters
    """
    gpio.setup(trigger_pin, gpio.OUT)
    gpio.setup(echo_pin, gpio.IN)

    gpio.setup(trigger_pin, False)
    time.sleep(2)
    gpio.output(trigger_pin, True)
    time.sleep(0.00001)
    gpio.output(trigger_pin, False)

    start, end = 0, 0

    # get the latest timestamp when the input value is low
    while gpio.input(echo_pin) == 0:
        start = time.time()

    # get the latest timestamp when the input value is high
    while gpio.input(echo_pin) == 1:
        end = time.time()

    print(start, end)

    # convert the duration into distance and round to 2 decimal places
    duration = end - start
    distance = duration * 17150
    distance = round(distance, 2)

    return distance

trigger_pin = 23
echo_pin = 24

try:
    print("Distance: {} cm".format(measure_distance(trigger_pin, echo_pin)))
except KeyboardInterrupt:
    print("Keyboard interrupt")
finally:
    gpio.cleanup()