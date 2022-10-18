---
description: With some physics and a TinyML model, add weight prediction to a pallet-wrapping machine.
---

# Real-time Stretch-film Machine: Weight Scale and Predictive Maintenance 

Created By:
Simone Salerno 

Public Project Link:
[https://studio.edgeimpulse.com/public/136188/latest](https://studio.edgeimpulse.com/public/136188/latest)

## Intro

In industrial settings, many factories need to handle pallets. It is a storage format that spans almost all sectors.

![Pallet Example](https://image.made-in-china.com/202f0j00htsRFrSMZZuH/PE-Stretch-Film-for-Carton-Packaging-and-Pallet-Packaging.jpg)

To speed up the packaging process, there is a machine that is devoted to wrapping the pallet contents into a plastic film to keep the contents tight and secured.

![Pallet Stretch-film Machine](https://upload.wikimedia.org/wikipedia/commons/0/0a/Pallet_wrapper.jpg)

That's the sole purpose of this machine in the factory or production facility.  But with the help of machine learning, we can upgrade these existing dumb-machines to add a new feature: weighing the pallets.

It may not appear that obvious, but we don't need a weight/pressure sensor to do this. Nor do we need to modify the 
circuitry or retrofit the machine.

Instead, we can use a "plug-in", external device that only consists of an accelerometer and a microcontroller.

And as we'll see shortly, this external device can even add predictive maintenance capabilites to the machine by pro-actively identifying malfunctions from the data and patterns collected.


## The Rationale

The methodology behind this measurement technique is pretty simple: the pallet machine has a rotating motor at its core that is necessary to wrap the plastic film around the pallet.

During its rotation, the motor is subject to a friction that is proportionate to the weight on the platform. We can capture slight variations in the rotation pattern by means of an IMU.

We'll then use the **accelerometer and gyroscope data as a proxy for the friction** on the motor. By modelling this relation through machine learning, we aim to be able to predict the weight based on the IMU readings.

This will work wonderfully, because the machine always applies the same rotation force to the motor: if a large weight is on the platform, it will rotate slower than if the platform had no weight upon it.

### Predictive Maintenance

Once we've modelled the relation between IMU data and weight, we can use it another way too: if we know the true weight of the pallet that's on the platform, we can compare it with the predicted weight, and look for discrepancies.

If they do not match by a large amount, it means that something is not working as usual. If the predicted weight is much higher than the actual one, it may mean that the motor is subject to more friction than it should be and that friction is not due to the pallet itself. Perhaps it needs to be oiled to work more smoothly, or some other issue is causing added strain on the motor.

## Hardware Requirements and Settings

The requirements are pretty simple: on the hardware side you only need an IMU and a microcontroller (or a board with an integrated IMU, such as the Arduino Nano BLE Sense).

To avoid using cables that may interfere with the operation of the machine, it is advisable to choose a board that has either WiFi or Bluetooth radio, so you can stream data to your PC wirelessly.

The setup is simple too: assemble your board with a battery in a plastic box, and anchor it on the rotating platform, near the edge of the rotating platter *(at the border, linear velocity is greater than in the center, so the IMU can pick-up pattern variations more easily)*.

This project is articulated in 3 steps:

 1. Collect training data
 2. Design the Impulse
 3. Deploy the model and use it

## Collect Training Data

The first step is to collect training data for our model. 

### Code 

If using the Arduino Nano BLE Sense (or similar board with integrated IMU and BLE), you can use the following two code snippets: the first one has to be flashed on the board to enable the BLE data streaming, the second one has to run on your PC to receive the streamed data.

On the Arduino:

```cpp
#include <Arduino_LSM9DS1.h>
#include <ArduinoBLE.h>


// data structure to hold 3 accelerometer + 3 gyroscope values
union imu_dtype {
  float values[6];
  uint8_t bytes[6 * sizeof(float)];
} imuReading;


BLEService imuService("9f0283a8-ffbb-44c2-87fc-f4133c1d1302");
BLECharacteristic imuCharacteristic("9f0283a8-ffbb-44c2-87fc-f4133c1d1305", BLERead | BLENotify, sizeof(imuReading.bytes));
BLEDevice central;


void setup() {
  Serial.begin(115200);
  delay(3000);
  Serial.println("Started");
  
  while (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    delay(1000);
  }

  while (!BLE.begin()) {
    Serial.println("Failed to initialize BLE!");
    delay(1000);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");

  // configure BLE
  BLE.setDeviceName("Arduino BLE Sense");
  BLE.setLocalName("Arduino BLE Sense");
  BLE.setAdvertisedService(imuService);
  imuService.addCharacteristic(imuCharacteristic);
  BLE.addService(imuService);
  BLE.advertise();
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;

  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
    IMU.readAcceleration(ax, ay, az);
    IMU.readGyroscope(gx, gy, gz);
    
    Serial.print(ax);
    Serial.print('\t');
    Serial.print(ay);
    Serial.print('\t');
    Serial.print(az);
    Serial.print('\t');
    Serial.print(gx);
    Serial.print('\t');
    Serial.print(gy);
    Serial.print('\t');
    Serial.println(gz);
    
    BLE.advertise();

    // try to connect to PC
    if (!central || !central.connected())
      central = BLE.central();

    // if connected, stream data
    if (central && central.connected()) {
      Serial.println("streaming...");
      
      imuReading.values[0] = ax;
      imuReading.values[1] = ay;
      imuReading.values[2] = az;
      imuReading.values[3] = gx;
      imuReading.values[4] = gy;
      imuReading.values[5] = gz;
      
      imuCharacteristic.writeValue(imuReading.bytes, sizeof(imuReading.bytes));
    }
  } 
}
```

On your PC, you need Python to run the following script that connects to the microcontroller and saves the streamed data to a file:

```bash
pip install bleak
```

```python
import asyncio
import csv
from time import sleep
from struct import unpack
from bleak import BleakScanner, BleakClient


readings = []
collect_time_in_seconds = 30


def on_notify(_, data):
    """
    To be run when new data comes from BLE
    :param _:
    :param data:
    :return:
    """
    global readings

    # packet is made of 6 floats (ax, ay, az, gx, gy, gz)
    parsed_data = unpack('ffffff', data)
    print(parsed_data)
    readings.append(parsed_data)


async def main():
    arduino = None
    imu_characteristic = '9f0283a8-ffbb-44c2-87fc-f4133c1d1305'
    devices = await BleakScanner.discover()

    # find Arduino device
    for device in devices:
        print('Found device', device.name, 'at address', device.address)

        if 'Arduino BLE Sense' in device.name:
            arduino = device
            break

    # no board found, abort
    if arduino is None:
        print('Cannot find Arduino board')
        return

    # connect to BLE characteristic
    async with BleakClient(arduino.address) as client:
        await client.start_notify(imu_characteristic, on_notify)
        print('Started collection...')
        sleep(collect_time_in_seconds)
        await client.stop_notify(imu_characteristic)

    # save to CSV
    filename = input('Which weight is this? ')

    with open('%s.csv' % filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ax', 'ay', 'az', 'gx', 'gy', 'gz'])
        writer.writerows(readings)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

### Data Collection

To accurately model the IMU <-> weight relation, you need a few reference weights. How much of them and at what increments, depends on your use case.

For this guide, I collected data at the following weights (in kg):

 - 0
 - 40
 - 80
 - 120
 - 160
 - 200
 - 240
 - 280
 - 320
 - 430
 - 600
 - 1000

At lower weights (until 300 kg), I collected data at 40 kg intervals because I wanted to differentiate at a finer granularity. Then I increased the step to 100, 200 and 400 kg because at higher weights I only wanted to get a rough idea.

Feel free to customize your own scale as you see fit.

*Warning: you can't expect to achieve a very fine granularity (eg. 1-5 kg) because the friction variation on the motor would be too small. Aim for 40-50 kg steps at least.*

As with all Machine Learning projects, the more data you collect, the better. I collected 30 seconds of data for each weight at a 26 Hz sampling rate. If your IMU supports higher rates (most allows up to 104 Hz), you can go with that and test if it increases your overall accuracy. The longer the time that you collect data, the more robust your model will be.

For each weight on the machine, follow these procedures:

 1. Put the microntroller board on the platform and turn it on
 2. Put the weight on the platform
 3. Start the machine and let it go for a few seconds (so it reaches its normal speed)
 4. Run the Python script and wait for the data collection to complete
 5. Input a name for the CSV file that will contain data for the given weight

Repeat the process for each weight.

You will end up with a list of CSV files, one for each weight. This is an easy format to import into Edge Impulse.

## Impulse Design

Edge Impulse allows for 3 different tasks:

 - Classification
 - Regression
 - Anomaly detection

In our case, we want to model a *continous* relation between the input (IMU data) and the output (weight), so it is a 'regression' task.

More specifically, this is a time-series regression task, so we will need to window our data and extract spectral features from it. This is most often the case when working with time series data.

The window duration depends on the working speed of your machine. My advicce here is to go with a large duration, because we expect the rotation to not be very fast: if your window is too short, it won't contain much variation in data.

Nevertheless, this is mostly a trial-and-error process. Since Edge Impulse makes it so easy to experiment with different configurations, start with a reasonable value of 3-5 seconds and then tune based on the accuracy feedback.

![Impulse Design](https://eloquentarduino.com/ei/palletizer/ei-palletizer-regression-impulse.png)

![DSP Results](https://eloquentarduino.com/ei/palletizer/ei-palletizer-regression-dsp.png)

The model doesn't need to be overly complex: start with a 2-layer fully-connected network and see if it performs well for you. If not, increase the number of layers or neurons.

![Topology](https://eloquentarduino.com/ei/palletizer/ei-palletizer-result.png)

## Firmware Deployment

Once you're satisfied with the results, it is time to deploy the trained Neural Network back to your board.

If using the [Eloquent Arduino library](https://eloquentarduino.com/libraries/eloquent-edge-impulse/), this part is very straightforward.

Once again, we'll use BLE to stream the predicted weight wirelessly to a PC. On the Arduino, run this snippet:

```cpp
#include <Arduino_LSM9DS1.h>
#include <ArduinoBLE.h>
#include <eloquent.h>

// replace this with the library downloaded from Edge Impulse
#include <palletizer_inferencing.h>
#include <eloquent/tinyml/edgeimpulse.h>

using namespace Eloquent::TinyML::EdgeImpulse;

Impulse impulse;
ImpulseBuffer buffer;

BLEService weightService("9f0283a8-ffbb-44c2-87fc-f4133c1e1302");
BLEFloatCharacteristic weightCharacteristic("9f0283a8-ffbb-44c2-87fc-f4133c1e1305", BLERead | BLENotify);
BLEDevice central;


void  setup() {
  Serial.begin(115200);
  delay(3000);

  while (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    delay(1000);
  }

  while (!BLE.begin()) {
    Serial.println("Failed to initialize BLE!");
    delay(1000);
  }

  // configure BLE
  BLE.setDeviceName("Arduino BLE Sense");
  BLE.setLocalName("Arduino BLE Sense");
  BLE.setAdvertisedService(weightService);
  weightService.addCharacteristic(weightCharacteristic);
  BLE.addService(weightService);
  BLE.advertise();

  Serial.println("Start collecting data...");
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;

  // read IMU data, if available
  if (!IMU.accelerationAvailable() || !IMU.gyroscopeAvailable())
    return;
    
  IMU.readAcceleration(ax, ay, az);
  IMU.readGyroscope(gx, gy, gz);

  float features[6] = {ax, ay, az, gx, gy, gz};

  if (!buffer.push(features, 6))
    // Queue is not full yet
    return;

  // we are ready to perform inference
  float prediction = impulse.regression(buffer.values);

  Serial.print("Predicted weight: ");
  Serial.println(prediction);

  // stream predicted weight over BLE
  BLE.advertise();

  // try to connect to PC
  if (!central || !central.connected())
    central = BLE.central();

  // if connected, stream data
  if (central && central.connected()) {
    Serial.println("streaming...");
    
    weightCharacteristic.writeValue(prediction);
  }
}
```

The `ImpulseBuffer` is a data structure that holds an array where you can push new values. When the buffer is full, it shifts the old elements out to make room for the new ones. This way, you have an "infinite" buffer that mimics the windowing scheme of Edge Impulse.

To perform the prediction over the window of collected data, you only need to call `impulse.regression(buffer.values)` and use the result as per your project needs.

In this example, we stream the value over BLE. In your own project, you could also use the value to control an actuator or raise an alarm when certain weights are detected.

## Real-world Deployment Example

To give you a real-world example on how to use this project, we'll pretend we have an LED display near the stretch-film machine where we want to see in real-time the predicted weight.

Since we're already streaming the data over BLE, we need a receiver device connected to the display. For the sake of the example, we'll use another Arduino BLE Sense.

![TM1637 Display](https://www.makerguides.com/wp-content/uploads/2019/08/TM1637-4-digit-7-segment-display-Arduino-tutorial-featured-image.gif)

On this device, run the following snippet:

```cpp
/**
 * Display weight from BLE on TM1637 display
 * Download library from https://github.com/avishorp/TM1637
 */
#include <ArduinoBLE.h>
#include <TM1637Display.h>


BLEDevice peripheral;
TM1637Display display = TM1637Display(2, 3);

union weight_dtype {
  float weight;
  uint8_t bytes[sizeof(float)];
} weightPayload;


void  setup() {
  Serial.begin(115200);
  delay(3000);

  while (!BLE.begin()) {
    Serial.println("Failed to initialize BLE!");
    delay(1000);
  }
}


void loop() {
  // connect to peripheral
  if (!peripheral) {
    BLE.scanForName("Arduino BLE Sense");
    peripheral = BLE.available();
  }

  if (!peripheral)
    return;

  if (!peripheral.connected())
    peripheral.connect();

  if (!peripheral.connected())
    return;

  BLE.stopScan();
  BLECharacteristic weightCharacteristic = peripheral.characteristic("9f0283a8-ffbb-44c2-87fc-f4133c1e1305");

  // read value
  if (!weightCharacteristic.readValue(weightPayload.bytes, sizeof(weightPayload.bytes)))
    return;
  
  Serial.print("Got: ");
  Serial.println(weightPayload.weight);
  display.showNumberDec((uint16_t) weightPayload.weight);
}
```

This should then render the predicted weight on the 7-segment display.

## Conclusion

This project aims to add machine learning to a traditional industrial machine, making it smarter and also adding predictive maintenance capabilites as well. Using only a microcontroller and an IMU, we were able to add weight estimation for pallets, and can identify when the rotational speed (force) of a motor is inconsistent with predicted values.
