# Commands to Control the SMELLIE Interlock
import sys,serial,time
import interlock as il

def main():

    #set up COM port connection. COM8, 9600 baud
    connection = serial.Serial('COM8',9600,timeout=1)

    print "SMELLIE Laser Interlock"
    print
    print "serial port: ",connection 
    print

    try:
        while True:
            print "Interlock relay status:"
            il.getInterlockStatus(connection)

            print "Set Interlock status (arm):"
            il.setInterlockArm(connection)

            print "Send Interlock Keep Alive:"
            for x in range(10):
                il.sendInterlockKeepAlive(connection)
                time.sleep(.1)
            
            print "Set Interlock status (disarm):"
            il.setInterlockDisarm(connection)

    except KeyboardInterrupt:
        il.setInterlockDisarm(connection)
        print "interlockSMELLIE::Keyboard Interrupt has locked the Laser. Please Restart"
        pass

    connection.close()

main()    
    

