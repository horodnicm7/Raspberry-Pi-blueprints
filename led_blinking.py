#!/user/bin/python

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
led_gpio_pin = 27
gpio.setup(led_gpio_pin, gpio.OUT)

try:
    while True:
        gpio.output(led_gpio_pin, True)
        time.sleep(1)
        gpio.output(led_gpio_pin, False)
        time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()