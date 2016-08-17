//////////////////////////////////////////////////////////
////Thermal Waves (GP49) Interlock & Relay Control
////v1.0, 31st May 2016
////Jeffrey Lidgard, jeffrey.lidgard@physics.ox.ac.uk
////University of Oxford, Department of Physics
//////////////////////////////////////////////////////////

#include <SPI.h>
#include "Adafruit_MAX31855.h"

//misc variables:
int byteRead = 0;
int delayInterval = 100;  //delay value in milliseconds

//flow meter variables:
const int flowMeterPin = 2;   //flow meter signal connected to digital pin 2 (input)
const int flowMeterLEDRedPin = A2; //flow red LED connected to pin A2
const int flowMeterLEDGreenPin = 6; //flow green LED connected to digital pin 6
boolean flowMeterState = false;
boolean flowMeterStateChange = false;
unsigned long flowPeriodDuration;
unsigned long flowTimeout = 100000; //slowest frequency measurable to be 10Hz (100000 microseconds).

//reference thermocouple variables:
#define MAXDO   11
#define MAXCS   12
#define MAXCLK  13
const int tempSensorLEDRedPin = A0; //temp red LED connected to pin A0
const int tempSensorLEDGreenPin = 5; //temp green LED connected to digital pin 5
boolean tempSensorState = false;
boolean tempSensorStateChange = false;
double tempSensorTemp = 0.0;
unsigned long tempSensorTempInt = 0;
double tempSensorTempThreshold = 40.0;
Adafruit_MAX31855 thermocouple(MAXCLK, MAXCS, MAXDO); // initialize the Thermocouple

//reset button variables:
const int resetButtonPin = 3; //reset button connected to digital pin 3 (input)
boolean resetButtonState = false;
boolean resetButtonStateChange = false;
boolean resetButtonLatch = false;
int resetButtonLEDRedPin = A1; //reset LED button connected to pin A1
int resetButtonLEDGreenPin = 4; //reset LED button connected to digital pin 4

//relay control variables
boolean forceSwitch=false;
const int powerRelayPin = 9; //power relay connected to digital pin 9
boolean powerRelayState = false;
boolean powerRelayStateChange = false;
const int polarityRelayPin = 8; //polarity relay connected to digital pin 8
const int polarityLEDRedPin = A3; //polarity Red LED to pin A3
const int polarityLEDGreenPin = 7; //polarity Green LED to digital pin 7
boolean polarityRelayState = false;

void setup() {

  //setup channels:
  Serial.begin(115200); //initialize serial communication at 115200 bits per second:

  randomSeed(42);

  pinMode(flowMeterPin, INPUT);
  pinMode(flowMeterLEDRedPin, OUTPUT);
  pinMode(flowMeterLEDGreenPin, OUTPUT);
  pinMode(tempSensorLEDRedPin, OUTPUT);
  pinMode(tempSensorLEDGreenPin, OUTPUT);
  pinMode(resetButtonPin, INPUT);
  pinMode(powerRelayPin, OUTPUT);
  pinMode(polarityRelayPin, OUTPUT);
  pinMode(polarityLEDRedPin, OUTPUT);
  pinMode(polarityLEDGreenPin, OUTPUT);
  pinMode(resetButtonLEDRedPin, OUTPUT);
  pinMode(resetButtonLEDGreenPin, OUTPUT);

  //set initial values:
  digitalWrite(powerRelayPin, false); //sets the relay state to initial position (OFF)
  
  digitalWrite(flowMeterLEDRedPin, false); //sets the relay state to initial position (OFF)
  digitalWrite(flowMeterLEDGreenPin, true); //sets the relay state to initial position (OFF)
  digitalWrite(tempSensorLEDRedPin, false); //sets the relay state to initial position (OFF)
  digitalWrite(tempSensorLEDGreenPin, true); //sets the relay state to initial position (OFF)
  digitalWrite(polarityLEDRedPin, false); //sets the relay state to initial position (OFF)
  digitalWrite(polarityLEDGreenPin, true); //sets the relay state to initial position (OFF)
  digitalWrite(resetButtonLEDRedPin, false); //sets the relay state to initial position (OFF)
  digitalWrite(resetButtonLEDGreenPin, true); //sets the relay state to initial position (OFF)
  
  // wait for things to stabilize
  delay(100);
}

void flowMeter(){
  //measure frequence of pulses from flow meter. 
  
  flowPeriodDuration = pulseIn(flowMeterPin, HIGH, flowTimeout); //could average this for a better result (but no need)

  //flow meter logic: (duration of pulse in microseconds)
  if (flowPeriodDuration<flowTimeout && flowPeriodDuration>10) flowMeterState = true; else flowMeterState = false;

  // 10Hz = 100    ms = 100000 microseconds
  // 100Hz = 10    ms =  10000 microseconds 
  // 1kHz =   1    ms =   1000 microseconds
  // 10kHz =  0.1  ms =    100 microseconds
  // 100kHz = 0.01 ms =     10 microseconds

  //note the duration is the time of the pulse. for frequency, take into account duty cycle (if 50% then factor of 2 on duration).
  //double hz = 1./(2.0*flowPeriodDuration/1000000.0);
  //Serial.print("Flow Duration:");Serial.print(flowPeriodDuration);Serial.print(" Flow Freq:");Serial.print(hz);Serial.print("Hz. Flow state:");Serial.println(flowMeterState);

  //update flow meter status. only switch if it needs to be switched
  if (flowMeterStateChange!=flowMeterState){
    digitalWrite(flowMeterLEDRedPin, flowMeterState); //sets the output pin (LED)
    digitalWrite(flowMeterLEDGreenPin, !flowMeterState); //sets the output pin (LED)
    flowMeterStateChange=flowMeterState;
    //resetButtonState = !resetButtonState; //toggle variable
    ////Serial.print("Changing Flow Meter State:");Serial.println(flowMeterState);  
  }
}

void resetButton(){
  //check if reset button was pressed. 
  
  resetButtonState = digitalRead(resetButtonPin); //read the input pin
  //Serial.print("Reset Button Value:");Serial.println(resetButtonState);

  //update reset button status. only switch if it needs to be switched
  if (resetButtonStateChange!=resetButtonState){
    resetButtonStateChange=resetButtonState;
    ////Serial.print("Changing Reset Button State:");Serial.println(resetButtonState);  
    resetButtonLatch = true; 
  }
  else resetButtonLatch = false; //set to true only on the loop cycle in which the button was pressed.
}

void powerRelaySwitch(boolean state){
  //update power relay status.
  forceSwitch=true; 
  powerRelayState=state;
  digitalWrite(powerRelayPin, powerRelayState); //sets the relay state
  
  digitalWrite(resetButtonLEDRedPin, powerRelayState); //sets the output pin (LED)
  digitalWrite(resetButtonLEDGreenPin, !powerRelayState); //sets the output pin (LED)
  
  Serial.print("Changing Power Relay State:\t");Serial.println(powerRelayState);  
}

void setOverrideState(boolean state){
  forceSwitch = state; 
  Serial.print("Set Override state:\t"); Serial.println(forceSwitch);
}

void powerRelay(){
  //update relay status based on flowmeter and temp sensor status. 

  if (forceSwitch==false) { //if not forced, then switch relay based on reset button, flow and temp.
    if (resetButtonLatch==true){ //if the reset button was pressed,
      if (flowMeterState==true && tempSensorState==true) powerRelayState = true;
    }
    else if (flowMeterState==false || tempSensorState==false) powerRelayState = false;
  
  
    //update relay status. only switch if it needs to be switched (or forced).
    if (powerRelayStateChange!=powerRelayState){
      digitalWrite(powerRelayPin, powerRelayState); //sets the relay state
      digitalWrite(resetButtonLEDRedPin, powerRelayState); //sets the output pin (LED)
      digitalWrite(resetButtonLEDGreenPin, !powerRelayState); //sets the output pin (LED)
      powerRelayStateChange=powerRelayState;
      ////Serial.print("Changing Power Relay State:");Serial.println(powerRelayState);  
    }
  }
}

void polarityRelaySwitch(boolean state){
  //update polarity relay status.
  polarityRelayState=state;
  digitalWrite(polarityRelayPin, polarityRelayState); //sets the relay state
  digitalWrite(polarityLEDRedPin, polarityRelayState); //sets the output pin (LED)
  digitalWrite(polarityLEDGreenPin, !polarityRelayState); //sets the output pin (LED)
  Serial.print("Changing Polarity Relay State:\t");Serial.println(polarityRelayState);
}

void referenceThermocouple() {
  //read data from reference thermocouple. reading I2S data from Adafruit thermocouple circuit.

  tempSensorTemp = thermocouple.readCelsius();

  //check value is ok
  if (isnan(tempSensorTemp)) {tempSensorState=false; tempSensorTemp=0.0;} //Serial.println("Something wrong with thermocouple!");

  //temp sensor logic:
  if (tempSensorTemp < tempSensorTempThreshold && tempSensorTemp != 0.) tempSensorState = true; //not zero for when temp sensor is d/c. works as long as not measuring zero (we don't here).
  else tempSensorState = false;

  //update temp sensor status. only switch if it needs to be switched
  if (tempSensorStateChange!=tempSensorState){
    digitalWrite(tempSensorLEDRedPin, tempSensorState); //sets the output pin (LED)
    digitalWrite(tempSensorLEDGreenPin, !tempSensorState); //sets the output pin (LED)
    tempSensorStateChange=tempSensorState;
    //resetButtonState = !resetButtonState;
    ////Serial.print("Changing Temp Sensor State:");Serial.println(tempSensorState);  
    ////Serial.print("Internal Temp = ");Serial.println(thermocouple.readInternal());
  }
  tempSensorTempInt = tempSensorTemp*100;
}

void serialCommunication(){
  // communicate via serial port
  if (Serial.available()) { //look what is in serial data buffer

    byteRead = Serial.read();
    //Serial.println(byteRead, DEC); //check value received

    switch(byteRead){
      case 97: // 97 = 'a' character. Report system status.
        Serial.print("Flow state:\t");Serial.print(flowMeterState);Serial.print("\t");
        Serial.print("Temp state:\t");Serial.print(tempSensorState);Serial.print("\t");
        Serial.print("Relay state:\t");Serial.print(powerRelayState);Serial.print("\t");
        Serial.print("Polarity state:\t");Serial.print(polarityRelayState);Serial.print("\t");
        Serial.print("Temperature:\t");Serial.print(tempSensorTempInt);Serial.print("\t");
        Serial.print("\n");
        break;
      case 98: polarityRelaySwitch(true); break;  // 98 = 'b' character. Set polarity relay on.
      case 99: polarityRelaySwitch(false); break;  // 99 = 'c' character. Set polarity relay off.
      case 100: powerRelaySwitch(true); break;  // 100 = 'd' character. Force power relay on.
      case 101: powerRelaySwitch(false); break; // 101 = 'e' character. Force power relay off.
      case 102: setOverrideState(false); break; // 102 = 'f' character. Turn off forced mode (use flow,temp,reset button to set relay).
    }
  }
}

void loop() {

  //main program delay
  delay(delayInterval); //delay by 1/x Hz (note the ultimate run rate is also effected by various function timeouts, eg serial.read and pulseIn.)

  referenceThermocouple(); //measure & check reference thermocouple temperature is less than threshold

  flowMeter(); //check flow meter has sent a pulse in the last x seconds.

  resetButton(); //check reset button has been pressed.

  powerRelay(); //if the conditions are passed, change the relay state.

  serialCommunication(); //receive commands, send data via serial port. Labview to read this data.
}
