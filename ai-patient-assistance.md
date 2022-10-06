---
description: Keyword Recognition and Notification for AI Patient Assistance With Edge Impulse and the Arduino Nano 33 BLE Sense
---

# AI-Powered Patient Assistance 

Created By:
[Adam Milton-Barker](https://www.adammiltonbarker.com/) 

Public Project Link:
[https://studio.edgeimpulse.com/public/140923/latest](https://studio.edgeimpulse.com/public/140923/latest)

## Project Demo

{% embed url="https://www.youtube.com/watch?v=JAw5SRfa95g" %}

## Project Repo

[https://www.adammiltonbarker.com/projects/downloads/AI-Patient-Assistance.zip](https://www.adammiltonbarker.com/projects/downloads/AI-Patient-Assistance.zip)

## Introduction

When hospitals are busy it may not always be possible for staff to be close when help is needed, especially if the hospital is short staffed. To ensure that patients are looked after promptly, hospital staff need a way to be alerted when a patient is in discomfort or needs attention from a doctor or nurse.

## Solution

A well known field of Artificial Intelligence is voice recognition. These machine learning and deep learning models are trained to recognize phrases or keywords, and combined with the Internet of Things can create fully autonomous systems that require no human interaction to operate.

As technology has advanced, it is now possible to run voice recognition solutions on low cost, resource constrained devices. This not only reduces costs considerably, but also opens up more possibilities for innovation. The purpose of this project is to show how a machine learning model can be deployed to a low cost IoT device (Arduino Nano 33 BLE SENSE), and used to notify staff when a patient needs their help.

The device will be able to detect three keywords **Doctor**, **Nurse**, and **Help**. The device also acts as a BLE peripheral, BLE centrals/masters such as a central server for example, could connect and listen for data coming from the device. The server could then process the incoming data and send a message to hospital staff or sound an alarm.

## Hardware

- Arduino Nano 33 BLE Sense [Buy](https://store.arduino.cc/products/arduino-nano-33-ble-sense)

## Platform

-  Edge Impulse [Visit](https://www.edgeimpulse.com)

## Software

- [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation)
- [Arduino CLI](https://arduino.github.io/arduino-cli/latest/)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Project Setup

Head over to [Edge Impulse](https://www.edgeimpulse.com) and create your account or login. Once logged in you will be taken to the project selection/creation page.

### Create New Project
Your first step is to create a new project. From the project selection/creation you can create a new project.

![Create Edge Impulse project](https://usercdn.edgeimpulse.com/project140923/31520f43ee661dcfee60c7c6f2c9fb075dd6b0691ab547c78765fd3eb2becbbb)

Enter a **project name**, select **Developer** and click **Create new project**.

![Choose project type](https://usercdn.edgeimpulse.com/project140923/7d43097af18e8f6a393a7c973b3cac63aca870dc327bf71d9b34c9fb7348f801)

We are going to be creating a voice recognition system, so now we need to select **Audio** as the project type.

### Connect Your Device

![Connect device](https://usercdn.edgeimpulse.com/project140923/9b4e4d4f3e259fb9eaa015c5317fb05b4f739607a61c5a3ee38f263bd443ab09)

You need to install the required dependencies that will allow you to connect your device to the Edge Impulse platform. This process is documented on the [Edge Impulse Website](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/arduino-nano-33-ble-sense) and includes installing:

- [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation)
- [Arduino CLI](https://arduino.github.io/arduino-cli/latest/)

Once the dependencies are installed, connect your device to your computer and press the **RESET** button twice to enter into bootloader mode, the yellow LED should now be pulsating.

Now download the the [latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/arduino-nano-33-ble-sense.zip) and unzip it, then double click on the relevant script for your OS either `flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`.

![Edge Impulse firmware installed](https://usercdn.edgeimpulse.com/project140923/85bf66854a6f687c179bf220d64037c54b03737c603993ab2dc2e27d64ad1374)

Once the firmware has been flashed you should see the output above, hit enter to close command prompt/terminal.

Open a new command prompt/terminal, and enter the following command:

`edge-impulse-daemon`

If you are already connected to an Edge Impulse project, use the following command:

`edge-impulse-daemon --clean`

Follow the instructions to log in to your Edge Impulse account.

![Device connected to Edge Impulse](https://usercdn.edgeimpulse.com/project140923/340b2db79a40f3b755e93162659d4461b12a47474c1209850ecad2e8a3351634)

Once complete head over to the devices tab of your project and you should see the connected device.

## Data Acquisition

We are going to create our own dataset, using the built in microphone on the Arduino Nano 33 BLE Sense. We are going to collect data that will allow us to train a machine learning model that can detect the words/phrases **Doctor**, **Nurse**, and **Help**.

We will use the **Record new data** feature on Edge Impulse to record 15 sets of 10 utterences of each of our keywords, and then we will split them into individual samples.

Ensuring your device is connected to the Edge Impulse platform, head over to the **Data Aqcquisition** tab to continue.

![Data acquisition](https://usercdn.edgeimpulse.com/project140923/98e52702576dbc4c7f83116a22f59bca21116406a141cdb04de387fa226d75ae)

In the **Record new data**, make sure you have selected your Arduino Nano 33 BLE Sense, then select **Built in microphone**, set the label as **Doctor**, change the sample length to 20000 (20 seconds), and leave all the other settings as.

Here we are going to record the data for the word **Doctor**. Make sure the microphone is close to you, click **Start sampling** and record yourself saying **Doctor** ten times.

![Recorded sample](https://usercdn.edgeimpulse.com/project140923/e07c91724c0407b76abb35300013e2080ff7f872cab14adee2f44d4097fc5e46)

You will now see the uploaded data in the **Collected data** window, next we need to split the data into ten individual samples.

![Data split](https://usercdn.edgeimpulse.com/project140923/de95218e947f9c68aa937f58b22b318609642bb23d0325a4b168965a57601656)

Click on the dots to the right of the sample and click on **Split sample**, this will bring up the sample split tool. Here you can move the windows until each of your samples are safely in a window. You can fine tune the splits by dragging the windows until you are happy, then click on **Split**

![Split data](https://usercdn.edgeimpulse.com/project140923/021d8196250625cd509e67fa150a7aa085577b1a0e198b4e775c22e57f55895f)

You will see all of your samples now populated in the **Collected data** window. Now you need to repeat this action 14 more times for the **Doctor** class, resulting in 150 samples for the Doctor class. Once you have finished, repeat this for the remaining classes: **Nurse** and **Help**. You will end up with a dataset of 450 samples, 150 per class.

![Main data](https://usercdn.edgeimpulse.com/project140923/77ea9d4da47f58548c3d4d358578eac1e0211b304c392db2df440c0a0f1157bd)

Now we have all of our main classes complete, but we still need a little more data. We need a **Noise** class that will help our model determine when nothing is being said, and we need an **Unknown** class, for things that our model may come up against that are not in the dataset.

For the noise class we will mix silent samples, and some other general noise samples. First of all record 100 samples with no speaking and store them in an **Noise** class.

![Data upload](https://usercdn.edgeimpulse.com/project140923/44af7ee1ce48e027a7e59cf7afcf8e603e32c92c7b504e3b82d2a19fc0e77763)

Next download the [Microsoft Scalable Noisy Speech Dataset](https://github.com/microsoft/MS-SNSD) and extract the data. Navigate to the **Noise** directory and copy 50 random samples. Next go to the **Data Acquisition** tab and upload the new data into the **Noise** class. Finally copy 100 samples from the unknown class and upload to the Edge Impulse platform as an **Unknown** class.

### Split Dataset

![split-data.jpg](https://usercdn.edgeimpulse.com/project140923/f91e796297b1fb61e1c2a36e09e7da4e8f410601cbee69a2fe8478b2f4d120ae)

We need to split the dataset into test and training samples. To do this head to the dashboard and scroll to the bottom of the page, then click on the **Perform train/test split**

![Recorded dataset](https://usercdn.edgeimpulse.com/project140923/718f288900610fba377eaca2eb457f76b869963d3e9b3ba34bd158eaa9f6e8f1)

Once you have done this, head back to the data acquisition tab and you will see that your data has been split.

## Create Impulse

![Create Impulse](https://usercdn.edgeimpulse.com/project140923/4e13b40192fa9df70221907da739f4ca111dbee66e94f72b8c2659612cfdc364)

Now we are going to create our network and train our model.

![Add processing block](https://usercdn.edgeimpulse.com/project140923/930d641805ae3e5f4f499f21d1d3f415b46b937612d6bfe0076ad05391241ce9)

Head to the **Create Impulse** tab and change the window size to 2000ms. Next click **Add processing block** and select **Audio (MFCC)**, then click **Add learning block** and select **Clasification (Keras)**.

![Created Impulse](https://usercdn.edgeimpulse.com/project140923/b170999abd8e66835b3669c358282ff57b4ac56ef42153c184512096db93a775)

Now click **Save impulse**.

### MFCC Block

#### Parameters

![Parameters](https://usercdn.edgeimpulse.com/project140923/f1f8cf0cd359fb70a8a732c4b14586ea97dececef7885cbed72083cdbaf75e17)

Head over to the **MFCC** tab and click on the **Save parameters** button to save the MFCC block parameters.

#### Generate Features

![Generate Features](https://usercdn.edgeimpulse.com/project140923/43bf78d56bd23fc6d5158af3f785d99462ea105b5328d0d5e6dffeeb6e54e27d)

If you are not automatically redirected to the **Generate features** tab, click on the **MFCC** tab and then click on **Generate features** and finally click on the **Generate features** button.

![Generated Features](https://usercdn.edgeimpulse.com/project140923/a72234c222cd5357d9e3a7004c6880d29441c200053b61a5301c846ed762cff9)

Your data should be nicely clustered and there should be as little mixing of the classes as possible. You should inspect the clusters and look for any data that is clustered incorrectly (You don't need to worry so much about the noise and unknown classes being mixed). If you find any data out of place, you can relabel or remove it. If you make any changes click **Generate features** again.

## Training

![Training](https://usercdn.edgeimpulse.com/project140923/ca7a38833708c70f4d4499202d5bf362b044f1a60214c7992f067a59a8eaf81b)

Now we are going to train our model. Click on the **NN CLassifier** tab then click **Auto-balance dataset**, **Data augmentation** and then **Start training**.

![Training complete](https://usercdn.edgeimpulse.com/project140923/0d3fcd8fdcbae81832d968bff409f94477c627e4a66eb998e4d5cf066f06bf37)

Once training has completed, you will see the results displayed at the bottom of the page. Here we see that we have 99.2% accuracy. Lets test our model and see how it works on our test data.

## Testing

### Platform Testing

![Test model](https://usercdn.edgeimpulse.com/project140923/2f5efd4cbf1fe22bdf9ba4dfc06122e01090ebddf820e80a33075f9b0dfccef9)

Head over to the **Model testing** tab where you will see all of the unseen test data available. Click on the **Classify all** and sit back as we test our model.

![Test model results](https://usercdn.edgeimpulse.com/project140923/f8498edfbaaada3872fb422789d74a45e1b37504721616a4bb1307ed8114b9fa)

You will see the output of the testing in the output window, and once testing is complete you will see the results. In our case we can see that we have achieved 96.62% accuracy on the unseen data, and a high F-Score on all classes.

### On Device Testing

![Live testing](https://usercdn.edgeimpulse.com/project140923/ad225bf5d660945bbdb52ef1d88db6c670fecd5911e376ade48c9f62297900c8)

Now we need to test how the model works on our device. Use the **Live classification** feature to record some samples for clasification. Your model should correctly identify the class for each sample.

## Performance Callibration

![Performance Callibration](https://usercdn.edgeimpulse.com/project140923/d7188d3f9d0bab7a863602c75866350984b4c7df4d93511aa991883970efdba4)

Edge Impulse has a great new feature called **Performance Callibration**, or **PerfCal**. This feature allows you to run a test on your model and see how well it will perform in the real world. The system will create a set of post processing configurations for you to choose from. These configurations help to minimize either false activations or false rejections

![Turn on perfcal](https://usercdn.edgeimpulse.com/project140923/75a1d63472765b15e28f69e4a5af8b916534c50638a0fd21bdf61f767266ffc4)

Once you turn on perfcal, you will see a new tab in the menu called **Performance callibration**. Navigate to the perfcal page and you will be met with some configuration options.

![Perfcal settings](https://usercdn.edgeimpulse.com/project140923/75def29752d9daaf2cd17ebdb12c9b9fecaef0b4ffd0dceefba8121a14d2d23c)

Select the **Noise** class from the drop down, and check the Unknown class in the list of classes below, then click **Run test** and wait for the test to complete.

![Perfcal configs](https://usercdn.edgeimpulse.com/project140923/f0f4421bd637c6e7e790f8fd207395c6eba3df4d5d648b72e0cf35e5aab948be)

The system will provide a number of configs for you to choose from. Choose the one that best suits your needs and click **Save selected config**. This config will be deployed to your device once you download and install the libray on your device.

## Versioning

![Versioning](https://usercdn.edgeimpulse.com/project140923/0362c32a3d4e13a62545fef3ec99dbd50d8e7188b13ea60ae077233f44921238)

We can use the versioning feature to save a copy of the existing network. To do so head over to the **Versioning** tab and click on the **Create first version** button.

![Versions](https://usercdn.edgeimpulse.com/project140923/8787b0e6e03865692b204717de2c365ec3829b2e7cfe2088944233a4af9deca1)

This will create a snapshot of your existing model that we can come back to at any time.

## Deployment

Now we will deploy an Arduino library to our device that will allow us to run the model directly on our Arduino Nano 33 BLE Sense.

![Build](https://usercdn.edgeimpulse.com/project140923/7a155c5879a8245f30d74782d3711f790b8a34ee7aca39d54d381a9a2f250f23)

Head to the deployment tab and select **Arduino Library** then scroll to the bottom and click **Build**.

![Build optimizations](https://usercdn.edgeimpulse.com/project140923/e591133c82426537aff4b50bf3eaf8dfa8133e037640393bd2b7ebe58b88cac7)

Note that the EON Compiler is selected by default which will reduce the amount of memory required for our model.

![Arduino library](https://usercdn.edgeimpulse.com/project140923/e9666db0e579060b15791c540c11de5cc78063cda4227d8ac315d63de7635139)

Once the library is built, you will be able to download it to a location of your choice.

## Arduino IDE

![Arduino library](https://usercdn.edgeimpulse.com/project140923/4f225a1bd492cc7e21059ab189b054464b71ed33e47e476588772737b0e1664d)

Once you have downloaded the library, open up Arduino IDE, click **Sketch** -> **Include library** -> **Upload .ZIP library...**, navigate to the location of your library, upload it and then restart the IDE.

### Non-Continuous Classification

![Non-continuous classification](https://usercdn.edgeimpulse.com/project140923/b6f8af6ec125cc124ae07111a404d939e1421a26df5588e7ec6a60ca4f0f9ee5)

Open the IDE again and go to **File** -> **Examples**, scroll to the bottom of the list, go to **AI_Patient_Assistance_inferencing** -> **nano_ble33_sense** -> **nano_ble33_sense_microphone**.

Download this project from [here](https://www.adammiltonbarker.com/projects/downloads/AI-Patient-Assistance.zip). Copy the contents of **libraries/ai_patient_assistance/ai_patient_assistance.ino** into the file and upload to your board. This may take some time.

![Arduino IDE serial](https://usercdn.edgeimpulse.com/project140923/964dc1f09968173a357c0eb72792d38a0e2d542515a56d64ac1437c0b984b8ae)

Once the script is uploaded, open up serial monitor and you will see the output from the program. The green LED on your device will turn on when it is recording, and off when recording has ended.

![Arduino Nano 33 BLE Sense](https://usercdn.edgeimpulse.com/project140923/64c2fc694ed5c72c164a3c45b183ee539bfdcc0a8f26ccabcf6c20021548a798)

Now you can test your program by saying any of the keywords when the green light is on. If a keyword is detected the red LED will turn on.

### Continuous Classification

![Continuous classification](https://usercdn.edgeimpulse.com/project140923/cb753bb37104f20e22019930f2dd795863c18722b3c1d26a96f57b7b3899c570)

Now open **AI_Patient_Assistance_inferencing** -> **nano_ble33_sense** -> **nano_ble33_sense_microphone_continuous**, copy the contents of **libraries/ai_patient_assistance/ai_patient_assistance_continuous.ino** into the file and upload to your board.

Once the script is uploaded, open up serial monitor and you will see the output from the program. The red LED will blink when a classification is made.

#### BLE

This program acts as a BLE peripheral which basically advertises itself and waits for a central to connect to it before pushing data to it. In this case our central/master is a smart phone, but in the real world this would be a BLE enabled server that would be able to interact with a database, send SMS, or forward messages to other devices/applications using a machine to machine communication protocol such as MQTT.

![nRF Connect BLE](https://usercdn.edgeimpulse.com/project140923/e8557463bc0a3a76758294abdfd80b5c10905864d5bbd537b571bf8be11c3960)

You can use a free BLE app such as [nRF Connect desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop) or [nRF Connect Mobile](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en_GB&gl=US) to connect to your device and read the data published by it.

When your BLE app connects to the program, the LED light will turn blue, once the app disconnects the LED will turn off.

## Conclusion

Here we have created a simple but effective solution for detecting specific keywords that can be part of a larger automated patient assistance system. Using a fairly small dataset we have shown how the Edge Impulse platform is a useful tool in quickly creating and deploying deep learning models on edge devices.

You can train a network with your own keywords, or build off the model and training data provided in this tutorial. Ways to further improve the existing model could be:

- Record more samples for training
- Record samples from multiple people

