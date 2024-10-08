

import serial
import time

a5 = [0x01, 0x03, 0x00, 0x07, 0x00, 0x01, 0x35, 0xcb]
ai = [0x01, 0x03, 0x00, 0x08, 0x00, 0x01, 0x05, 0xc8]
at = [0x01, 0x03, 0x00, 0x09, 0x00, 0x01, 0x54, 0x08]


ser = serial.Serial('COM3', 115200, timeout=0, parity='E', stopbits=2)

print 'is open', ser.is_open

time.sleep(4)


def genera(l):
    salida = []
    for e in l:
        salida.append(int(e.encode('hex'), 16))
    return salida

while True:
    ser.write(a5)
    time.sleep(1)
    l = ser.readline()
    g = genera(list(l))
    
    temp = g[3] * 256 + g[4]
    print "Temperature",  temp
    time.sleep(.1)

    ser.write(ai)
    time.sleep(1)
    l = ser.readline()
    g = genera(list(l))
    
    hum = g[3] * 256 + g[4]
    print "Humidity", hum
    time.sleep(.1)
    
    ser.write(at)
    time.sleep(1)
    l = ser.readline()
    g =  genera(list(l))
    
    roc = g[3] * 256 + g[4]
    print "Dew point", roc
    time.sleep(1)
    
    print " "