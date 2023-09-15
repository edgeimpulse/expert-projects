---
description: >-
  Take an existing accelerometer model built for the Thunderboard Sense 2, and
  prepare it for use on the SiLabs xG24 board.
---

# Porting a Posture Detection Project from the SiLabs Thunderboard Sense 2 to xG24

Created By: Salman Faris

Public Project: [https://studio.edgeimpulse.com/public/188507/latest](https://studio.edgeimpulse.com/public/188507/latest)

## Introduction

In this project I'm going to walkthrough how to port an existing project developed on the SiLabs Thunderboard Sense 2, to SiLabs' newer and more powerful xG24 development board.

The original project was developed by [Manivnnan Sivan](https://www.hackster.io/manivannan) to detect correct / incorrect posture of manufacturing workers using a wearable belt.

![Image from original project](../.gitbook/assets/silabs-xg24-posture-detection/device\_data-acquisition.jpeg)

I will walk you through how you can clone his Public Edge Impulse project, deploy to a SiLabs Thunderboard Sense 2, test it out, and then build and deploy to the newer SiLabs xG24 device instead.

## About the project : Posture Detection for Worker Safety

You can find more about the project here in the original project documentation, [Worker Safety Posture Detection](https://docs.edgeimpulse.com/experts/prototype-and-concept-projects/worker-safety-posture-detection).

The project is intended to help workers in manufacturing. They work in conditions that can put a lot of stress on their bodies. Depending on the worker's role in the production process, they might experience issues related to cramped working conditions, heavy lifting, or repetitive stress.

Poor posture can cause problems for the health of those who work in manufacturing. Along with that, research suggests that making efforts to improve posture among manufacturing employees can lead to significant increases in production. Workers can improve their posture by physical therapy, or simply by being more mindful during their work day.

[Manivnnan Sivan](https://www.hackster.io/manivannan) has created a wearable device using a SiLabs Thunderboard Sense 2 which can be fitted to a worker's waist. The worker can do their normal activities, and the TinyML model running on the hardware will predict the posture and communicate to the worker through BLE communication. The worker can get notified in the Light Blue App on their phone or smartwatch.

## Running the Project on Thunderboard Sense 2

Before porting, we need to run the project on the existing platform to understand how it's run and familiarize ourselves with it's parameters. So let's get started.

### Installing Dependencies

Before you proceed further, there are few other software packages you need to install.

* Edge Impulse CLI - Follow [this link](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation) to install necessary tooling to interact with the Edge Impulse Studio.
* LightBlue - This is a mobile application. Install from either Apple Store or Android / Google Play. This will be required to connect the board wirelessly over Bluetooth. The Android version can be found here: [https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer\&hl=en\_IN\&gl=US\&pli=1](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer\&hl=en\_IN\&gl=US\&pli=1). Apple / iOS users can download the App here: [https://apps.apple.com/us/app/lightblue/id557428110](https://apps.apple.com/us/app/lightblue/id557428110).

### Clone the Project

Go to the Edge Impulse project page using the [link here](https://studio.edgeimpulse.com/public/148375/latest), and clone it.

Click **Clone** on the right corner button to create a copy of the project.

![](../.gitbook/assets/silabs-xg24-posture-detection/clone-step1.png)

Provide a project name in the text field, and click on the **Clone project** button.

![](../.gitbook/assets/silabs-xg24-posture-detection/clone-step2.png)

Done, the project is successfully cloned into your Edge Impulse account:

![](../.gitbook/assets/silabs-xg24-posture-detection/clone-step3.png)

As we clone the project, it will be loaded with the dataset collected by Manivannan.

![](../.gitbook/assets/silabs-xg24-posture-detection/clone-step4.png)

### Run the Project

We can try to deploy the project on a Thunderboard Sense 2:

1. **Connect the development board to your computer** : Use a micro-USB cable to connect the development board to your computer. The development board should mount as a USB mass-storage device (like a USB flash drive), with the name `TB004`. Make sure you can see this drive.
2.  **Update the firmware** : The development board does not come with the right firmware yet. To update the firmware:

    2.1 [Download the latest Edge Impulse firmware.](https://cdn.edgeimpulse.com/firmware/silabs-thunderboard-sense2.bin)

    2.2 Drag the `silabs-thunderboard-sense2.bin` file to the TB004 drive.

    ![](../.gitbook/assets/silabs-xg24-posture-detection/2023-06-11\_16-13.png)

    2.3 Wait 30 seconds.

Next, open the CLI and run `edgeimpulse-daemon`

From here, Log in with your Edge Impulse credentials and choose the cloned project from the followed project list.

![](../.gitbook/assets/silabs-xg24-posture-detection/EIdaemon.png)

Then provide a name for the device that is connected to the computer.

![](../.gitbook/assets/silabs-xg24-posture-detection/EIdaemon2.png)

After completing these steps, you will see that the device is connected to the Edge Impulse Studio via the CLI.

![](../.gitbook/assets/silabs-xg24-posture-detection/edgeimpulse\_connect.png)

### Build & Deploy the Project

Choose "Deployment" from the left toolbar and then choose the target device as "SiLabs Thunderboard Sense 2", and click "Build" to start the process.

![](../.gitbook/assets/silabs-xg24-posture-detection/projectBuild.png)

After the build completes, a `.bin` file will be automatically generated and downloaded. You need to drag and drop it to the Thunderboard Sense 2 device drive.

![](../.gitbook/assets/silabs-xg24-posture-detection/FlashfirmwareDnD.png)

Done, we can now open the LightBlue mobile app to run and see the inference:

![](../.gitbook/assets/silabs-xg24-posture-detection/runonSense2.jpg)

Alternatively you can run it on a computer, if you don't have access to a phone. Run the command below to see if the tinyML model is inferencing.

`edge-impulse-run-impulse`

![](../.gitbook/assets/silabs-xg24-posture-detection/runonSense2-1.png)

Nice, so far we cloned and implemented the project. Now we are going to port to the new board!

## The New SiLabs EFR32MG24

SiLabs have launched the new EFR32MG24 also known as xG24 Wireless SoCs and they are full of interesting sensors and features making them very good for mesh IoT wireless connectivity using Matter, OpenThread, and Zigbee protocols for smart home, lighting, and building automation products or any other use case you see fit to this combination of sensors and connectivity.

![](../.gitbook/assets/silabs-xg24-posture-detection/efr32xg24-dev-kit-layout.jpeg)

The sensors present onboard are an accelerometer, a microphone, environmental sensors comprising temperature, humidity, and air pressure, a Hall sensor, an inertial and an interactional sensor.

![](../.gitbook/assets/silabs-xg24-posture-detection/heroshot.jpeg)

## Collect More Data Using the xG24

Compared to the Thunderboard Sense 2, the xG24 does have some changes while connecting to Edge Impulse and uploading the firmware.

1. First - [Download the base firmware image](https://cdn.edgeimpulse.com/firmware/silabs-xg24.zip) - Download the latest Edge Impulse firmware, and unzip the file. Once downloaded, unzip it to obtain the firmware-xg24.hex file, which we will be using in the following steps.
2. **Connect the xG24 Dev Kit to your computer** - Use a micro-USB cable to connect the xG24 Dev Kit to your development computer, and download and install [Simplicity Commander](https://community.silabs.com/s/article/simplicity-commander).

![](../.gitbook/assets/silabs-xg24-posture-detection/ConnectG24.webp)

3. **Load the base firmware image with Simplicity Commander** - You can use [Simplicity Commander](https://community.silabs.com/s/article/simplicity-commander) to flash your xG24 Dev Kit with the Edge Impulse [base firmware image](https://cdn.edgeimpulse.com/firmware/silabs-xg24.zip). To do this, first select your board from the dropdown list on the top left corner:

![](../.gitbook/assets/silabs-xg24-posture-detection/xg24-dk-commander-select-board.webp)

Then go to the "Flash" section on the left sidebar, and select the base firmware image file you downloaded in the first step above (i.e., the file named `firmware-xg24.hex`). You can now press the Flash button to load the base firmware image onto the xG24 Dev Kit.

![](../.gitbook/assets/silabs-xg24-posture-detection/g24-dk-commander-flash.webp)

After this, we can follow the usual method on how we select the device in the Edge Impulse Studio via the CLI.

Next, open the CLI and run `edgeimpulse-daemon`

From here, log in with your Edge Impulse credentials and choose the cloned project from the project list that follows.

![](../.gitbook/assets/silabs-xg24-posture-detection/EIdaemon.png)

Then provide a name for the device that is connected to the computer.

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24\_connection.png)

After doing these steps, you can see the device is connected to the Edge Impulse Studio via the CLI.

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24\_device.png)

I collected a bit of additional data using the xG24, and it looks good.

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24\_DataCollection.png)

Now, we need to retrain the data set, but before that we need to set the target as **SiLabs EFR32MG24**.

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24Training.png)

Great, we got nice accuracy in model training.

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24\_F1Score.png)

Now, we can build the model and deploy to the xG24. For the build, we need to choose the correct device first, then click "Build".

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24BuildModel.png)

After generating the `.bin` file, we need to use [Simplicity Commander](https://community.silabs.com/s/article/simplicity-commander) to flash your xG24 Dev Kit with this firmware. To do this, first select your board from the dropdown list on the top left corner:

![](../.gitbook/assets/silabs-xg24-posture-detection/xg24-dk-commander-select-board.webp)

Then go to the "Flash" section on the left sidebar, and select the generated firmware image file you downloaded after the build process. You can now press the Flash button to load the generated .hex file firmware image onto the xG24 Dev Kit.

![](../.gitbook/assets/silabs-xg24-posture-detection/g24-dk-commander-flash.webp)

Next, we can use the LightBlue mobile app to run and see the inference.

![](../.gitbook/assets/silabs-xg24-posture-detection/xG24App.jpg)

Alternatively, we can run on computer as we did for the Thunderboard Sense 2, if you don't have access to a phone. Run the command below to see if the tinyML model is inferencing.

`edge-impulse-run-impulse`

![](../.gitbook/assets/silabs-xg24-posture-detection/xg24\_inference.png)

Awesome, we have now successfully ported a project from Thunderboard Sense 2 to the xG24 Dev Kit!

## Conclusion

We can see here, the xG24 does a faster classification of these tinyML datasets without compromising the accuracy.

Here you can see the comparison data, and we can see **91.1765%** increased inferencing speed in the NN Classifier, while the RAM and Flash usage are the same.

![](../.gitbook/assets/silabs-xg24-posture-detection/model-optimization\_time.png)

Similar results are achieved in the field data when we are inferencing the live data stream. Here we can see a 92.3077% increase in speed in the classification, which is more than what was calculated in the model optimization.

![](../.gitbook/assets/silabs-xg24-posture-detection/InferenceTime.png)

To conclude the porting project post, we can confirm that it's worth to upgrade products and projects using the Thunderboard Sense 2 to the new and efficient SiLabs xG24 Dev Kit.
