---
description: >-
    A wearable for continuous gait analysis, aiming to detect gait abnormalities indicative of potential medical conditions.
---

# Continuous Gait Monitor (Anomaly Detection) - Nordic Thingy:53

Created By: Samuel Alexander

Public Project Link: [https://studio.edgeimpulse.com/public/366723/live](https://studio.edgeimpulse.com/public/366723/live)

![01-cover](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/01-cover.jpg)

## Introduction

Subtle changes in gait can be early indicators of various medical conditions, including neurodegenerative diseases like Parkinson's, multiple sclerosis, balance disorders, and even other injuries with far-reaching health consequences. Early detection often relies on subtle changes in how a person walks, such as reduced speed, shuffling steps, or unsteadiness. Unfortunately, current assessments primarily rely on periodic, in-clinic observations by healthcare professionals, potentially missing subtle yet significant changes occurring between visits. Moreover, subjective self-assessments of gait are often unreliable. This lack of continuous, objective monitoring hinders timely diagnoses, limits the effectiveness of treatment plans, and makes it difficult to track the progression of gait-related conditions. A proactive, data-driven solution is needed to ensure individuals and their healthcare providers have the information necessary for informed decision-making.

![02-gait](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/02-gait.png)

Image Credit: Can Tunca, "Human Gait Cycle", 2017, via mdpi.com

## Project Overview

This project aims to develop a wearable device for early gait disorder detection. We'll begin by collecting data representing normal gait patterns during walking, running, and standing.  Next, we'll extract relevant features using Edge Impulse tools, focusing on characteristics like leg swing acceleration, stride length, and foot placement (supination/pronation). Employing Edge Impulse's K-means anomaly detection block and feature importance analysis, the device will learn to distinguish healthy gait patterns (based on the individual's established baseline) from potential anomalies.  Initially, inference results will be displayed on a smartphone app. This proof-of-concept can be expanded into a wearable device that alerts users of gait abnormalities and trends, recommending healthcare consultations when appropriate.  Ultimately, our goal is to provide a proactive tool for early disorder identification, enabling timely intervention and improved outcomes.

![03-project](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/03-project.jpg)

### Why the Nordic Thingy:53? (Platform Continuity)

The Nordic Thingy:53 leverages the nRF5340 Arm Cortex-M33 SoC, providing the computational resources necessary for on-device AI inference. It also includes a built-in accelerometer to capture detailed gait data and Bluetooth 5.4 for wireless communication. Importantly, the same nRF5340 chip powers the nRF5340 Development Kit, providing a consistent hardware platform throughout the project's development cycle. This means we can easily prototype on the Thingy:53, refine algorithms and sensor selections on the Development Kit, and ultimately transition to a custom wearable design for mass production – all using the same core chip. This approach ensures a smooth and efficient development process.

![04-thingy](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/04-thingy.jpg)

## Hardware Requirements

- Nordic Thingy:53
- 3D printer

## Software Requirements

- Edge Impulse CLI
- nRF Programmer App (iPhone/Android)
- nRF Connect Desktop

## Dataset Collection

The Thingy:53 was used for collecting a dataset for training the AI model to establish a baseline of normal, healthy gait patterns. This dataset includes three types of movement: standing, walking, and running. To capture realistic data, the user wore the device while performing these activities. The dataset's variety helps the model accurately classify different gait patterns and detect potential abnormalities in various situations.

![05-dataset-collection](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/05-dataset-collection.gif)

A 3D printed shoe clip-on case modification is made for attaching the Thingy:53 to a shoe. Download the .stl files: https://www.thingiverse.com/thing:6558382

![06-cad](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/06-cad.png)

![07-mod](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/07-mod.jpg)

![08-shoe](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/08-shoe.jpeg)

This project assumes basic familiarity with connecting the Thingy:53 to Edge Impulse via the nRF Connect app. If needed, refer to this guide for assistance: https://docs.edgeimpulse.com/docs/edge-ai-hardware/mcu/nordic-semi-thingy53

![09-nrfconnect](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/09-nrfconnect.jpeg)

Collect data for each label **(standing, walking, running)** using the nRF Connect app. Choose:
- Sensor: Accelerometer
- Sample Length (ms): 20000
- Frequency (Hz): 20

For each label, we collected 13 repetitions of 20000 ms which equals to 260 seconds for each label. This seems to be plenty enough for our testing, however more data may be necessary if the gait patterns are performed under more variety of terrains.

![10-collect-data](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/10-collect-data.jpeg)

Split the 20000 ms sample into 4 sections of 5000 ms window.

![11-split-sample](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/11-split-sample.png)

![12-complete-dataset](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/12-complete-dataset.png)

Perform train and test split into approximately 80/20 ratio.

![13-train-test-split](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/13-train-test-split.png)

## Impulse Design

After thorough testing, including using the EON Tuner, the optimal settings for our time series data were determined.  We employ both a classifier and K-means anomaly detection to enable both gait pattern classification and anomaly scoring.

![14-create-impulse](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/14-create-impulse.png)

### Spectral Features

Spectral analysis transforms raw accelerometer data from the time domain into the frequency domain.  This reveals hidden patterns in gait data, such as stride frequency, step regularity, and harmonic components of movement patterns. These extracted spectral features can provide a richer representation of gait characteristics for the neural network, often leading to improved classification accuracy and a clearer understanding of potential gait abnormalities.

![15-spectral-features](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/15-spectral-features.png)

### Classifier

As mentioned, these parameter settings are alread using optimized values from the EON Tuner.

![16-tuned-classifier](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/16-tuned-classifier.png)

![17-tuned-testing](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/17-tuned-testing.png)

These are our result before using EON Tuner (default parameter values and settings).

![18-initial-results](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/18-initial-results.jpg)

The EON Tuner is a valuable tool for finding the best parameter settings and model architecture to maximize accuracy. While it can also optimize for performance or memory usage, our project has sufficient resources in these areas. Therefore, we prioritize accuracy as the primary optimization goal.

![19-eon-tuner-settings](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/19-eon-tuner-settings.png)

![20-eon-tuner](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/20-eon-tuner.png)

### Anomaly Detection (K-means)

K-means clustering is chosen for gait anomaly detection due to its computational efficiency and ability to robustly identify distinct clusters. While Gaussian Mixture Models (GMMs) can model more complex data distributions, in our testing K-means excels in identifying distinct clusters like normal walking, running, and standing.

We chose L1 Root Mean Square (RMS) for anomaly detection with accelerometer data (accX, accY, accZ) due to its sensitivity to outliers and interpretability.  L1 RMS emphasizes large deviations, which helps identify significant gait abnormalities and provides insights into the specific directions of those anomalies. It's also more robust to noisy accelerometer data compared to L2 RMS.

![21-anomaly-detection-settings](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/21-anomaly-detection-settings.png)

![22-anomaly-vertical-forward](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/22-anomaly-vertical-forward.jpg)

![23-anomaly-forward-sideways](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/23-anomaly-forward-sideways.jpg)

## Deployment

Now the AI model is ready to be deployed to the Edge. Nordic Thingy:53 is selected for our deployment option. For this project we chose unoptimized (float32) to preserve accuracy since our hardware has enough performance and memory headroom.

![24-deployment](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/24-deployment.png)

After building our model, we'll get the new firmware. Follow this guide to flash the firmware: https://docs.edgeimpulse.com/docs/edge-ai-hardware/mcu/nordic-semi-thingy53#updating-the-firmware

![25-write-firmware-nrfconnect](../.gitbook/assets/continuous-gait-monitor-nordic-thingy53/25-write-firmware-nrfconnect.png)

## Conclusion

This project successfully demonstrates the potential for wearable AI solutions in early detection of gait disorders. By harnessing the Thingy:53's capabilities and Edge Impulse's streamlined workflow, we developed a device capable of identifying gait anomalies. This tool offers proactive health monitoring, with the potential to alert users to subtle changes that may foreshadow underlying medical conditions.  Future work could expand the dataset for greater robustness, explore additional sensor modalities, and conduct clinical trials to thoroughly validate the system for diagnostic use.

See this project in action:

{% embed url="https://youtu.be/l7yP2IttN4Q" %}


