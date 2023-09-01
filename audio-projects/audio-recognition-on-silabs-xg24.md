---
description: >-
  Take an existing Edge Impulse model built for the Thunderboard Sense 2, and
  prepare it for use on the SiLabs xG24 board.
---

# Porting an Audio Project from the SiLabs Thunderboard Sense 2 to xG24

Created By: Pratyush Mallick

Public Project: [https://studio.edgeimpulse.com/public/66064/latest](https://studio.edgeimpulse.com/public/66064/latest)

## Intro

This project focuses on how to port an existing audio recognition project built with a SiLabs Thunderboard Sense 2, to the latest [EFR32MG24](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs) as used in the newer SiLabs xG24 Dev Kit. For demonstration purposes, we will be porting [Manivannan Sivan's](https://www.hackster.io/manivannan) ["Vehicle Predictive Maintenance"](https://www.hackster.io/manivannan/vehicle-predictive-maintenance-cf2ee3) project, which is an Edge Impulse based TinyML model to predict various vehicle failures like faulty drive shaft and brake-pad noises. Check out his work for more information.

The audio sensor on the Thunderboard Sense 2 and the xG24 Dev Kit are the same (TDK InvenSense ICS-43434), so ideally we're not required to collect any new data using the xG24 Dev Kit for the model to work properly. Had the audio sensor been a different model, it would most likely be necessary to capture a new dataset.

However, note has to be taken that the xG24 has two microphones, phones placed at the edges of the board.

In this project, I am going to walk you through how you can clone Mani's Public Edge Impulse project for the Thunderboard Sense 2 board, build it for the xG24, test it out, and then deploy to the newer SiLabs xG24 device instead.

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/silabs\_migrate.jpg)

## Installing Dependencies

Before you proceed further, there are few software packages you need to install.

* Edge Impulse CLI - Follow [this link](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation) to install the necessary tooling to interact with the Edge Impulse Studio and also run inference on the board.
* Simplicity Studio 5 - Follow [this link](https://www.silabs.com/developers/simplicity-studio) to install the IDE
* Simplicity Commander - Follow [this link](https://community.silabs.com/s/article/simplicity-commander?language=en\_US) to install the software. This will be required to flash firmware to the xG24 board.

## Clone And Build

If you don't have an Edge Impulse account, signup for free and log into [Edge Impulse](https://studio.edgeimpulse.com/). Then visit the below [Public Project](https://docs.edgeimpulse.com/docs/edge-impulse-studio/dashboard#1.-showcasing-your-public-projects-with-markdown-readmes) to get started.

> [https://studio.edgeimpulse.com/public/66064/latest](https://studio.edgeimpulse.com/public/66064/latest)

Click on the "Clone" button at top-right corner of the page.

That will bring you to the below popup tab. Enter a name for your clone project, and click on the "Clone project" button.

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/clonning\_project.jpg)

This action will copy all the collected data, generated features, and model parameters into your own Edge Impulse Studio. You can verify this by looking at the project name you entered earlier.

Now if you navigate to "Create impulse" from the left menu, you will see how the model was created originally.

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/edge\_impulse\_design.jpg)

As you can see, the model was created based on audio data sampled at 16KhZ. As mentioned, because the audio microphones used on the both board boards are the same, we're not required to collect any additional data from the new board.

However, if you do want to collect some data from the xG24, then you will need to flash the base firmware and then use the `edge-impulse-daemon` to connect the device to the Studio.

You can follow the guide below to go through the process, if you are interested in adding more data samples to your cloned project:

> ["Edge Impulse xG24 Dev Kit Guide"](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/silabs-xg24-devkit).

With default value of Window Size (10s) and Window Increase (500 ms), the processing block will throw an error, as represented below:

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/frame\_stride\_error.jpg)

This is because some of the features in Edge Impulse's processing block have been updated since this project was created, so you need to update some of the parameters in the Timer Series block such as Window Size and Window Increase, or increase the frame stride parameter in the MFE processing block. This is what my updated window parameters look like:

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/window\_increase\_updated.jpg)

If you added some new data and are not sure of the model design, then the [EON tuner](https://docs.edgeimpulse.com/docs/edge-impulse-studio/eon-tuner) can come to the rescue. You just have to select the target device as SiLabs EFR32MG24 (Cortex-M33 78MHz) and configure your desired parameters, then the Eon tuner will come up with suggested architectures which you can use.

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/EON\_tuner.jpg)

Next, navigate to the "Classification" tab from the left menu, and click on "Start training".

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/Training.jpg)

Alternatively, you can also collect more data as mentioned above, or add new recognized sounds with other audio classes, then begin your training.

## Test

When you are done training, navigate to the "Live Classification" page from the left menu. This feature of Edge Impulse comes in handy when migrating projects to different boards.

Rather than deploying the model and then testing it on the hardware, with this feature we can actually collect audio data from the hardware immediately, and run the model in the Studio on the collected data. This saves time and effort before hand.

For Edge Impulse supported boards we can directly download the base Edge Impulse firmware, and then directly record audio (or other) data from the target device.

You can refer to the previously mentioned official Docs link to get the latest firmware and connect the xG24 to the Edge Impulse Studio: ["Edge Impulse xG24 Dev Kit Guide"](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/silabs-xg24-devkit)

Once done, you can select the device name, select the sensor as "Microphone", sample length and the sampling frequency (ideally equally to collected samples).

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/Live\_Classification.jpg)

Alternatively, you can use ["Web Usb"](https://www.edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) to collect data, if you don't want to install any tools.

## Deploy

When you are done retraining, navigate to the "Deployment" tab from the left menu, select "SiLabs xG24 Dev Kit" under "Build firmware", then click on the "Build" button at the bottom of the page.

This will build your model and download a .zip file containing a `.hex` file and instructions.

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/deploy.jpg)

With the Thunderboard Sense 2 deploying firmware could be done by directly dragging and dropping files to the "USB Driver TB004" when the device was connected in flash mode to a host PC. However, for the xG24 we have to use Simplicity Commander to upload the firmware to the board. You need to first connect the xG24 board the PC, make note of the COM port for the board, and ideally it will be identified by the PC as a J-Link UART port.

Now open the Simplicity Commander tool and connect the board. Once connected, select the "Flash" option on the left and then select the downloaded `.hex` file and flash it to the board.

{% embed url="https://user-images.githubusercontent.com/45755431/223307262-30fa606c-8448-47f6-9889-bb488f6fb934.mp4" %}

To start the inferencing run the following command in your terminal:

```
edge-impulse-run-impulse
```

Note that this is a newer command supported by the Edge Impulse CLI, hence you may need to update your `edge-impulse-cli` version to get this running and avoid a package mismatch as shown below:

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/update\_npm\_to\_connect\_to\_edge\_impulse.jpg)

Now your model should be running, and recognize the same audio data and perform inferencing on the newer xG24 Dev Kit hardware, with little to no modifications to actual data or to the model architecture.

This highlights the platform agnostic nature of Edge Impulse, and was possible in this case because the audio sensor on both the Thunderboard and xG24 are the same. However, you would need do your own due diligence for migrating projects built with other sensor data such as humidity/temperature, or the light sensor, as those do vary between the boards.

One final note is that in this project, the xG24 is roughly 2x as fast as the Thunderboard Sense 2 in running the DSP, and 8x faster in running the inference:

![](../.gitbook/assets/audio-recognition-on-silabs-xg24/comparison.jpg)

Hopefully this makes upgrading your SiLabs projects easier!
