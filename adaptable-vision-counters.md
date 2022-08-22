---
description: Automatic FOMO-based objects counting using computer vision and a web app.
---

# Adaptable Vision Counters for Smart Industries 

Created By:
Nekhil R. 

Public Project Link:
[https://studio.edgeimpulse.com/public/126292/latest](https://studio.edgeimpulse.com/public/126292/latest)

## Project Demo

{% embed url="https://vimeo.com/737906235" %}

![](.gitbook/assets/adaptable-vision-counters/IMG_1520.JPG)

Automatic counting machines are very essential for correct packing in manufacturing industries. Currently, industries count either mechanically or through weight. Mechanical counting is restricted by size and shape of the product and it is often time-consuming.

Weight based counting assumes that each part has the exact same weight and uses a weight average to count. Even the most sophisticated manufacturing systems produce parts with slight variations in size and shape. These are even more pronounced for materials like wood and rubber where density changes by up to 50%. In addition to correct packing, these vision-based counters will be used to estimate the defective parts in a certain batch of production.

Consider if there are a higher number of defective parts, we can assume that something might be wrong with the production units.  This data can also be used to improve the quality of production and thus industry can make more products in less time.  So our adaptable counters are evolving as a solution to the world's accurate and flexible counting needs.

The Adaptable Counter is a device consisting of a Rapsberry Pi 4 and camera module, and the counting process is fully powered by FOMO. So it can count faster and more accurately than any other method. Adaptable counters are integrated with a cool looking website.

## Use-Cases    

These sample use-cases can be applied to any industry.

### 1. Counting from the Top     

In this case, we are counting defective and non-defective washers.

![](.gitbook/assets/adaptable-vision-counters/IMG_1664.jpg)

### 2. Counting in Motion    

In this case, we are counting bolts and washers and faulty washers passing through the conveyer belt.

![](.gitbook/assets/adaptable-vision-counters/IMG_1678.jpg)

### 3. Counting in a Bunch     

In this case, we are counting the bunch of lollipops.

![](.gitbook/assets/adaptable-vision-counters/IMG_1674.jpg)

### 4. Multiple Parts Counting

In this case, we are counting multiple parts such as Washers and Bolts.

![](.gitbook/assets/adaptable-vision-counters/IMG_1676.jpg)

## Software  

### Object Detection Model Training

![](.gitbook/assets/adaptable-vision-counters/EI_Logo.png)

Edge Impulse is one of the leading development platforms for machine learning on edge devices, free for developers and trusted by enterprises. Here we are using [FOMO](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices) to build a machine learning model that can recognize the products. Then we deploy the system on the Raspberry Pi 4B.

### Data Acquisition

Every machine learining project starts with data collection. A goood collection of data is one of the major factors that influences the performance of the model. Make sure you have a wide range of perspectives and zoom levels of the items that are being collected. You may take data from any device or development board, or upload your own datasets, for data acquisition. As we have our own dataset, we are uploading them using the Data Acquisition tab.

![](.gitbook/assets/adaptable-vision-counters/Data_Acquisition.png)

Simply navigate to the Data acquisition tab and select a file to upload. After that, give it a label and upload it to the training area. Edge Impulse will only accept JPG or PNG image files. Convert it to JPG or PNG format using a converter if you have any other formats.

In our case we have four labels - *Washer, Faulty Washer, Lollipop, Bolt*. We have uploaded all the collected data for these four different classes. Therefore, the computer will only recognize these items while counting. You must upload the dataset of other objects if you wish to recognize any other objects. The more data that neural networks have access to, the better their ability to recognize the object.

This is our counting setup (Just attached the Adaptable counter on the top of a small wooden plank):

![](.gitbook/assets/adaptable-vision-counters/IMG_1526.jpg)

### Labeling Data

You may view all of your dataset's unlabeled data in the labeling queue. Adding a label to an object is as simple as dragging a box around it. Edge Impulse attempts to automate this procedure by running an object tracking algorithm in the background in order to make life a little easier. If you have the same object in multiple photos the box moves for you and you just need to confirm the new box. Drag the boxes, then click Save labels. Continue doing this until your entire dataset has been labeled.

![](.gitbook/assets/adaptable-vision-counters/Label.png)

![](.gitbook/assets/adaptable-vision-counters/Labels.png)

### Designing an Impulse

![](.gitbook/assets/adaptable-vision-counters/Impulse_design.png)

With the training set in place, it is time to design the "impulse". An impulse is actually a machine learning pipeline for generating features from the input data. If you want to learn more about impulses, you can read more [here](https://docs.edgeimpulse.com/docs/edge-impulse-studio/impulse-design).

In the studio go to Create impulse, set the image width and image height to **96px**, the **resize mode** to **Fit the shortest axis**, and add the **Images** and **Object Detection (Images)** blocks. Then click Save impulse.

Then in the image tab, you can see the raw and processed features of every image. You can use the options to switch between 'RGB' and 'Grayscale' mode. As we are using **FOMO**, change the color depth to **Grayscale** and click Save parameters.

This will send you to the Feature generation screen. Here you'll:
* Resize all the data
* Apply the processing block on all this data.
* Create a visualization of your complete dataset.
* Click Generate features to start the process.

After generating the features for our data, we can see the individual measurable properties of the data represented in a 3-dimensional space. The below figure shows the features generated from our dataset. The generated features are well distinguishable.

![](.gitbook/assets/adaptable-vision-counters/Feature_Generation.png)

Now it's time to start training the machine learning model. Generating a machine learning model from scratch requires great time and effort.  Instead, we will use a technique called "transfer learning" which uses a pre-trained model on our data. That way we can create an accurate machine learning model, with fewer data inputs. Head over to the Object detection tab for the model generation.

In this case we are using the FOMO algorithm to train the model. So change the object detection model to **FOMO (Faster Objects, More Objects) MobileNetV2 0.35** and change the neural network settings as shown in the image. FOMO is a novel machine learning algorithm created by Edge Impulse, specifically designed for highly constrained devices. It works very well with the Raspberry Pi 4.

Now start training. After the model is done you'll see accuracy numbers below the training output. We have now trained our model with a training accuracy of 96.7%, pretty good.

![](.gitbook/assets/adaptable-vision-counters/Training_Accuracy.png)

To validate your model, go to **Model testing** and select **Classify all**. Here we hit 87.5% accuracy, which is great for a model with so little data.

![](.gitbook/assets/adaptable-vision-counters/Testing_Accuracy.png)

### Firebase (set-up)       

In our project, we use Firebase, a real-time database to instantly post and retrieve data, so that there is no time delay. Here we used the **Pyrebase** library which is a Python wrapper for Firebase.

To install Pyrebase, run the following command:
`pip install pyrebase`
    
Pyrebase is written for Python 3 and may not work correctly with Python 2.

First we created a project in the database:

![](.gitbook/assets/adaptable-vision-counters/firebasee_projectcreation.jpg)

Then head over to the Build section and create a realtime database:

![](.gitbook/assets/adaptable-vision-counters/db_creation.jpg)

Then select test mode, so we can update the data without any authentication:

![](.gitbook/assets/adaptable-vision-counters/security_roles.jpg)

This is our realtime database:

![](.gitbook/assets/adaptable-vision-counters/rtdb.jpg)

For use with only user-based authentication we can create the following configuration, that should be added in our Python code:

```json
import pyrebase
config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
  }
firebase = pyrebase.initialize_app(config)
```

Then add the apikey, authDomain and databaseURL (You can find all these in the project settings). Then we can store the values in the realtime database.

### Website

A webpage is created using HTML, CSS and JS to display the count in realtime. The data updated in Firebase is reflected in the webpage in realtime. The webpage displays **Recent Count** when the counting process is halted, and displays **Current Count** whenever the counting process is going on.

![](.gitbook/assets/adaptable-vision-counters/recent.png)

![](.gitbook/assets/adaptable-vision-counters/current_count.png)

## Code  

The entire code and assets are provided in the [GitHub repository](https://github.com/CodersCafeTech/Adaptable-Industrial-Counter.git).

## Hardware   

### Raspberry Pi 4B

![](.gitbook/assets/adaptable-vision-counters/IMG_1508_1.jpg)

The Raspberry Pi 4B is the brain of the system. The Raspberry Pi 4 has a 64 bit quad-core Cortex-A72 ARMv8 processor (the Broadcom BCM2711) and runs at a speed of 1.5GHz. So the counting can be done in an efficient way.

This tiny computer is fully supported by Edge Impulse. For setting up the Raspberry Pi with Edge Impulse please have a look [here](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-cpu-gpu-targets/raspberry-pi-4).

### Camera Module

![](.gitbook/assets/adaptable-vision-counters/IMG_1510_1.jpg)

This Raspberry Pi Camera Module is a custom-designed add-on for Raspberry Pi. It can be easily attached to the Raspberry Pi 4 with flex cables. It has a resolution of 5 megapixels and has a fixed focus lens onboard. In terms of still images, the camera is capable of 2592 x 1944 pixel static images, and also supports 1080p30, 720p60 and 640x480p60/90 video. This is well enough for our application.

### Power adapter 

![](.gitbook/assets/adaptable-vision-counters/IMG_1524.JPG)

For powering up the system we used a 5V 2A adapter. In this case we don't have any power hungry peripherals, so 2A current is enough. If you have 3A supply, please go for that.

For the sake of convienence we also used a acrylic case for setting up all the hardware.
