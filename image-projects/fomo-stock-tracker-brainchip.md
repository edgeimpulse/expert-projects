---
description: Manage the availability and location of your products in the warehouse using the Brainchip AKD1000 for fast and seamless detection using Machine Vision.
---

# Gesture Appliances Control with Pose Detection - BrainChip AKD1000 

Created By:
Christopher Mendez

[Edge Impulse Studio Public Project](https://studio.edgeimpulse.com/public/425288/live)

## Introduction

Industries, stores, workshops and many other professional environments have to manage an inventory, whether of products or tools, this need is normally addressed with a limited digital or manual solution. This project aims to contribute to the cited need with a smart approach that will let you know the products/tools quantity and their exact location in the rack, box or drawer.

[Project Thumbnail]()

The system will be constantly tracking the terminal blocks on a tray, counting them and streaming a live view in a web server, in addition, you will have real-time location feedback on an LED matrix.

## Hardware and Software Requirements

To develop this project we will use the following hardware:

- [Akida™ PCIe Board](https://shop.brainchipinc.com/products/akida%E2%84%A2-development-kit-pcie-board)
- [PCIe Slot For Raspberry Pi 5 Extension Adapter Board](https://52pi.com/products/p02-pcie-slot-for-rpi5)
- [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Camera Module 3 - IMX708](https://www.raspberrypi.com/products/camera-module-3/)
- [RGB LED Matrix](https://wiki.seeedstudio.com/Grove-RGB_LED_Matrix_w-Driver/)
- [Grove Base Hat for Raspberry Pi (Optional)](https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi.html)
- [Custom 3D parts]()

![Hardware required for the project](../.gitbook/assets/fomo-stock-tracker-brainchip/materials.png)

### Akida™ PCIe Board

It should be noted that the **AKD1000 Neuromorphic Hardware Accelerator** is the main component of this project thanks to some interesting characteristics that make it ideal for this use case. 

Considering that our project will end up being deployed in industrial and commercial environments, it's crucial that it can do its job efficiently and with very low energy consumption. This is where BrainChip's technology makes sense. Akida™ neuromorphic processor mimics the human brain to analyze only essential sensor inputs at the point of acquisition—processing data with unparalleled performance, precision, and economy of energy.

### Software
To develop the project model we are going to use:

- [Edge Impulse Studio](https://studio.edgeimpulse.com/)

## Hardware Setup

To fully assemble the project:

- Stack the PCIe Slot Extension Adapter Board under the Raspberry Pi and connect the flat cable accordingly ([dedicated instructions](https://wiki.52pi.com/index.php?title=EP-0219)).
- Screw the 3D-printed arm to the Raspberry Pi using the available spacers thread.
- Screw the MIPI camera to the 3D-printed arm and connect the flat cable from the camera to the CAM0 slot on the Raspberry Pi.
- Stack the Grove Base Hat on the Raspberry Pi 40 pins header.
- Connect the Grove cable from the LED Matrix to an I2C connector on the Grove Base Hat.
- Screw the cooling fan holder in the PCIe Slot Extension Adapter Board and connect it to +5V and GND on the 40 pins header (Optional).

![Hardware Setup Final Result]()

## Raspberry Pi 5 Setup

With the Raspberry Pi Imager, flash a micro-SD card with the Raspberry Pi OS Lite (64-bit), enter the OS Customisation menu by typing `Ctrl + Shift + X` and add your login credentials, enable the wireless LAN by adding your WiFi credentials and verify that the __SSH__ connection is enabled in the __Services__ settings.

![Raspberry Pi image settings](../.gitbook/assets/fomo-stock-tracker-brainchip/pi5-image.png)

Once the micro-SD card is flashed and verified, eject it and install it on your Raspberry Pi 5 slot.

## Setting up the Development Environment

Once the system is powered up and connected to the internet (I used WiFi), you can access it by an SSH connection: you will need to know the device's local IP address, in my case, I got it from the list of connected devices of my router. 

![Device IP Address](../.gitbook/assets/fomo-stock-tracker-brainchip/raspberry-ip.png)

To start setting up the device for a custom model deployment, let's verify we have installed all the packages we need.

I am using Putty for the SSH connection. Log in using the set credentials, in this case, the username is **raspberrypi** and the password is **raspberrypi**.

![SSH Connection through Putty](../.gitbook/assets/fomo-stock-tracker-brainchip/putty.png)

Once in, verify that the Akida PCIe board is detected:

```bash
lspci | grep Co-processor # will check if the PCIe card is plugged in correctly.
```

Create a __virtual environment__:

```bash
python3 -m venv .venv --system-site-packages #create virtual env
source .venv/bin/activate  #enter virtual env
```

Install the Akida driver:

![Verifying packages](../.gitbook/assets/gesture-appliances-control-brainchip/verifications.png)

You will also need Node Js v14.x to be able to use the [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation). Install it by running these commands:

```
bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
```
The last command should return the node version, v14 or above.

Finally, let's install the [Linux Python SDK](https://docs.edgeimpulse.com/docs/edge-impulse-for-linux/linux-python-sdk), you just need to run these commands:

```
bash
sudo apt-get install libatlas-base-dev libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev 
pip3 install edge_impulse_linux -i https://pypi.python.org/simple
```

> **As we are working with computer vision, we will need "opencv-python>=4.5.1.48, "PyAudio", "Psutil", and "Flask"**

## Data Collection

First, we need to create an [Edge Impulse Studio](https://studio.edgeimpulse.com) account if we haven't yet, and create a new project:

![New project creation](../.gitbook/assets/gesture-appliances-control-brainchip/new_project.png)

For the creation of the dataset of our model, we have two options, uploading the images from the BrainChip Development Kit or using our computer or phone. In this case, I chose to take them from the computer using the same webcam that we are finally going to use in the project.

![Dataset creating source](../.gitbook/assets/gesture-appliances-control-brainchip/pc_upload.png)

The dataset consists of 3 classes in which we finger point each appliance and a last one of unknown cases.

![Raw image & PoseNet output](../.gitbook/assets/gesture-appliances-control-brainchip/classes.png)

> **Taking at least +50 pictures of each class will let you create a robust enough model**

## Impulse Design

After having the dataset ready, it is time to define the structure of the model.

In the left side menu, we navigate to **Impulse design** > **Create impulse** and define the following settings for each block, respectively:

### Input block (Image data):

- Image width: 192
- Image height: 192
- Resize mode: Fit longest

### Processing block (PoseNet):

Use this block to turn raw images into pose vectors, then pair it with an ML block to detect what a person is doing.

PoseNet processing block is just enabled for Enterprise projects, if we want to use it on a Developer one, we need to locally run the block, for this, you must clone the [PoseNet block repository](https://github.com/edgeimpulse/pose-estimation-processing-block) and follow the __README__ steps.

You will end up with an URL similar to "https://abe7-2001-1308-a2ca-4f00-e65f-1ff-fe27-d3aa.ngrok-free.app" hosting the processing block, click on **Add a processing block** > **Add custom block**, then paste the [**ngrok**](https://ngrok.com/) generated URL, and click on **Add block**.

![Adding a Custom Block](../.gitbook/assets/gesture-appliances-control-brainchip/custom_block.png)

### Learning block (BrainChip Akida)

To classify the features extracted from the different poses, we'll use a classification learn block specifically designed for the hardware we're using.

![Adding a Custom Block](../.gitbook/assets/gesture-appliances-control-brainchip/learning.png)

Finally, we save the **Impulse design**, it should end up looking like this:

![Adding a Custom Block](../.gitbook/assets/gesture-appliances-control-brainchip/impulse_design_2.png)

## Model Training

After having designed the impulse, it's time to set the processing and learning blocks. The **Pose estimation** block doesn't have any configurable parameters, so we just need to click on **Save parameters** and then **Generate features**. 

In the _classifier block_ define the following settings:

- Number of training cycles: 100
- Learning rate: 0.001 

In the Neural network architecture, add 3 Dense layers with 35, 25 and 10 neurons respectively.

Here is the architecture **"Expert mode"** code (you can copy and paste it from here):

```
python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer, Dropout, Conv1D, Conv2D, Flatten, Reshape, MaxPooling1D, MaxPooling2D, AveragePooling2D, Rescaling, BatchNormalization, Permute, ReLU, Softmax
from tensorflow.keras.optimizers.legacy import Adam
EPOCHS = args.epochs or 100
LEARNING_RATE = args.learning_rate or 0.001
# this controls the batch size, or you can manipulate the tf.data.Dataset objects yourself
BATCH_SIZE = 32
train_dataset = train_dataset.batch(BATCH_SIZE, drop_remainder=False)
validation_dataset = validation_dataset.batch(BATCH_SIZE, drop_remainder=False)

# model architecture
model = Sequential()
#model.add(Rescaling(7.5, 0))
model.add(Dense(35,
    activity_regularizer=tf.keras.regularizers.l1(0.00001)))
model.add(ReLU())
model.add(Dense(25,
    activity_regularizer=tf.keras.regularizers.l1(0.00001)))
model.add(ReLU())
model.add(Dense(10,
    activity_regularizer=tf.keras.regularizers.l1(0.00001)))
model.add(ReLU())
model.add(Dense(classes, name='y_pred'))
model.add(Softmax())

# this controls the learning rate
opt = Adam(learning_rate=LEARNING_RATE, beta_1=0.9, beta_2=0.999)
callbacks.append(BatchLoggerCallback(BATCH_SIZE, train_sample_count, epochs=EPOCHS))

# train the neural network
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(train_dataset, epochs=EPOCHS, validation_data=validation_dataset, verbose=2, callbacks=callbacks)

import tensorflow as tf


def akida_quantize_model(
    keras_model,
    weight_quantization: int = 4,
    activ_quantization: int = 4,
    input_weight_quantization: int = 4,
):
    import cnn2snn

    print("Performing post-training quantization...")
    akida_model = cnn2snn.quantize(
        keras_model,
        weight_quantization=weight_quantization,
        activ_quantization=activ_quantization,
        input_weight_quantization=input_weight_quantization,
    )
    print("Performing post-training quantization OK")
    print("")

    return akida_model


def akida_perform_qat(
    akida_model,
    train_dataset: tf.data.Dataset,
    validation_dataset: tf.data.Dataset,
    optimizer: str,
    fine_tune_loss: str,
    fine_tune_metrics: "list[str]",
    callbacks,
    stopping_metric: str = "val_accuracy",
    fit_verbose: int = 2,
    qat_epochs: int = 200,
):
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor=stopping_metric,
        mode="max",
        verbose=1,
        min_delta=0,
        patience=10,
        restore_best_weights=True,
    )
    callbacks.append(early_stopping)

    print("Running quantization-aware training...")
    akida_model.compile(
        optimizer=optimizer, loss=fine_tune_loss, metrics=fine_tune_metrics
    )

    akida_model.fit(
        train_dataset,
        epochs=qat_epochs,
        verbose=fit_verbose,
        validation_data=validation_dataset,
        callbacks=callbacks,
    )

    print("Running quantization-aware training OK")
    print("")

    return akida_model


akida_model = akida_quantize_model(model)
akida_model = akida_perform_qat(
    akida_model,
    train_dataset=train_dataset,
    validation_dataset=validation_dataset,
    optimizer=opt,
    fine_tune_loss='categorical_crossentropy',
    fine_tune_metrics=['accuracy'],
    callbacks=callbacks)
```

Click on the __Start training__ button and wait for the model to be trained and the confusion matrix to show up.

### Confusion Matrix 

![Confusion matrix results](../.gitbook/assets/gesture-appliances-control-brainchip/confusion.png)

The results of the confusion matrix can be improved by adding more samples to the dataset.

## Project Setup

To be able to run the project, we need to go back to our SSH connection with the device and clone the project from the [Github repository](https://github.com/edgeimpulse/pose-akida-classification), for this, use the following command:

```
bash
git clone https://github.com/edgeimpulse/pose-akida-classification.git
```
Install all the project requirements with the following command, and wait for the process to be done.

```
bash
pip install -r requirements.txt
```

Install these other required packages with:

```
bash
apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
```

## Deployment

Once the project is cloned locally in the Akida Development Kit, you can download the project model from Edge Impulse Studio by navigating to the **Dashboard** section and downloading the **MetaTF** `.fbz` file.

![Downloading the project model](../.gitbook/assets/gesture-appliances-control-brainchip/model-down.png)

Once downloaded, from the model path, open a new terminal and copy the model to the Dev Kit using `scp` command as follows:

```
bash
scp <model file>.fbz ubuntu@<Device IP>:~ # command format
scp akida_model.fbz ubuntu@10.0.0.154:~ # actual command in my case
```
> _You will be asked for your Linux machine login password._

Now, the model is on the Akida Dev Kit local storage `(/home/ubuntu)` and you can verify it by listing the directory content using `ls`.

Move the model to the project directory with the following command:

```
bash
mv akida_model.fbz ./pose-akida-classification/
```

Here we have the model on the project directory, so now everything is ready to be run.

![Project directory](../.gitbook/assets/gesture-appliances-control-brainchip/model-copy.png)

## Run Inferencing

To run the project, type the following command:

```
bash
python3 class-pose.py akida_model.fbz 0
```

- The first parameter `class-pose.py` is the project's main script to be run.
- `akida_model.fbz` is the Meta TF model name we downloaded from our Edge Impulse project.
- `0` force the script to use the first camera available.

The project will start running and printing the inference results continuously in the terminal.

![Project running and printing the results](../.gitbook/assets/gesture-appliances-control-brainchip/running.png)

To watch a preview of the camera feed, you can do it by opening a new `ssh` session and running the `make-page.py` script from the project directory:

```
bash
python3 make-page.py
```

![Preview Web Page script command](../.gitbook/assets/gesture-appliances-control-brainchip/preview-web.png)

Finally, you will be able to see the camera preview alongside the inference results organized in the following order: `AC`, `Light`, `Other` and `TV`.

![Project running | Inference results](../.gitbook/assets/gesture-appliances-control-brainchip/results-preview.png)

## Google Assistant Setup

For the actual appliance control, I used the __Google Assistant SDK__ integration for __Home Assistant__. Follow the [documentation](https://www.home-assistant.io/integrations/google_assistant_sdk) to configure it for your setup.

> **The Home Assistant is running on a separate Raspberry PI.**

Once the integration is set, we can send `HTTP` requests to it with the following format:

- URL: `http://<Raspberry Pi IP>:8123/api/services/google_assistant_sdk/send_text_command`
- Headers:
    - Authorization: "Bearer <authentication key>"
    - Content-Type: "application/json"
- Body: {"command":"turn on the light"}

You must edit the `url` and `auth` variables in the code with the respective ones of your setup.

```
python
url = 'http://<Raspberry Pi IP>:8123/api/services/google_assistant_sdk/send_text_command'
auth = 'Bearer ******************************************************************************'
```

## Demo

![Final project deployment](../.gitbook/assets/gesture-appliances-control-brainchip/setup-on.png)

Here I show you the whole project working and controlling appliances when they are pointed.

{% embed url="https://youtu.be/xLTo_sYCn9Y" %}

## Conclusion

This project leverages the Brainchip Akida Neuromorphic Hardware Accelerator to propose an innovative solution to home automation. It can be optimized to work as a daily used gadget that may be at everyone's house in the near future.
