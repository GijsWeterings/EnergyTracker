"""
You probably want to run this as a deamon on startup
"""
import serial
import sys
from time import sleep

def initSerial():
    #Set COM port config
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.bytesize=serial.SEVENBITS
    ser.parity=serial.PARITY_EVEN
    ser.stopbits=serial.STOPBITS_ONE
    ser.xonxoff=0
    ser.rtscts=0
    ser.timeout=20
    ser.port="/dev/ttyUSB0"

    #Open COM port
    try:
        ser.open()
    except:
        sys.exit ("Error opening %s."  % ser.name)
    
    return ser

def readDataFromSerial():
    return "mock", ser.readLine()
    
    
ser = initSerial()

while True:
    (timestamp, data) = readDataFromSerial()
    print timestamp
    print data

    # sleep for 5 minutes
    sleep(300)