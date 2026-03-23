from time import sleep
from machine import Pin
sleep(.1)
red_led  = Pin(0, Pin.OUT)
yellow_led = Pin(1, Pin.OUT)
green_led = Pin(2, Pin.OUT)

def flash_led(led, delay=5):
    led.on()
    sleep(delay)
    led.toggle()

while True:
    flash_led(green_led, 30)
    flash_led(yellow_led)
    flash_led(red_led, 30)
