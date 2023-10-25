---
description: >-
  Use machine learning classification to monitor the operation of a DC motor, and identify fault conditions that indicate a need for maintenance.
---

# Condition Monitoring - Syntiant TinyML Board

Created By: Swapnil Verma

Public Project Link: [https://studio.edgeimpulse.com/public/283457/latest](https://studio.edgeimpulse.com/public/283457/latest)

## Introduction

Nearly all machines require routine maintenance to maintain proper functionality. If not provided, they can break down abruptly. Sometimes, even between routine maintenance being performed, parts of a machine may fail. A failure of a mission-critical or high availability system can be disastrous for an organisation. To avoid such a scenario, a condition monitoring system is recommended for predictive maintenance, to help detect a potential failure in advance to possible reduce downtime.

Most condition monitoring systems are architected similar to the below image:

![Conventional Architecture](../.gitbook/assets/condition-monitoring-syntiant-tinyml/conventional_architecture.png)

This generally works, but it has few potential problems:

- Cloud services used in condition monitoring or predictive maintenance systems cost a lot of money in licensing and subscription fees.
- Confidential data which an organisation may want to process and store on-site may also require an on-premise server to run the cloud services and software, which again adds to the cost of the system.
- Microcontrollers are cheap and have a lot of computing power. They are not always used to their full potential. We are mostly using them for data capture.

## A Solution

A solution I am proposing focuses on the machine learning part of the conventional condition monitoring architecture. Instead of using cloud services for inferencing of the classification algorithm, we can use a microcontroller and TinyML.

Microcontrollers like the one found on the [Syntiant TinyML board](https://www.syntiant.com/tinyml) are powerful enough to run machine learning models with 3 dense layers, and 256 neurons in each layer. Further, this is acconplished with ultra low power consumption. We can utilise this board to capture data and perform classification locally with the help of Edge Impulse.

Other parts of the architecture (e.g. database, dashboard, data ingestion model etc.) can also be replaced with in-house developed solutions, if desired.

![TinyML Architecture](../.gitbook/assets/condition-monitoring-syntiant-tinyml/updated_architecture.png)

## Hardware

To demostrate my solution, I prepared a test setup which requires the following components:

- Syntiant TinyML board
- A microSD card - Syntiant TinyML board requires this for IMU data collection.
- A DC motor
- A motor controller - For this application I have used the below items to prepare a motor controller circuit:
  - Arduino MKR WiFi 1010
  - MKR motor shield
  - A battery
- Different loads to simulate normal and failure operations
- A 3D printed workbench
  
![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3899.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3918.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3924.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3927.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3930.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3934.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3938.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3940.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3942.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3944.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3948.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3950.JPG)

![](../.gitbook/assets/condition-monitoring-syntiant-tinyml/IMG_3952.JPG)

I have used this hardware setup for data collection and testing the neural network model.

> **Note: Look close at the picture of the fan blades, as there are some that are intentionally missing blades in order to trigger imbalances and rotational movements that are abnormal from a "regular" fan, to simulate fault conditions.**

## How It Works

To build this prototype, the following steps are required:

![How it Works](../.gitbook/assets/condition-monitoring-syntiant-tinyml/how_it_works.png)

1. The computer in this setup performs multiple jobs. It is a UI for controlling the DC motor by a serial connection to the Arduino, and it is also a gateway for connecting to the Syntiant TinyML board with the Edge Impulse Studio.

> More information about how to connect a supported MCU board with Edge Impulse is [available here](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli).

2. A user can start or stop the DC motor via the Arduino serial connection, which then generates vibrations as it turns on and off. The pitch and amplitude of the vibration varies based on the load attached to the motor shaft.

3. The Syntiant TinyML board is physically attached to the motor mount. The board has a 6-axis motion sensor which picks up the vibrations generated by the motor and the load.

4. The vibration data is collected and sent to the Edge Impulse Studio for training and testing.

## Data Collection

Edge impulse has simplified the machine learning pipeline extensively for TinyML. It has made data collection, training a model using collected data, testing the model, and deployment of that model back to the embedded board trivial.

- To proceed with the IMU data collection using the Syntiant TinyML board and the Edge Impulse, you must flash the [IMU firmware](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/syntiant-tinyml-board#connecting-to-edge-impulse) provided in [this documentation](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/syntiant-tinyml-board). If it is your first time using the Syntiant TinyML board with the Edge Impulse, then I would recommend following [this documentation](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/syntiant-tinyml-board) from the beginning.

> Note: Plese make sure to download and flash the **IMU firmware** and NOT the Audio firmware.

- After flashing the firmware run the below command:

```
edge-impulse-daemon
```

This will start a wizard, and ask you to login and choose an Edge Impulse project. This is a good time to prepare a project in Edge Impulse if you have not already done so.

- The above step should establish a communication between the Syntiant TinyML board and your Edge Impulse project. To verify that,  navigate to the **Devices** tab of the project. You should see the Syntiant TinyML board listed, and the *Remote managment* column should have a green dot in it.

![Devices](../.gitbook/assets/condition-monitoring-syntiant-tinyml/devices_connected.png)

After establishing a connection between the Syntiant TinyML board and Edge Impulse Studio, we will now setup the Arduino and rest of the test bench for simulating a machine status.

- Download the Arduino code from the below GitHub repository and flash it to the MKR WiFi 1010:

[https://github.com/sw4p/condition_monitoring](https://github.com/sw4p/condition_monitoring)

The Arduino takes the following commands via its serial connection:
    - `MOTORON`: Turn the motor ON
    - `MOTOROFF`: Turn the motor OFF
    - `MOTORSPEED <-100 to 100>`: Change motor speed and direction based on the number provided.

- After connecting a load to the motor, turn on the motor by sending `MOTORON` via serial to the Arduino.

- Now navigate to the **Data acquisition** tab in the Edge Impulse Studio. Here you will find the device we connected in the previous step, and the sensor list. Select the _Accelerometer_ sensor and use the default parameters.

- Add a **Label name** based on the load connected. If it is a balanced load then use *Normal_Motion* as a label, and for unbalanced loads (fans that are missing blades), use *Error* as a label. Labels are classes of your data.

- Click **Start Sampling**, which will start the sample collection process. Once the sample is collected, it will be automatically uploaded to the Studio.

![Data Acquisition](../.gitbook/assets/condition-monitoring-syntiant-tinyml/data_acquisition.png)

- Repeat this process for unbalanced loads and also for the "Motor off" condition. Also make sure to collect a proportional amount of data per class.

> Note: The Syntiant NDP chip requires a negative class on which no predictions will occur, in our example this is the `Z_No_Motion` (motor off condition) class. Make sure the class name is last in alphabetical order with the negative class at the end.

![Data Proportion](../.gitbook/assets/condition-monitoring-syntiant-tinyml/data_proportion.png)

- Once enough data is collected, split it into Train and Test datasets from the Dashboard:

![Train and Test Split](../.gitbook/assets/condition-monitoring-syntiant-tinyml/train_test_split.png)

## Model Preparation

After data collection, the next step will be machine learning model preparation. To do so, navigate to the **Impulse design** tab and add the relevant **Preprocessing** and **Learning** blocks to the pipeline.

- The Edge Impulse Studio will automatically add an input block and it will recommend a suitable Preprocessing and Learning block based on the data type ((IMU and Classification, in this case). I have used the recommended ones in this project with the default arguments.

![Impulse Design](../.gitbook/assets/condition-monitoring-syntiant-tinyml/impulse_design.png)
  
- After Impulse design is complete, save the design and navigate to the **Preprocessing** tab (_Spectral features_ in this case) for the feature generation.

![Preprocessing](../.gitbook/assets/condition-monitoring-syntiant-tinyml/preprocessing.png)
  
- Click on the **Save parameters** button, then navigate to the **Generate features** tab and click the **Generate features** button for data preprocessing.

![Generate Feature](../.gitbook/assets/condition-monitoring-syntiant-tinyml/generate_feature.png)
  
- After feature generation is complete (it could take a few minutes), please navigate to the **Learning** tab (_Classifier_ in this case) to design the neural network architecture. Here again, I have used the default architecture and parameters recommended by the Edge Impulse Studio. After selecting a suitable training cycle and learning rate, click on the **Start training** button.

![Model Training](../.gitbook/assets/condition-monitoring-syntiant-tinyml/model_training.png)

- Once the training is complete, navigate to the **Model testing** tab, and click the **Classify all** button.  This will begin the process of evaluating the built model against unseen data, which was the _Test_ bucket of data set aside early when we did the split.

![Model Testing](../.gitbook/assets/condition-monitoring-syntiant-tinyml/model_testing.png)

After testing is finished, the Edge Impulse Studio will show the model accuracy, and other parameters.

> Even though it is a simple example, the Edge Impulse Studio prepared an excellent machine learning model just by using the default recommended parameters, in just a couple of minutes.

## Deployment

Once the training and testing is complete, we can convert the machine learning model into a library or binary for the Syntiant TinyML board and deploy it for local inference on the device.

Because the Syntiant TinyML board is fully supported by the Edge Impulse, this task is as easy as the previous procedures.

- Simply navigate to the **Deployment** tab and select the target device. Also, specify the deployment type based on the options provided and click **Build**.

![Deployment Tab](../.gitbook/assets/condition-monitoring-syntiant-tinyml/deployment_tab.png)

- After building the binary or library, the Studio will automatically download the firmware to the computer, and provide guidance on how to flash it to the selected board. Usually it requires running the downloaded `flash_<operating_system>` script, which should flash the binary onto the Syntiant TinyML board.

![Flash Instruction](../.gitbook/assets/condition-monitoring-syntiant-tinyml/flash_instruction.png)

## Conclusion

Once the firmware is loaded onto the board, you can run inference locally on the Syntiant TinyML board by using the Edge Impulse CLI to launch a runner application. With the TinyML board attached to your computer via USB, run the following command from a terminal to begin inferencing:

```
edge-impulse-run-impulse
```

This will output classification results in the terminal, and you can verify that your model is properly predicting the normal, unbalanced, and off states of the motor.

At this point, you can iterate and build your own firmware, integrate the inferencing into your own application, and develop alerting capabilities to raise awareness of unexpected or out-of-bounds conditions.

## References

- <a href="https://www.flaticon.com/free-icons/classification" title="classification icons">Classification icons created by SBTS2018 - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/performance" title="performance icons">Performance icons created by Design Circle - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/automation" title="automation icons">Automation icons created by Becris - Flaticon</a>
- <a href="https://www.flaticon.com/free-icons/stream" title="stream icons">Stream icons created by juicy_fish - Flaticon</a>

