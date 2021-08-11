#!/usr/bin/env python3 

import serial


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

while True:
    ser.readline()