#!/usr/bin/env python3 

import serial
from platform import system

if system() == 'Darwin':
    serialPort = '/dev/tty.usbmodem123451'
else:
    serialPort = '/dev/ttyACM0'

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

while True:
    ser.readline()