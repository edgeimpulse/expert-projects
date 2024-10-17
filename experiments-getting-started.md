---
description: Discover how to use the Experiments feature to test and improve machine learning model accuracy.
---

# Getting Started with Edge Impulse Experiments

Created By:
[Adam Milton-Barker](https://www.AdamMiltonBarker.com)

Public Project Link:
[https://studio.edgeimpulse.com/public/521263/latest](https://studio.edgeimpulse.com/public/521263/latest)

![](.gitbook/assets/experiments-getting-started/edge-impulse-experiments.jpg)

## Introduction

Edge Impulse Experiments are a powerful new feature that allows users to run multiple active Impulses within a single project. This enables seamless experimentation with various model configurations on the same dataset, offering a more efficient way to compare results.

The updated interface includes a new "Experiments" section, which centralizes Impulse management and integrates the EON Tuner for enhanced trial handling. Along with API enhancements and streamlined processes, these changes significantly accelerate development and improve project organization, making it easier to transition from data collection to deployment.

This project provides a walk through of how to use Experiments, along with a tutorial that will help you get started with Edge Impulse Experiments.

## Hardware

- Arduino Nano RPI2040 Connect [More Info](https://store.arduino.cc/products/arduino-nano-rp2040-connect)

## Platform

-  Edge Impulse [Visit](https://www.edgeimpulse.com)

## Software

- Edge Impulse CLI [Download](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation)
- Arduino CLI [Download](https://arduino.github.io/arduino-cli/latest/)
- Arduino IDE 2.2.1 [Download](https://www.arduino.cc/en/software)

## Getting Started

### Arduino Nano RPI2040 Connect

![Arduino Nano RPI2040 Connect](.gitbook/assets/experiments-getting-started/arduino-nano-rpi2040-connect.jpg "Arduino Nano RPI2040 Connect")

The Arduino Nano RP2040 Connect is a highly versatile development board, bringing the power of the Raspberry Pi RP2040 microcontroller to the compact Nano form factor. Equipped with dual-core 32-bit Arm Cortex-M0+ processors, it enables seamless creation of IoT projects with built-in Wi-Fi and Bluetooth support via the U-blox Nina W102 module. The board includes an accelerometer, gyroscope, RGB LED, and omnidirectional microphone, making it ideal for real-time data collection and embedded AI applications.

![Arduino Nano RPI2040 Connect Pins](.gitbook/assets/experiments-getting-started/arduino-nano-rpi2040-connect-pins.jpg "rduino Nano RPI2040 Connect Pins")

The Nano RP2040 Connect is fully compatible with the Arduino Cloud platform, allowing users to rapidly prototype IoT solutions. It also supports MicroPython for those who prefer Python for programming. With a clock speed of 133 MHz, the board is well-suited for machine learning tasks, offering support for frameworks like TinyML and TensorFlow Lite. Additionally, its 6-axis IMU and temperature sensor expand the board's capability for advanced real-world applications.

To begin working with the Edge Impulse platform and the Nano RPI2040 Connect, follow [this tutorial](https://docs.edgeimpulse.com/docs/edge-ai-hardware/mcu/raspberry-pi-rp2040) to connect your device.

## Edge Impulse

### Create Edge Impulse Project

![Create Edge Impulse Project](.gitbook/assets/experiments-getting-started/edge-impulse-project.jpg "Create Edge Impulse Project")

Now it's time to create your Edge Impulse project. Head over to [Edge Impulse](https://studio.edgeimpulse.com/), log in, and create your new project.

Edge Impulse offers Experiments to all users, with the Community tier allowing up to three simultaneous Experiments. Users on the Professional Plan and Enterprise tiers enjoy unlimited access to Experiments. You can explore all the platform's advanced features by signing up for an [Enterprise Trial](https://studio.edgeimpulse.com/trial-signup).

![Create Edge Impulse Project Dashboard](.gitbook/assets/experiments-getting-started/edge-impulse-project-dashboard.jpg "Create Edge Impulse Project Dashboard")

Once your project is created, you will see the project dashboard which will show you new additions to the platform.

### Connect Your Device

Next you need to connect your device to the Edge Impulse platform. Ensuring you have the Nano connected to your computer, open a command line or terminal and use the following command:

```bash
edge-impulse-daemon
```

![Edge Impulse Project Device Connection](.gitbook/assets/experiments-getting-started/edge-impulse-devices-cmd.jpg "Edge Impulse Project Device Connection")

You will be prompted for your Edge Impulse login details to proceed. Once authenticated you will need to choose the COM port that your device is connected to, and then select the Edge Impulse project you want to connect your device to.

![Edge Impulse Project Device Connected](.gitbook/assets/experiments-getting-started/edge-impulse-devices-rp2040-connected.jpg "Edge Impulse Project Device Connected")

If you now head over to your project and go the `Devices` tab, you will see your device is now connected.

### Collect Data

![Edge Impulse Project Collect Data](.gitbook/assets/experiments-getting-started/edge-impulse-rp2040-collect-data.jpg "Edge Impulse Project Collect Data")

Now that your device is connected to Edge Impulse, it is time to collect some data. Head over to the `Data aquisition` tab and select the RPI2040.

![Edge Impulse Project Collect Normal Data](.gitbook/assets/experiments-getting-started/edge-impulse-rp2040-collect-data-normal.jpg "Edge Impulse Project Collect Normal Data")

First we will create the `normal` data. This data will represent when a machine is running normally with no abnormal vibrations. Select the `Intertial` sensor and use `Normal` as the label. Next record about 3 minutes data, collected in 10 second samples from the device.

![Edge Impulse Project Collect Vibrations Data](.gitbook/assets/experiments-getting-started/edge-impulse-rp2040-collect-data-vibrations.jpg "Edge Impulse Project Collect Vibrations Data")

Next we will collect some `Vibrations` data. Change the label to `Vibrations` and record 3 minutes more of samples, but this time shake the Arduino around while the samples are being recorded.

![Edge Impulse Project Collected Data](.gitbook/assets/experiments-getting-started/edge-impulse-rp2040-collected-data.jpg "Edge Impulse Project Collected Data")

You should now have about 6 minutes of data. Note that at this point the data is not split into Training and Testing groups.

![Edge Impulse Project Collected Data Split](.gitbook/assets/experiments-getting-started/edge-impulse-data-train-test-split.jpg "Edge Impulse Project Collected Data Split")

Head to the project dashboard and scroll to the `Danger Zone` at the bottom. Click on the `Perform train/test split` button to split the data.

![Edge Impulse Project Collected Data Split](.gitbook/assets/experiments-getting-started/edge-impulse-data-split.jpg "Edge Impulse Project Collected Data Split")

Back on the `Data aquisition` tab, you will now see that the data has been split.

### Create Impulse

![Edge Impulse Project Create Impulse](.gitbook/assets/experiments-getting-started/edge-impulse-create-impulse.jpg "Edge Impulse Project Create Impulse")

Now it is time to create your Impulse. Head over to the `Create Impulse` tab and you should see the configuration for your Nano RPI2040. You can accept the defaults here.

### Spectral Analysis

![Edge Impulse Project Create Spectral Analysis Impulse](.gitbook/assets/experiments-getting-started/edge-impulse-create-impulse-spectral.jpg "Edge Impulse Project Create Spectral Analysis Impulse")

First we will use the `Spectral Analysis` Processing block. Spectral Analysis is ideal for examining repetitive movements, particularly using accelerometer data. Tthis tool breaks down signals to reveal their frequency and power patterns over time.

Click `Add` to add the Spectral Analysis Processing block to your Impulse.

### Classification

![Edge Impulse Project Create Spectral Analysis Classification Impulse](.gitbook/assets/experiments-getting-started/edge-impulse-create-impulse-spectral-classification.jpg "Edge Impulse Project Create Spectral Analysis Classification Impulse")

For the Learning block, we will use `Classification` to classify between `Normal` and `Vibrations`. Click `Add` to add the Classification block to your Impulse.

Next click `Save Impulse`.

### Feature Generation

![Edge Impulse Project Spectral Analysis Classification Features](.gitbook/assets/experiments-getting-started/edge-impulse-generate-features.jpg "Edge Impulse Project Spectral Analysis Classification Features")

Now we will generate the features that the AI model will use to learn. Head over to the `Spectral Features` tab and click on `Autotune parameters`. An autotune job will start and you will see the output on the right hand side of the UI.

![Edge Impulse Project Spectral Analysis Classification Features](.gitbook/assets/experiments-getting-started/edge-impulse-save-parameters.jpg "Edge Impulse Project Spectral Analysis Classification Features")

Once the job is complete click `Save parameters`. You will be redirected to the `Generate features` tab.

![Edge Impulse Project Spectral Analysis Classification Features](.gitbook/assets/experiments-getting-started/edge-impulse-generated-features.jpg "Edge Impulse Project Spectral Analysis Classification Features")

A feature generation job will start, and once finished you will see the features on the right hand side. The features should be nicely clustered, if you notice features that are not clustered correctly you can click on them, review the samples and update your dataset or settings to fix.

### Training

![Edge Impulse Project Spectral Analysis Classification Training](.gitbook/assets/experiments-getting-started/edge-impulse-train-spectral-classifier.jpg "Edge Impulse Project Spectral Analysis Classification Training")

Now it is time to train our model. Head over to the `Classifier` tab, leave the default settings intact, and click on `Save and train`.

A training job will start, and once completed you will see the results on the right hand side of the UI.

### Testing

![Edge Impulse Project Spectral Analysis Classification Testing](.gitbook/assets/experiments-getting-started/edge-impulse-train-spectral-classifier-testing.jpg "Edge Impulse Project Spectral Analysis Classification Testing")

If you now head over to the `Model testing` tab, you will be able to use your newly trained model on the Test data that was set aside. The Test data was not shown to the model during training, so this will help to evaluate how well the model performs on unseen data.

The testing process will start and you will see the results once complete.

![Edge Impulse Project First Experiment](.gitbook/assets/experiments-getting-started/edge-impulse-first-experiment.jpg "Edge Impulse Project First Experiment")

If you head to the `Experiments` tab, you will see that you now have your first Experiment listed.

### Deployment

![Edge Impulse Project Deployment](.gitbook/assets/experiments-getting-started/edge-impulse-deployment.jpg "Edge Impulse Project Deployment")

You are now able to deploy your model to your Arduino. Head over to the `Deployment` tab and search for Arduino, then follow the steps provided to you to deploy the model to your device.

As this tutorial is specifically related to Experiments, we will continue straight to EON Tuner and creating our next Experiment.

### EON Tuner

![Edge Impulse Project EON Tuner](.gitbook/assets/experiments-getting-started/edge-impulse-eon-tuner.jpg "Edge Impulse Project EON Tuner")

The EON™ Tuner simultaneously tests multiple model architectures, chosen based on your device and latency needs, to identify the best one for your application. The tuning process can take a while, but you can monitor its progress at any point during the search.

![Edge Impulse Project EON Tuner](.gitbook/assets/experiments-getting-started/edge-impulse-eon-tuner-run.jpg "Edge Impulse Project EON Tuner")

On the `Experiments` tab, select `EON Tuner`. For the `Search space configuration` select `Classification` in the `Usecase templates` drop down, then click `Start tuning` to run.

At this point, it is time to grab a coffee and put your feet up, as this will take some time to complete.

## Experiment 2

![Edge Impulse Project EON Tuner](.gitbook/assets/experiments-getting-started/edge-impulse-eon-tuner-add.jpg "Edge Impulse Project EON Tuner")

If at any time during the EON tuning process, you see a configuration you would like to try, you can simply click the `Add` button for that configuration.

![Edge Impulse Project EON Tuner](.gitbook/assets/experiments-getting-started/edge-impulse-eon-tuner-choose.jpg "Edge Impulse Project EON Tuner")

Here we see a configuration that has a considerable reduction for latency, RAM, and ROM, so we will use this configuration for our next Experiment.

![Edge Impulse Project Experiment 2](.gitbook/assets/experiments-getting-started/edge-impulse-experiment-2.jpg "Edge Impulse Project Experiment 2")

The platform will create the blocks for your new Impulse and add the features automatically for you. If you head back to the `Experiments` tab you will now see your new model waiting for you to test or deploy.

## Experiment 3

While the EON Tuner will help identify the best architectures and configuration automatically, you can also manually add a new Experiment in order to go through the blocks and neural network setup process again, by simply clicking on the "**Create new impulse**" button on the Experiments page.

At this point, once you have trained yet a third model and tested it's results, you now have 3 different models to choose from, and can select the best one to deploy to your device. In the Professional and Enterprise tiers, you can continue to evaluate and iterate with even more Experiments.

## Conclusion

In this tutorial, we demonstrated how to build a defect detection system with Edge Impulse and the Arduino Nano RP2040, and how to leverage the EON Tuner to optimize your model. From there, we built a second and third model with the new Experiments feature in Edge Impulse to allow us to evaluate different options and results. With this, you can easily refine and enhance your models, showcasing the power and simplicity of Edge Impulse's new Experiments feature for continuous improvement in machine learning projects.

