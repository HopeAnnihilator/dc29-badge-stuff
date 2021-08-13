#!/usr/bin/env python3

import serial
from random import randint, choice, sample
from time import sleep
from subprocess import Popen
from platform import system

if system() == 'Darwin':
    serialPort = '/dev/tty.usbmodem123451'
else:
    serialPort = '/dev/ttyACM0'

leds = [1, 2, 3, 4]

ser = serial.Serial(
    port = serialPort,
    baudrate = 4000000,
    bytesize = serial.EIGHTBITS,
    stopbits = serial.STOPBITS_ONE,
    parity = serial.PARITY_NONE,
    timeout = 1,
    rtscts = False,
    xonxoff = False,
)

max_brightness = 255
min_repeat = 5
max_repeat = 20
min_brightness = 0

# initialize device properly
ser.write(b'\n\r')

def change_led(led, rgb):
    ser.write(b'1')
    ser.write(str(led).encode())
    ser.write((str(rgb[0]) + '\r').encode())
    ser.write((str(rgb[1]) + '\r').encode())
    ser.write((str(rgb[2]) + '\r').encode())
    ser.write(b'y')

def butterfly(leds):
    for led in leds:
        change_led(led, sample(range(min_brightness, max_brightness), 3))
        sleep(0.06)
        change_led(led, [0, 0, 0])
        sleep(0.02)

def swap_colors(leds):
    for i in range(0, 4):
        led = choice(leds)
        change_led(led, sample(range(min_brightness, max_brightness), 3))  
        sleep(0.05)


def dance(leds):
    for i in range(0, 4):
        led = choice(leds)
        change_led(led, sample(range(min_brightness, max_brightness), 3)) 
        sleep(0.06)
        change_led(led, [0, 0, 0])

def cycle(leds):
    # when popping be sure to create a new list instead of modifying original array
    leds = list(leds)
    while len(leds) > 0:
        ser.write(b'1')
        led = choice(leds)
        leds.pop(leds.index(led))
        change_led(led, sample(range(min_brightness, max_brightness), 3)) 
        sleep(0.06)
        change_led(led, [0, 0, 0]) 

def circle(leds):
    for led in leds:
        change_led(led, sample(range(min_brightness, max_brightness), 3)) 
        sleep(0.06)
        change_led(led, [0, 0, 0]) 
        sleep(0.02)


def exit_on(): 
    brightnesses = sample(range(min_brightness, max_brightness), 3)
    for i in brightnesses:
        if i >= max_brightness / 1.5:
            return brightnesses
    exit_on()

def main():
    global leds
    # turn all leds off
    for led in leds:
        change_led(led, [0, 0, 0])
    
    try:
        while True:
            leds = list(reversed(leds))
            switch = randint(1, 5)
            if switch == 1:
                for i in range(0, randint(min_repeat, max_repeat)):
                    butterfly(leds)
            if switch == 2:
                for i in range(0, randint(min_repeat, max_repeat)):
                    swap_colors(leds)
            if switch == 3:
                for i in range(0, randint(min_repeat, max_repeat)):
                    dance(leds)
            if switch == 4:
                for i in range(0, randint(min_repeat, max_repeat)):
                    cycle(leds)
            if switch == 5:
                for i in range(0, randint(min_repeat, max_repeat)):
                    circle(leds)
            sleep(0.05)
            change_led(led, [0, 0, 0])
            sleep(0.05)


    except KeyboardInterrupt:
        for led in leds:
            rgb = exit_on()
            change_led(led, rgb)
        exit()




main()
