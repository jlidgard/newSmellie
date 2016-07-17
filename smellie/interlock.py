# Commands to Control the SMELLIE Interlock
import sys,serial,time

def getInterlockStatus(serial):
    serial.write("v\r\n")
    time.sleep(0.05)
    response = serial.readline()
    time.sleep(0.05)
    return response

def setInterlockArm(serial):
    serial.write("a\r\n")
    time.sleep(0.05)
    response = serial.readline()
    time.sleep(0.05)
    return response
	
def setInterlockDisarm(serial):
    serial.write("d\r\n")
    time.sleep(0.05)
    response = serial.readline()
    time.sleep(0.05)
    return response
    
def sendInterlockKeepAlive(serial):
    serial.write("1\r\n")
    time.sleep(0.05)

    

