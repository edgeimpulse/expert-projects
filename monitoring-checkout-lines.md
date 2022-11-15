---
description: Using a Renesas RZ/V2L Evaluation Kit to monitor people in line at a retail checkout lane.
---

# Monitoring Checkout Lines with Computer Vision 

Created By:
Solomon Githu

Public Project Link:
[https://studio.edgeimpulse.com/public/140398/latest](https://studio.edgeimpulse.com/public/140398/latest)

## Intro

No one likes waiting in lines! Research shows that people wait in lines three to five days a year. Long queues at supermarkets cause shopper fatigue, reduce the customer experience and lead to carts abandonment.

Existing surveillance cameras can be used in stores near the queue area. Using Computer Vision models
, the camera will be able to understand how many customers are in a queue. When the queue reaches a certain threshold of customers, this can be identified as a long queue, so staff can take action and even suggest that another counter should be opened.

A branch of mathematics known as **queuing theory** investigates the formation, operation, and causes of queues. The arrival process, service process, number of servers, number of system spaces, and number of consumers are all factors that are examined by queueing theory. The goal of queueing theory is to strike a balance that is efficient and affordable.

For this project, I developed a solution that can identify when a long queue is forming at a counter. If a counter is seen to have 51 percent of the total customers then the system flags this as a long queue with a red indicator. Similarly the shortest serving counter is indicated with a green indicator signaling that people should be redirected there.

## Computer Vision Model - YOLOv5 vs MobileNetV2

Object detection has evolved over the past 20 years. However it can be tricky sometimes. It is important to understand the main characteristics of each model for a use case. 

I used [Edge Impulse project versioning](https://forum.edgeimpulse.com/t/you-can-now-version-your-projects/671) to store various models of YOLOv5 and MobileNet V2. 

![Project Versions](.gitbook/assets/monitoring-checkout-lines/img1_screenshot%20Project%20Versions.jpg)

We can see that MobileNetV2 SSD FPN-Lite 320x320 has both training and testing performances of over 70%. However, when I gave  it images of retail stores then the performance was not good and most of the time it failed to detect people. This can be related to the fact that an image of retail store has many objects such as people, shelves and carts. Having a maximum image size of 320x320 means that meaningful data for the objects are destroyed. This can be seen in the screenshot below of a test sample.

![MobileNet V2 Testing](.gitbook/assets/monitoring-checkout-lines/img2_screenshot%20MobileNetV2%20Testing.jpg)

I settled with YOLOv5 model which allows an higher image size of 640x640. You can find the public project here: [Person Detection with Computer Vision](https://studio.edgeimpulse.com/public/140398/latest).  To add this project to your Edge Impulse projects, click “Clone”  at the top of the window. 


## Dataset Preparation

For my dataset, I sourced images of people from public available datasets such as [Kaggle](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset) among others. This range from images of people  in retail stores and various environments. 

In total, I had 588 images for training and 156 images for testing.

![Training Dataset](.gitbook/assets/monitoring-checkout-lines/img3_screenshot%20Training%20data.jpg)

![Testing Dataset](.gitbook/assets/monitoring-checkout-lines/img4_screenshot%20Testing%20data.jpg)

With 744 images it would be tiresome to draw bounding boxes and give a name for all instances where a person appears. Edge Impulse offers various [AI-assisted labelling](https://www.edgeimpulse.com/blog/3-ways-to-do-ai-assisted-labeling-for-object-detection) methods to automate this process. In my case, I chose YOLOv5 and it was able to annotate more than 90% of people. To use this feature, in the Labelling queue select "Classify using YOLOv5" under "Label suggestions".

![AI-Assisted Labeling](.gitbook/assets/monitoring-checkout-lines/img5_screenshot%20Yolov5%20assisted%20Labelling.jpg)

## Impulse Design

An [Impulse](https://docs.edgeimpulse.com/docs/edge-impulse-studio/impulse-design) is a machine learning pipeline that indicates the type of input data, extracts features from the data and finally a neural network that trains on the features from your data.

For the YOLOv5 model that I settled with, I used an image width and height of 640 and the "Resize mode" set to "Squash". The processing block was set to "Image" and the learning block set to "Object Detection (Images)".

![Impulse Design](.gitbook/assets/monitoring-checkout-lines/img6_screenshot%20Impulse%20Design.jpg)

Under "Image" in Impulse design, the color depth of the images is set to RGB and the next step was to extract features.

![Features](.gitbook/assets/monitoring-checkout-lines/img7_screenshot%20Features.jpg)

Here in the features tab we can see the on-device performance for generating features during the deployment. These metrics are for the Renesas RZ/V2L(CPU). The [Renesas RZ/V2L Evaluation Board Kit](https://www.edgeimpulse.com/blog/announcing-official-support-for-the-renesas-rzv2l-evk) was recently supported by Edge Impulse. This board is designed for vision AI applications and it offers a powerful hardware acceleration through its Dynamically Reconfigurable Processor (DRP) and multiply-accumulate unit (AI-MAC).

The last step was to train the model. Another great tool with Edge Impulse is that you can [Bring your own model](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/adding-custom-learning-blocks) to the studio. I added a YOLOv5 model to use it in this project. You can follow the [GitHub repo tutorial](https://github.com/edgeimpulse/yolov5) on how to add YOLOv5 to your Edge Impulse account/organization.

![Choosing YOLOv5 Model](.gitbook/assets/monitoring-checkout-lines/img8_screenshot%20Choosing%20a%20model.jpg)

I used 500 training cycles with a learning rate of 0.001. It is advised to train a YOLOv5 model using more than 1500 photos per class and more than 10,000 instances per class to produce a robust YOLOv5 model.

![Training Performance](.gitbook/assets/monitoring-checkout-lines/img9_screenshot%20Training%20model.jpg)

## Model Testing

After training the model, I did a test with the unseen(test) data and the results were impressive, 85% accuracy.

![Model Testing](.gitbook/assets/monitoring-checkout-lines/img10_screenshot%20Model%20testing.jpg)

In this test sample which has a precision score of 90%, we can see that the model was able to detect all people in the image.

![Model Testing Sample](.gitbook/assets/monitoring-checkout-lines/img11_screenshot%20Model%20testing%20sample.jpg)

## Deploying to Renesas RZ/V2L Evaluation Kit

The Renesas Evaluation Kit comes with the RZ/V2L board and a 5-megapixel Google Coral Camera. To setup the board, Edge Impulse has prepared a [guide](https://docs.edgeimpulse.com/renesas/development-platforms/officially-supported-cpu-gpu-targets/renesas-rz-v2l) that shows how to prepare the Linux Image, install Edge Impulse CLI and finally connecting to Edge Impulse Studio.

![RZ/V2L with Camera](.gitbook/assets/monitoring-checkout-lines/img12_RZ_V2L%20with%20camera.JPG)

To deploy the model to the RZ/V2L we can run the command ```edge-impulse-linux-runner``` after ```edge-impulse-linux``` which lets us log in to our account and select the cloned public project.

We can also download an executable of the model which contains the signal processing and ML code, compiled with optimizations for the processor, plus a very simple IPC layer (over a Unix socket). This executable is called [.eim model](https://docs.edgeimpulse.com/docs/edge-impulse-for-linux/edge-impulse-for-linux#.eim-models)

To do a similar method, create a directory and navigate into the directory:
```bash
mkdir monitoring_retail_checkout_lines && \
cd monitoring_retail_checkout_lines
```
Next download the eim model with the command:
```bash
edge-impulse-linux-runner --download modelfile.eim --force-target runner-linux-aarch64
```
In this command we specify that the eim model will be downloaded into a "file" called **modelfile**. Also to mention, we also specify that we want the binary for Linux AARCH64 since the RZ/V2L has the [Arm Cortex-A55 processor](https://developer.arm.com/Processors/Cortex-A55).

![Download .eim](.gitbook/assets/monitoring-checkout-lines/img13_screenshot%20Download%20eim.jpg)

Now we can run the executable model locally using the [Edge Impulse Linux CLI](https://docs.edgeimpulse.com/docs/edge-impulse-for-linux/edge-impulse-for-linux):
```bash
edge-impulse-linux-runner --model-file modelfile.eim
```
We pass the downloaded filename **modelfile** in the command.

![Linux-runner .eim](.gitbook/assets/monitoring-checkout-lines/img14_screenshot%20Linux-runner%20eim.jpg)

We can go to the URL provided and we will see the feed being captured by the camera as well as the bounding boxes if present.

![Linux-runner Public Webserver](.gitbook/assets/monitoring-checkout-lines/img19_screenshot%20linux%20runner%20on%20RZ_V2L.jpg)

![Linux-runner Public Webserver](.gitbook/assets/monitoring-checkout-lines/img20_screenshot2%20linux%20runner%20on%20RZ_V2L.jpg)

## Analyzing Checkout Lines with Computer Vision and a Smart Application

Using the eim executable and [Python SDK](https://docs.edgeimpulse.com/docs/edge-impulse-for-linux/edge-impulse-for-linux#sdks) for Edge Impulse for Linux, I developed a Web Application using [Flask](https://flask.palletsprojects.com/en/2.2.x/) that counts the number of people at each queue and computes a distribution of total counts across the available counters which enables identifying long and short queues.

The application shows which counter is serving more than 51 percent of the total number of people with a red indicator. At the same time the counter with the lowest serving customers is shown with a green indicator signaling that people should be redirected there.

For the demo I obtained a public available video footage of a retail store which shows 3 counter points. A snapshot of the footage can be seen below.

![Test Image](.gitbook/assets/monitoring-checkout-lines/img15_test%20image.jpg)

The application obtains the bounding boxes coordinates ( x and y) for each detected person using the Python SDK. From the video footage I identified where the checkout lines for the 3 cashiers appear in the x coordinate. These form 3 regions of interest. Next, the Python script checks how many bounding boxes' x coordinates appear in each region of interest and increments the person count accordingly.

Note that if you are using another surveillance footage then you will need to identify the location of the region(s) of interest.

![Regions of Interest](.gitbook/assets/monitoring-checkout-lines/img16_regions%20of%20interest.jpg)

You can clone the public [GitHub repository](https://github.com/SolomonGithu/retail-checkout-lines-management-with-Edge-Impulse) to your RZ/V2L board. The installation steps are in the repository. You can run the Flask application or the binary executable built with [PyInstaller](https://pyinstaller.org/en/stable/) for AARCH64 platform.

Afterwards, I projected the demo footage from a monitor to the 5-megapixel Google Coral camera attached to the RZ/V2L board. From the left, we have cashier number 1, then 2 in the middle and 3 on the far right. The gauges on the right are responsive and they can be red, green or orange. Red implies that the cashier has 51% of the total number of people in the queues while green shows the cashier with the lowest customer(s). Orange shows the cashier who has a count that is in the middle of the highest and lowest. This enables us to easily identify when long queues are forming at a cashier.

![Application Running](.gitbook/assets/monitoring-checkout-lines/img17_deploying%20the%20application.jpg)

![Application Running](.gitbook/assets/monitoring-checkout-lines/img18_deploying%20the%20application%20gif.gif)

A challenge that I faced was the overlapping bounding boxes in the regions of interest so I had to merge nearby overlaps to one bounding box. This method can only be applied to this demo footage. In other cases we do not know how many real objects to reference when doing the merge.

## Conclusion

Implementing Computer Vision models comes with its challenges. Some challenges can be identify accompanying guests, distinguish customers who are in the queue and not shopping, among others.

A future work for this project can be to predict queueing times for different days and particular times of the day.

With Edge Impulse, developing ML models and deploying them has always been easy. Knowledge on machine learning and microcontrollers is not known by everyone but the [Edge Impulse platform](https://www.edgeimpulse.com) provides easy, smarter and faster tools that we can use to create build edge ML solutions quickly.
