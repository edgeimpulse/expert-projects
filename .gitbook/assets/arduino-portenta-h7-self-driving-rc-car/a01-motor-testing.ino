// RC Car servo and big motor driver
// By Jeremy Ellis
// MIT license

// for now reference at https://github.com/hpssjellis/particle.io-photon-high-school-robotics/tree/master/a11-dc-motor-drivers
// although pin names wrong

// You are suppossed to get it working using the web-app
// Draw your circuit diagram first
// This program will just tell you if  the connections are working
// See https://www.pololu.com/product/1451 for assistance

// On motor driver board LED goes red for one direction and green for the other






#include <Arduino.h> // Only needed by https://platformio.org/
#include <Servo.h>

Servo myServo_D2;
int myMainSpeed = 30;
int myMainDelay = 2000;
int mySecurityDelay = 3000;

void setup() {
  
    myServo_D2.attach(D2); // D2 should do PWM on Portenta
    pinMode(D3, OUTPUT);   // digital 0 to 1
    pinMode(D5, OUTPUT);   // PWM 0 to 255
    pinMode(D6, OUTPUT);   // digital 0 to 1
    
                            // both off = glide, both on = brake (if motor can do that) 
    digitalWrite(D6, 0);    // not needing to be attached
    digitalWrite(D3, 1);    // set one direction 
    
    pinMode(LEDB, OUTPUT);

    // to connect wires and put car on ground
    digitalWrite(LEDB, LOW);    // D7 on
    delay(mySecurityDelay * 2 );
    digitalWrite(LEDB, HIGH);    // D7 on
    delay(mySecurityDelay);
    
}

void loop() {
    
    digitalWrite(LEDB, LOW);    // D7 on

    myServo_D2.write(110); // turn
    analogWrite(D5, myMainSpeed);   // go medium
    delay(myMainDelay);
    analogWrite(D5, 0);     // stop
    delay(mySecurityDelay); 
    
    myServo_D2.write(70);   // turn
    analogWrite(D5, myMainSpeed);   // go medium   
    delay(myMainDelay);    
    analogWrite(D5, 0);     // stop
    delay(mySecurityDelay); 


    myServo_D2.write(90);   // go straight
    analogWrite(D5, myMainSpeed);   // go medium   
    delay(myMainDelay);    
    analogWrite(D5, 0);     // stop
    delay(mySecurityDelay); 



    
    digitalWrite(LEDB, HIGH);  // D7 off
    delay(mySecurityDelay * 3);            // wait 9 seconds
        
}
