#!/usr/bin/env python3

import serial
from random import randint, choice
from time import sleep
from subprocess import Popen

ser = serial.Serial(
    port = '/dev/ttyACM0',
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

def butterfly():
    for j in range(1, 5):
        ser.write(b'1')
        ser.write(str(j).encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write(b'y')
        sleep(0.06)
        ser.write(b'1')
        ser.write(str(j).encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write(b'y')
        sleep(0.02)

def swap_colors():
    sleep(0.05)
    ser.write(b'1')
    ser.write(str(randint(1, 4)).encode())
    ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
    ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
    ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
    ser.write(b'y')

def dance():
    sleep(0.06)
    ser.write(b'1')
    led = randint(1, 4)
    ser.write(str(led).encode())
    ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
    ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
    ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
    ser.write(b'y')
    sleep(0.06)
    ser.write(b'1')
    ser.write(str(led).encode())
    ser.write((str(0) + '\r').encode())
    ser.write((str(0) + '\r').encode())
    ser.write((str(0) + '\r').encode())
    ser.write(b'y')

def cycle(reverse):
    if not reverse:
        leds = [1, 2, 3, 4]
    else: 
        leds = [4, 3, 2, 1]
    while len(leds) > 0:
        ser.write(b'1')
        led = choice(leds)
        leds.pop(leds.index(led))
        ser.write(str(led).encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write(b'y')
        sleep(0.06)
        ser.write(b'1')
        ser.write(str(led).encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write(b'y')

def circle(reverse):
    if reverse:
        leds = [2, 4, 3, 1]
    else:
        leds = [1, 3, 4, 2]
    for led in leds:
        ser.write(b'1')
        ser.write(str(led).encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write((str(randint(min_brightness, max_brightness)) + '\r').encode())
        ser.write(b'y')
        sleep(0.06)
        ser.write(b'1')
        ser.write(str(led).encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write(b'y')
        sleep(0.02)

def leds_off():
    for i in range(1, 5):
        ser.write(b'1')
        ser.write(str(i).encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write((str(0) + '\r').encode())
        ser.write(b'y')
        sleep(0.01)

def create_brightness(): 
    brightnesses = [randint(min_brightness, max_brightness), randint(min_brightness, max_brightness), randint(min_brightness, max_brightness)]
    for i in brightnesses:
        if i >= max_brightness / 1.5:
            return brightnesses
    create_brightness()

def leds_on():
    for i in range(1, 5):
        brightness = create_brightness()
        ser.write(b'1')
        ser.write(str(i).encode())
        ser.write((str(brightness[0]) + '\r').encode())
        ser.write((str(brightness[1]) + '\r').encode())
        ser.write((str(brightness[2]) + '\r').encode())
        ser.write(b'y')
        sleep(0.01)
def main():
    # turn all leds off
    leds_off()
    reverse = True
    try:
        while True:
            ran_func = randint(1, 5)
            reverse = not reverse
            if ran_func == 1:
                for i in range(0, randint(min_repeat, max_repeat)):
                    butterfly()
            if ran_func == 2:
                for i in range(0, randint(min_repeat, max_repeat)):
                    swap_colors()
            if ran_func == 3:
                for i in range(0, randint(min_repeat, max_repeat)):
                    dance()
            if ran_func == 4:
                for i in range(0, randint(min_repeat, max_repeat)):
                    cycle(reverse)
            if ran_func == 5:
                for i in range(0, randint(min_repeat, max_repeat)):
                    circle(reverse)
            leds_off()


    except KeyboardInterrupt:
        leds_on()
        exit()




main()
