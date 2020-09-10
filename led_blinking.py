#!/user/bin/python

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

class Led(object):
    def __init__(self, led_pin):
        self.led_gpio_pin = led_pin
        gpio.setup(self.led_gpio_pin, gpio.OUT)

    def turn_on(self):
        gpio.output(self.led_gpio_pin, True)

    def turn_off(self):
        gpio.output(self.led_gpio_pin, False)


try:
    led = Led(27)
    while True:
        led.turn_on()
        time.sleep(1)
        led.turn_off()
        time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()