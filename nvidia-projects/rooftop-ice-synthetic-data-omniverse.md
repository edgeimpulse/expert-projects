---
description: >-
  Rooftop ice buildup detection using Edge Impulse, with synthetic data created with NVIDIA Omniverse Replicator and sun studies.
---

# Rooftop Ice Detection with Things Network Visualization - Nvidia Omniverse Replicator

Created By: Eivind Holt

Public Project Link: [https://studio.edgeimpulse.com/public/332581/live](https://studio.edgeimpulse.com/public/332581/live)

GitHub Repo: [https://github.com/eivholt/icicle-monitor](https://github.com/eivholt/icicle-monitor)

![](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/cover1.png)

## Introduction

This portable device monitors buildings and warns the responsible parties when potentially hazardous icicles are formed. In ideal conditions icicles can form at a rate of [more than 1 cm (0.39 in) per minute](https://en.wikipedia.org/wiki/Icicle). Each year, many people are injured and killed by these solid projectiles, leading responsible building owners to often close sidewalks in the spring to minimize risk. This project demonstrates how an extra set of digital eyes can notify property owners icicles are forming and need to be removed before they can cause harm.

![Downtown, photo: Avisa Nordland](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/IMG_8710.jpg)

## Hardware used

* [Arduino Portenta H7](https://docs.arduino.cc/hardware/portenta-h7/)
* [Arduino Portenta Vision Shield w/LoRa Connectivity](https://docs.arduino.cc/hardware/portenta-vision-shield/)
* NVIDIA GeForce RTX
* [Otii Arc from Qoitech](https://www.qoitech.com/otii-arc-pro/)

## Software used

* [Edge Impulse Studio](https://studio.edgeimpulse.com/studio)
* [NVIDIA Omniverse Code](https://www.nvidia.com/en-us/omniverse/) with [Replicator](https://developer.nvidia.com/omniverse/replicator)
* [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) with [Edge Impulse extension](https://github.com/edgeimpulse/edge-impulse-omniverse-ext)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Blender](https://www.blender.org/)

## Code and machine learning repository

Project [Impulse](https://studio.edgeimpulse.com/public/332581/live) and [Github code repository](https://github.com/eivholt/icicle-monitor).

## Working principle

Icicle formation is detected using a neural network (NN) designed to identify objects in images from the onboard camera. The NN is trained and tested exclusively on synthesized images. The images are generated with realistic simulated lighting conditions. A small amount of real images are used to verify the model.

{% embed url="https://youtube.com/shorts/aIkj3uZ_MSE" %}

## Challenges

The main challenge of detecting forming icicles is the translucent nature of ice and natural variation of sunlight. Because of this we need a great number of images to train a model that captures enough features of the ice with varying lighting conditions. Capturing and annotating such a large dataset is incredibly labor intensive. We can mitigate this problem by synthesizing images with varying lighting conditions in a realistic manner and have the objects of interest automatically labeled.

{% embed url="https://youtu.be/qvDXRqBxECo" %}

## Mobility

A powerful platform combined with a high resolution camera with fish-eye lens would increase the ability to detect icicles. However, by deploying the object detection model to a small, power-efficient, but highly constrained device, options for device installation increase. Properly protected against moisture this device can be mounted outdoors on walls or poles facing the roofs in question. LoRaWAN communication enables low battery consumption and long transmission range.

![Arduino Portenta H7](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/20240413_215105_.jpg)

## Object detection using neural network

[FOMO (Faster Objects, More Objects)](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices) is a novel machine learning algorithm that allows for visual object detection on highly constrained devices through training of a neural network with a number of convolutional layers.

![Edge Impulse](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/EILogo.svg)

### Capturing training data and labeling objects

One of the most labor intensive aspects of building any machine learning model is gathering the training data and to label it. For an object detection model this requires taking hundreds or thousands of images of the objects to detect, drawing rectangles around them and choosing the correct label for each class. Recently generating pre-labeled images has become feasible and has proven great results. This is referred to as synthetic data generation with domain randomization. In this project a model will be trained exclusively on synthetic data and we will see how it can detect the real life counterparts.

### Domain randomization using NVIDIA Omniverse Replicator

NVIDIA Omniverse Code is an IDE that allows us to compose 3D scenes and to write simple Python code to capture images. Further, the extension Replicator is a toolkit that allows us to label the objects in the images and to simplify common domain randomization tasks, such as scattering objects between images. For an in-depth walkthrough on getting started with Omniverse and Replicator [see this article](https://docs.edgeimpulse.com/experts/featured-machine-learning-projects/surgery-inventory-synthetic-data).

### Making a scene

It's possible to create an empty scene in Omniverse and add content programmatically. However, composing initial objects by hand serves as a practical starting point. In this project [a royalty free 3D model of a house](https://www.cgtrader.com/free-3d-models/exterior/house/house-model-3d-dom-2) was used as a basis.

![3D house model](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/house.png)

### Icicle models

To represent the icicle a high quality model pack was purchased at [Turbo Squid](https://www.turbosquid.com/3d-models/). 

![3D icicle models purchased at Turbo Squid](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/turbo-squid-icicle.png)

To be able to import the models into Omniverse and Isaac Sim all models have to be converted to [OpenUSD-format](https://developer.nvidia.com/usd). While USD is a great emerging standard for describing, composing, simulating and collaborting within 3D-worlds, it is not yet commonly supported in asset marketplaces. [This article](https://docs.edgeimpulse.com/experts/featured-machine-learning-projects/surgery-inventory-synthetic-data) outlines considerations when performing conversion using Blender to USD. Note that it is advisable to export each individual model and to choose a suitable origin/pivot point.

Blender change origin cheat sheet:
+ Select vertex on model (Edit Mode), Shift+S-> Cursor to selected
+ (Object Mode) Select Hierarchy, Object>Set Origin\Origin to 3D Cursor
+ (Object Mode) Shift+S\Cursor to World Origin

Tip for export:
+ Selection only
+ Convert Orientation:
    + Forward Axis: X
    + Up Axis: Y

![3D icicle models exported from Blender](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Blender_select_vertex.png)

### Setting semantic metadata on objects

To be able to produce images for training and include labels we can use a feature of Replicator toolbox found under menu Replicator> Semantics Schema Editor.

![Semantics Schema Editor](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/semantic-editor.png)

Here we can select each top node representing an item for object detection and adding a key-value pair. Choosing "class" as Semantic Type and "ice" as Semantic Data enables us to export this string as label later.

### Creating a program for domain randomization

With a basic 3D stage created and objects of interest labeled we can continue creating a program that will make sure we produce images with slight variations. Our program can be named anything, ending in .py and preferably placed close to the stage USD-file. The following is a description of such a program [replicator_init.py](https://github.com/eivholt/icicle-monitor/blob/main/omniverse-replicator/replicator_init.py):


To keep the items generated in our script separate from the manually created content we start by creating a new layer in the 3D stage:

```python
with rep.new_layer():
```

Next we specify that we want to use ray-tracing as our image output. We create a camera and hard code the position. We will point it to our icicles for each render later. Then we use our previously defined semantics data to get references to the icicles for easier manipulation. We also define references to a plane on which we want to scatter the icicles. Lastly we define our render output by selecting the camera and setting the desired resolution. Due to an issue in Omniverse where artifacts are produces at certain resolutions, e.g. 120x120 pixels, we set the output resolution at 128x128 pixels. Edge Impulse Studio will take care of scaling the images to the desired size should we use images of different size than the configured model size.

```python
rep.settings.set_render_pathtraced(samples_per_pixel=64)
cameraPlane = rep.get.prims(path_pattern='/World/CameraPlane')
icePlane = rep.get.prims(path_pattern='/World/IcePlane')
icicles = rep.get.prims(semantics=[("class", "ice")])

camera = rep.create.camera(position=(0, 0, 0))
render_product = rep.create.render_product(camera, (128, 128))
```

Due to the asynchronous nature of Replicator we need to define our randomization logic as call-back methods by first registering them in the following fashion:

```python
rep.randomizer.register(randomize_camera)
rep.randomizer.register(scatter_ice)
```

Before defining the logic of the randomization methods we define what will happen during each render:

```python
with rep.trigger.on_frame(num_frames=10000, rt_subframes=50):
    rep.randomizer.scatter_ice(icicles)
    rep.randomizer.randomize_camera(icicles)
```

The parameter *num_frames* specifies the desired number of renders. The *rt_subframes* parameter allows the rendering process to advance a set number of frames before the result is captured and saved to disk. A higher setting enhances complex ray tracing effects like reflections and translucency by giving them more time to interact across surfaces, though it increases rendering time. Each randomization routine is invoked with the option to include specific parameters.

To save each image and its corresponding semantic data, we utilize a designated API. While customizing the writer was considered, attempts to do so using Replicator version 1.9.8 on Windows led to errors. Therefore, we are employing the "BasicWriter" and will develop an independent script to generate a label format that is compatible with the Edge Impulse.

```python
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(
    output_dir="[set output]",
    rgb=True,
    bounding_box_2d_loose=True)

writer.attach([render_product])
asyncio.ensure_future(rep.orchestrator.step_async())
```

*rgb* indicates that we want to save images to disk as png-files. Note that labels are created setting *bounding_box_2d_loose*. This is used in this case instead of *bounding_box_2d_tight* as the latter in some cases would not include the tip of the icicles in the resulting bounding box. It also creates labels from previously defined semantics. The code ends with running a single iteration of the process in Omniverse Code, so we can preview the results.

The bounding boxes can be visualized by clicking the sensor widget, checking "BoundingBox2DLoose" and finally "Show Window".

![Omniverse bounding box](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/omniverse-bb.png)

Now we can implement the randomization logic. First a method that flips and scatters the icicles on a defined plane.

```python
def scatter_ice(icicles):
with icicles:
    carb.log_info(f'Scatter icicle {icicles}')
    ice_rotation = random.choice(
        [
            (-90, 90, 0),
            (-90, -90, 0),
        ]
    )
    rep.modify.pose(rotation=ice_rotation)
    rep.randomizer.scatter_2d(surface_prims=icePlane, check_for_collisions=True)
return icicles.node
```

Next a method that randomly places the camera on an other defined plane and makes sure the camera is pointing at the group of icicles and randomizes focus.

```python
def randomize_camera(targets):
with camera:
    rep.randomizer.scatter_2d(surface_prims=cameraPlane)
    rep.modify.pose(look_at=targets)
    rep.modify.attribute("focalLength", rep.distribution.uniform(10.0, 40.0))
return camera.node
```

We can define the methods in any order we like, but in *rep.trigger.on_frame* it is crucial that the icicles are placed before pointing the camera.

### Running domain randomization

With a basic randomization program in place, we could run it from the embedded script editor (Window> Script Editor), but more robust Python language support can be achieved by developing in Visual Studio Code instead. To connect VS Code with Omniverse we can use the Visual Studio Code extension [Embedded VS Code for NVIDIA Omniverse](https://marketplace.visualstudio.com/items?itemName=Toni-SM.embedded-vscode-for-nvidia-omniverse). See [extension repo](https://github.com/Toni-SM/semu.misc.vscode) for setup. When ready to run go to Replicator> Start and check progress in the defined output folder.

![Produced images](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/output1.png)

### Randomizing colors

The surface behind the icicles may vary greatly, both in color and texture. Using Replicator randomizing the color of an objects material is easy.

In the scene in Omniverse either manually create a plane behind the icicles, or create one programmatically.

In code, define a function that takes in a reference to the plane we want to randomize the color of and use one of the distribution functions with min and max value span:

```python
def randomize_screen(screen):
    with screen:
        # Randomize each RGB channel for the whole color spectrum.
        rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))
    return screen.node
```

Then get a reference to the plane:

```python
screen = rep.get.prims(path_pattern='/World/Screen')
```

Lastly register the function and trigger it on each new frame:

```python
rep.randomizer.register(randomize_screen)
with rep.trigger.on_frame(num_frames=2000, rt_subframes=50):  # rt_subframes=50
    # Other randomization functions...
    rep.randomizer.randomize_screen(screen)
```

![Random background color](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/random_color.png)

![Random background color](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/output2.png)

Now each image will have a background with random (deterministic, same starting seed) RGB color. Replicator takes care of creating a material with a shader for us. As you might remember, in an effort to reduce RAM usage our neural network reduces RGB color channels to grayscale. In this project we could simplify the color randomization to only pick grayscale colors. The example has been included as it would benefit in projects where color information is not reduced. To only randomize in grayscale, we could change the code in the randomization function to use the same value for R, G and B as follows:

```python
def randomize_screen(screen):
    with screen:
        # Generate a single random value for grayscale
        gray_value = rep.distribution.uniform(0, 1)
        # Apply this value across all RGB channels to ensure the color is grayscale
        rep.randomizer.color(colors=gray_value)
    return screen.node
```

![Random background grayscale](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/random_grayscale.png)

### Randomizing textures

To further steer training of the object detection model in capturing features of the desired class, the icicles, and not features that appear due to short commings in the domain randomization, we can create images with the icicles in front of a large variety of background images. A simple way of achieving this is to use a large dataset of random images and randomly assigning one of them to a background plane for each image generated.

```python
import os

def randomize_screen(screen, texture_files):
    with screen:
        # Let Replicator pick a random texture from list of .jpg-files
        rep.randomizer.texture(textures=texture_files)
    return screen.node

# Define what folder to look for .jpg files in
folder_path = 'C:/Users/eivho/source/repos/icicle-monitor/val2017/testing/'
# Create a list of strings with complete path and .jpg file names
texture_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Register randomizer
rep.randomizer.register(randomize_screen)

# For each frame, call randomization function
with rep.trigger.on_frame(num_frames=2000, rt_subframes=50):
    # Other randomization functions...
    rep.randomizer.randomize_screen(screen, texture_files)
```

![Random background texture](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/random_texture.png)

![Random background texture, camera perspective](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/random_texture_viewport.png)

![Random background texture](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/output3.png)

We could instead generate textures with random shapes and colors. Either way, the resulting renders will look weird, but help the model training process weight features that are relevant for the icicles, not the background.

These are rather unsophisticated approaches. More realistic results would be achieved by changing the [materials](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/materials.html) of the actual walls of the house used as background. Omniverse has a large selection of available materials available in the NVIDIA Assets browser, allowing us to randomize a [much wider range of aspects](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html) of the rendered results.

### Creating realistic outdoor lighting conditions using sun studies

In contrast to a controlled indoor environment, creating a robust object detection model intended for outdoor use needs training images with a wide range of realistic natural light. When generating synthetic images we can utilize an [extension that approximates real world sunlight](https://docs.omniverse.nvidia.com/extensions/latest/ext_sun-study.html) based on sun studies. 

{% embed url="https://youtu.be/MRD-oAxaV8w" %}

The extension let's us set world location, date and time. We can also mix this with the Environment setting in Omniverse, allowing for a wide range of simulation of clouds, proper [Koyaanisqatsi](https://www.youtube.com/watch?v=tDW-1JIa2gI). As of March 2024 it is not easy to randomize these parameters in script, but this [is likely to change](https://forums.developer.nvidia.com/t/randomize-time-of-day-in-dynamic-sky/273833/9). In the mean time we can set the parameters, generate a few thousand images, change time of day, generate more images and so on.

{% embed url="https://youtu.be/qvDXRqBxECo" %}

![Sun study](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/output5.png)

![Sun study](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/output4.png)

![Sun study](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/output6.png)

### Creating label file for Edge Impulse Studio

Edge Impulse Studio supports a wide range of image labeling formats for object detection. The output from Replicator's BasicWriter needs to be transformed so it can be uploaded either through the web interface or via [web-API](https://docs.edgeimpulse.com/reference/ingestion-api#ingestion-api).

Provided is a simple Python program, [basic_writer_to_pascal_voc.py](https://github.com/eivholt/icicle-monitor/blob/main/scripts/basic_writer_to_pascal_voc.py). [Documentation on EI label formats](https://docs.edgeimpulse.com/docs/edge-impulse-studio/data-acquisition/uploader#understanding-image-dataset-annotation-formats). Run the program from shell with

``` 
python basic_writer_to_pascal_voc.py <input_folder>
```

or debug from Visual Studio Code by setting input folder in `launch.json` like this: 

```
"args": ["../out"]
```

This will create a file `bounding_boxes.labels` that contains all labels and bounding boxes per image.

## Creating an object detection project in Edge Impulse Studio

Look at the [provided object detection Edge Impulse project](https://studio.edgeimpulse.com/public/332581/live) or [follow a guide to create a new FOMO project](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices#how-to-get-started).

### Uploading images and labels using CLI edge-impulse-uploader

Since we have generated both synthetic images and labels, we can use the [CLI tool from Edge Impulse](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-uploader) to efficiently upload both. Use:

```
edge-impulse-uploader --category split --directory [folder]
```

to connect to account and project and upload image files and labels in `bounding_boxes.labels`. To switch project first do:

```
edge-impulse-uploader --clean
```

At any time we can find "Perform train/test split" under "Danger zone" in project dashboard to distribute images between training/testing in a 80/20 split.

### Model training and performance

Since our synthetic training images are based on both individual and two different sized clusters of icicles, we can't trust the model performance numbers too much. Greater F1 scores are better, but we will never achieve 100%. Still, we can upload increasing numbers of labeled images and observe how performance numbers increase.

2000 images:

![2000 images](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/2000-images.png)

6000 images:

![6000 images](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/6000-images-120cycles.png)

14000 images:

![14000 images](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/14000-images-120cycles_no-opt.png)

26000 images:

![26000 images](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/26000-images-light-5000coco-120cycles_no-opt.png)

Note that the final results include 5000 images from the [COCO 2017 dataset](https://cocodataset.org/#download). Adding this reduces F1 score a bit, but results in a model with significantly less overfitting, that shows almost no false positives when classifying random background scenes.

If we look at results from model testing in Edge Impulse Studio at first glance the numbers are less than impressive.

![Model testing](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/model-testing1.png)

However if we investigate individual samples where F1 score is less than 100%, we see that the model indeed has detected the icicles, but clustered differently than how the image was originally labeled. What we should look out for are samples that contain visible icicles where none were detected.

In the end virtual and real-life testing tells us how well the model really performs.

### Testing model in simulated environment with NVIDIA Isaac Sim and Edge Impulse extension

We can get useful information about model performance with minimal effort by testing it in a virtual environment. Install [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) and [Edge Impulse extension](https://github.com/edgeimpulse/edge-impulse-omniverse-ext).

![Edge Impulse extension](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/EI-ext-enable.png)

Install Sun study extension in Isaac Sim to be able to vary light conditions while testing.

![Sun study in Isaac Sim](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Isaac-sunstudy.png)

Paste API key found under Edge Impulse Studio> Dashboard> Keys> Add new API key:

![Edge Impulse extension API key](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/EI-ext-api-key.png)

To be able to classify any virtual camera capture we first need to build a version of the model that can run in a JavaScript environment. In Edge Impulse Studio, go to Deployment, find "WebAssembly" in the search box and hit Build. We don't need to keep the resulting .zip package, the extension will find and download it by itself.

![Edge Impulse WebAssembly](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/EI-webasm.png)

Back in the Edge Impulse extension in Isaac, when we expand the "Classification" group, a message will tell us everything is ready: "Your model is ready! You can now run inference on the current scene".

Before we test it we will make some accommodations in the viewport.

Switch to "RTX - Interactive" to make sure the scene is rendered realistically. 

Set viewport resolution to square 1:1 with either the same resolution as our intended device inference (120x120 pixels), or close (512x512 pixels).

![Isaac Sim viewport resolution](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Isaac-resolution.png)

Display Isaac bounding boxes by selecting "BoundingBox2DLoose" under the icon that resembles a robotic sensor, the hit "Show Window". Now we can compare the ground truth with model prediction.

![Isaac Sim sensors](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Isaac-sensor.png)

![Isaac Sim model testing](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Isaac-EI-1.png)

![Isaac Sim model testing](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Isaac-EI-2.png)

![Isaac Sim model testing](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Isaac-EI-3.png)

## Deployment to device and LoRaWAN

### Testing model on device using OpenMV

To get visual verification our model works as intended we can go to Deployment in Edge Impulse Studio, select **OpenMV Firmware** as target and build. 

![Edge Impulse Studio Deployment OpenMV Firmware](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/OpenMV_deployment.png)

Follow the [documentation](https://docs.edgeimpulse.com/docs/run-inference/running-your-impulse-openmv) on how to flash the device and to modify the `ei_object_detection.py` code. Remember to change: `sensor.set_pixformat(sensor.GRAYSCALE)`! The file `edge_impulse_firmware_arduino_portenta.bin` is our firmware for the Arduino Portenta H7 with Vision shield.

![Testing model on device with OpenMV](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/OpenMV-testing.png)

### Deploy model as Arduino compatible library and send inference results to The Things Network with LoRaWAN

Start by selecting Arduino library as Deployment target.

![Deploy model as Arduino compatible library](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/EI-arduino-library.png)

Once built and downloaded, open Arduino IDE, go to **Sketch> Include Library> Add .zip Library ...** and locate the downloaded library. Next go to **File> Examples> [name of project]_inferencing> portenta_h7> portenta_h7_camera** to open a generic sketch template using our model. To test the model continuously and print the results to console this sketch is ready to go. The code might appear daunting, but we really only need to focus on the loop() function.

![Arduino compatible library example sketch](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/EI-arduino-library-example.png)

### Transmit results to The Things Stack sandbox using LoRaWAN
Using The Things Stack sandbox (formely known as The Things Network) we can create a low-power sensor network that allows transmitting device data with minimal energy consumption, long range without network fees. Your area might already be covered by a crowd funded network, or you can [initiate your own](https://www.thethingsnetwork.org/community/bodo/). [Getting started with LoRaWAN](https://www.thethingsindustries.com/docs/getting-started/) is really fun!

![The Things Network](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/ttn-map.png)

Following the [Arduino guide](https://docs.arduino.cc/tutorials/portenta-vision-shield/connecting-to-ttn/) we create an application in The Things Stack sandbox and register our first device.

![The Things Stack application](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/ttn-app.png)

![The Things Stack device](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/ttn-device.png)

Next we will simplify things by merging an example Arduino sketch for transmitting a LoRaWAN-message with the Edge Impulse generated object detection model code. Open the example sketch called LoraSendAndReceive included with the MKRWAN(v2) library mentioned in the [Arduino guide](https://docs.arduino.cc/tutorials/portenta-vision-shield/connecting-to-ttn/). In the [project code repository](https://github.com/eivholt/icicle-monitor/tree/main/portenta-h7/portenta_h7_camera_lora) we can find an Arduino sketch witht the merged code.

![Arduino transmitting inference results over LoRaWAN](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/arduino-lora.png)

In short we perform inference every 10 seconds. If any icicles are detected we simply transmit a binary 1 to the The Things Stack application. It is probably obvious that the binary payload is redundant, the presence of a message is enough, but this could be extended to transmit e.g. prediction confidence, number of clusters, battery level, temperature or light level.

```python
if(bb_found) {
    int lora_err;
    modem.setPort(1);
    modem.beginPacket();
    modem.write((uint8_t)1); // This sends the binary value 0x01
    lora_err = modem.endPacket(true);
}
```

A few things to consider in the implementation:
The device should enter deep sleep mode and disable/put to sleep all periferals between object detection. Default operation of the Portenta H7 with the Vision shield consumes a lot of energy and will drain battery quickly. To find out how much energy is consumed we can use a device such as the [Otii Arc from Qoitech](https://www.qoitech.com/otii-arc-pro/). Hook up positive power supply to VIN, negative to GND. Since VIN bypasses the Portenta power regulator we should provide 5V, however in my setup the Otii Arc is limited to 4.55V. Luckily it seems to be sufficient and we can take some measurements. By connecting the Otii Arc pin RX to the Portenta pin D14/PA9/UART1 TX, in code we can write debug messages to Serial1. This is incredibly helpful in establishing what power consumption is associated with what part of the code.

![Arduino Portenta H7 power specs](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/portenta_h7_power.png)

![Arduino Portenta H7 pin-out](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/portenta_h7_pinout.png)

![Otii Arc hook-up](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/otii-arc-portenta.png)

![Otii Arc power profile](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/otii-icicle-profile.png)

As we can see the highlighted section should be optimized for minimal power consumption. This is a complicated subject, especially on a [complex board such as the Arduino Portenta H7](https://github.com/arduino/ArduinoCore-mbed/issues/619) and out of scope for this article. Provided are some examples for general guidance: [snow monitor](https://www.hackster.io/eivholt/low-power-snow-depth-sensor-using-lora-e5-b8e7b8#toc-power-profiling-16), [mail box sensor](https://community.element14.com/challenges-projects/project14/rf/b/blog/posts/got-mail-lorawan-mail-box-sensor).

The project code runs inference on an image every 10 seconds. This is for demonstration purposes and should be much less frequent, like once per hour during daylight. Have a look at this project for an example of how to [remotely control inference interval](https://www.hackster.io/eivholt/low-power-snow-depth-sensor-using-lora-e5-b8e7b8#toc-lora-application-14) via LoRaWAN downlink message. This could be further controlled automatically via an application that has access to an [API for daylight data](https://developer.yr.no/doc/GettingStarted/).

![YR weather API](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/yr-sun.png)

In the The Things Stack application we need to define a function that will be used to decode the byte into a JSON structure that is easier to interpet when we pass the message further up the chain of services. The function can be found in the [project code repository](https://github.com/eivholt/icicle-monitor/blob/main/TheThingsStack/decoder.js).

![The Things Stack decoder](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/ttn-decoder.png)

```javascript
function Decoder(bytes, port) {
    // Initialize the result object
    var result = {
        detected: false
    };

    // Check if the first byte is non-zero
    if(bytes[0] !== 0) {
        result.detected = true;
    }

    // Return the result
    return result;
}
```

Now we can observe messages being received and decoded in **Live data** in TTS console.

![The Things Stack live data](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/ttn-data.png)

An integral part of TTS is a MQTT message broker. At this point we can use [any MQTT client to subscribe to topics](https://www.thethingsindustries.com/docs/integrations/mqtt/mqtt-clients/) and create any suitable notification system for the end user. The following is a MQTT client written in Python to demonstrate the principle. Note that the library paho-mqtt has been used in a way so that it will block the program execution until two messages have been received. Then it will print the topic and payloads. A real-life implementation would rather register a callback and perform some action for each message received.

```
python
# pip install paho-mqtt
import paho.mqtt.subscribe as subscribe

m = subscribe.simple(topics=['#'], hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"icicle-monitor",'password':"NNSXS.V7RI4O2LW3..."}, msg_count=2)
for a in m:
    print(a.topic)
    print(a.payload)
```

```
json
v3/icicle-monitor@ttn/devices/portenta-h7-icicle-00/up
{"end_device_ids":{"device_id":"portenta-h7-icicle-00","application_ids":{"application_id":"icicle-monitor"},"dev_eui":"3036363266398F0D","join_eui":"0000000000000000","dev_addr":"260BED9C"},"correlation_ids":["gs:uplink:01HSKMT8KSZFJ7FB23RGSTJAEA"],"received_at":"2024-03-22T17:54:52.358270423Z","uplink_message":{"session_key_id":"AY5jAnqK0GdPG1yygjCmqQ==","f_port":1,"f_cnt":9,"frm_payload":"AQ==","decoded_payload":{"detected":true},"rx_metadata":[{"gateway_ids":{"gateway_id":"eui-ac1f09fffe09141b","eui":"AC1F09FFFE09141B"},"time":"2024-03-22T17:54:52.382076978Z","timestamp":254515139,"rssi":-51,"channel_rssi":-51,"snr":13.5,"location":{"latitude":67.2951736450195,"longitude":14.4321346282959,"altitude":50,"source":"SOURCE_REGISTRY"},"uplink_token":"CiIKIAoUZXVpLWFjMWYwOWZmZmUwOTE0MWISfCf/+CRQbEMOvrnkaCwjsi/evBhDurYRJILijo5K00mQ=","received_at":"2024-03-22T17:54:52.125610010Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7,"coding_rate":"4/5"}},"frequency":"867300000","timestamp":254515139,"time":"2024-03-22T17:54:52.382076978Z"},"received_at":"2024-03-22T17:54:52.154041574Z","confirmed":true,"consumed_airtime":"0.046336s","locations":{"user":{"latitude":67.2951772015745,"longitude":14.43232297897339,"altitude":13,"source":"SOURCE_REGISTRY"}},"version_ids":{"brand_id":"arduino","model_id":"lora-vision-shield","hardware_version":"1.0","firmware_version":"1.2.1","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","ns_id":"EC656E0000000181","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}'

v3/icicle-monitor@ttn/devices/portenta-h7-icicle-00/up
{"end_device_ids":{"device_id":"portenta-h7-icicle-00","application_ids":{"application_id":"icicle-monitor"},"dev_eui":"3036363266398F0D","join_eui":"0000000000000000"},"correlation_ids":["as:up:01HSKMTN7F60CC3BQXE06B3Q4X","rpc:/ttn.lorawan.v3.AppAs/SimulateUplink:17b97b44-a5cd-45f0-9439-2de42e187300"],"received_at":"2024-03-22T17:55:05.070404295Z","uplink_message":{"f_port":1,"frm_payload":"AQ==","decoded_payload":{"detected":true},"rx_metadata":[{"gateway_ids":{"gateway_id":"test"},"rssi":42,"channel_rssi":42,"snr":4.2}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7}},"frequency":"868000000"},"locations":{"user":{"latitude":67.2951772015745,"longitude":14.43232297897339,"altitude":13,"source":"SOURCE_REGISTRY"}}},"simulated":true}'
```

Observe the difference in the real uplink (first) and simulated uplink (last). In both we find "decoded_payload":{"detected":true}.

TTS has a range of [integration options](https://www.thethingsindustries.com/docs/integrations/) for specific platforms, or you could set up a [custom webhook using standard HTTP/REST](https://www.thethingsindustries.com/docs/integrations/webhooks/) mechanism.

## Limitations

### Weatherproofing

For permanent outdoor installation the device requires a properly sealed enclosure. The camera is mounted on the shield PCB and will need some engineering to be able to see through the enclosure while remaining water tight. For inspiration on how to create weather-proof enclosures that allow sensors and antennas outside access, [see this project](https://www.hackster.io/eivholt/low-power-snow-depth-sensor-using-lora-e5-b8e7b8) on friction fitting and use of rubber washers. The referenced project also proves that battery operated sensors can work with no noticeable degradation in winter conditions (to at least -15 degrees Celcius).

### Obscured view

The project has no safe-guard against false negatives. The device will not report if it's view is blocked. This could be resolved by placing static markers on both sides of an area to monitor and included in synthetic training data. Absence of at least one marker could trigger a notification that the view is obscured.

![Markers to avoid false negatives](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/marker.png)

### Object scale

Due to optimization techniques in Faster Objects - More Objects (FoMo) determining relative sizes of the icicles is not feasible. As even icicles with small mass can be harmful at moderate elevation this is not a crucial feature.

![Object scale](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/object-scale.png)

### Exact number of icicles

The object detection model has not been trained to give an exact number of icicles in view. This has no practical implication other than the model verification results appearing worse than practical performance.

![Icicle grouping](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/grouping.png)

### Non-vertical icicles and snow

Icicles can appear bent or angled either due to wind or more commonly due to ice and snow masses slowly dropping over roof edges. The dataset generated in this project does not cover this, but it would not take a lot of effort to extend the domain randomization to rotate or warp the icicles.

![AULSSON_EBBA](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/AULSSON_EBBA.png)

![Martin Cathrae](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/Martin-Cathrae.png)

The training images could benefit from simulating snow with particle effects in Omniverse. The project could also be extended to detect build-up of snow on roofs. For inspiration check out this demo of simulated snow dynamic made in 2014 by Walt Disney Animation Studios for the movie Frozen: 

{% embed url="https://youtu.be/9H1gRQ6S7gg" %}

### Grayscale

To be able to compile a representation of our neural network and have it run on the severely limited amount of RAM available on the Arduino Portenta H7, pixel representation has been limited to a single channel - grayscale. Colors are not needed to detect icicles so this does not affect the results.

![Grayscale](../.gitbook/assets/rooftop-ice-synthetic-data-omniverse/grayscale1.png)

## Further reading

Insights into [how icicles are formed](https://www.insidescience.org/news/riddles-rippled-icicle).

