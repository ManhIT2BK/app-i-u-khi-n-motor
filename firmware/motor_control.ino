// #include <Wire.h>
// #include <Adafruit_PWMServoDriver.h>

// Adafruit_PWMServoDriver pwm =
// Adafruit_PWMServoDriver();

// void setup() {

//   Serial.begin(9600);

//   pwm.begin();

//   pwm.setOscillatorFrequency(27000000);

//   pwm.setPWMFreq(50);

//   delay(10);

//   for(int i=1;i<=6;i++){

//     pwm.writeMicroseconds(i,1500);
//   }
// }

// void loop() {

//   if(Serial.available()){

//     String msg =
//     Serial.readStringUntil('\n');

//     int comma = msg.indexOf(',');

//     if(comma > 0){

//       int motor =
//       msg.substring(0,comma).toInt();

//       int pwmValue =
//       msg.substring(comma+1).toInt();

//       pwm.writeMicroseconds(
//         motor,
//         pwmValue
//       );
//     }
//   }
// }