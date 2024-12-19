---
description: >-
  A TinyML model using Edge Impulse and the Wio Terminal with a thermal camera to predict faulty
  lithium ion cells in a BMS pack.
---

# Faulty Lithium-Ion Cell Identification in Battery Packs

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/102553/latest](https://studio.edgeimpulse.com/public/102553/latest)

![](../.gitbook/assets/lithium-ion/intro.jpg)

## Faulty Lithium ion Cell BMS Pack

This prototype uses a Wio Terminal and Edge Impulse to predict overheated faulty cells in a BMS pack. For this project, I used an MLX 90640 Thermal Camera with the Wio Terminal to collect thermal data from a BMS pack.

A working demo of my prototype is available on YouTube here:

{% embed url="https://www.youtube.com/watch?v=0fzT5PdRwiQ" %}

## Problem Statement

In an existing BMS pack, a temperature sensor is integrated with each cell pack, consisting of 14 cells, for identifying an overheated cell pack. But there is no system to identify an individual faulty cell that is overheating in a BMS pack.

![Existing BMS pack architecture](../.gitbook/assets/lithium-ion/diagram-1.jpg)

![](../.gitbook/assets/lithium-ion/diagram-2.jpg)

* Only one temperature sensor is deployed to detect the overall temperature of battery packs (14 \* Li-ion Cells).
* Identifying the individual cell temperature is challenging due to infrastructure cost for a BMS pack.

Cost for deploying Temperature sensor for each cell:

* Number of cells in BMS pack: 112
* Cost of Temperature sensor: 500 INR ($0.75 USD)
* Total cost: 112 \* 500 INR = 56,000 INR ($760 USD) \*approx

Additionally, there is no interface support in a microcontroller to support 112 individual temperature sensor readings.

## Solution using TinyML model

![](../.gitbook/assets/lithium-ion/architecture-1.jpg)

I have developed a prototype by using the MLX90640 thermal camera and Wio Terminal to collect the thermal data of the BMS pack and uploaded the data sets (Label: Faulty Battery 1.....6 and "Normal" to Edge Impulse).

## Hardware Setup

In this prototype, 6 lithium-ion cells are connected to the load (Rheostat) and the MLX90640 and Wio Terminal are attached to the stand where the MLX90640 thermal camera is facing downwards over the lithium-ion cells.

![](../.gitbook/assets/lithium-ion/prototype.jpg)

## Algorithm

The MLX90640 sends 32x24 thermal data to the Wio Terminal through I2C. Since this project focuses on identifying an overheated cell in the pack, I have used simple filtering logic to filter out the normal cell temperature by setting it to zero.

![](../.gitbook/assets/lithium-ion/algorithm.jpg)

Upload the datasets created for this project from the below link.

Go to Edge Impulse -> Data acquisition and then the Uploader option to upload the datasets.

![](../.gitbook/assets/lithium-ion/acquisition.jpg)

If you want to develop new datasets from scratch, flash the below code to the Wio Terminal using the Arduino IDE. For that, you need to configure Wio Terminal setup in the Arduino IDE. Please follow this link to get setup: [https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)

This code will print the thermal data in array format, later it can be converted to .csv format as mentioned in the above datasets. Ideally the .csv data looks like this:

![](../.gitbook/assets/lithium-ion/csv.jpg)

Once the datasets are uploaded, then in the "Create impulse" section change the Window size to 768 ( 24\*32 = 768 ).

![](../.gitbook/assets/lithium-ion/impulse.jpg)

Next, in Feature Explorer, we can see the generated raw features of thermal data.

![](../.gitbook/assets/lithium-ion/features.jpg)

## Neural Network Configuration

![](../.gitbook/assets/lithium-ion/neural-network.jpg)

I have used reshape to change the 1D data to 2D data with 24 columns (due to placement of the thermal camera) , in some cases it might be 32 to get the best accuracy.

Then I have included couple of 2D conversion layers with pool layers, followed by a Flatten layer. Then 2 DNN (30 neurons , 10 neurons) in sequential is used.

![](../.gitbook/assets/lithium-ion/layers.jpg)

## Deployment

In the Deployment section , select Arduino code and download the firmware package.

![](../.gitbook/assets/lithium-ion/deployment-1.jpg)

Then add the Zip file as a Library in Arduino IDE.

![](../.gitbook/assets/lithium-ion/deployment-2.jpg)

Once it is added, download the final application code from [this GitHub link](https://github.com/Manivannan-maker/FaultyCellIdentification), and flash it to the Wio Terminal.

## Output

In a model training, 100% accuracy is achieved, and in model testing 87.5% accuracy is achieved.

![](../.gitbook/assets/lithium-ion/accuracy.jpg)

In normal case, when all the battery in the pack is operating in normal temperature.

![](../.gitbook/assets/lithium-ion/normal.jpg)

In a faulty battery condition, the model will predict the cell location index and display it with a predicted value. In this particular setup, a faulty cell is placed in location 5 and discharged for 1 hour. The cell gets overheated, and the model predicts the overheated cell location, number 5 in this battery pack.

![](../.gitbook/assets/lithium-ion/faulty-1.jpg)

If you cannot create a faulty cell for testing, you can simulate it using this method. Place a heated soldering iron on top of (near, but do not touch!) a battery cell, or move the soldering iron from across the battery pack from cell 1 to cell 6 in the pack. The model will predict the overheated cell locations as 1 to 6, as the soldering iron moves from 1 to 6. By adding the heat from the soldering iron, you can simulate the faulty battery condition and test it.

![](../.gitbook/assets/lithium-ion/faulty-2.jpg)

## Schematics

![](../.gitbook/assets/lithium-ion/schematics.jpg)

## Summary

This project demonstrated a cheap and effective way to use computer vision and thermal imaging using the Wio Terminal, to identify lithium ion battery cells that are overheating, in more granular fashion than would be normally possible. This is a prototype of course, but could be used in robotics, automated warehouse and forklift devices, electric vehicles, or other places where batteries are arranged into packs.
