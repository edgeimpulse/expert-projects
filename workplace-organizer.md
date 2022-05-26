---
description: An autonomous security robot that listens for suspicious sounds, then goes on patrol to look for intruders.
---

# Workplace Organizer with NVIDIA Jetson Nano 2GB

Created By:
-- 

Public Project Link:
[]()

## Intro

Having an organized workplace allows the workers to have greater efficiency in their activities, directly impacting their productivity. 

When you are in an environment where people work multiple shifts and must share the same set of tools, there are a number of challenges that arise. By interviewing a few facility managers, we have found out that the most prominent problem is that employees do not return the tools in their designated space at the end of a shift, causing increased anxiety and delays in the activity of the following shift, since they must find the missing tools or replacements for them.

![]()

## Our Solution

We believe the computer vision approach is the best in overcoming this obstacle and Edge Impulse offers the right tools for it.
 
There are a few possible routes in creating an algorithm for detecting missing tools in their placeholder:

1. Train a model to recognize the different tools, define the number of each tool it must recognize at all times, and run an alert if any is missing;
1. Run an anomaly detection algorithm to detect if something is “missing” from the photo. - Non-specific (the algorithm won’t be able to exactly tell how many tools are missing);
1. Place stickers/tokens of a strident color under tools and run an object classification/detection algorithm to detect the number of tokens present in the image -  Resource effective, Increased Specificity, Repeatable, Implies 3D printing (but small stickers can be used as well if you do not have access to a 3D printer).

The winner in our opinion is number 3 so let’s get on with it and show you how it works.

### Hardware requirements

 - Jetson Nano 2GB Developer Kit
 - microSD card (64GB UHS-1 recommended)
 - Display
 - USB keyboard and mouse
 - USB camera (or a CSI camera like the Raspberry Pi Camera V2)
 - USB cable or CSI for rPi camera
 - Skadis pegboard or a toolbox
 - Stickers or 3D printed marker

### Software requirements
 - Edge Impulse account

## Hardware Setup

NVIDIA Jetson Nano 2GB DevKit has a quick get-started guide [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit) that, based on your operating system, will help you write the OS on an SD card and start the system. We also recommend having an enclosure for the Jetson to protect it from all sorts of nefarious events. In this tutorial, we have found the [reComputer](https://www.seeedstudio.com/re-computer-case-p-4465.html) case to be a good fit.

![]()

![]()

Usually, tools in the industrial environment are stored either horizontally, in drawers, or vertical, on panels, in designated spots. We will use the vertical panel setup from our workshop to develop the solution (IKEA Skadis pegboard and custom-made 3D printed supports - you can find the link [here](https://www.thingiverse.com/thing:2853261) if you like them), the difference, if you have a horizontal setup, would be the camera placement position.

![]()

We initially designed and 3D printed some tokens that perfectly fit in the pegboard slots. They print very quickly and are reusable. We did quite a bit of experimentation to find out what shape and color yield the best results. Firstly, we have tried using red and blue oval pegs. Unsurprisingly, this yielded poor results because they blended too well with the patterned background. Next up, we have decided to use colored geometric shapes. The best results, by far, were obtained with blue triangles, and to top it all off, a great jump in the model’s accuracy was gained by slightly scaling and rotating the triangles (without modifying their aspect ratio). You can find the 3D files that were most successful [here](https://www.myminifactory.com/object/3d-print-edge-impulse-ikea-skadis-markers-216427). 

![]()

![]()

![]()

## Software Setup

Register for a free account on the Edge Impulse platform [here](https://studio.edgeimpulse.com/login), then power up the Jetson and either run a display with a keyboard setup or login via ssh to run the following commands to install the Linux runner. Start a terminal and run the setup script:

`wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/jetson.sh | bash`

For more in-depth details about the Jetson setup, you can check [this](https://docs.edgeimpulse.com/docs/nvidia-jetson-nano) link, although the above command is enough for going to the next step.

### Creating an Edge Impulse Project

The first step towards building your TinyML Model is creating a new Edge Impulse Project.

Once logged in to your Edge Impulse account, you will be greeted by the Project Creation screen.

![]()

Click on **Create new project**, give it a meaningful name, select **Developer** as your desired project type and press **Create new project**.

![]()

Afterward, select **Images** as the type of data you wish to use.

![]()

Due to the possibility of having to detect more than 1 marker in the image, we will pick **Classify multiple objects** when asked what you want to detect.

![]()

### Connecting the device

To connect the Jetson Nano to the Edge Impulse project, run the following command in the terminal:

`edge-impulse-linux -disable-microphone`

If you have previously used your device in the past for other edge impulse projects, run the following command to reassign the device to a new project:

`edge-impulse-linux -disable-microphone -clean`

If you have only one active project, the device will be automatically assigned to it. If you have multiple Edge Impulse projects, select in the terminal the one you wish to attach your device to.

Give a recognizable name to your board and press enter.

Your board is now connected to the Edge Impulse project and you can see it in the connected devices panel.

### Collecting and preparing the dataset

There are multiple ways to go about gathering your dataset:

1. Manually taking a bunch of photos, aka data points, using an application like “Cheese!” or “guvcview”.
1. Recording a Video and extracting the frames every 1 second, using a Python script.
1. Take photos using the Data Acquisition panel in Edge Impulse Studio.

For this tutorial, we will be using the first option. A thing to keep in mind when gathering photos is that they will be resized to fit in a 320x320px box, required by the MobileNetV2 SSD FPN-Lite 320x320 architecture so try your best to keep the subject in the middle of the frame. Moreover, to avoid overfitting your network, move the camera a little when gathering your dataset, change the light a bit, change the angles etc.

To install [guvcview](https://www.google.com/search?sxsrf=APq-WBuDl6H6DCIFBzm2mZVV2SmDD_Z8TA:1648217840969&q=guvcview&spell=1&sa=X&ved=2ahUKEwi4m7H3ueH2AhUhSfEDHYpUCHwQkeECKAB6BAgBEDI), run the following command in the terminal:

`sudo apt install guvcview`

And afterward run guvcview to launch the application and start gathering photos.

Once we have plenty of photos (we have collected around 115 pictures for our use case), it’s time to upload them to Edge Impulse and label them. Click on the **upload** button, select **choose files**, select all your photos and then begin uploading. 

After that, you will see them in the **Data acquisition** panel.

![]()
