---
description: >-
  Use multi-modal audio classification and thermal imaging to identify anomalies or defects in HVAC cooling systems.
---

# AI-driven Audio and Thermal HVAC Monitoring - SeeedStudio XIAO ESP32

Created By: Kutluhan Aktar

Public Project Link: [https://studio.edgeimpulse.com/public/418121/latest](https://studio.edgeimpulse.com/public/418121/latest)

GitHub Repository: [https://github.com/KutluhanAktar/AI-driven-Sound-Thermal-Image-based-HVAC-Fault-Diagnosis/](https://github.com/KutluhanAktar/AI-driven-Sound-Thermal-Image-based-HVAC-Fault-Diagnosis/)

![](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_run_models.gif)

## Description

One of the most prominent hurdles in operating manufacturing plants is to regulate the enervating heat produced by industrial processes. Therefore, an efficient industrial cooling system is the fulcrum of managing a profitable, sustainable, and robust industrial facility. There are various cooling system designs and structures to provide versatile heat regulation for different business requirements. For instance, natural draft cooling benefits the density discrepancy between the produced hot air and ambient fresh air, mechanical draft cooling utilizes sprayed hot water to transfer heat from a condenser to dry air, and water cooling uses cold water directly to reduce the targeted component temperature.

When all cooling requirements are considered, water cooling options are still the most popular and budget-friendly cooling systems applicable to various cooling scenarios, including but not limited to condominiums, office buildings, and industrial facilities. Water cooling systems, also known as hydronic cooling systems, are mainly considered as the most adaptable and advantageous HVAC (heating, ventilation, and air conditioning) systems utilizing water to transfer heat from one location to another[^1]. Since hydronic HVAC systems use water to absorb and transfer heat, they are more energy efficient as compared to air-based systems since water has a higher thermal capacity. According to the applied heat transfer method and water source, water-based cooling systems provide design flexibility with low-maintenance.

Nonetheless, despite the advantages of relying on water as a coolant, water-based HVAC systems still require regular inspection and maintenance to retain peak condition and avert pernicious cooling aberrations deteriorating heat regulation for industrial facilities, office buildings, or houses. Since water-based cooling equipment is a part of various demanding industrial applications[^2], including but not limited to chemicals or petrochemicals, welding, medical, pharmaceutical, automotive, data centers, and metalworking, maintaining consistent and reliable heat transfer is essential to sustain profitable business growth. Thus, to reduce production costs and increase manufacturing efficiency, mechanics should examine each cooling component painstakingly and regularly.

Since hydronic HVAC systems can be intricate and multifaceted depending on the application requirements, there are plentiful malfunctions that can affect cooling efficiency and heat transfer capacity, resulting in catastrophic production downtime for industrial processes. For instance, chillers using metal tubes (copper or carbon steel) to circulate water are susceptible to corrosion and abrasion, leading to leaks and component failures. Accumulating sediment or particulates in the complex tubing systems can corrode or clog pipes, leading to inadequate heat transfer. Or, perforce, neglected electronic components can degrade and fail due to prolonged wear and tear, leading to inconsistent cooling results. Unfortunately, these HVAC system malfunctions not only deteriorate industrial process sustainability but also engender hazardous environmental impacts due to high energy loss.

Water-based or not, an installed HVAC system accounts for up to 50% of the total energy consumption of an establishment, surpassing the total energy consumption of lighting, elevators, and office equipment[^3]. Thus, an unnoticed abnormality can multiply energy consumption while the HVAC system tries to compensate for the heat transfer loss. Furthermore, since HVAC systems are tightly coupled systems and operate with protracted lag and inertia, they are vulnerable even to minuscule abnormalities due to the ripple effect of a single equipment failure, whether a capacitor, pipe, or gasket.

Relevant data indicates that the amount of energy waste caused by a malfunctioning cooling system and faulty control accounts for about 15%–30% of the total energy consumption of studied facilities. Thus, by running a malfunctioning cooling system, buildings became profligate energy devourers, resulting in harsh energy production demands causing excess carbon and methane emitted into the atmosphere. Therefore, applying real-time (automated) malfunction diagnosis to HVAC systems can abate excessive energy consumption and improve energy efficiency leading to savings ranging from 5% to 30% [^3]. In addition to preventing energy loss, automated HVAC fault detection can extend equipment lifespan, avoid profit loss, and provide stable heat transfer during industrial processes. In that regard, automated malfunction detection also obviates exorbitant overhaul processes due to prolonged negligence, leading to a nosedive in production quality.

After perusing recent research papers on detecting component failures to automate HVAC maintenance, I noticed that there are no practical applications focusing on identifying component abnormalities of intricate water-based HVAC systems to diagnose consecutive thermal cooling malfunctions before instigating hazardous effects on both production quality and the environment. Hence, I decided to build a versatile multi-model AIoT device to detect anomalous sound emanating from cooling fans via a neural network model and to diagnose consecutive thermal cooling malfunctions based on specifically produced thermal images via a visual anomaly detection model. In addition to AI-driven features, I decided to develop a capable and feature-rich web application (dashboard) to improve user experience and make data transfer easier between development boards.

As I started to work on developing my AI-powered device features, I realized that no available open-source data sets were fulfilling the purpose of multi-model HVAC malfunction diagnosis. Thus, since I did not have the resources to collect data from an industrial-level HVAC system, I decided to build a simplified HVAC system simulating the required component failures for data collection and in-field model testing. I got heavily inspired by PC (computer) water cooling systems while designing my simplified HVAC system. Similar to a closed-loop PC water cooling design, I built my system by utilizing a water pump, plastic tubings, an aluminum radiator, and aluminum blocks. As for the coolant reservoir, I decided to design a custom one and print the parts with my 3D printer. Nonetheless, since I decided to produce a precise thermal image by scanning cooling components, I still needed an additional mechanism to move a thermal camera on the targeted components — aluminum blocks. Thus, I decided to design a fully 3D-printable CNC router with the thermal camera container head to position the thermal camera, providing an automatic homing sequence. My custom CNC router is controlled by Arduino Nano and consists of a 28BYJ-48 stepper motor, GT2 pulleys, a timing belt, and gear clamps. While producing thermal images and running the visual anomaly detection model, I simply added an aquarium heater to the closed-water loop in order to instantiate aluminum block cooling malfunctions.

As mentioned earlier, to provide full-fledged AIoT features with seamless integration and simplify complex data transfer procedures between development boards while constructing separate data sets and running multiple models, I decided to develop a versatile web application (dashboard) from scratch. To briefly summarize, the web dashboard can receive audio buffers via HTTP POST requests, save audio samples by given classes, communicate with the Particle Cloud to obtain variables or make Particle boards register them, produce thermal images from thermal imaging buffers to store image samples, and run the visual anomaly detection model on the generated thermal images. In the following tutorial, you can inspect all web dashboard features in detail.

Since this is a multi-model AI-oriented project, I needed to construct two different data sets and train two separate machine learning models in order to build a capable device. First, I focused on constructing a valid audio data set for detecting anomalous sound originating from cooling fans. Since XIAO ESP32C6 is a compact and high-performance IoT development board providing 512KB SRAM and 4 MB Flash, I decided to utilize XIAO ESP32C6 to collect audio samples and run my neural network model for anomalous sound detection. To generate fast and accurate audio samples (buffers), I decided to use a Fermion I2S MEMS microphone. Also, I connected an SSD1306 OLED display and four control buttons to program a feature-rich on-device user interface. After collecting an audio sample, XIAO ESP32C6 transfers it to the web dashboard for data collection. As mentioned earlier, I designed my custom CNC router based on Arduino Nano due to its operating voltage. To provide seamless device operations, XIAO ESP32C6 communicates with Arduino Nano to move the thermal camera container head.

After completing constructing my audio data set, I built my neural network model (Audio MFE) with Edge Impulse to detect sound-based cooling fan abnormalities. Audio MFE models employ a non-linear scale in the frequency domain, called Mel-scale, and perform well on audio data, mostly for non-voice recognition. Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I have not encountered any issues while uploading and running my Audio MFE model on XIAO ESP32C6. As labels, I simply differentiated the collected audio samples by the cooling fan failure presence:

- normal
- defective

After training and testing my neural network model (Audio MFE), I deployed the model as an Arduino library and uploaded it to XIAO ESP32C6. Therefore, the device is capable of detecting anomalous sound emanating from the cooling fans by running the neural network model onboard without any additional procedures or latency.

Since I wanted to employ the secure and reliable Particle Cloud as a proxy to transfer thermal imaging (scan) buffers to the web dashboard, I decided to utilize Photon 2, which is a feature-packed IoT development board optimized for cloud prototyping. To collect accurate thermal imaging buffers, I employed an MLX90641 thermal imaging camera producing 16x12 IR arrays (buffers) with fully calibrated 110° FOV (field-of-view). Also, I connected an ST7735 TFT display and an analog joystick to program a secondary on-device user interface. Even though I managed to create a snapshot (preview) image from the collected thermal scan buffers, Photon 2 is not suitable for generating thermal images, saving image samples, and running a demanding visual anomaly detection model simultaneously due to memory limitations. Therefore, after registering the collected thermal scan buffers to the Particle Cloud, I utilized the web dashboard to obtain the registered buffers via the Particle Cloud API, produce thermal image samples, and run the visual anomaly detection model.

Considering the requirements of producing accurate thermal images and running a visual anomaly detection model, I decided to host my web application (dashboard) on a LattePanda Mu (x86 Compute Module). Combined with its Lite Carrier board, LattePanda Mu is a promising single-board computer featuring an Intel N100 quad-core processor with 64 GB onboard storage.

After completing constructing my thermal image data set, I built my visual anomaly detection model with Edge Impulse to diagnose ensuing thermal cooling malfunctions after applying anomalous sound detection to the water-based HVAC system. Since analyzing cooling anomalies based on thermal images of HVAC system components is a complicated task, I decided to employ an advanced and precise machine learning algorithm based on the GMM anomaly detection algorithm and FOMO. Supported by Edge Impulse Enterprise, FOMO-AD is an exceptional algorithm for detecting unanticipated defects by applying unsupervised learning techniques. Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I have not encountered any issues while uploading and running my FOMO-AD model on LattePanda Mu. As labels, I utilized the default classes required by Edge Impulse to enable the F1 score calculation:

- no anomaly
- anomaly

After training and testing my FOMO-AD visual anomaly detection model, I deployed the model as a Linux (x86_64) application (.eim) and uploaded it to LattePanda Mu. Thus, the web dashboard is capable of diagnosing thermal cooling anomalies based on the specifically produced thermal images by running the visual anomaly detection model on the server (LattePanda Mu) without any additional procedures, reduced accuracy, or latency.

In addition to the discussed features, the web dashboard informs the user of the latest system log updates (completed operations) on the home (index) page automatically and sends an SMS to the verified phone number via Twilio so as to notify the user of the latest cooling status.

Considering the complex structure of this device based on a customized water-based HVAC system, I decided to design two unique PCBs after testing the prototype connections via breadboards. Since I wanted my PCB designs to represent the equilibrium of cooling fan failures and thermal (heat) malfunctions, I got inspired by two ancient rival Pokémon — Kyogre and Groudon.

Finally, in addition to the custom CNC router and coolant reservoir parts, I designed a plethora of complementary 3D parts, from unique PCB encasements to radiator mounts, so as to make the device as robust and compact as possible. To print flexible parts handling water pressure, I utilized a color-changing TPU filament.

So, this is my project in a nutshell 😃

Please refer to the following tutorial to inspect in-depth feature, design, and code explanations.

:gift::art: Huge thanks to [ELECROW](https://www.elecrow.com/pcb-manufacturing.html?idd=5) for sponsoring this project with their high-quality PCB manufacturing service and for sending me a [CrowVision 11.6'' TouchScreen Module (1366x768)](https://www.elecrow.com/crowvision-11-6-raspberry-pi-capacitive-touch-display-hd-1366-768-ips-screen-for-raspberry-pi.html?idd=5).

🚀🤖 Furthermore, you can check [the brand-new ELECROW project community](https://www.elecrow.com/share-projects.html?idd=5) to gain insight into the manufacturing process of my PCB designs.

:gift::art: Huge thanks to [Seeed Studio](https://www.seeedstudio.com/) for sponsoring these products:

⭐ XIAO ESP32C6 | [Inspect](https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32C6-p-5884.html)

⭐ Grove - MLX90641 Thermal Imaging Camera (16x12 IR Array w/ 110° FOV) | [Inspect](https://www.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array-MLX90641-110-degree-p-4612.html)

:gift::art: Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sponsoring these products:

⭐ Fermion: I2S MEMS Microphone | [Inspect](https://www.dfrobot.com/product-2637.html?tracking=60f546f8002be)

⭐ LattePanda Mu | [Inspect](https://www.dfrobot.com/product-2820.html?tracking=60f546f8002be)

⭐ Lite Carrier Board for LattePanda Mu | [Inspect](https://www.dfrobot.com/product-2822.html?tracking=60f546f8002be)

:gift::art: Also, huge thanks to [Anycubic](https://www.anycubic.com/) for sponsoring an [Anycubic Kobra 2](https://store.anycubic.com/products/kobra-2?utm_source=pr&utm_medium=review&utm_campaign=kutluhan_kobra2_0522).

![1](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_0.jpg)

![2](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_18_completed.jpg)

![3](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_13.jpg)

![4](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_6.jpg)

![5](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_1.png)

![6](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_3.png)

![7](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_4.png)

![8](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_2.jpg)

![9](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_3.jpg)

![10](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_4.jpg)

![11](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_5.jpg)

![12](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_7.png)

![13](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_11.png)

![14](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_collect_audio.gif)

![15](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_homing.gif)

![16](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_1.jpg)

![17](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_2.jpg)

![18](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_3.jpg)

![19](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_2.jpg)

![20](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_4.jpg)

![21](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_5.jpg)

![22](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_6.jpg)

![23](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_7.jpg)

![24](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_8.jpg)

![25](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_3.jpg)

![26](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_2.jpg)

![27](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_3.jpg)

![28](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_9.jpg)

![29](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_20.jpg)

![30](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_21.jpg)

![31](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_10.png)

![32](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_8.jpg)

![33](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_9.jpg)

![34](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_collect_thermal.gif)

![35](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_1.jpg)

![36](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_2.jpg)

![37](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_3.jpg)

![38](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_4.jpg)

![39](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_5.jpg)

![40](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_6.jpg)

![41](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_8.jpg)

![42](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_16.jpg)

![43](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_17.jpg)

![44](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_8.png)

![45](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_9.png)

![46](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_sms_1.jpg)

![47](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_sms_2.jpg)

![48](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_10.jpg)

![49](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_10.jpg)

![50](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_run_models.gif)

## Demonstration Videos

Since this HVAC malfunction detection device performs various interconnected features between different development boards and the web application (dashboard), I needed to compartmentalize consecutive processes and describe functions under the same code file separately to provide comprehensive step-by-step instructions.

Thus, I highly recommend watching the demonstration videos before scrutinizing the tutorial steps to effortlessly grasp device capabilities that might look complicated in the instructions.

{% embed url="https://www.youtube.com/watch?v=joLbKgfadg0" %}

{% embed url="https://www.youtube.com/watch?v=OD8HYZu69qY" %}

## Step 0: A brief introduction to device features and structure

As my projects became more intricate due to complex designs and multiple development board integrations, I decided to create concise illustrations to improve my tutorials, visualize the special tasks associated with each development board, and delineate the complicated data transfer procedures between different boards or complementary applications.

Thus, before proceeding with the following steps, I highly recommend inspecting these illustrations to comprehend the device features and structure better.

Note: Since downsizing these high-resolution illustrations is necessary for loading the tutorial page, I noticed the text on the illustrations lost legibility. Therefore, I also added the original image files below for further inspection.

![51](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/HVAC_infographic_xiao.png)

![52](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/HVAC_infographic_particle.png)

![53](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/HVAC_infographic_lattepanda.png)

![54](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/HVAC_infographic_schematic.png)

Before designing my simplified water-based HVAC system to simulate the required component failures for data collection and in-field model testing, I thoroughly inspected common water-cooled HVAC mechanisms[^4] to understand the inner workings of applying water as a coolant for transferring excess heat in industrial processes.

![55](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_based_HVAC_schematic_1.png)

![56](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_based_HVAC_schematic_2.png)

## Step 1.a: Designing and soldering the Kyogre-inspired PCB

As I was developing device features, I noticed that I needed to run different data collection procedures and machine learning models simultaneously. Therefore, I decided to create two separate PCB designs to run the required tasks conclusively. Since I wanted my PCB designs to represent the equilibrium of cooling fan failures and thermal (heat) malfunctions, I got inspired by two ancient rival Pokémon — Kyogre and Groudon. Their legendary fights depict the epitome of the conflict between water cooling and exuberating heat :)

Before prototyping my Kyogre-inspired PCB design, I inspected the detailed pin reference of XIAO ESP32C6 and needed to prepare components requiring soldering for programming. Aside from the other components, I employed a soldering station to solder jumper wires to each leg of the micro switch in order to make it compatible with the custom switch connector on the CNC router, which will be explained in the following steps.

![57](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_sound_1.jpg)

![58](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_sound_2.jpg)

![59](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_sound_3.jpg)

![60](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_sound_4.jpg)

Then, I checked the wireless (Wi-Fi) and serial communication quality between XIAO ESP32C6, Arduino Nano, and the web dashboard (application) while transferring and receiving data packets. In the meantime, I also tested the torque capacity of the 28BYJ-48 stepper motor.

![61](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_sound_5.jpg)

![62](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_sound_6.jpg)

I designed my Kyogre-inspired PCB by utilizing Autodesk Fusion 360 and KiCad in tandem. Since I wanted to design a unique 3D-printed encasement to simplify the PCB integration to the special mounts (also 3D-printed) of the aluminum water cooling radiator, I created the PCB outline (edge) on Fusion 360 and then imported the outline file (DXF) to KiCad. In this regard, I was able to design custom 3D parts compatible with the PCB outline precisely.

To replicate this malfunction detection device for water-cooled HVAC systems, you can download the Gerber file below or order the discussed PCB design directly from [my ELECROW community page](https://www.elecrow.com/share/sharepj/center/no/13accecfa8c56518d43f0f9ab46fe6f4).

![63](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_1.jpg)

![64](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_2.jpg)

![65](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_3.jpg)

By utilizing a TS100 soldering iron, I attached the component list depicted below.

📌 Component list of the Kyogre PCB:

*L_1, L_2 (Headers for XIAO ESP32C6)*

*A1 (Headers for Arduino Nano)*

*Mic1 (Fermion: I2S MEMS Microphone)*

*SSD1306 (Headers for SSD1306 OLED Display)*

*L1 (Headers for Bi-Directional Logic Level Converter)*

*SW1 (Micro Switch (JL024-2-026))*

*ULN2003 (Headers for 28BYJ-48 Stepper Motor)*

*R1 (20K Resistor)*

*R2 (220Ω Resistor)*

*C1, C2, C3, C4, K1 (6x6 Pushbutton)*

*D1 (5 mm Common Anode RGB LED)*

*J2 (Headers for Additional Stepper Motor Power Supply)*

*J1 (Power Jack)*

Since some components were tricky to solder due to the unique structure of the Kyogre PCB, I utilized the soldering station to hold the problematic parts.

![66](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_4.jpg)

![67](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_5.jpg)

![68](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_6.jpg)

![69](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_7.jpg)

![70](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_7.jpg)

After concluding soldering all components, I tested whether the Kyogre PCB operated as expected or was susceptible to electrical issues.

![71](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_8.jpg)

### Step 1.a.1: Making connections and adjustments on the Kyogre PCB

```
// Connections
// XIAO ESP32C6 :
//                                Fermion: I2S MEMS Microphone
// 3.3V    ------------------------ 3V3
// D1      ------------------------ WS (+20K)
// 3.3V    ------------------------ SEL
// D0      ------------------------ SCK
// D2      ------------------------ DO (+220Ω)
//                                SSD1306 OLED Display (128x64)
// D4/SDA  ------------------------ SDA
// D5/SCL  ------------------------ SCL
//                                Control Button (A)
// D8      ------------------------ +
//                                Control Button (B)
// D9      ------------------------ +
//                                Control Button (C)
// D10     ------------------------ +
//                                Control Button (D)
// D3      ------------------------ +
//                                Arduino Nano
// RX (D7) ------------------------ TX (D4)
// TX (D6) ------------------------ RX (D2)
&
&
&
// Connections
// Arduino Nano :
//                                28BYJ-48 Stepper Motor (w/ ULN2003)
// D8      ------------------------ IN1
// D9      ------------------------ IN2
// D10     ------------------------ IN3
// D11     ------------------------ IN4
//                                Micro Switch with Pulley (JL024-2-026)
// D12     ------------------------ +
//                                Home Button
// D7     ------------------------ +
//                                5mm Common Anode RGB LED
// D3      ------------------------ R
// D5      ------------------------ G
// D6      ------------------------ B
//                                XIAO ESP32C6
// RX (D2) ------------------------ TX (D6) 
// TX (D4) ------------------------ RX (D7)
```

:hash: Since [XIAO ESP32C6](https://wiki.seeedstudio.com/xiao_esp32c6_getting_started/) is a feature-rich development board providing an I2S port, I was able to connect a [Fermion I2S MEMS microphone](https://wiki.dfrobot.com/SKU_SEN0526_Fermion_I2S_MEMS_Microphone) to collect raw audio buffers easily. Nevertheless, after conducting some experiments, I noticed the produced audio buffers were noisy or completely inaccurate. Therefore, I added additional resistors to the WS (+20K) and DO (+220Ω) pins of the I2S microphone. Then, I managed to obtain precise raw audio buffers.

:hash: To provide the user with a feature-packed interface, I connected an SSD1306 OLED display and four control buttons to XIAO ESP32C6. I also connected an RGB LED to Arduino Nano to inform the user of the CNC router status while performing operations according to the CNC commands transferred by XIAO ESP32C6.

:hash: Since Arduino Nano operates at 5V and XIAO ESP32C6 requires 3.3V logic level voltage, their pins cannot be connected directly, even for serial communication. Therefore, I utilized a bi-directional logic level converter to shift the voltage for the connections between XIAO ESP32C6 and Arduino Nano.

:hash: To control the CNC router effortlessly, I connected a 28BYJ-48 stepper motor to Arduino Nano via its built-in ULN2003 driver module. Since I wanted to implement automatic homing sequence to the CNC router, I connected a micro switch with pulley (JL024-2-026) to Arduino Nano, similar to a 3D printer switch.

:hash: Since the 28BYJ-48 stepper motor can be current-demanding on full load, I connected an additional 5V battery to supply the stepper motor without damaging other components.

![72](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_sound_9.jpg)

## Step 1.b: Designing and soldering the Groudon-inspired PCB

Before prototyping my Groudon-inspired PCB design, I inspected the detailed pin reference of Particle Photon 2 and needed to prepare components requiring soldering for programming.

Then, I checked the wireless (Wi-Fi) and cloud communication quality between Photon 2, the Particle Cloud, and the web dashboard (application) while transferring and receiving data packets.

![73](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_thermal_1.jpg)

![74](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/breadboard_thermal_2.jpg)

I designed my Groudon-inspired PCB by utilizing Autodesk Fusion 360 and KiCad in tandem. Since I wanted to design a unique 3D-printed encasement to simplify the PCB integration to the custom CNC router (also 3D-printed) moving the thermal camera container head, I created the PCB outline (edge) on Fusion 360 and then imported the outline file (DXF) to KiCad. In this regard, I was able to design custom 3D parts compatible with the PCB outline precisely.

To replicate this malfunction detection device for water-cooled HVAC systems, you can download the Gerber file below or order the discussed PCB design directly from [my ELECROW community page](https://www.elecrow.com/share/sharepj/center/no/13accecfa8c56518d43f0f9ab46fe6f4).

![75](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_1.jpg)

![76](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_2.jpg)

![77](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_3.jpg)

By utilizing a TS100 soldering iron, I attached the component list depicted below.

📌 Component list of the Groudon PCB:

*Photon2 (Headers for Particle Photon 2)*

*MLX90641 (Headers for MLX90641 Thermal Imaging Camera)*

*ST7735 (Headers for ST7735 1.8" TFT Display)*

*U1 (COM-09032 Analog Joystick)*

*K1 (6x6 Pushbutton)*

*D1 (5 mm Common Anode RGB LED)*

*J1 (Power Jack)*

Since some components were tricky to solder due to the unique structure of the Groudon PCB, I utilized the soldering station to hold the problematic parts.

![78](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_4.jpg)

![79](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_5.jpg)

![80](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_6.jpg)

After concluding soldering all components, I tested whether the Groudon PCB operated as expected or was susceptible to electrical issues.

![81](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_7.jpg)

### Step 1.b.1: Making connections and adjustments on the Groudon PCB

```
// Connections
// Particle Photon 2 :  
//                                MLX90641 Thermal Imaging Camera (16x12 w/ 110° FOV)
// D1 / SCL   --------------------- SCL
// D0 / SDA   --------------------- SDA
//                                ST7735 1.8" Color TFT Display
// 3.3V --------------------------- LED
// D17 / SCK  --------------------- SCK
// D15 / MOSI --------------------- SDA
// D3   --------------------------- AO (DC)
// D4   --------------------------- RESET
// D2   --------------------------- CS
// GND  --------------------------- GND
// 3.3V --------------------------- VCC
//                                COM-09032 Analog Joystick
// A0   --------------------------- VRX
// A1   --------------------------- VRY
// D19  --------------------------- SW
//                                Control Button (OK)
// D9   --------------------------- +
//                                5mm Common Anode RGB LED
// D13  --------------------------- R
// D14  --------------------------- G
// D5   --------------------------- B
```

:hash: Since [Particle Photon 2](https://docs.particle.io/reference/datasheets/wi-fi/photon-2-datasheet/) is a capable IoT development board providing Particle Cloud compatibility out of the box, I was able to set up cloud variables and functions effortlessly to communicate with Photon 2 via the Particle Cloud API through the web dashboard.

:hash: To obtain accurate thermal scan (imaging) buffers, I connected [an MLX90641 thermal imaging camera](https://wiki.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array/) to Photon 2 via a Grove 4-pin connection cable. Since the MLX90641 camera produces 16x12 IR arrays (buffers) with fully calibrated 110° FOV (field-of-view), I was able to generate considerably large thermal images by combining four sequential buffers and adjusting pixel size.

:hash: Although Photon 2 is a powerful development board, it is not suitable for generating thermal images, saving image samples, and running a demanding visual anomaly detection model simultaneously due to memory limitations. Therefore, the web dashboard, hosted by LattePanda Mu, handles all of the mentioned operations after Photon 2 registers the produced thermal scan (imaging) buffers to the associated Particle Cloud variables.

:hash: To provide the user with a feature-rich interface, I connected an ST7735 TFT display and a COM-09032 analog joystick to Photon 2. I also added an RGB LED to inform the user of the device status while performing operations related to thermal buffer collection and registration.

![82](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/pcb_thermal_8.jpg)

## Step 2.a: Designing and printing the aluminum radiator mounts and the Kyogre PCB encasement

Since I focused on building a versatile and accessible AI-driven device that identifies the faulty cooling components via anomalous sound detection and diagnoses ensuing thermal cooling malfunctions via visual anomaly detection based on thermal images, I decided to design complementary 3D-printable parts that improve the robustness, compatibility, and capabilities of the device considering harsh operating conditions of industrial plants.

First, I wanted to fix the large aluminum radiator position and integrate the Kyogre PCB as close as possible to the radiator. Thus, I designed these parts:

- the main body of the right radiator mount,
- the main body of the left radiator mount,
- two tilted snap-fit joints perfectly sized for the radiator,
- four special legs (back and front) supporting the radiator mounts,
- the unique PCB encasement derived from the Kyogre PCB outline,
- the PCB encasement connector providing a buckle-shaped joint interlocking with the right radiator mount.

Furthermore, I decided to emboss the Seeed logo on the main body of the left radiator mount to highlight the qualifications of this segment of the AI-powered HVAC malfunction detection device.

I utilized Autodesk Fusion 360 to model all of the mentioned 3D-printable parts and test their clearances to print flawless joints. For further examination, you can download their STL files below.

![83](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_1.png)

![84](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_2.png)

![85](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_3.png)

![86](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_4.png)

![87](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_5.png)

![88](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_6.png)

![89](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_7.png)

![90](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_8.png)

![91](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_9.png)

![92](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_10.png)

![93](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_11.png)

![94](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_12.png)

After designing 3D models and exporting them as STL files, I sliced the exported models in PrusaSlicer, which provides lots of groundbreaking features such as paint-on supports and height range modifiers.

![95](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_13.png)

![96](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_14.png)

![97](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_15.png)

![98](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_16.png)

![99](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_17.png)

![100](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_18.png)

![101](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_19.png)

![102](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_sound_20.png)

Since I wanted to apply a unique industrial theme representing vivid industrial processes, I utilized this PLA filament:

- ePLA-Matte Tangerine

Finally, I printed all of the mentioned models with my Anycubic Kobra 2 3D Printer.

![103](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/printed_1.jpg)

### Step 2.a.1: Assembling the 3D-printed components

After printing all 3D models related to the aluminum radiator, I started to combine the radiator mount parts via M3 screws through the assembly-ready screw holes.

Then, I fastened the unique Kyogre PCB encasement to the complementary PCB connector via M3 screws. Since the PCB connector is compatible with the right radiator mount via its buckle-shaped snap-fit joint, I was able to interlock the PCB connector with the right mount body effortlessly.

Although I applied hot glue between parts while affixing them via M3 screws, it was still not enough to build a production-ready device, especially considering the harsh operating conditions of industrial HVAC systems. Thus, I employed a well-known injection molding technique to make the connections more sturdy. In this technique, a heat press mechanism is generally utilized to add threaded brass inserts between 3D-printed parts to connect them firmly. In my version, I simply used a soldering iron to embed M3 screws directly into the assembly-ready holes instead of threaded inserts to fasten the parts together.

![104](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_1.jpg)

![105](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_2.jpg)

![106](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_3.jpg)

![107](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_4.jpg)

![108](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_5.jpg)

![109](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_6.jpg)

![110](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_7.jpg)

![111](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_8.jpg)

![112](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_9.jpg)

![113](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_10.jpg)

![114](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_11.jpg)

As discussed earlier, I employed the soldering iron to embed M3 screws directly into the assembly-ready holes to affix parts tightly.

![115](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_12_injection.jpg)

![116](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_13.jpg)

![117](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_14.jpg)

![118](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_15.jpg)

![119](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_16.jpg)

![120](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_17.jpg)

![121](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_18.jpg)

![122](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_19.jpg)

After combining all the parts, I placed the aluminum radiator on the radiator mounts via their bracket-shaped snap-fit joints in order to test the strength of the mounts while carrying the radiator in a tilted position.

![123](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_sound_20_fit_test.jpg)

## Step 2.b: Designing and printing the CNC router moving the thermal camera and the Groudon PCB encasement

After modeling the 3D parts related to the aluminum radiator, I focused on designing a custom CNC router to move the thermal imaging camera to collect thermal scan (imaging) buffers from the predefined locations on the aluminum cooling blocks to produce an accurate thermal image. Also, I wanted to integrate the Groudon PCB as close as possible to the CNC router since the MLX90641 thermal imaging camera must be connected to Photon 2. Thus, I designed these parts:

- two chamfered CNC rods,
- the micro switch connector,
- two special pins for attaching GT2 20T pulleys,
- the left CNC stand providing slots for the CNC rods, the 28BYJ-48 stepper motor, the ULN2003 driver board, and the micro switch connector,
- the right CNC stand providing slots for the CNC rods and the GT2 20T pulley pins,
- the thermal camera container head providing holes to pass CNC rods and slots for the MLX90641 thermal imaging camera, GT2 timing belt, and aluminum gear clamps,
- the unique PCB encasement derived from the Groudon PCB outline,
- the PCB encasement connector providing a buckle-shaped joint interlocking with the right CNC stand while preventing any contact with the embedded GT2 20T pulley pins.

Furthermore, I decided to emboss the Elecrow logo and the Edge Impulse logo on the left and right CNC stands respectively to highlight the qualifications of this segment of the AI-powered HVAC malfunction detection device.

I utilized Autodesk Fusion 360 to model all of the mentioned 3D-printable parts and test their clearances to print flawless joints. For further examination, you can download their STL files below.

![124](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_1.png)

![125](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_2.png)

![126](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_3.png)

![127](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_4.png)

![128](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_5.png)

![129](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_6.png)

![130](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_7.png)

![131](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_8.png)

![132](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_9.png)

![133](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_10.png)

![134](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_11.png)

![135](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_12.png)

![136](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_13.png)

![137](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_14.png)

![138](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_15.png)

![139](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_16.png)

![140](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_17.png)

![141](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_18.png)

![142](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_19.png)

![143](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_20.png)

![144](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_21.png)

After designing 3D models and exporting them as STL files, I sliced the exported models in PrusaSlicer, which provides lots of groundbreaking features such as paint-on supports and height range modifiers.

![145](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_22.png)

![146](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_23.png)

![147](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_24.png)

![148](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_25.png)

![149](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_26.png)

![150](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_27.png)

![151](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_28.png)

![152](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_29.png)

![153](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_30.png)

![154](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_thermal_31.png)

Since I wanted to apply a unique industrial theme representing vivid industrial processes, I utilized this PLA filament contrasting with the previous filament color:

- ePLA-Matte Morandi Purple

Finally, I printed all of the mentioned models with my Anycubic Kobra 2 3D Printer.

![155](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/printed_2.jpg)

### Step 2.b.1: Assembling the 3D-printed components

After printing all 3D models related to the custom CNC router, I started to combine the CNC parts via M3 screws through the assembly-ready screw holes and the provided slots for the associated parts.

Then, I fastened the unique Groudon PCB encasement to the complementary PCB connector via M3 screws. Since the PCB connector is compatible with the right CNC stand via its buckle-shaped snap-fit joint and avoids any contact with the GT2 20T pulley pins, I was able to interlock the PCB connector with the right CNC stand effortlessly.

Although I applied hot glue between parts while affixing them via M3 screws, it was still not enough to build a production-ready device, especially for a constantly moving CNC router. Thus, I employed a well-known injection molding technique to make the connections more sturdy. In this technique, a heat press mechanism is generally utilized to add threaded brass inserts between 3D-printed parts to connect them firmly. In my version, I simply used a soldering iron to embed M3 screws directly into the assembly-ready holes instead of threaded inserts to fasten the parts together.

![156](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_1.jpg)

![157](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_2.jpg)

![158](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_3.jpg)

![159](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_4.jpg)

![160](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_5.jpg)

![161](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_6.jpg)

![162](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_7.jpg)

![163](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_8.jpg)

![164](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_9.jpg)

![165](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_10.jpg)

![166](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_11.jpg)

![167](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_12.jpg)

![168](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_13.jpg)

![169](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_14.jpg)

![170](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_15.jpg)

As discussed earlier, I employed the soldering iron to embed M3 screws directly into the assembly-ready holes to affix parts tightly.

For the parts with provided slots, I utilized the hot glue gun to reinforce the connections.

![171](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_16_injection.jpg)

![172](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_17.jpg)

![173](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_18.jpg)

![174](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_19.jpg)

Before finalizing all slot connections via the hot glue gun, I started to work on building the positioning mechanism of the CNC router by integrating these mechanical components into their corresponding slots:

- a 28BYJ-48 stepper motor,
- a ULN2003 driver board,
- a GT2 60T pulley attached to the stepper motor,
- two GT2 20T pulleys attached to the special pulley pins,
- GT2 6 mm timing belt,
- two GT2 aluminum gear clamps.

After affixing the timing belt via the gear clamps, I utilized two M3 screws to adjust the tightness of the timing belt.

![175](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_20_cnc.jpg)

![176](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_21_cnc.jpg)

![177](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_22_cnc.jpg)

![178](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_23_cnc.jpg)

![179](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_24_cnc.jpg)

![180](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_25_cnc.jpg)

![181](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_26_cnc.jpg)

![182](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_27_cnc.jpg)

![183](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_28_cnc.jpg)

![184](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_29_cnc.jpg)

![185](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_thermal_30_cnc.jpg)

## Step 2.c: Designing and printing the water-cooled HVAC system accessories

After modeling the 3D parts related to the custom CNC router, I realized that my overall design was still lacking some of the features I wanted to implement to build an industrial-level HVAC malfunction detection device, such as an impervious custom reservoir for the simplified water cooling system. Thus, I designed these additional parts:

- an aluminum cooling block holder allowing plastic tubing adjustment,
- an impermeable water reservoir compatible with the water cooling pump,
- a removable top cover for the reservoir with built-in plastic tubing fittings — IN and OUT,
- a custom case and a removable top cover for LattePanda Mu with the Lite Carrier board.

Furthermore, I decided to emboss the DFRobot logo and the project name on the top cover of the LattePanda Mu case to emphasize the qualifications of this segment of the AI-powered HVAC malfunction detection device.

I utilized Autodesk Fusion 360 to model all of the mentioned 3D-printable parts and test their clearances to print flawless joints. For further examination, you can download their STL files below.

![186](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_1.png)

![187](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_2.png)

![188](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_3.png)

![189](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_4.png)

![190](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_5.png)

![191](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_6.png)

![192](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_7.png)

![193](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_8.png)

![194](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_9.png)

![195](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_10.png)

After designing 3D models and exporting them as STL files, I sliced the exported models in PrusaSlicer, which provides lots of groundbreaking features such as paint-on supports and height range modifiers.

![196](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_11.png)

![197](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_12.png)

![198](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_13.png)

![199](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_14.png)

![200](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_15.png)

![201](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_16.png)

![202](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_17.png)

![203](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_18.png)

![204](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_19.png)

![205](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_HVAC_accessories_20.png)

Since I wanted to print pliable parts unsusceptible to water pressure and enclosing the Lite Carrier board perfectly, I utilized this TPU (flexible) filament:

- eTPU-95A Color Change by Temp

Thanks to this TPU filament's temperature-based color-changing ability, I was able to observe the current water temperature effortlessly while simulating thermal cooling malfunctions.

Finally, I printed all of the mentioned models with my Anycubic Kobra 2 3D Printer.

![206](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_all_parts_1.jpg)

### Step 2.c.1: Assembling the 3D-printed components

After printing all 3D models related to the additional features, I started to combine the components with their associated parts.

First, I installed the special heatsink, providing thermal paste, on LattePanda Mu and attached LattePanda Mu to the Lite Carrier board via the built-in connector (slot).

Since the Lite Carrier board does not support Wi-Fi connection out of the box, I connected an AC8265 wireless NIC module (WLAN expansion card) via the built-in M.2 E Key (2230).

![207](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/lattepanda_assembly_1.jpg)

![208](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/lattepanda_assembly_2.jpg)

![209](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/lattepanda_assembly_3.jpg)

Since the water reservoir does not need assembly, I simply placed its removable top cover. Then, I fastened the aluminum cooling blocks to their holders via the hot glue gun. Since the LattePanda Mu case is printed with a flexible filament, I was able to place the Lite Carrier board into the case effortlessly.

![210](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_1.jpg)

![211](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_2.jpg)

![212](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_3.jpg)

![213](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_4.jpg)

![214](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_5.jpg)

![215](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_6.jpg)

![216](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_7.jpg)

![217](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_8.jpg)

![218](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_9.jpg)

![219](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_10.jpg)

![220](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_11.jpg)

![221](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_12.jpg)

![222](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_13.jpg)

![223](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_accessories_14.jpg)

## Step 3: Setting up a simplified water-cooled HVAC system manifesting potential cooling malfunctions

As discussed earlier, I needed to build a simplified water-based HVAC system to construct data sets fulfilling the purpose of multi-model HVAC malfunction diagnosis and to conduct in-field model testing. Since I got heavily inspired by PC (computer) water cooling systems, I built my simplified system by utilizing these water cooling components, reminiscent of a closed-loop PC water cooling design:

- an aluminum water cooling radiator,
- two aluminum water cooling blocks (40 x 80 mm),
- a water cooling pump (4.8 W - 240 L/H),
- 10 mm plastic tubing (hose),
- three 120 mm case fans (RGB) compatible with the radiator.

As mentioned, I decided to model a 3D-printable water reservoir, including a removable top cover with built-in plastic tubing fittings — IN and OUT.

After concluding assembling all of the 3D-printed parts, I started to build the simplified water-based HVAC system.

![224](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/assembly_all_parts_2.jpg)

:hash: First, I attached 120 mm RGB case fans to the aluminum radiator via M3 screws and nuts.

![225](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_cooling_assembly_1.jpg)

![226](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_cooling_assembly_2.jpg)

:hash: Then, I attached a terminal input female DC barrel jack to the water pump and connected two aluminum cooling blocks via plastic tubing.

![227](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_cooling_assembly_3.jpg)

:hash: I created the closed-loop water cooling system by making connections via plastic tubing respectively: 

*Water Pump OUT ➜ Radiator IN ➜ Radiator OUT ➜ First Aluminum Block IN ➜ First Aluminum Block OUT ➜ Second Aluminum Block IN ➜ Second Aluminum Block OUT ➜ Custom Water Reservoir IN*

![228](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_cooling_assembly_4.jpg)

:hash: Finally, I fastened the water pump into the custom water reservoir and passed the cooling system IN and OUT tubings through the built-in plastic fittings on the reservoir top cover. Since I utilized TPU flexible filament to print the custom water cooling parts, I did not encounter any issues while connecting plastic tubings or circulating water through the system.

![229](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_cooling_assembly_5.jpg)

![230](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/water_cooling_assembly_6.jpg)

After completing the simplified closed-loop water cooling system, I started to work on combining PCBs, 3D parts, and the remaining components.

:hash: First, I attached the Kyogre PCB to its unique encasement affixed to the right radiator mount.

![231](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_1.jpg)

:hash: Then, I made the required connections between the ULN2003 driver board and the Kyogre PCB via jumper wires.

![232](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_2.jpg)

:hash: I fastened the micro switch (JL024-2-026) to its connector attached to the left CNC stand and made the required connections between the micro switch and the Kyogre PCB via jumper wires.

![233](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_3.jpg)

:hash: I attached the Groudon PCB to its unique encasement affixed to the right CNC stand.

![234](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_4.jpg)

:hash: I fastened the MLX90641 thermal imaging camera to its slot on the thermal camera container head via the hot glue gun. Then, I made the required connections between the thermal imaging camera and the Groudon PCB by extending the Grove 4-pin connection cable via jumper wires.

![235](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_5.jpg)

![236](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_6.jpg)

:hash: I attached the radiator to the radiator mounts in a tilted position and placed the aluminum cooling blocks under the custom CNC router, aligning the thermal imaging camera position.

![237](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_7.jpg)

![238](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_8.jpg)

:hash: While conducting experiments with the completed HVAC system, I noticed the custom reservoir started leaking after changing color. I assume the reason is that the color-changing additives in the TPU filament slightly distort the infill shape of the bottom of the 3D-printed reservoir. Thus, I employed a glass jar as the reservoir to replace the leaking one.

![239](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_9_faulty_part.jpg)

![240](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_10_faulty_part.jpg)

:hash: To showcase the web dashboard, I connected the CrowVision 11.6'' touchscreen module to LattePanda Mu via an HDMI to Mini-HDMI cable. Since I placed the Lite Carrier board into its custom flexible case, I did not encounter any issues while connecting peripherals to LattePanda Mu.

![241](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_11.jpg)

![242](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_12.jpg)

![243](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_13.jpg)

![244](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_14.jpg)

After concluding all of the mentioned assembly stages, I started to conduct experiments to simulate and detect HVAC system cooling malfunctions.

![245](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_15.jpg)

![246](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_16.jpg)

![247](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_17_completed.jpg)

## Step 4: Creating an account to utilize Twilio's SMS API

Since I decided to inform the user of the latest diagnosed cooling malfunctions via SMS after running the Audio MFE and visual anomaly detection models consecutively, I decided to utilize Twilio's SMS API. In this regard, I was also able to transfer the prediction date and the modified resulting image name for further inspection through the web dashboard (application).

[Twilio](https://www.twilio.com/docs/messaging/quickstart/php) provides a trial text messaging service to transfer an SMS from a virtual phone number to a verified phone number internationally. Also, Twilio supports official helper libraries for different programming languages, including PHP, enforcing its suite of APIs.

:hash: First of all, sign up for [Twilio](https://www.twilio.com/try-twilio) and navigate to the *Account* page to utilize the default (first) account or create a new account.

I noticed that creating free subsidiary accounts (projects) more than once may lead to the permanent suspension of a Twilio user account. So, I recommend using the default trial account or a previously created account if you have multiple iterations or did not subscribe to a paid plan.

![248](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_1.png)

![249](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_2.png)

:hash: After verifying a phone number for the selected account (project), set the initial account settings for SMS in PHP.

![250](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_3.png)

:hash: To configure the SMS settings, go to *Messaging ➡ Send an SMS*.

:hash: Since a virtual phone number is required to transfer an SMS via Twilio, click *Get a Twilio number*.

![251](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_4.png)

Since Twilio provides a free 10DLC virtual phone number for each trial account, Twilio allows the user to utilize the text messaging service immediately after activating the given virtual phone number.

:hash: After obtaining the free virtual phone number, download the [Twilio PHP Helper Library](https://github.com/twilio/twilio-php) to send an SMS via the web dashboard.

![252](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_5.png)

:hash: Finally, go to *Geo permissions* to adjust the allowed recipients depending on your region.

![253](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_6.png)

:hash: After configuring the required settings, go to *Account ➡ API keys & tokens* to get the account SID and the auth token under *Live credentials* to be able to employ Twilio's SMS API to send SMS.

![254](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_set_7.png)

## Step 5.0: Setting up the XAMPP application and the required Python modules on LattePanda Mu (Ubuntu 22.04)

Before starting to develop the web dashboard (application), I needed to configure the required software and Python modules on LattePanda Mu to be able to host the web dashboard, produce thermal images for data collection, and run the FOMO-AD visual anomaly detection model.

Since the web dashboard heavily relies on Python modules, especially for running the FOMO-AD model via the Edge Impulse Linux Python SDK, I set up [Ubuntu](https://docs.lattepanda.com/content/3rd_delta_edition/Operating_Systems_Ubuntu/) as the operating system for LattePanda Mu. As I was working on this device, Ubuntu 22.04 was officially supported by LattePanda Mu. You can inspect the prioritized operating system versions [here](https://docs.lattepanda.com/content/mu_edition/os_compatible/).

Plausibly, the XAMPP application provides an official Linux installer. So, creating a local server with a MariaDB database to host the web dashboard (application) on LattePanda Mu becomes straightforward and effortless.

:hash: First, download [the XAMPP Linux installer](https://www.apachefriends.org/download.html).

:hash: After downloading the XAMPP installer, change its permissions via the terminal (command line).  

*sudo chmod 755 /home/kutluhan/Downloads/xampp-linux-x64-8.2.12-0-installer.run*

![255](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xampp_set_1.png)

:hash: Then, execute the XAMPP installer via the terminal.

*sudo /home/kutluhan/Downloads/xampp-linux-x64-8.2.12-0-installer.run*

![256](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xampp_set_2.png)

![257](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xampp_set_3.png)

:hash: After configuring the required settings via the installer, run the XAMPP application (lampp) via the terminal.

*sudo /opt/lampp/manager-linux-x64.run*

:hash: Since the XAMPP development environment does not create a shortcut on Linux, you always need to use the terminal to launch XAMPP (lampp) unless you enable autostart.

![258](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xampp_set_4.png)

![259](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xampp_set_5.png)

After installing and setting up the XAMPP application (lampp) on LattePanda Mu, I needed to configure some settings to make the web dashboard (application) access the terminal and execute Python scripts.

:hash: First, create the web application folder under the lampp folder and change its permissions via the terminal to be able to generate, open, and save files.

*sudo chmod -R 777 /opt/lampp/htdocs/HVAC_malfunction_diagnosis_dashboard*

![260](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_set_1.png)

However, even after changing the permissions, the web application cannot access the terminal and utilize the sudo command required to execute necessary Python scripts with the root user (super-user) privileges.

Although assigning super-user privileges to different users is a security risk, I decided to give the web application the ability to access the terminal with root user privileges. In this case, it was applicable since the XAMPP application is only operating as a local development environment.

:hash: Since we need to edit the *sudoers* file to change user privileges, open the terminal and utilize the *visudo* command to alter the *sudoers* file safely.

*sudo visudo*

:hash: Since the XAMPP application (lampp) employs *daemon* as the user name, add these lines to the end of the *sudoers* file to enable the web application to run the sudo command without requiring a password.

```
# Disable sudo password.
&lt;_username_> ALL=(ALL) NOPASSWD: ALL
daemon ALL=(ALL) NOPASSWD: ALL
```

![261](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_set_2.png)

After configuring the required permissions and privileges for the web application, I needed to install the necessary Python modules.

:hash: First, install the OpenCV module required to generate and modify thermal images.

*sudo apt-get install python3-opencv*

![262](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/module_set_1.png)

:hash: To run Edge Impulse machine learning models on LattePanda Mu, install [the Edge Impulse Linux Python SDK](https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux/linux-python-sdk) via the terminal.

*sudo pip3 install edge_impulse_linux*

*sudo apt-get install python3-pyaudio*

![263](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/module_set_2.png)

![264](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/module_set_3.png)

## Step 5: Developing a feature-rich web application to communicate w/ the Particle Cloud and process requests from XIAO ESP32C6

As discussed earlier, I decided to develop a versatile web dashboard (application) to improve the user experience and run essential device features, including but not limited to executing Python scripts.

Since the web application features interconnect with data collection and model running procedures executed by different development boards, please refer to the web application code files or the following steps focusing on the device qualifications to review all of the web application capabilities thoroughly.

As shown below, the web application consists of seven folders and nine code files in various programming languages:

- /assets
  - class.php
  - dashboard_updates.php
  - index.css
  - index.js
  - Particle_cloud_connection.php
- /generate_thermal_img
  - /img_detection
  - /img_sample
  - generate_thermal_image_and_run_model.py	
- /model
- /sample_audio_files
  - /files
  - convert_raw_to_wav.py
  - save_audio_sample.php	
- index.php

![265](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_struct_1.png)

![266](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_struct_2.png)

![267](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_struct_3.png)

![268](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_struct_4.png)

![269](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_struct_5.png)

📁 *class.php*

To bundle all functions under a specific structure, I created a class named *dashboard*. Please refer to the following steps to inspect all interconnected device features.

⭐ Define the required configurations to communicate with Photon 2 via the Particle Device Cloud API.

⭐ In the *__init__* function:

⭐ Define the Twilio account credentials and required settings.

```
	public function __init__($conn){
		$this->conn = $conn;
		// Define the Twilio account credentials and object.
		$_sid    = "&lt;__SID__>";
        $token  = "&lt;__ACCESS_TOKEN__>";
        $this->twilio = new Client($_sid, $token);
		// Define the user and the Twilio-verified phone numbers.
		$this->user_phone = "+____________";
		$this->from_phone = "+____________";	
	}
```

⭐ In the *append_log_update* function:

⭐ Insert a new system log update regarding data collection or model inference results into the *system_log* MariaDB database table.

```
	public function append_log_update($type, $category, $class, $date, $info){
		// Insert new system log updates (sample collections or model inference results) into the system_log MariaDB database table.
		$sql = "INSERT INTO `$this->table` (`type`, `category`, `class`, `date`, `info`)
		        VALUES ('$type', '$category', '$class', '$date', '$info')";
	    mysqli_query($this->conn, $sql);
	}
```

⭐ In the *optain_modify_log_updates* function:

⭐ Fetch all system log updates registered on the *system_log* database table.

⭐ According to the given log category, modify the obtained information to generate HTML elements for each system log update.

⭐ While generating HTML elements for the retrieved log updates, append each HTML element to an array so as to create a thorough index.

⭐ Finally, return the produced HTML element index (list).

⭐ If there is no registered system log update in the database table, return the default HTML element index.

```
	public function optain_modify_log_updates(){
		$generated_html_elements = [];
		// Obtain all system log updates registered on the MariaDB database table — system_log.
		$sql = "SELECT * FROM `$this->table` ORDER BY `id` DESC";
		$result = mysqli_query($this->conn, $sql);
		$check = mysqli_num_rows($result);
		if($check > 0){
			while($row = mysqli_fetch_assoc($result)){
				$html_element = '';
				// Modify the fetched log updates as HTML elements according to the passed log category.
				if($row["type"] == "thermal_img" && $row["category"] == "detection"){
					$is_cooling_malfunction = ($row["class"] == "malfunction") ? '&lt;p>&lt;i class="fa-solid fa-triangle-exclamation">&lt;/i> Cooling Malfunction Detected!&lt;/p>' : '&lt;p>&lt;i class="fa-solid fa-circle-check">&lt;/i> Cooling Status is Stable!&lt;/p>';
					$html_element = '
										&lt;section class="t_detection">
										&lt;img src="generate_thermal_img/img_detection/'.$row["info"].'" />
										&lt;h2>&lt;i class="fa-regular fa-image">&lt;/i> Thermal Image&lt;/h2>
										&lt;p>&lt;i class="fa-solid fa-circle-info">&lt;/i> Malfunction Diagnosis&lt;/p>
										&lt;p>&lt;i class="fa-solid fa-triangle-exclamation">&lt;/i> Anamolous Sound Detected!&lt;/p>
										'.$is_cooling_malfunction.'
										&lt;p>&lt;i class="fa-regular fa-clock">&lt;/i> '.$row["date"].'&lt;/p>
										&lt;div class="overlay thermal_detect">&lt;a href="generate_thermal_img/img_detection/'.$row["info"].'" download>&lt;button>&lt;i class="fa-solid fa-cloud-arrow-down">&lt;/i>&lt;/button>&lt;/a>&lt;/div>
										&lt;/section>
					                ';
				}else if($row["type"] == "thermal_img" && $row["category"] == "sample"){
					$html_element = '
										&lt;section class="t_sample">
										&lt;img src="generate_thermal_img/img_sample/'.$row["info"].'" />
										&lt;h2>&lt;i class="fa-regular fa-image">&lt;/i> Thermal Image&lt;/h2>
										&lt;p>&lt;i class="fa-solid fa-circle-info">&lt;/i> Sample Collection&lt;/p>
										&lt;p>&lt;i class="fa-regular fa-clock">&lt;/i> '.$row["date"].'&lt;/p>
										&lt;div class="overlay thermal_sample">&lt;a href="generate_thermal_img/img_sample/'.$row["info"].'" download>&lt;button>&lt;i class="fa-solid fa-cloud-arrow-down">&lt;/i>&lt;/button>&lt;/a>&lt;/div>
										&lt;/section>
					                ';					
				}else if($row["type"] == "audio_file"){
					$html_element = '
										&lt;section class="a_sample">
										&lt;img src="assets/audio_icon.jpg" />
										&lt;h2>&lt;i class="fa-solid fa-music">&lt;/i> Anamolous Sound&lt;/h2>
										&lt;p>&lt;i class="fa-solid fa-circle-info">&lt;/i> Sample Collection&lt;/p>
										&lt;p>&lt;i class="fa-solid fa-volume-high">&lt;/i> Class: '.$row["class"].'&lt;/p>
										&lt;p>&lt;i class="fa-regular fa-clock">&lt;/i> '.$row["date"].'&lt;/p>
										&lt;div class="overlay audio_sample">&lt;a href="sample_audio_files/files/'.$row["info"].'" download>&lt;button>&lt;i class="fa-solid fa-cloud-arrow-down">&lt;/i>&lt;/button>&lt;/a>&lt;/div>
										&lt;/section>
					                ';						
				}
				// Append the most recently modified HTML element to the associated main element array so as to create a list of the generated HTML elements.
				array_push($generated_html_elements, $html_element);
			}
			// Finally, return the generated HTML element list (array).
			return $generated_html_elements;
		}else{
			return '
						&lt;section>&lt;img src="assets/database_empty.jpg" />&lt;h2>There are no system log updates on the database yet.&lt;/h2>&lt;/section>
						&lt;section>&lt;img src="assets/database_empty.jpg" />&lt;h2>There are no system log updates on the database yet.&lt;/h2>&lt;/section>
						&lt;section>&lt;img src="assets/database_empty.jpg" />&lt;h2>There are no system log updates on the database yet.&lt;/h2>&lt;/section>
						&lt;section>&lt;img src="assets/database_empty.jpg" />&lt;h2>There are no system log updates on the database yet.&lt;/h2>&lt;/section>
						&lt;section>&lt;img src="assets/database_empty.jpg" />&lt;h2>There are no system log updates on the database yet.&lt;/h2>&lt;/section>
						&lt;section>&lt;img src="assets/database_empty.jpg" />&lt;h2>There are no system log updates on the database yet.&lt;/h2>&lt;/section>
				   ';
		}		
	}
```

⭐ In the *particle_register_parameter* function:

⭐ Define the authorization configurations and cloud function arguments (POST data parameters) required by the Particle Cloud API.

⭐ By making a cURL call (POST request), employ the Particle Cloud API to make Photon 2 collect a thermal scan (imaging) buffer and register the collected buffer to the Particle Cloud.

```
    public function particle_register_parameter($variable){
		// Define the required authorization configurations and function arguments (POST data parameters).
		$data = "access_token=".$this->Particle["access_token"]."&args=".$variable;
		// By making a cURL call (POST request), communicate with the Particle Cloud API to activate the given Cloud function on Photon 2.
		$url = $this->Particle["API"].$this->Particle["device_id"].$this->Particle["_function"];
		$curl = curl_init();
		curl_setopt($curl, CURLOPT_POST, 1);
		curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
		curl_setopt($curl, CURLOPT_URL, $url);
		//curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
		// Execute the defined cURL call.
		$result = curl_exec($curl);
		if(!$result){ echo "Particle Cloud API => Connection Failed!"; }
		else{ echo "Particle Cloud API => Connection Successful!"; }
        curl_close($curl);
	}
```

⭐ In the *particle_obtain_parameter* function:

⭐ By making a cURL call (GET request), employ the Particle Cloud API to obtain information regarding the passed Cloud variable registered by Photon 2.

⭐ If the Cloud response is successful, decode the received JSON data packet to fetch the given Cloud variable value. Then, return the obtained value.

```
    public function particle_obtain_parameter($variable){
		// By making a cURL call (GET request), communicate with the Particle Cloud API to obtain the variables registered by Photon 2.
		$url = $this->Particle["API"].$this->Particle["device_id"].$this->Particle["variables"][$variable-1]
		       ."?access_token=".$this->Particle["access_token"];
		$curl = curl_init();
		curl_setopt($curl, CURLOPT_URL, $url);
		curl_setopt($curl, CURLOPT_HEADER, false);
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
		// Execute the defined cURL call.
		$result = curl_exec($curl);
		if(!$result){ return "Particle Cloud API => Connection Failed!"; }
		// If the Cloud connection is successful, decode the received JSON data packet to obtain the registered value of the passed variable. Then, return the obtained value.
		else{
			$data_packet = json_decode($result);
			return $data_packet->result;
		}
        curl_close($curl);
	}
```

⭐ In the *particle_generate_thermal_image_from_buffers* function:

⭐ Obtain all thermal scan (imaging) buffers registered by Photon 2 individually from the Particle Cloud.

⭐ Then, generate a precise thermal image from the fetched buffers by executing a Python script — *generate_thermal_image_and_run_model.py*.

⭐ According to the passed process type, save the produced image as a sample directly or run an inference with the Edge Impulse FOMO-AD model via the same Python script.

⭐ Finally, return the response transferred by the executed Python script.

Since the web application executes the given Python script via the *shell_exec* function, it is not possible to observe debugging errors like using the terminal. Thus, I appended *2>&1* to the command line in the *shell_exec* function to display debugging errors on the browser directly. In this regard, I was able to develop the web application way faster.

```
    public function particle_generate_thermal_image_from_buffers($process_type){
		// Obtain thermal imaging buffers registered on the Particle Cloud.
		$thermal_buffers = [];
		for($i=0; $i&lt;count($this->Particle["variables"]); $i++){
			$thermal_buffers[$i] = $this->particle_obtain_parameter($i+1);
		}
		// Generate and save a thermal image from the given buffers by executing the generate_thermal_image_and_run_model.py file.
		// As executing the Python script, transmit the obtained thermal buffers and the given process type as Python Arguments.
		$path = str_replace("/assets", "/generate_thermal_img", dirname(__FILE__));
		$arguments = '--buff_1='.$thermal_buffers[0].' --buff_2='.$thermal_buffers[1].' --buff_3='.$thermal_buffers[2].' --buff_4='.$thermal_buffers[3].' --process='.$process_type;
		$run_Python = shell_exec('sudo python3 "'.$path.'/generate_thermal_image_and_run_model.py" '.$arguments.' 2>&1'); // Add 2>&1 for debugging errors directly on the browser.
		// If the passed process type is detection, obtain and return the detected thermal cooling malfunction class after running the FOMO-AD (visual anomaly detection) model via the Python script.
		// Otherwise, obtain the default sample collection response.
		return $run_Python;
	}
```

⭐ In the *Twilio_send_SMS* function:

⭐ Via the Twilio SMS API, send an SMS from the Twilio virtual phone number to the registered (user) phone number to transfer the given text message.

```
	public function Twilio_send_SMS($body){
		// Configure the SMS object.
        $sms_message = $this->twilio->messages
			->create($this->user_phone,
				array(
					   "from" => $this->from_phone,
                       "body" => $body
                     )
                );
		// Send the SMS.
		echo("SMS SID: ".$sms_message->sid);	  
	}		
```

⭐ Define the required MariaDB database configurations for LattePanda Mu.

```
$server = array(
	"server" => "localhost",
	"username" => "root",
	"password" => "",
	"database" => "hvac_system_updates"
);

$conn = mysqli_connect($server["server"], $server["username"], $server["password"], $server["database"]);
```

📁 *Particle_cloud_connection.php*

⭐ Include the *class.php* file and define the *dashboard* object of the *dashboard* class.

```
include_once "class.php";

// Define the dashboard object of the dashboard class.
$dashboard = new dashboard();
$dashboard->__init__($conn);
```

⭐ If requested via HTTP GET request, communicate with the Particle Cloud to obtain the value of the passed Cloud variable (individually) registered by Photon 2 and return the fetched value.

```
if(isset($_GET["obtain_particle_cloud_variable"])){
	$variable_value = $dashboard->particle_obtain_parameter($_GET["obtain_particle_cloud_variable"]);
	echo $variable_value;
}
```

⭐ If requested via HTTP GET request, communicate with the Particle Cloud in order to make Photon 2 collect a thermal imaging buffer and register the collected buffer to the passed Cloud variable.

```
if(isset($_GET["collect_particle_cloud_variable"])){
	$dashboard->particle_register_parameter($_GET["collect_particle_cloud_variable"]);
}
```

⭐ If requested via HTTP GET request:

⭐ Communicate with the Particle Cloud to obtain all thermal imaging buffers registered by Photon 2.

⭐ Generate a thermal image from the obtained buffers by executing a Python script — *generate_thermal_image_and_run_model.py*.

⭐ According to the passed process type (sample or detection), save the generated image as a sample or run an inference with the Edge Impulse FOMO-AD (visual anomaly detection) model via the same Python script.

⭐ Then, decode the response generated by the Python script to obtain the image tag (default sample or detected label) and the creation date.

⭐ After producing the thermal image and conducting the given process type successfully, update the system log on the MariaDB database accordingly.

⭐ Finally, depending on the process type, send an SMS via Twilio to inform the user of the latest system log update regarding cooling status.

```
if(isset($_GET["generate_cloud_thermal_image"])){
	// Generate the thermal image from the obtained (Cloud-registered) buffers.
	// If the passed process type is detection, run an inference with the Edge Impulse FOMO-AD (visual anomaly detection) model on LattePanda Mu via the same Python script.
	// Then, depending on the passed process type, obtain the response generated by the Python script.
	$python_response = $dashboard->particle_generate_thermal_image_from_buffers($_GET["generate_cloud_thermal_image"]);
	// Decode the Python script response to obtain the image tag (sample or detected label) and the creation date. 
	$img_tag = explode(":", $python_response)[0];
	$date = explode(":", $python_response)[1];
	$info = $img_tag."__".$date.".jpg";
	// After generating and saving the thermal image successfully, update the system log on the MariaDB database accordingly.
	$dashboard->append_log_update("thermal_img", $_GET["generate_cloud_thermal_image"], $img_tag, $date, $info);
	// Finally, send an SMS via Twilio to inform the user of the latest system log update regarding cooling status.
	if($_GET["generate_cloud_thermal_image"] == "detection"){
		$is_cooling_malfunction = ($img_tag == "malfunction") ? "⚠️ Cooling Malfunction Detected!" : "✅ Cooling Status is Stable!";
		$message_body = "❄️ Malfunction Diagnosis ❄️"
						."\n\r\n\r⚠️ Anamolous Sound Detected!\n\r\n\r"
						.$is_cooling_malfunction
						."\n\r\n\r⏰ Date: ".$date
						."\n\r📁 🖼️ ".$info
						."\n\r\n\r💻 Please refer to the web dashboard to inspect all system log updates!"
						."\n\r\n\r🌐 http://192.168.1.21/HVAC_malfunction_diagnosis_dashboard/\n\r\n\r";
        $dashboard->Twilio_send_SMS($message_body);
	}
}
```

📁 *dashboard_updates.php*

⭐ Include the *class.php* file and define the *dashboard* object of the *dashboard* class.

```
include_once "class.php";

// Define the dashboard object of the dashboard class.
$dashboard = new dashboard();
$dashboard->__init__($conn);
```

⭐ If requested via HTTP GET request:

⭐ Retrieve all of the system log updates on the MariaDB database table — system_log.

⭐ According to the given log category, modify the obtained information to generate HTML elements for each system log update.

⭐ Then, create a JSON object from the produced HTML element index (list).

⭐ Finally, return the recently generated JSON object.

```
if(isset($_GET["new_update"])){
	$generated_html_elements = $dashboard->optain_modify_log_updates();
	
	// Create a JSON object from the generated HTML elements.
	$data = array("generated_html_elements" => $generated_html_elements);
	$j_data = json_encode($data);
    
	// Return the recently generated JSON object.
	echo($j_data);
}
```

📁 *save_audio_sample.php*

⭐ Include the *class.php* file and define the *dashboard* object of the *dashboard* class.

```
include_once "../assets/class.php";

// Define the dashboard object of the dashboard class.
$dashboard = new dashboard();
$dashboard->__init__($conn);
```

⭐ Define the text file name for the received raw audio buffer (I2S).

⭐ If XIAO ESP32C6 transfers the selected audio class name via a GET (URL) parameter, modify the text file name accordingly.

```
# Get the current date and time.
$date = date("Y_m_d_H_i_s");

# Define the text file name of the received raw audio buffer (I2S).
$txt_file = "audio_%s__".$date;

// If XIAO ESP32C6 transfers the raw audio buffer (data) with the selected audio class, save the received buffer as a text (TXT) file and modify the file name accordingly. 
if(isset($_GET["audio"]) && isset($_GET["class"])){
	$txt_file = sprintf($txt_file, $_GET["class"]);
}
```

⭐ If XIAO ESP32C6 transfers the collected raw audio buffer (I2S) via an HTTP POST request:

⭐ Save the received audio buffer to the defined text (TXT) file.

⭐ Then, convert the recently saved raw audio buffer (TXT file) to a WAV audio file by executing a Python script — *convert_raw_to_wav.py*.

⭐ As executing the Python script, transmit the required audio conversion parameters for the Fermion I2S MEMS microphone as Python Arguments.

⭐ After generating the WAV audio file from the raw audio buffer, remove the converted text file from the server.

⭐ After completing the audio conversion process successfully, update the system log on the MariaDB database accordingly.

Since the web application executes the given Python script via the *shell_exec* function, it is not possible to observe debugging errors like using the terminal. Thus, I appended *2>&1* to the command line in the *shell_exec* function to display debugging errors on the browser directly. In this regard, I was able to develop the web application way faster.

```
if(!empty($_FILES["audio_sample"]["name"])){
	// Text File:
	$received_buffer_properties = array(
	    "name" => $_FILES["audio_sample"]["name"],
	    "tmp_name" => $_FILES["audio_sample"]["tmp_name"],
		"size" => $_FILES["audio_sample"]["size"],
		"extension" => pathinfo($_FILES["audio_sample"]["name"], PATHINFO_EXTENSION)
	);
    // Check whether the uploaded file's extension is in the allowed file formats.
	$allowed_formats = array('jpg', 'png', 'bmp', 'txt');
	if(!in_array($received_buffer_properties["extension"], $allowed_formats)){
		echo "FILE => File Format Not Allowed!";
	}else{
		// Check whether the uploaded file size exceeds the 5 MB data limit.
		if($received_buffer_properties["size"] > 5000000){
			echo "FILE => File size cannot exceed 5MB!";
		}else{
			// Save the uploaded file (TXT).
			move_uploaded_file($received_buffer_properties["tmp_name"], "./".$txt_file.".".$received_buffer_properties["extension"]);
			echo "FILE => Saved Successfully!";
		}
	}
	// Convert the recently saved raw audio buffer (TXT file) to a WAV audio file by executing a Python script — convert_raw_to_wav.py.
	// As executing the Python script, transmit the required audio conversion parameters for the Fermion I2S MEMS microphone as Python Arguments.
	$path = dirname(__FILE__);
	$arguments = '--nchannels=2 --sampwidth=2 --framerate=22000';
	$run_Python = shell_exec('sudo python3 "'.$path.'/convert_raw_to_wav.py" '.$arguments.' 2>&1'); // Add 2>&1 for debugging errors directly on the browser.
	// After generating the WAV audio file from the raw audio buffer, remove the converted text file from the server.
	if(file_exists("./".$txt_file.".txt")) unlink("./".$txt_file.".txt");
	// After completing the audio conversion process successfully, update the system log on the MariaDB database accordingly.
	$dashboard->append_log_update("audio_file", "sample", $_GET["class"], $date, $txt_file.".wav");
}
```

📁 *index.js*

⭐ Utilizing the *setInterval* function, every 5 seconds, make an HTTP GET request to the *dashboard_updates.php* file to:

⭐ Retrieve the HTML element index (list) as a JSON object generated from the system log updates registered on the MariaDB database table.

⭐ Decode the obtained JSON object.

⭐ Pass the fetched HTML elements (sections) to the web dashboard home (index) page automatically.

⭐ According to the given display category option, show the associated elements only on the index page.

```
setInterval(function(){
	$.ajax({
		url: "./assets/dashboard_updates.php?new_update",
		type: "GET",
		success: (response) => {
			// Decode the obtained JSON object.
			const data = JSON.parse(response);
			// Assign the fetched HTML elements (sections) as the most recent system log updates to the web dashboard home (index) page.
			$(".log_updates").html(data.generated_html_elements);
			// According to the passed display option, show the associated system log updates on the dashboard — home page.
			if(current_display_option == 1){ $(".t_sample").hide(); $(".a_sample").hide(); }
			if(current_display_option == 2){ $(".t_detection").hide(); $(".a_sample").hide(); }
			if(current_display_option == 3){ $(".t_detection").hide(); $(".t_sample").hide(); }
		}
	});
}, 5000);
```

⭐ According to the clicked horizontal menu button, change the display category option and the clicked button's appearance by toggling classes.

```
var current_display_option = -1; 
$(".category_menu").on("click", "button", event => {
	$(".category_menu button").removeClass("active");
	$(event.target).addClass("active");
	current_display_option = event.target.id;
});
```

📁 You can inspect *index.php* and *index.css* files below, which are for designing the web dashboard home (index) page.  

![270](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_1.png)

![271](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_2.png)

![272](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_3.png)

![273](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_4.png)

![274](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_5.png)

![275](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_6.png)

![276](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_7.png)

![277](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_8.png)

![278](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_9.png)

![279](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_10.png)

## Step 5.1: Converting the raw audio buffers transferred by XIAO ESP32C6 via POST requests to WAV files and transmitting the required conversion parameters as Python Arguments

As explained earlier, I needed to convert the raw audio buffers transferred by XIAO ESP32C6 to WAV audio files in order to save compatible audio samples for Edge Impulse. Therefore, I programmed a simple Python script to perform the audio conversion process.

Since Python scripts can obtain parameters as Python Arguments from the terminal (shell) directly, the web dashboard (application) passes the required audio conversion variables effortlessly.

📁 *convert_raw_to_wav.py*

⭐ Include the required modules.

```
import argparse
from glob import glob
import wave
import os
from time import sleep
```

⭐ Obtain and decode audio conversion parameters transferred by the web dashboard as Python Arguments.

⭐ Get all text (.txt) files consisting of raw audio buffers (I2S) transferred by XIAO ESP32C6.

⭐ Then, open each text file to convert the stored raw audio buffers to WAV audio files and save the produced WAV audio samples to the *files* folder.

```
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--nchannels", required=True, help="number of audio channels (1 for mono, 2 for stereo)")
    parser.add_argument("--sampwidth", required=True, help="sample width in bytes")
    parser.add_argument("--framerate", required=True, help="sampling frequency")
    args = parser.parse_args()
    nchannels = int(args.nchannels)
    sampwidth = int(args.sampwidth)
    framerate = int(args.framerate)
    # List all raw audio buffers (I2S) transferred by XIAO ESP32C6 as text (.txt) files.
    path = str(os.path.dirname(os.path.realpath(__file__)))
    buffers = glob(path + "/*.txt")
    # Then, convert the passed raw audio buffers generated by XIAO ESP32C6 (via the I2S microphone) to WAV audio files.
    for buf in buffers:
        with open(buf, "rb") as input_buf:
            raw_buffer = input_buf.read()
            file_name = buf.replace('sample_audio_files/', 'sample_audio_files/files/').replace('.txt', '.wav')
            with wave.open(file_name, "wb") as audio_file:
                audio_file.setnchannels(nchannels)
                audio_file.setsampwidth(sampwidth)
                audio_file.setframerate(framerate)
                audio_file.writeframesraw(raw_buffer)
```

![280](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_python_0.png)

## Step 5.2: Transferring the thermal scan (imaging) buffers obtained from the Particle Cloud as Python Arguments to generate a precise thermal image

As discussed earlier, Photon 2 is not suitable for generating thermal images, saving image samples, and running a demanding visual anomaly detection model simultaneously due to memory limitations. Therefore, I utilized the web dashboard to obtain the thermal scan (imaging) buffers registered on the Particle Cloud and programmed a Python script to perform the mentioned processes.

Since Python scripts can obtain parameters as Python Arguments from the terminal (shell) directly, the web dashboard (application) passes the obtained thermal imaging buffers and the given process type effortlessly.

📁 *generate_thermal_image_and_run_model.py*

To bundle all functions under a specific structure, I created a class named *thermal_img*. Please refer to the following steps to inspect all interconnected device features.

⭐ Include the required modules.

```
import cv2
import numpy
from edge_impulse_linux.image import ImageImpulseRunner
import argparse
import os
import datetime
from time import sleep
```

⭐ In the *__init__* function:

⭐ Get the absolute folder path to avoid errors while running this script via the web dashboard (application).

⭐ Define the required configurations to run the Edge Impulse FOMO-AD visual anomaly detection model converted to a Linux (x86_64) application (.eim).

⭐ Define the required variables to generate a thermal image from the given thermal scan (imaging) buffers, including the template (blank) image.

```
    def __init__(self, model_file):
        # Get the absolute folder path to avoid errors while running this script via the web dashboard (application).
        self.path = str(os.path.dirname(os.path.realpath(__file__)))
        # Define the required configurations to run the Edge Impulse FOMO-AD (visual anomaly detection) model.
        self.model_file = os.path.join(self.path, model_file).replace("/generate_thermal_img", "")
        self.threshold = 5
        self.detected_class = ""
        self.__debug = False
        # Define the required variables to generate a thermal image from the given thermal scan (imaging) buffers.
        self.t_img = {"w": 192, "h": 192, "p_w": 6, "p_h": 8, "temp_img": self.path+"/thermal_template.jpg"}
        self.thermal_buff_width = 16
        self.thermal_buff_height = 12
```

⭐ In the *generate_thermal_img* function:

⭐ Open and read the template (blank) image (192 x 192) via the built-in OpenCV function — *imread*.

⭐ Since the MLX90641 thermal imaging camera produces 16x12 IR arrays (buffers), I decided to set the pixel width as six (6) and the pixel height as eight (8) to fill the template image completely with four sequential buffers.

⭐ For each passed thermal imaging buffer ((16x12) x 4):

⭐ Define the coordinates for the first pixel.

⭐ Starting with the first pixel, draw each individual data point with the color indicator on the template image to generate a precise thermal image, estimated by the specific color algorithm based on the temperature ranges defined on Photon 2.

⭐ Note: Indicators are defined in the BGR format.

⭐ After drawing a pixel successfully, update the successive data point coordinates.

⭐ After generating the thermal image from the given buffers, store the modified template frame before saving an image file.

```
    def generate_thermal_img(self, thermal_buff):
        # Get the template (blank) thermal image (192 x 192).
        template = cv2.imread(self.t_img["temp_img"])
        # Generate the thermal image from the given buffers ((16x12) x 4).
        p_num = 1
        for t in range(len(thermal_buff)):
            # Define buffer starting points.
            if(t==0): img_x, img_x_s, img_y, img_y_s = 0, 0, 0, 0
            if(t==1): img_x, img_x_s, img_y, img_y_s = int(self.t_img["w"]/2), int(self.t_img["w"]/2), 0, 0
            if(t==2): img_x, img_x_s, img_y, img_y_s = 0, 0, int(self.t_img["h"]/2), int(self.t_img["h"]/2)
            if(t==3): img_x, img_x_s, img_y, img_y_s = int(self.t_img["w"]/2), int(self.t_img["w"]/2), int(self.t_img["h"]/2), int(self.t_img["h"]/2)
            for p in thermal_buff[t]:
                # Draw individual data points of each thermal buffer with the color indicator estimated by the specific color algorithm based on the defined temperature ranges to generate a precise thermal image.
                # Note: Indicators are defined in the BGR format.
                match p:
                    case 'w':
                        cv2.rectangle(template, (img_x,img_y), (img_x+self.t_img["p_w"],img_y+self.t_img["p_h"]), (255,255,255), -1)
                    case 'c':
                        cv2.rectangle(template, (img_x,img_y), (img_x+self.t_img["p_w"],img_y+self.t_img["p_h"]), (255,255,0), -1)
                    case 'b':
                        cv2.rectangle(template, (img_x,img_y), (img_x+self.t_img["p_w"],img_y+self.t_img["p_h"]), (255,0,0), -1)
                    case 'y':
                        cv2.rectangle(template, (img_x,img_y), (img_x+self.t_img["p_w"],img_y+self.t_img["p_h"]), (0,255,255), -1)
                    case 'o':
                        cv2.rectangle(template, (img_x,img_y), (img_x+self.t_img["p_w"],img_y+self.t_img["p_h"]), (0,165,255), -1)
                    case 'r':
                        cv2.rectangle(template, (img_x,img_y), (img_x+self.t_img["p_w"],img_y+self.t_img["p_h"]), (0,0,255), -1)
                # Update the successive data point coordinates.
                img_x += self.t_img["p_w"]
                if(p_num==self.thermal_buff_width):
                    img_x = img_x_s
                    img_y += self.t_img["p_h"]
                    p_num = 0
                p_num += 1
        # After generating the thermal image, register the modified frame before saving an image file.
        self.generated_thermal_image = template
```

⭐ In the *save_thermal_img* function:

⭐ Depending on the passed process type (sample or detection), save the stored thermal image frame as a sample to the *img_sample* folder directly or save the modified model resulting image (after running the FOMO-AD model) to the *img_detection* folder.

⭐ Print the passed image tag (sample or the detected label) with the creation (or prediction) date as the response to the web dashboard.

```
    def save_thermal_img(self, img_tag, _type):
        # Depending on the passed process type (sample or detection), save the produced (registered) frame to the img_sample or img_detection folder by adding the creation date to the file name.
        folder = "img_sample" if _type=="sample" else "img_detection"
        date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = "{}/{}/{}__{}.jpg".format(self.path, folder, img_tag, date)
        cv2.imwrite(file_name, self.generated_thermal_image)
        print(img_tag+":"+date)
```

⭐ In the *run_inference* function:

⭐ Print the provided information of the Edge Impulse FOMO-AD visual anomaly detection model.

⭐ Get the latest stored thermal image (frame).

⭐ After obtaining the latest thermal image, resize the retrieved frame if necessary and generate features from the cropped frame depending on the given model characteristics.

⭐ Run an inference.

⭐ Since the Edge Impulse FOMO-AD model categorizes a passed image by individual cells (grids) based on the dichotomy between two predefined classes (anomaly and no anomaly), utilize the mean visual anomaly value to detect overall (high-risk) thermal cooling malfunctions based on the confidence threshold estimated while testing the model accuracy on Edge Impulse.

⭐ If the calculated mean visual anomaly value is higher than the given threshold:

⭐ Obtain the visual anomaly grid produced by the FOMO-AD model, consisting of individual cells with coordinates, assigned labels, and anomaly scores.

⭐ If a cell's assigned label is anomaly and its anomaly score is higher than the given threshold:

⭐ Draw a rectangle on the model resulting image (cropped) with the provided cell coordinates.

⭐ Calculate the cell's anomaly intensity level — Low (L), Moderate (M), High (H) — in relation to the given threshold.

⭐ Then, draw the evaluated anomaly intensity level to the top-left corner of the cell rectangle.

⭐ Save the model resulting image modified with the cell rectangles and their evaluated anomaly intensity levels.

⭐ Finally, stop the running inference.

```
    def run_inference(self, process):
        # Run inference to identify HVAC cooling malfunctions based on the generated thermal images via visual anomaly detection.
        with ImageImpulseRunner(self.model_file) as runner:
            try:
                resulting_image = ""
                # Print the information of the Edge Impulse FOMO-AD model converted to a Linux (x86_64) application (.eim).
                model_info = runner.init()
                if(self.__debug): print('\nLoaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
                labels = model_info['model_parameters']['labels']
                # Get the latest registered thermal image (frame) generated from the passed thermal imaging buffers.
                latest_img = self.generated_thermal_image
                # After obtaining the latest image, resize (if necessary) and generate features from the retrieved frame depending on the provided model so as to run an inference.
                features, cropped = runner.get_features_from_image(latest_img)
                res = runner.classify(features)
                # Since the Edge Impulse FOMO-AD (visual anomaly detection) model categorizes given image samples by individual cells (grids)
                # based on the dichotomy between two predefined classes (anomaly and no anomaly), utilize the mean visual anomaly value to detect overall (high-risk) thermal cooling malfunctions.
                if res["result"]["visual_anomaly_mean"] >= self.threshold:
                    # If the given thermal image sample indicates a thermal cooling malfunction:
                    self.detected_class = "malfunction"
                    # Obtain the cells with their assigned labels and anomaly scores evaluated by the FOMO-AD (visual anomaly detection) model.
                    intensity = ""
                    c_offset = 5
                    for cell in res["result"]["visual_anomaly_grid"]:
                        # Draw each cell assigned with an anomaly score greater than the given model threshold on the resulting image.
                        if cell["label"] == "anomaly" and cell["value"] >= self.threshold:
                            cv2.rectangle(cropped, (cell["x"], cell["y"]), (cell["x"]+cell["width"], cell["y"]+cell["height"]), (0,255,0), 2)
                            # According to the given threshold, calculate the anomaly intensity level — Low (L), Moderate (M), High (H) — for each individual cell provided by the FOMO-AD model.
                            if(cell["value"] >= self.threshold and cell["value"] &lt; self.threshold+c_offset):
                                intensity = "L"
                            elif(cell["value"] >= self.threshold+c_offset and cell["value"] &lt; self.threshold+(2*c_offset)):
                                intensity = "M"
                            elif(cell["value"] >= self.threshold+(2*c_offset)):
                                intensity = "H"
                            # Then, draw the estimated anomaly intensity level to the top-left corner of the passed cell.
                            cv2.putText(cropped, intensity, (cell["x"]+2, cell["y"]+10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,255,0), 1, cv2.LINE_AA)
                else:
                    # If the given thermal image sample indicates a stable cooling process:
                    self.detected_class = "normal"
                # Save the generated model resulting image modified with the passed cells and their evaluated anomaly intensity levels (if applicable) to the img_detection folder on the web dashboard.
                if self.detected_class != "":
                    if(self.__debug): print("\nFOMO-AD Model Detection Result => " + self.detected_class + "\n")
                    self.generated_thermal_image = cropped
                    self.save_thermal_img(self.detected_class, process)
            # Stop the running inference.    
            finally:
                if(runner):
                    runner.stop()
```

⭐ Define the *thermal_img* object of the *thermal_img* class and pass the path of the FOMO-AD model (Linux (x86_64) application) on the server.

```
thermal_img = thermal_img("model/ai-driven-hvac-fault-diagnosis-(thermal)-linux-x86_64-v1.eim")
```

⭐ Obtain and decode thermal scan (imaging) buffers and the process type transferred by the web dashboard as Python Arguments.

⭐ After obtaining the required parameters, generate a precise thermal image from the passed thermal scan (imaging) buffers.

⭐ Depending on the passed process type (sample or detection), run an inference with the Edge Impulse FOMO-AD visual anomaly detection model to diagnose thermal cooling malfunctions or save the produced thermal image directly as a sample.

```
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--buff_1", required=True, help="thermal image buffer (16x12)")
    parser.add_argument("--buff_2", required=True, help="thermal image buffer (16x12)")
    parser.add_argument("--buff_3", required=True, help="thermal image buffer (16x12)")
    parser.add_argument("--buff_4", required=True, help="thermal image buffer (16x12)")
    parser.add_argument("--process", required=True, help="1) sample=only generate thermal image to collect data 2) detection=generate thermal image and run an inference")
    args = parser.parse_args()
    buff_1 = args.buff_1
    buff_2 = args.buff_2
    buff_3 = args.buff_3
    buff_4 = args.buff_4
    process = args.process
    # After obtaining the required parameters via Python Arguments, generate a thermal image from the given thermal imaging buffers.
    thermal_img.generate_thermal_img([buff_1, buff_2, buff_3, buff_4])
    # Depending on the passed process type (sample or detection), run an inference with the Edge Impulse FOMO-AD (visual anomaly detection) model
    # to diagnose cooling malfunctions or save the produced thermal image directly as a sample.
    if(process=="detection"):
        thermal_img.run_inference(process)
    elif(process=="sample"):
        thermal_img.save_thermal_img(process, process)
```

![281](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_python_2.png)

![282](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_python_3.png)

## Step 5.3: Running the web application on LattePanda Mu

Since [LattePanda Mu](https://docs.lattepanda.com/content/mu_edition/get_started/) is a budget-friendly compute module providing consistent multitasking performance thanks to Intel N100 quad-core processor and 8GB LPDDR5 memory, I decided to host the web application on LattePanda Mu combined with its Lite Carrier board.

:hash: After setting up the XAMPP application (lampp) on LattePanda Mu, open the *phpMyAdmin* tool on the browser manually to create a new database named *hvac_system_updates*.

*http://localhost/phpmyadmin/*

![283](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/database_set_1.png)

:hash: After adding the database successfully, go to the SQL section to create a MariaDB database table named *system_log* with the required data fields.   

```
CREATE TABLE `system_log`(		
	id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
	type varchar(255),
    category varchar(255),
    class varchar(255),
    `date` varchar(255),
    info varchar(255)
);
```

![284](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/database_set_2.png)

![285](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/database_set_3.png)

![286](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/database_set_4.png)

⚠️🔊♨️🖼️ After running the web dashboard for the first time, the home (index) page waits for obtaining the latest system log updates registered on the MariaDB database table.

⚠️🔊♨️🖼️ If there is no registered system log update in the database table, the index page displays the default placeholders to notify the user.

![287](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_1.png)

![288](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_2.png)

![289](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_3.png)

![290](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_4.png)

## Step 6.a: Setting up XIAO ESP32C6 on Arduino IDE

Although XIAO ESP32C6 is a production-ready and compact IoT development board, before proceeding with the following steps, I needed to set XIAO ESP32C6 on the Arduino IDE, install the required libraries, and configure some default settings.

When I was setting up XIAO ESP32C6 on the Arduino IDE, the current stable release of the Arduino-ESP32 board package (2.0.15) did not support the ESP32-C6 chipset. Therefore, I utilized the latest development release (3.0.0-rc1).

:hash: First, remove the Arduino-ESP32 board package if you have already installed it on the Arduino IDE.

![291](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xiao_esp32c6_set_1.png)

:hash: Then, go to *Preferences ➡ Additional Boards Manager URLs* and add the official development version URL for the Arduino-ESP32 board package:

*https://espressif.github.io/arduino-esp32/package_esp32_dev_index.json*

![292](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xiao_esp32c6_set_2.png)

![293](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xiao_esp32c6_set_3.png)

:hash: To install the required core, navigate to *Tools ➡ Board ➡ Boards Manager*, search for *esp32*, and select the latest development release — 3.0.0-rc1.

![294](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xiao_esp32c6_set_4.png)

:hash: After installing the core, navigate to *Tools ➡ Board ➡ ESP32 Arduino* and select *XIAO_ESP32C6*.

![295](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xiao_esp32c6_set_5.png)

:hash: Download and inspect the required libraries for the components connected to XIAO ESP32C6:

Adafruit_SSD1306 | [Download](https://github.com/adafruit/Adafruit_SSD1306)

Adafruit-GFX-Library | [Download](https://github.com/adafruit/Adafruit-GFX-Library)

:hash: If the Arduino IDE shows the correct port number but fails to upload the given code file, push and release the RESET button while pressing the BOOT button. Then, XIAO ESP32C6 should accept the uploaded code in the BootLoader mode.

## Step 6.b: Setting up Particle Photon 2 on Visual Studio Code and enabling data transmission with the Particle Cloud

Even though C++ is available for programming Particle development products, the Arduino IDE is not suitable due to the additional requirements for the Particle Device OS. Fortunately, Particle officially supports Visual Studio Code (VSCode) and provides the Particle Workbench, which is an integrated development and debugging environment. Since the Particle Workbench capitalizes on the built-in IntelliSense features of VSCode, it makes programming Photon 2 straightforward and effortless.

:hash: First, download Visual Studio Code (VSCode) from [the official installer](https://code.visualstudio.com/download).

:hash: After installing VS Code, go to Extensions Marketplace and search for [the Particle Workbench extension](https://docs.particle.io/quickstart/workbench/).

:hash: While downloading the Workbench extension, VSCode should install and build all dependencies automatically, including the device toolchain, C++ extension, Particle CLI, etc.

![296](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_workbench_1.png)

:hash: After downloading the Workbench extension, go to the Command Palette and select *Particle: Create New Project*. Then, enter the project directory name.

![297](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_workbench_2.png)

After creating a new project successfully on VSCode, I decided to utilize the Particle web-based setup wizard to configure the required settings for the Particle Cloud easily, providing step-by-step instructions.

:hash: First, open the Particle setup wizard on the browser.

*https://setup.particle.io/*

![298](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_1.png)

:hash: After initiating the setup process, the wizard requests the user to create a Particle account.

![299](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_2.png)

:hash: After creating a new account, connect Particle Photon 2 to the computer through the USB port and resume the setup process.

![300](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_3.png)

![301](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_4.png)

:hash: Then, the setup wizard should recognize Photon 2 (P2) and fetch the board information automatically.

![302](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_5.png)

![303](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_6.png)

:hash: After getting the board information, the setup wizard updates Photon 2 to the latest Device OS and firmware.

![304](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_7.png)

:hash: After updating Photon 2, create a new product (device group) and add Photon 2 to the created product with a unique name — hvac_control.

![305](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_8.png)

![306](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_9.png)

:hash: Connect Photon 2 to a Wi-Fi network in order to enable data transmission with the Particle Cloud.

![307](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_10.png)

![308](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_11.png)

:hash: Finally, go to the Particle Console to check whether the Cloud connection is established successfully.

![309](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_up_12.png)

:hash: After setting up Photon 2 successfully via the web-based setup wizard, return to the Workbench extension and select *Particle: Configure Project for Device* on the Command Palette.

:hash: Choose the compatible device OS version and select the target platform — Photon 2 / P2.

![310](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_workbench_3.png)

:hash: Then, obtain the device ID from the Particle Console and enter it on the Workbench extension to enable extra features, such as cloud compiling.

![311](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_workbench_4.png)

![312](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_set_workbench_5.png)

Even though Particle supports Arduino libraries, integrating them into the VSCode Workbench extension is not a simple copy-paste process.

The Particle development environment requires the following file structure to compile a library. The *src* folder must contain all of the essential library files (.cpp and .h).

- MyLibrary/
  - examples/
    - usage/
      - usage.ino			
  - src/
    - MyLibrary.cpp
    - MyLibrary.h		
  - library.properties
  - README.md
  - LICENSE
	
Thus, we need to modify the file structure of an existing Arduino library if it is not compatible with that of Particle.

Nevertheless, Particle provides a plethora of production-ready Arduino libraries maintained by the Particle community. Thus, adding officially supported Arduino libraries to the Workbench extension is uncomplicated.

:hash: First, search for the required library on the Particle libraries ecosystem via [the Library search tool](https://docs.particle.io/getting-started/device-os/firmware-libraries/).

:hash: If there is a supported version of the library in the ecosystem, go to the Workbench Welcome Screen and click *Code ➜ Install library*.

:hash: Then, enter the library name to install the given library with all dependencies.

Following the discussed steps, I installed these libraries from the Particle libraries ecosystem:

Adafruit_GFX_RK | [Inspect](https://docs.particle.io/reference/device-os/libraries/a/Adafruit_GFX_RK/)

Adafruit_ST7735_RK | [Inspect](https://docs.particle.io/reference/device-os/libraries/a/Adafruit_ST7735_RK/)

After installing the supported libraries, I modified the remaining Arduino libraries required for the components connected to Photon 2:

Seeed_Arduino_MLX9064x | [Inspect](https://github.com/Seeed-Studio/Seeed_Arduino_MLX9064x/)

You can download the Arduino libraries I modified for the Particle development environment below.

![313](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_lib_set_1.png)

![314](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_lib_set_2.png)

After completing setting up libraries, I tested the connection quality between Photon 2 and the Particle Cloud by utilizing [the provided cloud transmission methods](https://docs.particle.io/reference/device-os/api/cloud-functions/particle-variable-calculated/) — *Particle.variable()* and *Particle.function()*.

![315](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_cloud_0_test.png)

After ensuring consistent cloud data transmission, I needed to generate a user access token to make the web application (dashboard) employ the Particle Device Cloud API to communicate with the Particle Cloud.

Despite the fact that the Particle CLI lets the user generate access tokens, you can also create a token using the official web-based token generation tool on the browser.

:hash: After signing in to your account, go to [the web-based token generation tool](https://docs.particle.io/reference/cloud-apis/access-tokens/#create-a-token-browser-based-), enter the expiration time, and create a new user access token.

![316](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_token_create_1.png)

![317](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/particle_token_create_2.png)

## Step 6.c: Displaying images on the SSD1306 OLED screen and the ST7735 TFT display

I followed the exact same process to display images on the SSD1306 OLED screen (XIAO ESP32C6) and the ST7735 TFT display (Photon 2).

:hash: To be able to display images (icons), first convert image files (PNG or JPG) to monochromatic bitmaps. Then, convert the generated bitmaps to compatible C data arrays. I decided to utilize [LCD Assistant](http://en.radzio.dxp.pl/bitmap_converter/) to create C data arrays.

:hash: After installing LCD Assistant, upload a monochromatic bitmap and select *Vertical* or *Horizontal*, depending on the screen type.

:hash: Then, save all the converted C data arrays to the *logo.h* file.

⭐ In the *logo.h* file, I defined multi-dimensional arrays to group the assigned logos and their sizes — width and height.

```
// XIAO ESP32C6 :
//
// Define the assigned interface logo information as arrays.
PROGMEM static const unsigned char *interface_logos[] = {home_bits, audio_bits, faulty_audio_bits, cnc_pos_bits};
int interface_widths[] = {home_width, audio_width, faulty_audio_width, cnc_pos_width};
int interface_heights[] = {home_height, audio_height, faulty_audio_height, cnc_pos_height};
//
display.drawBitmap(0, (SCREEN_HEIGHT-l_h)/2, interface_logos[menu_option], l_w, l_h, SSD1306_WHITE);
&
&
&
// Particle Photon 2 : 
//
// Define the assigned interface logo information as arrays.
PROGMEM static const unsigned char *interface_logos[] = {home_bits, scan_bits, inspect_bits};
int interface_widths[] = {home_width, scan_width, inspect_width};
int interface_heights[] = {home_height, scan_height, inspect_height};
//
st7735.drawBitmap((SCREEN_WIDTH-interface_widths[i_x])/2, (SCREEN_HEIGHT-interface_heights[i_x])/2, interface_logos[i_x], interface_widths[i_x], interface_heights[i_x], _menu.scan_c);
```

![318](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/img_convert_1.png)

![319](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/img_convert_2.png)

![320](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/img_convert_3.png)

## Step 7: Collecting the raw audio buffers produced by the I2S MEMS microphone

After setting up all development boards on their associated software, I started to work on improving and refining code to perform functions flawlessly. First, I focused on programming XIAO ESP32C6, which manages audio sample collection and data transmission to the web application.

As explained in the previous steps, the device performs lots of interconnected features between different development boards and the web application for data collection and running advanced AI models. Thus, the described code snippets show the different aspects of the same code file. Please refer to the code files or the demonstration videos to inspect all interconnected functions in detail.

📁 *HVAC_fault_diagnosis_anomalous_sound.ino*

⭐ Include the required libraries.

```
#include &lt;WiFi.h>
#include &lt;driver/i2s.h>
#include &lt;Adafruit_GFX.h>
#include &lt;Adafruit_SSD1306.h>
```

⭐ Add the icons to be shown on the SSD1306 OLED display, which are saved and grouped in the *logo.h* file.

```
#include "logo.h"
```

⭐ Define the required server configurations for the web application hosted on LattePanda Mu.

⭐ Then, initialize the *WiFiClient* object.

```
char server[] = "192.168.1.21";
// Define the web application (HVAC malfunction dashboard) path.
String application = "/HVAC_malfunction_diagnosis_dashboard/";

// Initialize the WiFiClient object.
WiFiClient client; /* WiFiSSLClient client; */
```

⭐ Define the Fermion I2S MEMS microphone pin configurations, audio sample bits, and the I2S processor port.

```
#define I2S_SCK    D0
#define I2S_WS     D1
#define I2S_DO     D2
#define DATA_BIT   (16) //16-bit
// Define the I2S processor port.
#define I2S_PORT I2S_NUM_0
```

⭐ Configure the SSD1306 screen settings.

```
#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64  // OLED display height, in pixels
#define OLED_RESET    -1  // Reset pin # (or -1 if sharing Arduino reset pin)

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
```

⭐ In the *i2s_install* function, configure the I2S processor port with the passed sampling rate and set the channel format as *ONLY_RIGHT*.

```
void i2s_install(uint32_t sampling_rate){
  // Configure the I2S processor port for the I2S microphone (ONLY_RIGHT).
  const i2s_config_t i2s_config = {
    .mode = i2s_mode_t(I2S_MODE_MASTER | I2S_MODE_RX),
    .sample_rate = sampling_rate,
    .bits_per_sample = (i2s_bits_per_sample_t)DATA_BIT,
    .channel_format = I2S_CHANNEL_FMT_ONLY_RIGHT,
    .communication_format = i2s_comm_format_t(I2S_COMM_FORMAT_STAND_I2S),
    .intr_alloc_flags = 0,
    .dma_buf_count = 16,
    .dma_buf_len = audio_buff_size,
    .use_apll = false
  };
 
  i2s_driver_install(I2S_PORT, &i2s_config, 0, NULL);
}
```

⭐ In the *i2s_setpin* function,  assign the given I2S microphone pin configurations to the defined I2S port via the built-in I2S driver.

```
void i2s_setpin(){
  // Set the I2S microphone pin configurations.
  const i2s_pin_config_t pin_config = {
    .bck_io_num = I2S_SCK,
    .ws_io_num = I2S_WS,
    .data_out_num = -1,
    .data_in_num = I2S_DO
  };
 
  i2s_set_pin(I2S_PORT, &pin_config);
}
```

⭐ Wait until XIAO ESP32C6 establishes a successful connection with the given Wi-Fi network.

```
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, pass);
  // Attempt to connect to the given Wi-Fi network.
  while(WiFi.status() != WL_CONNECTED){
    // Wait for the network connection.
    delay(500);
    Serial.print(".");
  }
  // If connected to the network successfully:
  Serial.println("Connected to the Wi-Fi network successfully!");
```

⭐ According to the pressed control button (A or C), adjust the highlighted menu option number by one — -1 (UP) or +1 (DOWN).

```
  if(!digitalRead(control_button_A)){
    menu_option-=1;
    if(menu_option &lt; 0) menu_option = 3;
    delay(500);
  }
  if(!digitalRead(control_button_C)){
    menu_option+=1;
    if(menu_option > 3) menu_option = 0;
    delay(500);
  }
```

⭐ In the *show_interface* function:
⭐ According to the passed screen command and menu option number, get the assigned icon information, show the home screen with the highlighted menu option, or display the associated layout after the highlighted menu option is selected.

⭐ Depending on the status of the CNC positioning process (Waiting, Ongoing, Saved, or Image Ready), display the associated buffer operation status indicator on the screen for each positioning point (location).

⭐ Show the associated class icon and name according to the audio class predicted by the Audio MFE model.

```
void show_interface(String com, int menu_option){
  // Get the assigned interface logo information.
  int l_w = interface_widths[menu_option];
  int l_h = interface_heights[menu_option];
  if(com == "home"){
    display.clearDisplay();
    display.drawBitmap(0, (SCREEN_HEIGHT-l_h)/2, interface_logos[menu_option], l_w, l_h, SSD1306_WHITE);   
    display.setTextSize(1); 
    (menu_option == 1) ? display.setTextColor(SSD1306_BLACK, SSD1306_WHITE) : display.setTextColor(SSD1306_WHITE);
    display.setCursor(l_w+5, 5); display.println("Collect Audio");
    (menu_option == 2) ? display.setTextColor(SSD1306_BLACK, SSD1306_WHITE) : display.setTextColor(SSD1306_WHITE);
    display.setCursor(l_w+5, 20); display.println("Faulty Sound");
    (menu_option == 3) ? display.setTextColor(SSD1306_BLACK, SSD1306_WHITE) : display.setTextColor(SSD1306_WHITE);
    display.setCursor(l_w+5, 35); display.println("CNC Positioning");
    display.setCursor(l_w+5, 45); display.println("&Thermal Buffer");
    display.setCursor(l_w+5, 55); display.println("Collection");
    display.display();
  }else if(com == "collect"){
    int l_offset = 1;
    display.clearDisplay();
    display.drawBitmap((SCREEN_WIDTH-l_w)/2, l_offset, interface_logos[menu_option], l_w, l_h, SSD1306_WHITE);   
    display.setTextSize(1);
    display.setCursor((SCREEN_WIDTH/2)-45, (2*l_offset)+l_h+5);
    display.println("[A] => normal");
    display.setCursor((SCREEN_WIDTH/2)-45, (8*l_offset)+l_h+15);
    display.println("[C] => defective");
    display.display();
  }else if(com == "CNC"){
    int l_offset = 2, h_offset = 16;
    // Depending on the status of the CNC positioning point (Waiting, Ongoing, Saved, or Image Ready), display the associated CNC status icon on the screen.
    int i_1 = _CNC.pos_status[0], i_2 = _CNC.pos_status[1], i_3 = _CNC.pos_status[2], i_4 = _CNC.pos_status[3];
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(l_offset, l_offset); display.println("Position [1] =>");
    display.drawBitmap(SCREEN_WIDTH-CNC_widths[i_1]-l_offset, l_offset, CNC_logos[i_1], CNC_widths[i_1], CNC_heights[i_1], SSD1306_WHITE);
    display.setCursor(l_offset, l_offset + h_offset); display.println("Position [2] =>");
    display.drawBitmap(SCREEN_WIDTH-CNC_widths[i_2]-l_offset, l_offset+h_offset, CNC_logos[i_2], CNC_widths[i_2], CNC_heights[i_2], SSD1306_WHITE);
    display.setCursor(l_offset, l_offset + (2*h_offset)); display.println("Position [3] =>");
    display.drawBitmap(SCREEN_WIDTH-CNC_widths[i_3]-l_offset, l_offset+(2*h_offset), CNC_logos[i_3], CNC_widths[i_3], CNC_heights[i_3], SSD1306_WHITE);
    display.setCursor(l_offset, l_offset + (3*h_offset)); display.println("Position [4] =>");
    display.drawBitmap(SCREEN_WIDTH-CNC_widths[i_4]-l_offset, l_offset+(3*h_offset), CNC_logos[i_4], CNC_widths[i_4], CNC_heights[i_4], SSD1306_WHITE);
    display.display();
  }else if(com == "run"){
    int l_c_w = class_widths[predicted_class], l_c_h = class_heights[predicted_class], l_offset = 2;
    String p_c = "[ "+classes[predicted_class]+" ]"; p_c.toUpperCase();
    int p_c_l = p_c.length()*5;  
    display.clearDisplay();
    display.drawBitmap((SCREEN_WIDTH-l_c_w)/2, l_offset, class_logos[predicted_class], l_c_w, l_c_h, SSD1306_WHITE);
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor((SCREEN_WIDTH-p_c_l)/2, SCREEN_HEIGHT-(6*l_offset)); display.println(p_c);
    display.display();
  }
}
```

⭐ In the *microphone_sample* function:

⭐ Obtain the information generated by the I2S microphone and save it to the input buffer — *sample_audio_buffer*.

⭐ If the I2S microphone generates raw audio data successfully, scale the produced raw audio buffer depending on the model requirements. Otherwise, the sound might be too quiet for classification.

⭐ If requested for debugging, display the average (mean) output values on the serial plotter.

```
bool microphone_sample(bool _debug){ 
  // Obtain the information generated by the I2S microphone and save it to the input buffer — sample_audio_buffer.
  size_t bytesIn = 0;
  esp_err_t result = i2s_read(I2S_PORT, &sample_audio_buffer, audio_buff_size, &bytesIn, portMAX_DELAY);
  // If the I2S microphone generates raw audio data successfully:
  if(result == ESP_OK){
    Serial.println("\nAudio Data Generated Successfully!");
    // Depending on the given model, scale (resize) the raw audio buffer (data) collected by the I2S microphone. Otherwise, the sound might be too quiet for classification.
    for(int x = 0; x &lt; bytesIn/2; x++){
      sample_audio_buffer[x] = (int16_t)(sample_audio_buffer[x]) * 8;
    }
    // If requested, display the average (mean) audio data reading on the serial plotter.
    if(_debug){
      int16_t samples_read = bytesIn / 8;
      if(samples_read > 0){
        float mean = 0;
        for(int16_t i = 0; i &lt; samples_read; ++i){ mean += (sample_audio_buffer[i]); }
        mean /= samples_read;
        Serial.println(mean);
      }
    }
    // Exit. 
    return true;
  }else{
    Serial.println("\nAudio Data Collection Failed!");
    // Exit.
    return false;
  }
}
```

⭐ In the *make_a_post_request* function:

⭐ Connect to the web application with the configured server settings.

⭐ Create the *query* string by appending the passed URL query (GET) parameters.

⭐ Define the *AudioSample* boundary parameter to transfer the produced raw audio sample to the web application as a plain text file.

⭐ Estimate the total message (content) length.

⭐ Initiate an HTTP POST request with the created *query* string as additional URL parameters to the web application.

⭐ While making the POST request, according to the defined buffer multiplier, collect and write (transfer) raw audio buffers consecutively to prevent memory allocation issues.

⭐ Then, conclude data (buffer) writing and the POST request.

⭐ Wait until fully transferring the raw audio sample produced from individual buffers.

```
boolean make_a_post_request(String request){
  // Connect to the web application named HVAC_malfunction_diagnosis_dashboard. Change '80' with '443' if you are using SSL connection.
  if(client.connect(server, 80)){
    // If successful:
    Serial.println("\nConnected to the web application successfully!\n");
    // Create the query string:
    String query = application + request;
    // Make an HTTP POST request:
    String head = "--AudioSample\r\nContent-Disposition: form-data; name=\"audio_sample\"; filename=\"new_sample.txt\";\r\nContent-Type: text/plain;\r\n\r\n";
    String tail = "\r\n--AudioSample--\r\n";
    // Get the total message length.
    uint32_t totalLen = head.length() + audio_buff_size*buf_multiplier + tail.length();
    // Start the request:
    client.println("POST " + query + " HTTP/1.1");
    client.println("Host: 192.168.1.21");
    client.println("Content-Length: " + String(totalLen));
    client.println("Connection: Keep-Alive");
    client.println("Content-Type: multipart/form-data; boundary=AudioSample");
    client.println();
    client.print(head);
    // According to the given buffer multiplier, collect and transfer I2S raw audio buffers consecutively to prevent memory allocation issues.
    for(int t=0; t&lt;buf_multiplier; t++){
      microphone_sample(false);
      for(int i=0; i&lt;audio_buff_size; i++) client.print(sample_audio_buffer[i]);
    }
    // Complete data (buffer) writing.
    client.print(tail);
    // Wait until transferring the generated (multiplied) raw audio sample.
    delay(5000);
    // If successful:
    Serial.println("HTTP POST => Data transfer completed!\n");
    return true;
  }else{
    Serial.println("\nConnection failed to the web application!\n");
    delay(2000);
    return false;
  }
}
```

⭐ After highlighting a menu option on the home screen, if the control button B is pressed, navigate to the selected option's layout.

⭐ If the first option *(Collect Audio)* is activated:

⭐ Inform the user of the audio sample collection settings on the SSD1306 screen.

⭐ According to the pressed control button (A or C), select an audio class for the sample.

- A ➜ normal
- C ➜ defective

⭐ Before producing an audio sample, check the I2S microphone status by running the *microphone_sample* function once.

⭐ If the  I2S microphone generates a raw audio buffer as expected, notify the user on the screen.

⭐ Then, collect raw audio buffers and transfer them simultaneously to the web application until reaching the predefined buffer multiplier number in order to send the produced audio sample without triggering memory allocation errors.

⭐ Notify the user of the web application data transmission success on the screen by showing the associated status icons.

⭐ If the control button D is pressed, redirect the user to the home screen.

```
  if(menu_option == 1 && !digitalRead(control_button_B)){
    option_update = true;
    while(option_update){
      // Inform the user of the data collection settings.
      int l_offset = 5;
      show_interface("collect", menu_option);
      delay(2000);
      // According to the pressed control button (A or C), generate an audio sample from the collected raw audio buffers
      // and transfer the generated sample with the selected audio class to the web dashboard (application). 
      if(!digitalRead(control_button_A) || !digitalRead(control_button_C)){
        // Get the selected audio class.
        String selected_class = (!digitalRead(control_button_A)) ? "normal" : "defective";
        // Before proceeding with generating an audio sample, check the I2S microphone status.
        if(microphone_sample(false)){
          // After collecting data successfully, notify the user via the screen.
          display.clearDisplay();
          display.drawBitmap((SCREEN_WIDTH-collected_width)/2, l_offset, collected_bits, collected_width, collected_height, SSD1306_WHITE);   
          display.setTextSize(1);
          display.setCursor(0, collected_height+(2*l_offset));
          display.println("I2S microphone\ncollecting data!");
          display.display();
          delay(3000);
          // If the I2S microphone is operating precisely, generate a one-second audio sample by utilizing the buffer multiplier.
          // Simultaneously, transfer the collected raw data buffers to the web dashboard (application) while making an HTTP POST request in order to avoid memory allocation errors.
          if(make_a_post_request("sample_audio_files/save_audio_sample.php?audio=new&class="+selected_class)){
            // If successful:
            display.clearDisplay();
            display.drawBitmap((SCREEN_WIDTH-connected_width)/2, l_offset, connected_bits, connected_width, connected_height, SSD1306_WHITE);   
            display.setTextSize(1);
            display.setCursor(0, connected_height+(2*l_offset));
            display.println("Sample Transferred\nSuccessfully!");
            display.display();
            delay(5000);
          }else{
            display.clearDisplay();
            display.drawBitmap((SCREEN_WIDTH-error_width)/2, l_offset, error_bits, error_width, error_height, SSD1306_WHITE);   
            display.setTextSize(1);
            display.setCursor(0, error_height+(2*l_offset));
            display.println("Server => Connection\nFailed!");
            display.display();
            delay(5000);
          }
        }else{
          display.clearDisplay();
          display.drawBitmap((SCREEN_WIDTH-error_width)/2, l_offset, error_bits, error_width, error_height, SSD1306_WHITE);   
          display.setTextSize(1);
          display.setCursor(0, error_height+(2*l_offset));
          display.println("Sample Collection\nFailed!");
          display.display();
          delay(3000);
        }
      }
      // If the control button D is pressed, redirect the user to the home screen.
      if(!digitalRead(control_button_D)){
        option_update = false;
      }
    }
  }
```

![321](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_1.png)

![322](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_3.png)

![323](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_6.png)

![324](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_8.png)

![325](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_9.png)

## Step 7.1: Generating raw audio samples and passing the produced samples to the web application for saving them as WAV files

⚠️🔊♨️🖼️ If XIAO ESP32C6 establishes a successful connection with the given Wi-Fi network and all connected components operate as expected, the device shows the home screen on the SSD1306 OLED display.

- Collect Audio
- Faulty Sound
- CNC Positioning & Thermal Buffer Collection

![326](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_1.jpg)

⚠️🔊♨️🖼️ The device lets the user adjust the highlighted menu option on the home screen by pressing the control buttons — A (↑) and C (↓).

⚠️🔊♨️🖼️ After changing the highlighted menu option, the device also updates the icon on the home screen with the assigned option icon.

⚠️🔊♨️🖼️ As a menu option is highlighted, if the control button B is pressed, the device navigates to the selected option's layout.

⚠️🔊♨️🖼️ Note: If the user presses the control button D, XIAO ESP32C6 returns to the home screen.

![327](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_2.jpg)

⚠️🔊♨️🖼️ If the user activates the first menu option — *Collect Audio*:

⚠️🔊♨️🖼️ On the associated layout, the device informs the user of the audio sample collection settings, which allow the user to assign an audio class to the sample by pressing a control button.

- A ➜ normal
- C ➜ defective

![328](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_3.jpg)

⚠️🔊♨️🖼️ After selecting an audio class, the device checks whether the I2S microphone operates accurately and informs the user regarding the microphone status on the screen before producing an audio sample.

![329](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_4.jpg)

⚠️🔊♨️🖼️ If the I2S microphone works as expected, the device collects raw audio buffers and transfers them simultaneously to the web application until reaching the predefined buffer multiplier number while maintaining an HTTP POST request.

⚠️🔊♨️🖼️ In this regard, the device can produce and send long raw audio samples to the web application without triggering memory allocation issues.

⚠️🔊♨️🖼️ After concluding the POST request, the device notifies the user of the data transmission success on the screen by showing the associated status icons.

![330](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_5.jpg)

⚠️🔊♨️🖼️ As explained in the previous steps, after receiving the produced raw audio sample, the web application saves the sample as a plain text file temporarily.

⚠️🔊♨️🖼️ Then, the web application runs a Python script to convert the raw audio sample to a WAV audio file compatible with Edge Impulse.

⚠️🔊♨️🖼️ After converting the given sample with the passed audio conversion parameters successfully, the web application updates the system log on the MariaDB database accordingly.

⚠️🔊♨️🖼️ Finally, the web application updates its home (index) page automatically to showcase the latest system log entries. In addition to displaying the collection dates and the assigned audio classes, the web application lets the user download audio samples individually on the home page.

![331](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_5.png)

![332](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_6.png)

![333](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_7.png)

![334](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_11.png)

After collecting samples of normal and defective sound originating from the HVAC system cooling fans, I managed to construct a valid audio data set stored on the web application.

![335](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_collect_audio.gif)

![336](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_audio_samples_1.png)

## Step 8.a: Controlling CNC (thermal camera container head) motions via Arduino Nano

Since I decided to build a fully 3D-printable custom CNC router to position the MLX90641 thermal imaging camera, I needed to design a separate CNC control mechanism based on Arduino Nano. In this regard, I was able to move the thermal camera container head according to the CNC commands received via serial communication.

After programming XIAO ESP32C6, I focused on improving and refining CNC functions performed by Arduino Nano.

📁 *HVAC_thermal_camera_CNC.ino*

⭐ Include the required libraries.

```
#include &lt;SoftwareSerial.h>
#include &lt;Stepper.h>
```

⭐ Define the 28BYJ-48 stepper motor configurations and initialize the stepper object.

```
int stepsPerRevolution = 2038, max_motor_RPM = 10, step_delay = 500, CNC_go_to_switch = 15, CNC_switch_to_home = 1;
Stepper CNC_motor(stepsPerRevolution, 8, 10, 9, 11); // IN1-IN3-IN2-IN4
```

⭐ Define a software serial port *(XIAO)* since the default (USB) hardware serial port is occupied for debugging.

```
const int rxPin = 2, txPin = 4;
SoftwareSerial XIAO(/*RX=*/rxPin, /*TX=*/txPin);
```

⭐ Define all of the required CNC commands and step numbers by creating a struct — *_CNC* — so as to organize and call them efficiently.

```
struct _CNC{
  String pos_command[5] = {"1", "2", "3", "4", "h"};
  int step_number[4] = {1, 1, 3, 1};
  int pos_delay = 5000;
};
```

⭐ Initiate the defined software serial port to communicate with XIAO ESP32C6.

```
XIAO.begin(115200);
```

⭐ In the *CNC_motor_move* function:

⭐ Rotate the stepper motor of the CNC router to move the thermal camera container head according to the passed step number and the direction.

- CW:  Clockwise
- CCW: Counter-clockwise

⭐ While turning the stepper motor counter-clockwise, check whether the thermal camera container head triggers the micro switch by colliding.

⭐ If so, force the container head to return to the home position. Then, turn the RGB LED to white.

```
int CNC_motor_move(int step_number, String _direction){
  int revs = 0;
  // Move the CNC stepper motor according to the passed step number and the direction.
  // CW:  Clockwise
  // CCW: Counter-clockwise
  if(_direction == "CW"){
    for(int i=0; i&lt;step_number; i++){
      CNC_motor.setSpeed(max_motor_RPM/2);
      CNC_motor.step(stepsPerRevolution/8);
      delay(step_delay);
      revs++;
    }
  }else if(_direction == "CCW"){
    for(int i=0; i&lt;step_number; i++){
      CNC_motor.setSpeed(max_motor_RPM/2);
      CNC_motor.step(-stepsPerRevolution/4);
      delay(step_delay);
      revs++;
      // If the thermal camera container head triggers the stop micro switch by colliding, force the container head to return to the home position.
      if(digitalRead(CNC_stop_switch)){
        if(CNC_position_home()) adjustColor(255,255,255);
        break;      
      }      
    }
  }
  // Return the total revolution number.
  return revs;
}
```

⭐ In the *CNC_position_home* function, return the thermal camera container head to the home position — 0.

```
bool CNC_position_home(){
  // Return the thermal camera container head to the home position — 0.
  for(int i=0; i&lt;CNC_switch_to_home; i++){
    CNC_motor.setSpeed(max_motor_RPM);
    CNC_motor.step(stepsPerRevolution/8);
    delay(step_delay);
  }
  return true;
}
```

⭐ Obtain the data packet transferred by XIAO ESP32C6 via serial communication.

```
  if(XIAO.available() > 0){
    data_packet = XIAO.readString();
  }
```

⭐ Depending on the received CNC coordinate update command, change the thermal camera container head position by rotating the stepper motor by the predefined step number.

⭐ When starting the positioning process, turn the RGB LED to red.  After completing the positioning process, turn the RGB LED to yellow.

⭐ Then, send the coordinate update confirmation message — *CNC_OK* — to XIAO ESP32C6 via serial communication.

⭐ After sending the confirmation message, turn the RGB LED to green.

⭐ After going through four coordinate updates, if XIAO ESP32C6 transmits the zeroing command, return the thermal camera container head to the starting point (zeroing) by estimating the total revolved step number.

⭐ When starting the zeroing process, turn the RGB LED to red.  After completing the zeroing process, turn the RGB LED to yellow.

⭐ Then, send the zeroing confirmation message — *CNC_OK* — to XIAO ESP32C6 via serial communication.

⭐ After sending the zeroing confirmation message, turn the RGB LED to purple.

⭐ Finally, clear the received data packet.

```
  if(data_packet != ""){
    Serial.print("Received Data Packet => "); Serial.println(data_packet);
    // Depending on the received coordinate update command from XIAO ESP32C6, change the thermal camera container head position via the stepper motor.
    if(data_packet.indexOf(_CNC.pos_command[0]) > -1){
      adjustColor(255,0,0);
      CNC_motor_move(_CNC.step_number[0], "CW");
      adjustColor(255,255,0);
      delay(_CNC.pos_delay);
      // Transfer (reply) the coordinate update confirmation message to XIAO ESP32C6 via serial communication.
      XIAO.print("CNC_OK");
      delay(1000);
      adjustColor(0,255,0);
    }else if(data_packet.indexOf(_CNC.pos_command[1]) > -1){
      adjustColor(255,0,0);
      CNC_motor_move(_CNC.step_number[1], "CW");
      adjustColor(255,255,0);
      delay(_CNC.pos_delay);
      // Transfer (reply) the coordinate update confirmation message to XIAO ESP32C6 via serial communication.
      XIAO.print("CNC_OK");
      delay(1000);
      adjustColor(0,255,0);
    }else if(data_packet.indexOf(_CNC.pos_command[2]) > -1){
      adjustColor(255,0,0);
      CNC_motor_move(_CNC.step_number[2], "CW");
      adjustColor(255,255,0);
      delay(_CNC.pos_delay);
      // Transfer (reply) the coordinate update confirmation message to XIAO ESP32C6 via serial communication.
      XIAO.print("CNC_OK");
      delay(1000);
      adjustColor(0,255,0);
    }else if(data_packet.indexOf(_CNC.pos_command[3]) > -1){
      adjustColor(255,0,0);
      CNC_motor_move(_CNC.step_number[3], "CW");
      adjustColor(255,255,0);
      delay(_CNC.pos_delay);
      // Transfer (reply) the coordinate update confirmation message to XIAO ESP32C6 via serial communication.
      XIAO.print("CNC_OK");
      delay(1000);
      adjustColor(0,255,0);
    }else if(data_packet.indexOf(_CNC.pos_command[4]) > -1){
      // If requested, after going through four coordinate updates, return the thermal camera container head to the starting point (zeroing).
      int zeroing = 0;
      for(int i=0; i&lt;4; i++) zeroing+=_CNC.step_number[i];
      Serial.print("Zeroing the container head for "); Serial.print(zeroing); Serial.println(" steps!\n");
      adjustColor(255,0,0);
      CNC_motor_move(zeroing, "CCW");
      adjustColor(255,255,0);
      delay(_CNC.pos_delay);
      // Transfer (reply) the coordinate update confirmation message to XIAO ESP32C6 via serial communication.
      XIAO.print("CNC_OK");
      delay(1000);
      adjustColor(255,0,255);
    }
    // Clear the received data packet.
    data_packet = "";
  }
```

⭐ If the home button is pressed, initiate the container head homing sequence, which returns the container head to the home position (0) by utilizing the micro switch.

```
  if(!digitalRead(CNC_home_button)){
    Serial.println("\nHoming sequence activated!\n");
    adjustColor(0,0,255);
    CNC_motor_move(CNC_go_to_switch, "CCW");
  }
```

![337](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_cnc_1.png)

![338](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_cnc_2.png)

![339](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_cnc_3.png)

## Step 8.b: Communicating with Arduino Nano and the web application to initiate the four-step CNC positioning sequence for consecutive thermal imaging buffer collection via the Particle Cloud

After completing the CNC router programming, controlled by Arduino Nano, I focused on improving the remaining XIAO ESP32C6 features, including transferring commands to Arduino Nano and communicating with the web application regarding thermal imaging buffer collection.

As explained in the previous steps, the device performs lots of interconnected features between different development boards and the web application for data collection and running advanced AI models. Thus, the described code snippets show the different aspects of the same code file. Please refer to the code files or the demonstration videos to inspect all interconnected functions in detail.

📁 *HVAC_fault_diagnosis_anomalous_sound.ino*

⭐ Define all of the required CNC commands and variables by creating a struct — *_CNC* — so as to organize and call them efficiently.

```
struct _CNC{
  String pos_command[5] = {"111111111", "222222222", "333333333", "444444444", "hhhhhhhhh"};
  int pos_status[4] = {4, 4, 4, 4};
  boolean serial_update = false;
};
```

⭐ Initiate the hardware serial port (Serial1) to communicate with Arduino Nano.

```
Serial1.begin(115200, SERIAL_8N1, /*RX=*/D7,/*TX=*/D6);
```

⭐ In the *make_a_get_request* function:

⭐ Connect to the web application with the configured server settings.

⭐ Create the *query* string by appending the passed URL query (GET) parameters.

⭐ Make an HTTP GET request with the given URL parameters to the web application.

⭐ Wait until successfully completing the request process.

```
boolean make_a_get_request(String request){
  // Connect to the web application named HVAC_malfunction_diagnosis_dashboard. Change '80' with '443' if you are using SSL connection.
  if(client.connect(server, 80)){
    // If successful:
    Serial.println("\nConnected to the web application successfully!\n");
    // Create the query string:
    String query = application + request;
    // Make an HTTP GET request:
    client.println("GET " + query + " HTTP/1.1");
    client.println("Host: 192.168.1.21");
    client.println("Connection: close");
    client.println();
    // Wait until completing the request process.
    delay(2000);
    // If successful:
    Serial.println("HTTP GET => Connection established!\n");
    return true;
  }else{
    Serial.println("\nConnection failed to the web application!\n");
    delay(2000);
    return false;
  }
}
```

⭐ In the *nano_update_response* function:

⭐ Wait until Arduino Nano transfers a data packet via serial communication.

⭐ Then, return the obtained data packet.

```
String nano_update_response(){
  // Wait until Arduino Nano transfers a data packet via serial communication.
  String data_packet = "";
  while(_CNC.serial_update){
    if(Serial1.available() > 0){
      data_packet = Serial1.readString();
    }
    if(data_packet != ""){
      _CNC.serial_update = false;
    }
    delay(1000); 
  }
  // Then, return the obtained data packet.
  return data_packet;
}
```

⭐ In the *thermal_buffer_collection_via_CNC* function:

⭐ Initiate the four-step CNC positioning sequence consisting of different CNC commands — from 1 to 4.

⭐ For each CNC positioning command:

⭐ Transfer the given command to Arduino Nano via serial communication.

⭐ Update the buffer operation status indicator to *Ongoing* on the screen with the associated status icon.

⭐ Wait until Arduino Nano replies with the coordinate update confirmation message *(CNC_OK)* via serial communication after moving the thermal camera container head to the predefined position.

⭐ After obtaining the confirmation message, update the buffer status indicator to *Completed* on the screen with the associated status icon.

⭐ After positioning the container head according to the passed CNC command, make an HTTP GET request to the web application (dashboard) in order to make Photon 2 collect and register the associated thermal imaging buffer through the Particle Cloud API.

⭐ If the GET request is successful, update the buffer status indicator to *Saved* on the screen with the associated status icon.

⭐ Then, increase the command number to resume the positioning sequence.

⭐ After concluding the four-step CNC positioning sequence successfully, return the thermal camera container head to the starting point (zeroing) by transmitting the zeroing command to Arduino Nano via serial communication.

⭐ Wait until Arduino Nano replies with the zeroing confirmation message *(CNC_OK)* via serial communication after moving the thermal camera container head to the starting point.

⭐ After obtaining the zeroing confirmation message, change all buffer status indicators on the screen to *Image Ready*.

⭐ After finalizing the CNC positioning sequence and the zeroing procedure, make a successive HTTP GET request to the web application to initiate the thermal image conversion process with the thermal imaging buffers registered on the Particle Cloud.

⭐ If the GET request is successful, halt all processes and redirect the user to the home screen.

```
void thermal_buffer_collection_via_CNC(String process_type){
  // Initiate the four-step CNC positioning sequence so as to move the thermal camera container head to the predefined points for consecutive data (thermal imaging buffer) collection.
  if(position_start &lt; 4){
    // Transfer CNC commands to Arduino Nano via serial communication.
    Serial1.print(_CNC.pos_command[position_start]);
    delay(2000);
    // Update the given position status to Ongoing.
    _CNC.pos_status[position_start] = 0;
    show_interface("CNC", menu_option);
    delay(500);
    // Wait until Arduino Nano returns the coordinate update confirmation message via the serial communication.
    _CNC.serial_update = true;
    String pos_confirmation = nano_update_response();
    // If Arduino Nano transfers the coordinate confirmation message, update the given position status to Completed.
    // Then, increase the point (position) number.
    if(pos_confirmation == "CNC_OK"){
      _CNC.pos_status[position_start] = 1;
      show_interface("CNC", menu_option);
      delay(5000);
      // After positioning the container head on the given location (point), make an HTTP GET request to the web dashboard in order to make Photon 2 collect and register the associated thermal imaging buffer through the Particle Cloud API.
      // If registered successfully, update the given position status to Saved.
      String request = "assets/Particle_cloud_connection.php?collect_particle_cloud_variable="+String(position_start+1);
      if(make_a_get_request(request)) _CNC.pos_status[position_start] = 2;
      // Update the position (point) number.
      position_start++;
      if(position_start == 4){ show_interface("CNC", menu_option); delay(500); zeroing = true; }
    }
  }
  // After passing all four position points successfully, return the thermal camera container head to the starting point (zeroing).
  if(zeroing){
    Serial1.print(_CNC.pos_command[position_start]);
    delay(4000);
    // Wait until Arduino Nano returns the zeroing confirmation message via the serial communication.
    _CNC.serial_update = true;
    String zero_confirmation = nano_update_response();
    if(zero_confirmation == "CNC_OK"){
      // After the container head returns to the starting point, update all position status indicators (icons) to Image Ready.
      for(int i=0; i&lt;4; i++) _CNC.pos_status[i] = 3;
      position_start++;
      delay(1000);
      zeroing = false;
      // Notify the user of the latest updated status indicators.
      show_interface("CNC", menu_option);
      delay(3000);
    }        
  }
  // If Photon 2 registers all thermal imaging buffers successfully and the web dashboard is ready to generate a thermal image from the passed buffers,
  // make an HTTP GET request to the web dashboard to initiate the thermal image conversion process.
  if(_CNC.pos_status[0] == 3 && _CNC.pos_status[1] == 3 && _CNC.pos_status[2] == 3 && _CNC.pos_status[3] == 3){
    // If the web dashboard generates the thermal image successfully, redirect the user to the home screen.
    String request = "assets/Particle_cloud_connection.php?generate_cloud_thermal_image="+process_type;
    if(make_a_get_request(request)){ delay(5000); option_update = false; defective_sound = false; }
  }
}
```

⭐ If the third option *(CNC Positioning & Thermal Buffer Collection)* is activated:

⭐ Clear the previously assigned buffer status indicators.

⭐ Initiate the four-step CNC positioning sequence so as to move the thermal camera container head to the predefined locations for consecutive thermal scan (imaging) buffer collection through the Particle Cloud API.

⭐ Notify the user of each buffer status indicator update by showing their associated status icons on the SSD1306 screen — *Waiting, Ongoing, Saved*, and *Image Ready*.

⭐ If the control button D is pressed, redirect the user to the home screen.

```
  if(menu_option == 3 && !digitalRead(control_button_B)){
    position_start = 0;
    zeroing = false;
    option_update = true;
    // Clear the previously assigned buffer status indicators.
    for(int i=0; i&lt;4; i++) _CNC.pos_status[i] = 4;
    while(option_update){
      // Notify the user of the CNC positioning status of each individual point by showing their associated status icons on the SSD1306 screen — Waiting, Ongoing, Saved, or Image Ready.
      show_interface("CNC", menu_option);
      delay(2000);
      // Start the CNC positioning sequence and collect thermal scan (imaging) buffers on predefined locations (points) through the Particle Cloud API.
      thermal_buffer_collection_via_CNC("sample");
      // If the control button D is pressed, redirect the user to the home screen.
      if(!digitalRead(control_button_D)){
        option_update = false;
      }
    }
  }
```

![340](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_2.png)

![341](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_7.png)

## Step 8.c: Generating the required thermal imaging buffers via a specific color algorithm and registering the produced buffers to Particle Cloud variables

After working on the XIAO ESP32C6 data transmission procedure with the web application and the custom CNC router positioning sequence, I focused on developing and improving Particle Photon 2 functions related to thermal imaging buffer collection and registration.

As discussed earlier, I set up the Particle Workbench on Visual Studio Code (VSCode) to be able to utilize the Particle Device OS to program Photon 2. You can inspect the integrated Particle Cloud transmission methods of the Device OS and their limitations from [here](https://docs.particle.io/reference/device-os/api/cloud-functions/overview-of-api-field-limits/).

📁 *HVAC_fault_diagnosis_thermal_image.cpp*

⭐ Include Particle Device OS APIs.

```
#include "Particle.h"
```

⭐ Include the required libraries.

```
#include &lt;Wire.h>
#include &lt;MLX90641_API.h>
#include &lt;MLX9064X_I2C_Driver.h>
#include "Adafruit_ST7735.h"
```

⭐ Add the icons to be shown on the ST7735 TFT display, which are saved and grouped in the *logo.h* file.

```
#include "logo.h"
```

⭐ Via the built-in Device OS functions, connect to the Particle Cloud automatically.

⭐ Then, enable threading to run the given program (application) and the built-in cloud transmission system (network management) concurrently.

```
SYSTEM_MODE(AUTOMATIC);

SYSTEM_THREAD(ENABLED);
```

⭐ Define the Particle Cloud variable names and registration status indicators by creating a struct — *_thermal* — so as to organize and call them efficiently.

```
struct _thermal{
  String buff_1 = "empty";
  String buff_2 = "empty";
  String buff_3 = "empty";
  String buff_4 = "empty";
  boolean buff_1_st = false;
  boolean buff_2_st = false;
  boolean buff_3_st = false;
  boolean buff_4_st = false;
};
```

⭐ Define the MLX90641 thermal imaging camera configurations, including the 7-bit unshifted device address and the open air shift value.

```
const byte MLX90641_address = 0x33; // Default 7-bit unshifted address of the MLX90641 camera.
#define TA_SHIFT 12 // Default shift value for the MLX90641 camera in the open air.
uint16_t eeMLX90641[832];
float MLX90641To[192];
uint16_t MLX90641Frame[242];
paramsMLX90641 MLX90641;
int errorno = 0;
```

⭐ To create a specific color algorithm for converting IR array data items to color-based indicators to produce a thermal imaging buffer, define temperature threshold ranges. Then, define the required information to generate a preview (snapshot) thermal image from the produced buffers.

```
int min_temp = 18, mod_temp_1 = 20, mod_temp_2 = 22, mod_temp_3 = 24, max_temp = 26;
#define thermal_buff_width   16
#define thermal_buff_height  12
#define thermal_buff_num     4
#define thermal_buff_size    thermal_buff_width * thermal_buff_height
#define thermal_img_size     thermal_buff_size * thermal_buff_num
```

⭐ Configure the ST7735 TFT screen settings.

```
#define SCREEN_HEIGHT 160
#define SCREEN_WIDTH  128
#define TFT_CS  D2
#define TFT_DC  D3
#define TFT_RST D4
Adafruit_ST7735 st7735(&SPI, TFT_CS, TFT_DC, TFT_RST);
```

⭐ Define the required variables for the home screen and the option layouts by creating a struct — *_menu* — so as to organize and call them efficiently.

```
struct _menu {
  int background = st7735.color565(23, 30, 39);
  int border = st7735.color565(186, 12, 46);
  int scan_c = st7735.color565(174, 225, 205);
  int inspect_c = st7735.color565(243, 208, 40);
  int menu_c = st7735.color565(255, 255, 255);
  int highlight = st7735.color565(76, 74, 70);
  int text_c = st7735.color565(76, 74, 70);
  int text_c_h = st7735.color565(186, 12, 46);
  int status_c[2] = {ST77XX_RED, ST7735_GREEN};
};
```

⭐ To prevent errors due to threading that manages simultaneous cloud transmission, declare custom application functions before the *setup* function.

```
String get_and_display_data_from_MLX90641(int buffer_size);
int collect_thermal_buffers(String num);
void show_interface(String command);
boolean is_MLX_Connected();
void joystick_read();
void adjustColor(int r, int g, int b);
```

⭐ Assign new variables to the Particle Cloud by utilizing the built-in *Particle.variable* method.

```
  Particle.variable("thermal_buff_1", _thermal.buff_1);
  Particle.variable("thermal_buff_2", _thermal.buff_2);
  Particle.variable("thermal_buff_3", _thermal.buff_3);
  Particle.variable("thermal_buff_4", _thermal.buff_4);
```

⭐ Assign new functions to the Particle Cloud by utilizing the built-in *Particle.function* method.

```
  Particle.function("collect_thermal_buffers", collect_thermal_buffers);
```

⭐ Initialize the ST7735 screen with the required configurations.

```
  st7735.initR(INITR_BLACKTAB);
  st7735.setRotation(2);
  st7735.fillScreen(ST77XX_BLACK);
  st7735.setTextSize(1);
  st7735.setTextWrap(false);
```

⭐ Initiate the I2C communication and set the clock speed to 2M to generate accurate thermal scan (imaging) buffers via the MLX90641 thermal imaging camera.

```
  Wire.begin();
  Wire.setClock(2000000);
```

⭐ Check the I2C connection success with the MLX90641 thermal imaging camera and the camera parameter extraction status.

⭐ If the thermal imaging camera operates as expected and the parameter extraction is successful, release the *eeMLX90641* array and set the refresh rate to 16 Hz. 

```
  if(is_MLX_Connected() == false){
    st7735.fillScreen(ST77XX_RED);
    st7735.setCursor(0, 20);
    st7735.setTextColor(ST77XX_BLACK);
    st7735.println("MLX90641 not detected at default I2C address!");
    st7735.println("Please check wiring. Freezing.");
    while (1);
  }

  // Obtain the MLX90641 thermal imaging camera parameters and check the parameter extraction status.
  int status;
  status = MLX90641_DumpEE(MLX90641_address, eeMLX90641);
  errorno = status;
  //MLX90641_CheckEEPROMValid(eeMLX90641);//eeMLX90641[10] & 0x0040;
 
  if(status != 0){
    st7735.fillScreen(ST77XX_RED);
    st7735.setCursor(0, 20);
    st7735.setTextColor(ST77XX_BLACK);
    st7735.println("Failed to load MLX90641 system parameters!");
    while(1);
  }
 
  status = MLX90641_ExtractParameters(eeMLX90641, &MLX90641);
  if(status != 0){
    st7735.fillScreen(ST77XX_RED);
    st7735.setCursor(0, 20);
    st7735.setTextColor(ST77XX_BLACK);
    st7735.println("MLX90641 parameter extraction failed!");
    while(1);
  }

  // Once the MLX90641 parameters are extracted successfully, release the eeMLX90641 array and set the refresh rate to 16 Hz.
  MLX90641_SetRefreshRate(MLX90641_address, 0x05);
```

⭐ According to the analog joystick movements (UP or DOWN), adjust the highlighted menu option number and the screen update status.

```
  joystick_read();
  if(j_y_read > j_max) { menu_option = 0; b_update = true; delay(500); }
  if(j_y_read &lt; j_min) { menu_option = 1; b_update = true; delay(500); }
```

⭐ In the *show_interface* function:

⭐ According to the passed screen command and the menu option number, show the default home screen or the selected option layout.

⭐ Stop the home screen flickering by showing it for once when requested in the loop.

⭐ If the screen command is *scan*:

⭐ Show the associated interface icon on the layout.

⭐ Then, display the registration status indicators for each thermal imaging buffer with the assigned icons.

⭐ If the screen command is *inspect*:

⭐ Show the associated interface icon on the layout.

⭐ If all thermal scan (imaging) buffers are collected and registered successfully:

⭐ Obtain individual data points of each produced thermal buffer by converting them from strings to char arrays.

⭐ For each passed thermal imaging buffer ((16x12) x 4):

⭐ Define the coordinates for the first pixel.

⭐ Starting with the first pixel, draw each individual data point with the color indicator to display an accurate preview thermal image on the screen, estimated by the specific color algorithm based on the defined temperature threshold ranges.

⭐ After drawing a pixel successfully, update the successive data point coordinates.

⭐ If the registered thermal buffers do not meet the requirements, show the blank preview image to notify the user.

```
void show_interface(String command){
  if(command == "home"){
    adjustColor(0,0,0);
    st7735.fillScreen(_menu.background);
    // Define the menu option buttons.
    st7735.fillRoundRect(b_x, b_y, m_b_w, m_b_h, m_b_r, _menu.border);
    st7735.fillRoundRect(b_i_x, b_i_y, m_b_i_w, m_b_i_h, m_b_i_r, _menu.scan_c);
    st7735.setTextColor(_menu.text_c);
    st7735.setTextSize(2);
    st7735.setCursor(b_i_x+25, b_i_y+10);
    st7735.println("Scan");
    st7735.fillRoundRect(b_x, SCREEN_HEIGHT-b_y-m_b_h, m_b_w, m_b_h, m_b_r, _menu.border);
    st7735.fillRoundRect(b_i_x, SCREEN_HEIGHT-b_i_y-m_b_i_h, m_b_i_w, m_b_i_h, m_b_i_r, _menu.inspect_c);
    st7735.setCursor(b_i_x+8, SCREEN_HEIGHT-b_i_y-m_b_i_h+10);
    st7735.println("Inspect");
    // Show the interface (home) icon.
    st7735.fillRect(ic_x, ic_y, ic_w, ic_h, _menu.background);
    int i = 0;
    st7735.drawBitmap((SCREEN_WIDTH-interface_widths[i])/2, (SCREEN_HEIGHT-interface_heights[i])/2, interface_logos[i], interface_widths[i], interface_heights[i], _menu.menu_c);
    // Stop the screen flickering.
    show_home = false;
  }else if(command =="scan"){
    adjustColor(0,255,1);
    st7735.fillScreen(_menu.highlight);
    int i_x = menu_option+1;
    st7735.drawBitmap((SCREEN_WIDTH-interface_widths[i_x])/2, 10, interface_logos[i_x], interface_widths[i_x], interface_heights[i_x], _menu.scan_c);
    st7735.setTextSize(1); 
    st7735.setTextColor(_menu.scan_c);
    // According to the registered thermal scan buffers, show the assigned buffer status icons.
    int l_x = 5, l_y = 25+interface_heights[i_x], l_offset = 25;
    st7735.setCursor(l_x, l_y); st7735.println("Buffer [1] =>");
    st7735.drawBitmap(SCREEN_WIDTH-status_widths[_thermal.buff_1_st]-l_x, l_y-(status_heights[_thermal.buff_1_st]/2), status_logos[_thermal.buff_1_st], status_widths[_thermal.buff_1_st], status_heights[_thermal.buff_1_st], _menu.status_c[_thermal.buff_1_st]);
    st7735.setCursor(l_x, l_y+l_offset); st7735.println("Buffer [2] =>");
    st7735.drawBitmap(SCREEN_WIDTH-status_widths[_thermal.buff_2_st]-l_x, l_y-(status_heights[_thermal.buff_2_st]/2)+l_offset, status_logos[_thermal.buff_2_st], status_widths[_thermal.buff_2_st], status_heights[_thermal.buff_2_st], _menu.status_c[_thermal.buff_2_st]);
    st7735.setCursor(l_x, l_y+(2*l_offset)); st7735.println("Buffer [3] =>");
    st7735.drawBitmap(SCREEN_WIDTH-status_widths[_thermal.buff_3_st]-l_x, l_y-(status_heights[_thermal.buff_3_st]/2)+(2*l_offset), status_logos[_thermal.buff_3_st], status_widths[_thermal.buff_3_st], status_heights[_thermal.buff_3_st], _menu.status_c[_thermal.buff_3_st]);
    st7735.setCursor(l_x, l_y+(3*l_offset)); st7735.println("Buffer [4] =>");
    st7735.drawBitmap(SCREEN_WIDTH-status_widths[_thermal.buff_4_st]-l_x, l_y-(status_heights[_thermal.buff_4_st]/2)+(3*l_offset), status_logos[_thermal.buff_4_st], status_widths[_thermal.buff_4_st], status_heights[_thermal.buff_4_st], _menu.status_c[_thermal.buff_4_st]);
  }else if(command == "inspect"){
    adjustColor(255,255,0);
    st7735.fillScreen(_menu.highlight);
    int i_x = menu_option+1;
    st7735.drawBitmap(10, SCREEN_HEIGHT-interface_heights[i_x]-10, interface_logos[i_x], interface_widths[i_x], interface_heights[i_x], _menu.inspect_c);
    st7735.setTextSize(1);
    st7735.setTextColor(_menu.inspect_c);
    // Notify the user whether the required thermal scan buffers are registered or not.
    // If all of them registered successfully, generate and draw the preview thermal image from the passed buffers.
    int l_x = 20+interface_widths[i_x], l_y = SCREEN_HEIGHT-interface_heights[i_x]-10, l_offset = 10;
    if(_thermal.buff_1_st && _thermal.buff_2_st && _thermal.buff_3_st && _thermal.buff_4_st){
      st7735.setCursor(l_x, l_y); st7735.println("Press OK");
      st7735.setCursor(l_x, l_y+l_offset); st7735.println("to clear");
      st7735.setCursor(l_x, l_y+(2*l_offset)); st7735.println("thermal");
      st7735.setCursor(l_x, l_y+(3*l_offset)); st7735.println("image!");
      delay(500);
      // Obtain individual data points of each passed thermal buffer by converting them from strings to char arrays.
      const char *img_buff_points[] = {_thermal.buff_1.c_str(), _thermal.buff_2.c_str(), _thermal.buff_3.c_str(), _thermal.buff_4.c_str()};
      // Generate the preview thermal image [{16x12} x 4] by applying the specific color algorithm based on the defined temperature ranges.
      int p_w = 3, p_h = 4, img_x, img_x_s, img_y, img_y_s, p_num = 1, y_off = 10;
      int img_w = thermal_buff_width*p_w, img_h = thermal_buff_height*p_h;
      for(int t = 0; t &lt; thermal_buff_num; t++){
        // Define buffer starting points.
        if(t==0) img_x = img_x_s = (SCREEN_WIDTH-(img_w*2))/2, img_y = img_y_s = y_off;
        if(t==1) img_x = img_x_s = (SCREEN_WIDTH/2), img_y = img_y_s = y_off;
        if(t==2) img_x = img_x_s = (SCREEN_WIDTH-(img_w*2))/2, img_y = img_y_s = y_off+img_h;
        if(t==3) img_x = img_x_s = (SCREEN_WIDTH/2), img_y = img_y_s = y_off+img_h;
        for(int i = 0; i &lt; thermal_buff_size; i++){
          // Draw individual data points of each thermal buffer with the color indicator estimated by the given algorithm to generate a precise thermal image.
          switch(img_buff_points[t][i]){
            case 'w':
              st7735.fillRect(img_x, img_y, p_w, p_h, ST77XX_WHITE);
            break;
            case 'c':
              st7735.fillRect(img_x, img_y, p_w, p_h, ST77XX_CYAN);
            break;
            case 'b':
              st7735.fillRect(img_x, img_y, p_w, p_h, ST77XX_BLUE);
            break;
            case 'y':
              st7735.fillRect(img_x, img_y, p_w, p_h, ST77XX_YELLOW);
            break;
            case 'o':
              st7735.fillRect(img_x, img_y, p_w, p_h, st7735.color565(255, 165, 0));
            break;
            case 'r':
              st7735.fillRect(img_x, img_y, p_w, p_h, ST77XX_RED);
            break;
          }
          // Update the successive data point coordinates.
          img_x += p_w;
          if(p_num==thermal_buff_width){
            img_x = img_x_s;
            img_y += p_h;
            p_num=0;
          }
          p_num+=1;
        }
      }
    }else{
      st7735.setCursor(l_x, l_y); st7735.println("Please");
      st7735.setCursor(l_x, l_y+l_offset); st7735.println("register");
      st7735.setCursor(l_x, l_y+(2*l_offset)); st7735.println("all scan");
      st7735.setCursor(l_x, l_y+(3*l_offset)); st7735.println("buffers!");
      // If the registered buffers do not meet the requirements, show the blank thermal image — template.
      int p_w = 3, p_h = 4;
      int img_w = thermal_buff_width*p_w*2, img_h = thermal_buff_height*p_h*2, img_x = (SCREEN_WIDTH-img_w)/2, img_y = 10;
      st7735.fillRect(img_x, img_y, img_w, img_h, st7735.color565(144, 238, 144));
    }
  }
}
```

⭐ In the *get_and_display_data_from_MLX90641* function:

⭐ Get the required variables generated by the MLX90641 thermal imaging camera to calculate the IR array (16x12).

⭐ Estimate the temperature reflection loss based on the sensor's ambient temperature.

⭐ Then, compute and store the IR array.

⭐ Apply the specific algorithm based on the defined temperature ranges to convert each data point of the given IR array to color-based indicators.

⭐ Then, produce the thermal scan (imaging) buffer by appending each evaluated color indicator to the given string variable.

⭐ Finally, return the produced thermal imaging buffer — string.

```
String get_and_display_data_from_MLX90641(int buffer_size){
  String conv_buff;
  // Obtain the IR thermal imaging array (16x12 buffer) generated by the MLX90641 thermal imaging camera.
  for(byte x = 0 ; x &lt; 2 ; x++){
    int status = MLX90641_GetFrameData(MLX90641_address, MLX90641Frame);
    // Get the required MLX90641 variables to calculate the thermal imaging buffer.
    float vdd = MLX90641_GetVdd(MLX90641Frame, &MLX90641);
    float Ta = MLX90641_GetTa(MLX90641Frame, &MLX90641);
    // Estimate the temperature reflection loss based on the sensor's ambient temperature.
    float tr = Ta - TA_SHIFT; 
    float emissivity = 0.95;
    // Generate the thermal imaging array (buffer).
    MLX90641_CalculateTo(MLX90641Frame, &MLX90641, emissivity, tr, MLX90641To);
  }
  // According to the declared temperature threshold ranges, define a specific algorithm to convert each data point of the given thermal buffer to color-based indicators.
  for(int i = 0 ; i &lt; buffer_size ; i++){
    String _p;
    // Assess and assign a color-based indicator for the passed data point via the algorithm.
    if(MLX90641To[i] &lt;= min_temp) _p = 'w';
    if(MLX90641To[i] > min_temp && MLX90641To[i] &lt;= mod_temp_1) _p = 'c';
    if(MLX90641To[i] > mod_temp_1 && MLX90641To[i] &lt;= mod_temp_2) _p = 'b';
    if(MLX90641To[i] > mod_temp_2 && MLX90641To[i] &lt;= mod_temp_3) _p = 'y';
    if(MLX90641To[i] > mod_temp_3 && MLX90641To[i] &lt;= max_temp) _p = 'o';
    if(MLX90641To[i] > max_temp) _p = 'r';
    // Append the evaluated indicator as a string item to register the given buffer as an array (string).
    conv_buff += _p;
  }
  // Return the generated array (string).
  return conv_buff;
}
```

⭐ After changing the menu option number, highlight the selected option and show the associated icon on the home screen.

⭐ After highlighting a menu option on the home screen, if the joystick button is pressed, navigate to the selected option's layout.

⭐ If the first option *(Scan)* is activated:

⭐ If the control button OK is pressed, produce a thermal imaging buffer and assign the generated buffer to the predefined string variable linked to the Particle Cloud variable according to the current buffer number — from 0 to 3. Also, update the associated buffer registration status indicator as registered.

⭐ Then, increase the buffer number incrementally.

⭐ After registering thermal buffers, show the buffer status indicators with the assigned icons on the screen to inform the user of the ongoing procedure.

⭐ To avoid flickering, only update the latest changed buffer status indicator.

⭐ If the analog joystick moves to the left, redirect the user to the default home screen.

:hash: As mentioned earlier, the string variables are linked to the Particle Cloud variables. Since Photon 2 updates the cloud variables automatically when the linked variables are modified, do not forget to add delays in while loops. Otherwise, the while loop interrupts and blocks the Particle Cloud network connection (threading).

```
  if(menu_option == 0){
    if(b_update){
      st7735.fillRoundRect(b_i_x, b_i_y, m_b_i_w, m_b_i_h, m_b_i_r, _menu.highlight);
      st7735.setTextColor(_menu.text_c_h); st7735.setTextSize(2); st7735.setCursor(b_i_x+25, b_i_y+10); st7735.println("Scan");
      st7735.fillRoundRect(b_i_x, SCREEN_HEIGHT-b_i_y-m_b_i_h, m_b_i_w, m_b_i_h, m_b_i_r, _menu.inspect_c);
      st7735.setTextColor(_menu.text_c); st7735.setCursor(b_i_x+8, SCREEN_HEIGHT-b_i_y-m_b_i_h+10); st7735.println("Inspect");
      st7735.fillRect(ic_x, ic_y, ic_w, ic_h, _menu.background); int i_x = menu_option+1;
      st7735.drawBitmap((SCREEN_WIDTH-interface_widths[i_x])/2, (SCREEN_HEIGHT-interface_heights[i_x])/2, interface_logos[i_x], interface_widths[i_x], interface_heights[i_x], _menu.scan_c);
    }b_update = false;
    if(!j_b_read){
      s_update = true;
      show_interface("scan");
      while(s_update){
        joystick_read();
        // If the control button (OK) is pressed, generate thermal scan buffers
        // and assign the collected buffers to the associated arrays (strings) incrementally (from 1 to 4). 
        if(!c_b_read){
          if(buff_num == 0) { _thermal.buff_1 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_1_st = true;}
          if(buff_num == 1) { _thermal.buff_2 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_2_st = true;}
          if(buff_num == 2) { _thermal.buff_3 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_3_st = true;}
          if(buff_num == 3) { _thermal.buff_4 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_4_st = true;}
          // Change the associated array number.
          buff_num++; if(buff_num > 3) buff_num = 0;
          // Update the assigned buffer status icons after registering buffers to arrays (strings).
          buff_update = true;
          delay(250);
        }
        // Show the buffer status icons on the screen to inform the user of the ongoing procedure.
        if(buff_update){
          // Change the assigned status icon of the recently registered buffer.
          int i_x = menu_option+1, l_x = 5, l_y = 25+interface_heights[i_x], l_offset = 25;
          if(_thermal.buff_1_st){
            st7735.fillRect(SCREEN_WIDTH-status_widths[0]-l_x, l_y-(status_heights[0]/2), status_widths[0], status_heights[0], _menu.highlight);
            st7735.drawBitmap(SCREEN_WIDTH-status_widths[1]-l_x, l_y-(status_heights[1]/2), status_logos[1], status_widths[1], status_heights[1], _menu.status_c[1]);
          }
          if(_thermal.buff_2_st){
            st7735.fillRect(SCREEN_WIDTH-status_widths[0]-l_x, l_y-(status_heights[0]/2)+l_offset, status_widths[0], status_heights[0], _menu.highlight);
            st7735.drawBitmap(SCREEN_WIDTH-status_widths[1]-l_x, l_y-(status_heights[1]/2)+l_offset, status_logos[1], status_widths[1], status_heights[1], _menu.status_c[1]);
          }
          if(_thermal.buff_3_st){
            st7735.fillRect(SCREEN_WIDTH-status_widths[0]-l_x, l_y-(status_heights[0]/2)+(2*l_offset), status_widths[0], status_heights[0], _menu.highlight);
            st7735.drawBitmap(SCREEN_WIDTH-status_widths[1]-l_x, l_y-(status_heights[1]/2)+(2*l_offset), status_logos[1], status_widths[1], status_heights[1], _menu.status_c[1]);
          }
          if(_thermal.buff_4_st){
            st7735.fillRect(SCREEN_WIDTH-status_widths[0]-l_x, l_y-(status_heights[0]/2)+(3*l_offset), status_widths[0], status_heights[0], _menu.highlight);
            st7735.drawBitmap(SCREEN_WIDTH-status_widths[1]-l_x, l_y-(status_heights[1]/2)+(3*l_offset), status_logos[1], status_widths[1], status_heights[1], _menu.status_c[1]);
          }
          // Avoid flickering.
          buff_update = false;
        }
        // Do not forget to add delays in while loops. Otherwise, the while loop interrupts the Particle Cloud network connection.
        delay(2000);
        // If the X-axis of the joystick moves to the left, redirect the user to the home screen.
        if(j_x_read > j_max){
          s_update = false;
          show_home = true;
          menu_option = -1;
        }
      }
    }
  }
```

⭐ If the second option *(Inspect)* is activated:

⭐ Display the preview thermal image generated from the registered thermal imaging buffers on the layout.

⭐ If the registered thermal buffers do not meet the requirements, show the blank preview image.

⭐ If the control button OK is pressed, clear all registered thermal scan buffers and set their status indicators as blank. Then, remove the latest preview thermal image by displaying the blank one.

⭐ If the analog joystick moves to the left, redirect the user to the default home screen.

:hash: Do not forget to add delays in while loops. Otherwise, the while loop interrupts and blocks the Particle Cloud network connection (threading).

```
  if(menu_option == 1){
    if(b_update){
      st7735.fillRoundRect(b_i_x, b_i_y, m_b_i_w, m_b_i_h, m_b_i_r, _menu.scan_c);
      st7735.setTextColor(_menu.text_c); st7735.setTextSize(2); st7735.setCursor(b_i_x+25, b_i_y+10); st7735.println("Scan");
      st7735.fillRoundRect(b_i_x, SCREEN_HEIGHT-b_i_y-m_b_i_h, m_b_i_w, m_b_i_h, m_b_i_r, _menu.highlight);
      st7735.setTextColor(_menu.text_c_h); st7735.setCursor(b_i_x+8, SCREEN_HEIGHT-b_i_y-m_b_i_h+10); st7735.println("Inspect");
      st7735.fillRect(ic_x, ic_y, ic_w, ic_h, _menu.background); int i_x = menu_option+1;
      st7735.drawBitmap((SCREEN_WIDTH-interface_widths[i_x])/2, (SCREEN_HEIGHT-interface_heights[i_x])/2, interface_logos[i_x], interface_widths[i_x], interface_heights[i_x], _menu.inspect_c);
    }b_update = false;
    if(!j_b_read){
      s_update = true;
      show_interface("inspect");
      while(s_update){
        joystick_read();
        // If the control button (OK) is pressed, clear all thermal scan buffers and the latest generated thermal image.
        if(!c_b_read){
          _thermal.buff_1 = _thermal.buff_2 = _thermal.buff_3 = _thermal.buff_4 = "empty";
          _thermal.buff_1_st = _thermal.buff_2_st = _thermal.buff_3_st = _thermal.buff_4_st = false;
          buff_num = 0;
          delay(500);
          show_interface("inspect");
          delay(500);
        }
        // Do not forget to add delays in while loops. Otherwise, the while loop interrupts the Particle Cloud network connection.
        delay(2000);
        // If the X-axis of the joystick moves to the left, redirect the user to the home screen.
        if(j_x_read > j_max){
          s_update = false;
          show_home = true;
          menu_option = -1;
        }
      }
    }
  }
```

⭐ In the *collect_thermal_buffers* function:

:hash: As discussed earlier, this function is linked to a Particle Cloud function. Thus, the Particle Cloud API can access and execute the given function remotely.

⭐ According to the passed buffer number (from 1 to 4), produce a thermal imaging buffer and assign the generated buffer to the predefined string variable linked to the Particle Cloud variable.

⭐ Also, update the associated buffer status indicator as registered and blink the RGB LED as green to notify the user of the buffer registration success.

⭐ If requested, clear all registered thermal scan buffers and set their status indicators as blank.

```
int collect_thermal_buffers(String num){
  // If requested by the user, generate thermal scan (imaging) buffers
  // and assign the collected buffers to the associated arrays (strings) according to the passed buffer number (from 1 to 4). 
  if(num == "1"){
    _thermal.buff_1 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_1_st = true;
    buff_num = 1;
    adjustColor(0,255,0);
    delay(1000);
    adjustColor(0,0,0);
    buff_update = true;
    return buff_num;
  }else if(num == "2"){
    _thermal.buff_2 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_2_st = true;
    buff_num = 2;
    adjustColor(0,255,0);
    delay(1000);
    adjustColor(0,0,0);
    buff_update = true;
    return buff_num;
  }else if(num == "3"){
    _thermal.buff_3 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_3_st = true;
    buff_num = 3;
    adjustColor(0,255,0);
    delay(1000);
    adjustColor(0,0,0);
    buff_update = true;
    return buff_num;
  }else if(num == "4"){
    _thermal.buff_4 = get_and_display_data_from_MLX90641(thermal_buff_size); _thermal.buff_4_st = true;
    buff_num = 4;
    adjustColor(0,255,0);
    delay(1000);
    adjustColor(0,0,0);
    buff_update = true;
    return buff_num;
  }else if(num == "clear"){
    // If requested, clear all thermal scan buffers.
    _thermal.buff_1 = _thermal.buff_2 = _thermal.buff_3 = _thermal.buff_4 = "empty";
    _thermal.buff_1_st = _thermal.buff_2_st = _thermal.buff_3_st = _thermal.buff_4_st = false;
    buff_num = 0;
    adjustColor(0,0,1);
    delay(1000);
    adjustColor(0,0,0);
    buff_update = true;
    return buff_num;
  }else{
    adjustColor(255,0,0);
    delay(1000);
    adjustColor(0,0,0);
    return -1;
  }
}
```

![342](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_1.png)

![343](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_2.png)

![344](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_3.png)

![345](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_4.png)

![346](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_5.png)

![347](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_6.png)

![348](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_7.png)

![349](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_particle_8.png)

## Step 8.d: Producing accurate thermal images from the registered buffers and saving them as samples via the web application

⚠️🔊♨️🖼️ If the user presses the home button, Arduino Nano homes the thermal camera container head by employing the micro switch on the CNC router.

⚠️🔊♨️🖼️ When the homing sequence starts, Arduino Nano turns the RGB LED to blue. After returning the container head to the home position (0), it turns the RGB LED to white.

![350](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_0_home_1.jpg)

![351](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_0_home_2.jpg)

![352](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_homing.gif)

⚠️🔊♨️🖼️ If Particle Photon 2 establishes a successful connection with the Particle Cloud and all connected components operate as expected, the device shows the home screen on the ST7735 TFT display.

- Scan
- Inspect

⚠️🔊♨️🖼️ The device lets the user adjust the highlighted menu option on the home screen by moving the analog joystick — UP (↑) and DOWN (↓).

⚠️🔊♨️🖼️ After changing the highlighted menu option, the device also updates the icon on the home screen with the assigned option icon.

⚠️🔊♨️🖼️ As a menu option is highlighted, if the joystick button is pressed, the device navigates to the selected option's layout.

⚠️🔊♨️🖼️ Note: If the user moves the joystick to the left, Photon 2 returns to the default home screen.

![353](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_1.jpg)

⚠️🔊♨️🖼️ If the user activates the first menu option — *Scan*:

⚠️🔊♨️🖼️ The device shows the current buffer registration status indicators with the assigned icons on the screen to inform the user of the ongoing procedure. Then, the device turns the RGB LED to cyan.

⚠️🔊♨️🖼️ The device lets the user manually produce thermal imaging buffers and register the generated buffers to the linked Particle Cloud variables by pressing the control button OK. For each press, the device registers the produced buffer to the Particle Cloud incrementally — from 1 to 4.

⚠️🔊♨️🖼️ After registering a thermal imaging buffer successfully, the device updates the associated buffer status indicator as registered.

![354](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_2.jpg)

![355](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_3.jpg)

![356](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_4.jpg)

![357](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_5.jpg)

![358](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_6.jpg)

![359](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_7.jpg)

:hash: Since XIAO ESP32C6 communicates with the web application (dashboard) to handle the thermal imaging buffer collection in sync with the four-step CNC positioning sequence, the following descriptions show features performed by XIAO ESP32C6 and Photon 2 in tandem.

⚠️🔊♨️🖼️ If the user activates the third menu option provided by XIAO ESP32C6 — *CNC Positioning & Thermal Buffer Collection*:

⚠️🔊♨️🖼️ The device shows the buffer operation status indicators with the assigned icons on the SSD1306 OLED display for each thermal imaging buffer as *Waiting*.

![360](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_1.jpg)

![361](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_2.jpg)

⚠️🔊♨️🖼️ XIAO ESP32C6 transfers the first CNC positioning command to Arduino Nano via serial communication to initiate the four-step CNC positioning sequence. Then, the device updates the first buffer operation status indicator to *Ongoing*.

⚠️🔊♨️🖼️ After XIAO ESP32C6 sends a CNC positioning command, Arduino Nano informs the user of the positioning process by adjusting the RGB LED color.

- Red ➡ command received via serial communication
- Yellow ➡ the positioning process is completed
- Green ➡ the coordinate update confirmation message — *CNC_OK* — sent (replied) to XIAO ESP32C6 via serial communication

⚠️🔊♨️🖼️ After receiving the coordinate update confirmation message, XIAO ESP32C6 updates the associated buffer operation status indicator to *Completed* on the screen.

![362](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_3.jpg)

![363](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_4.jpg)

![364](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_5.jpg)

![365](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_6.jpg)

![366](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_7.jpg)

⚠️🔊♨️🖼️ Then, XIAO ESP32C6 makes an HTTP GET request to the web dashboard in order to make Photon 2 produce a thermal imaging buffer and register the generated buffer to the first linked cloud variable via the Particle Cloud API.

⚠️🔊♨️🖼️ After making the GET request successfully, the device updates the associated buffer operation status indicator to *Saved* on the screen.

![367](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_8.jpg)

⚠️🔊♨️🖼️ After the web application runs the linked cloud function via the Particle Cloud API, Photon 2 employs the MLX90641 thermal imaging camera to generate a 16x12 IR array.

⚠️🔊♨️🖼️ Then, Photon 2 applies the specific color algorithm to convert the generated IR array to a thermal imaging buffer based on the predefined temperature thresholds.

- 'w' ➜ White
- 'c' ➜ Cyan
- 'b' ➜ Blue
- 'y' ➜ Yellow
- 'o' ➜ Orange
- 'r' ➜ Red

⚠️🔊♨️🖼️ After producing the thermal imaging buffer successfully, Photon 2 turns the RGB LED to green and updates the first buffer registration status indicator to registered.

⚠️🔊♨️🖼️ Since Photon 2 updates the cloud variables automatically as the linked program variables are modified, the produced thermal imaging buffer is registered to the first linked cloud variable automatically.

⚠️🔊♨️🖼️ Then, the device turns off the RGB LED.

![368](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_1.jpg)

![369](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_2.jpg)

![370](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_3.jpg)

⚠️🔊♨️🖼️ Until concluding the four-step CNC positioning sequence and registering all required thermal imaging buffers to the Particle Cloud, the device repeats the same procedure.

![371](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_9.jpg)

![372](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_10.jpg)

![373](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_11.jpg)

![374](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_4.jpg)

![375](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_5.jpg)

![376](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_12.jpg)

![377](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_13.jpg)

![378](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_14.jpg)

![379](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_6.jpg)

![380](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_7.jpg)

![381](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_15.jpg)

![382](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_16.jpg)

![383](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_17.jpg)

![384](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_8.jpg)

![385](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_9.jpg)

⚠️🔊♨️🖼️ After finalizing the four-step CNC positioning sequence, XIAO ESP32C6 transmits the CNC zeroing command to Arduino Nano via serial communication.

⚠️🔊♨️🖼️ Then, Arduino Nano returns the thermal camera container head to the starting point (zeroing) by estimating the total revolved step number.

⚠️🔊♨️🖼️ After XIAO ESP32C6 sends the zeroing command, Arduino Nano informs the user of the zeroing process by adjusting the RGB LED color.

- Red ➡ command received via serial communication
- Yellow ➡ the zeroing process is completed
- Purple ➡ the zeroing confirmation message — *CNC_OK* — sent (replied) to XIAO ESP32C6 via serial communication

⚠️🔊♨️🖼️ After obtaining the zeroing confirmation message, XIAO ESP32C6 updates all buffer operation status indicators to *Image Ready* on the screen.

![386](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_18.jpg)

![387](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_19.jpg)

![388](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_20.jpg)

![389](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_collect_cnc_21.jpg)

⚠️🔊♨️🖼️ Then, XIAO ESP32C6 makes an HTTP GET request to the web dashboard in order to obtain all thermal imaging buffers registered on the Particle Cloud via the Particle Cloud API.

⚠️🔊♨️🖼️ As discussed in the previous steps, the web dashboard produces a precise thermal image (192 x 192) from the obtained buffers and saves the generated image on the server by running a Python script.

⚠️🔊♨️🖼️ After producing an accurate thermal image with the passed thermal imaging buffers successfully, the web application updates the system log on the MariaDB database accordingly.

⚠️🔊♨️🖼️ Finally, the web application updates its home (index) page automatically to showcase the latest system log entries. In addition to displaying the sample images and the collection dates, the web application lets the user download image samples individually on the home page.

![390](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_10.png)

⚠️🔊♨️🖼️ If the user activates the second menu option provided by Photon 2 — *Inspect*:

⚠️🔊♨️🖼️ The device turns the RGB LED to yellow.

⚠️🔊♨️🖼️ The device draws each individual data point (color-based indicator) of the registered buffers on the ST7735 TFT display to show an accurate preview (snapshot) thermal image.

⚠️🔊♨️🖼️ If the registered thermal buffers do not meet the requirements to produce a thermal image, show the blank preview image to notify the user.

⚠️🔊♨️🖼️ Also, the device lets the user clear all registered thermal scan buffers and set their status indicators as blank by pressing the control button OK. Then, it also removes the latest preview thermal image by displaying the blank one.

![391](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_8.jpg)

![392](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_9.jpg)

![393](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_10.jpg)

After producing thermal images manifesting stable and malfunctioning water-based HVAC system operations, I managed to construct a valid thermal image data set stored on the web application.

![394](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_collect_thermal.gif)

![395](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_collect_0.jpg)

![396](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_sample_collect_1.png)

![397](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_sample_collect_2.png)

![398](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_sample_collect_3.png)

![399](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_sample_collect_4.png)

## Step 9: Building a neural network model (Audio MFE) w/ Edge Impulse Enterprise

As discussed earlier, while collecting audio samples to construct a valid audio data set, I simply differentiated the generated audio samples by the cooling fan failure presence:

- normal
- defective

After finalizing my audio data set, I started to work on my Audio MFE neural network model to identify anomalous sound emanating from the cooling fans.

Since Edge Impulse provides developer-friendly tools for advanced AI applications and supports almost every development board due to its model deployment options, I decided to utilize Edge Impulse Enterprise to build my Audio MFE neural network model. Also, Edge Impulse Enterprise incorporates state-of-the-art machine learning algorithms and scales them for edge devices such as XIAO ESP32C6.

For sound-based abnormality detection, Edge Impulse provides the required tools for inspecting audio samples, slicing them into smaller windows, and modifying windows to extract features from the supported audio file formats — WAV, MP4, etc.

Even though [the Audio MFE processing block](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/audio-mfe) extracts time and frequency features from a signal, it employs a non-linear scale in the frequency domain, called Mel-scale. In that regard, the Audio MFE block extracts more features in the lower frequencies and fewer features in the high frequencies, thus it performs exceptionally well for non-voice recognition use cases.

Plausibly, Edge Impulse Enterprise allows building predictive models with enhanced machine learning algorithms optimized in size and precision and deploying the trained model as an Arduino library. Therefore, I was able to build an accurate Audio MFE neural network model to identify anomalous sound originating from the cooling fans and run the optimized model on XIAO ESP32C6 without any additional requirements.

You can inspect [my Audio MFE neural network model on Edge Impulse](https://studio.edgeimpulse.com/public/418121/latest) as a public project.

## Step 9.1: Uploading and processing samples

After splitting my audio data set into training and testing samples, I uploaded them to my project on Edge Impulse Enterprise.

:hash: First of all, to utilize the incorporated tools for advanced AI applications, sign up for [Edge Impulse Enterprise](https://edgeimpulse.com/pricing).

:hash: Then, create a new project under your organization.

![400](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_1.png)

:hash: Navigate to the *Data acquisition* page and click the *Upload data* icon.

![401](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_2.png)

:hash: Choose the data category (training or testing) and select WAV audio files.

:hash: Utilize the *Enter Label* section to label the passed audio samples automatically with the same class in the file names.

:hash: Then, click the *Upload data* button to upload the labeled audio samples.

![402](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_3.png)

![403](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_4.png)

![404](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_5.png)

![405](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_7.png)

![406](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_8.png)

![407](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_9.png)

![408](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_10.png)

![409](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_11.png)

![410](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_12.png)

![411](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_set_13.png)

## Step 9.2: Training the model on sound-based anomalous behavior

After uploading and labeling my training and testing samples successfully, I designed an impulse and trained the model to detect anomalous sound originating from the cooling fans of the water-based HVAC system.

An impulse is a custom machine learning model in Edge Impulse. I created my impulse by employing the *Audio (MFE)* processing block and the *Classification* learning block.

The *Audio MFE* processing block extracts time and frequency features from a signal and simplifies the generated features for non-voice recognition by using a non-linear scale — Mel-scale.

The *Classification* learning block represents a Keras neural network model. This learning block lets the user change the model settings, architecture, and layers.

:hash: Go to the *Create impulse* page and leave *Window size* and *Window increase* parameters as default. In this case, I did not need to slice the passed audio samples since all of them have roughly one-second duration.

![412](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_1.png)

:hash: Before generating features for the Audio MFE model, go to the *MFE* page to configure the block settings if necessary.

:hash: Since the MFE block transforms a generated window into a table of data where each row represents a range of frequencies and each column represents a span of time, you can configure block parameters to adjust the frequency amplitude to change the MFE's output — [spectrogram](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/spectrogram).

:hash: After inspecting the generated MFE parameters, I decided to utilize the default settings since my audio samples are simple and do not require precise tuning.

:hash: Click *Save parameters* to save the calculated MFE parameters.

![413](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_2.png)

![414](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_3.png)

![415](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_4.png)

![416](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_5.png)

:hash: After saving parameters, click *Generate features* to apply the *MFE* signal processing block to training samples.

![417](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_6.png)

![418](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_7.png)

:hash: Finally, navigate to the *Classifier* page and click *Start training*.

![419](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_8.png)

![420](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_9.png)

According to my prolonged experiments, I modified the neural network settings and architecture to achieve reliable accuracy and validity:

📌 Neural network settings:

- Number of training cycles ➡ 100  
- Learning rate ➡ 0.010
- Validation set size ➡ 10

After generating features and training my Audio MFE model, Edge Impulse evaluated the precision score (accuracy) as *100%*.

Since I configured this neural network model to conform to the cooling fans of my simplified HVAC system, the precision score (accuracy) is approximately *100%*. Thus, I highly recommend retraining the model before running inferences to detect anomalous sound emanating from different HVAC system components.

![421](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_10.png)

![422](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_train_11.png)

## Step 9.3: Evaluating the model accuracy and deploying the model

After building and training my Audio MFE neural network model, I tested its accuracy and validity by utilizing testing samples.

The evaluated accuracy of the model is *100%*.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

![423](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_test_1.png)

![424](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_test_2.png)

![425](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_test_3.png)

After validating my neural network model, I deployed it as a fully optimized and customizable Arduino library.

:hash: To deploy the validated model as an Arduino library, navigate to the *Deployment* page and search for *Arduino library*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as an Arduino library.

![426](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_deploy_1.png)

![427](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_deploy_2.png)

![428](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_audio_deploy_3.png)

## Step 10: Building a visual anomaly detection model (FOMO-AD) w/ Edge Impulse Enterprise

As discussed earlier, while producing thermal image samples to construct a valid image data set, I utilized the default classes to label the generated samples, required by Edge Impulse to enable the F1 score calculation:

- no anomaly
- anomaly

After finalizing my thermal image data set, I started to work on my visual anomaly detection model to diagnose ensuing thermal cooling malfunctions after applying anomalous sound detection to the water-based HVAC system.

Since Edge Impulse provides developer-friendly tools for advanced AI applications and supports almost every development board due to its model deployment options, I decided to utilize Edge Impulse Enterprise to build my visual anomaly detection model. Also, Edge Impulse Enterprise incorporates elaborate model architectures for advanced computer vision applications and optimizes the state-of-the-art vision models for edge devices and single-board computers such as LattePanda Mu.

Since analyzing cooling anomalies based on thermal images of HVAC system components is a complicated task, I decided to employ an advanced and precise machine learning algorithm based on the GMM anomaly detection algorithm enriched with the optimized features of the Edge Impulse FOMO model. Thus, supported by Edge Impulse Enterprise, FOMO-AD is an exceptional algorithm for detecting unanticipated defects by applying unsupervised learning techniques.

Although [the FOMO-AD visual anomaly detection model](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/visual-anomaly-detection) is based on the FOMO algorithm, the FOMO-AD models behave significantly differently than FOMO models. By definition, the FOMO-AD models train only on normal (stable) image samples. Thus, handling unseen data or anomalies is not a challenge since the algorithm does not rely on the existence of training data demonstrating all possible anomalies. However, in this regard, the model accuracy is not calculated during training, and Edge Impulse requires predefined labels (anomaly and no anomaly) to estimate the precision (F1) score by running the model testing process.

Plausibly, Edge Impulse Enterprise allows building advanced computer vision models optimized in size and accuracy efficiently and deploying the trained model as a supported firmware (Linux x86_64) for LattePanda Mu. Therefore, I was able to build an accurate visual anomaly detection model to diagnose thermal cooling malfunctions based on thermal images and run the optimized model on LattePanda Mu without any additional requirements.

You can inspect [my FOMO-AD visual anomaly detection model on Edge Impulse](https://studio.edgeimpulse.com/public/419123/latest) as a public project. 

## Step 10.1: Uploading images (samples) to Edge Impulse and assigning anomaly classes

After splitting my thermal image data set into training (stable) and testing (thermal malfunction) samples, I uploaded them to my project on Edge Impulse Enterprise.

:hash: First of all, to utilize the incorporated tools for advanced AI applications, sign up for [Edge Impulse Enterprise](https://edgeimpulse.com/pricing).

:hash: Then, create a new project under your organization.

![429](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_1.png)

:hash: To be able to label image samples manually on Edge Impulse for FOMO-AD visual anomaly detection models, go to *Dashboard ➡ Project info ➡ Labeling method* and select *One label per data item*.

![430](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_2.png)

:hash: Navigate to the *Data acquisition* page and click the *Upload data* icon.

![431](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_3.png)

:hash: Distinguish image samples as training and testing samples depending on the presence of anomaly (malfunction).

:hash: Choose the data category (training or testing) and select the associated image files.

:hash: Utilize the *Enter Label* section to label the passed image samples automatically with the required class — *no anomaly* for training and *anomaly* for testing.

:hash: Then, click the *Upload data* button to upload the labeled image samples.

![432](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_4.png)

![433](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_5.png)

![434](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_6.png)

![435](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_7.png)

![436](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_8.png)

![437](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_9.png)

![438](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_10.png)

![439](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_set_11.png)

## Step 10.2: Training the FOMO-AD model on the thermal images showcasing stable heat transfer

After uploading and labeling my training and testing samples with the default classes successfully, I designed an impulse and trained the model to diagnose ensuing thermal cooling malfunctions after applying anomalous sound detection to the water-based HVAC system.

An impulse is a custom machine learning model in Edge Impulse. I created my impulse by employing the *Image* processing block and the *FOMO-AD (Images)* learning block.

The *Image* processing block optionally turns the input image format to grayscale or RGB and generates a features array from the passed raw image.

The *FOMO-AD (Images)* learning block represents a machine learning algorithm that identifies anomalies based on the trained normal (stable) images by applying a Gaussian Mixture Model.

In this case, I configured the input image format as RGB since distinguishing thermal cooling malfunctions based on thermal images highly relies on color differences.

As stated by Edge Impulse, they empirically obtained the best anomaly detection results by applying 96x96 ImageNet weights regardless of the intended raw image input resolution. Thus, I utilized the same resolution for my visual anomaly detection model.

:hash: Go to the *Create impulse* page and set image width and height parameters to 96. Then, select the resize mode parameter as *Fit shortest axis* so as to scale (resize) given training and testing image samples.

:hash: Select the *Image* processing block.

![440](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_1.png)

:hash: Then, to choose the visual anomaly detection algorithm, click *Add a learning block* and select the *FOMO-AD (Images)* learning block. Finally, click *Save Impulse*.

![441](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_2.png)

![442](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_3.png)

:hash: Before generating features for the visual anomaly detection model, go to the *Image* page and set the *Color depth* parameter as *RGB*. Then, click *Save parameters*.

![443](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_4.png)

:hash: After saving parameters, click *Generate features* to apply the *Image* processing block to training image samples.

![444](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_5.png)

![445](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_6.png)

:hash: After generating features successfully, navigate to the *FOMO-AD* page and click *Start training*.

![446](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_7.png)

:hash: According to my prolonged experiments, I modified the neural network settings and architecture to achieve reliable accuracy and validity:

📌 Neural network settings:

- Capacity ➡ High

📌 Neural network architecture:

- MobileNetV2 0.35

The FOMO-AD learning block has one adjustable parameter — capacity. Higher capacity means a higher number of Gaussian components, increasing the model adaptability considering the original distribution.

As discussed earlier, by definition, Edge Impulse does not evaluate the precision score (accuracy) during training.

![447](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_8.png)

![448](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_train_9.png)

## Step 10.3: Evaluating the model accuracy and deploying the model

After building and training my FOMO-AD visual anomaly detection model, I tested its accuracy and validity by utilizing testing samples.

In addition to validating the model during testing, Edge Impulse evaluates the F1 precision score (accuracy) and provides per region anomalous scoring results for the passed testing images. To tweak the learning block sensitivity, Edge Impulse lets the user change the suggested confidence threshold estimated based on the top anomaly scores in the training dataset. In that regard, the user can adjust the anomaly detection rate according to the expected real-world conditions.

After validating my FOMO-AD model, Edge Impulse evaluated the precision score (accuracy) as *100%*.

Since I configured this visual anomaly detection model to conform to the produced thermal images of my simplified HVAC system components, the precision score (accuracy) is approximately *100%*. Thus, I highly recommend constructing a new thermal image data set of different HVAC system components and retraining the model before running inferences to diagnose thermal cooling malfunctions.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

![449](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_1.png)

![450](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_2.png)

:hash: Then, click the *Gear* icon and select *Set confidence thresholds* to tweak the learning block sensitivity to adjust the anomaly detection rate based on the expected real-world conditions.

According to my rigorous experiments, I set the confidence threshold as 5.

![451](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_3.png)

![452](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_4.png)

![453](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_5.png)

:hash: After setting the confidence threshold, select a testing image sample and click *Show classification* to inspect the detected label and the per region anomalous scoring results.

Since this classification page provides max and mean anomaly scores, Edge Impulse lets the user compare region anomaly results effortlessly based on the altered confidence thresholds.

![454](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_6.png)

![455](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_test_7.png)

After setting the confidence threshold, I deployed my visual anomaly detection model as a fully optimized and customizable Linux (x86_64) application (.eim).

:hash: To deploy the validated model as a Linux (x86_64) application, navigate to the *Deployment* page and search for *Linux (x86)*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as a Linux (x86_64) application (.eim).

![456](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_deploy_1.png)

![457](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_deploy_2.png)

![458](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_thermal_deploy_3.png)

## Step 11.a: Setting up the neural network model (Audio MFE) on XIAO ESP32C6

Since Edge Impulse optimizes and formats signal processing, configuration, and learning blocks into a single package while deploying models as Arduino libraries, even for complex machine learning algorithms, I was able to import my advanced model effortlessly to run inferences on XIAO ESP32C6.

:hash: After downloading the model as an Arduino library in the ZIP file format, go to *Sketch ➡ Include Library ➡ Add .ZIP Library...*

:hash: Then, include the *AI-driven_HVAC_Fault_Diagnosis_Audio__inferencing.h* file to import the Edge Impulse Audio MFE neural network model.

```
#include &lt;AI-driven_HVAC_Fault_Diagnosis_Audio__inferencing.h>
```

After importing my model successfully, I programmed XIAO ESP32C6 to run inferences to identify anomalous sound emanating from the cooling fans.

However, the Arduino IDE kept throwing a compile error message as shown below during my initial experiments.

```
error: either all initializer clauses should be designated or none of them should be ...
```

:hash: To solve the mentioned compiling error, open the *ei_classifier_config.h* file and set *EI_CLASSIFIER_TFLITE_ENABLE_ESP_NN* to 0.

* \Arduino\libraries\AI-driven_HVAC_Fault_Diagnosis_Audio__inferencing\src\edge-impulse-sdk\classifier\ei_classifier_config.h*

```
//#define EI_CLASSIFIER_TFLITE_ENABLE_ESP_NN   1
#define EI_CLASSIFIER_TFLITE_ENABLE_ESP_NN     0 // set to
```

![459](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_xiao_compile_error_1.png)

![460](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/edge_xiao_compile_error_2.png)

As explained in the previous steps, the device performs lots of interconnected features between different development boards and the web application for data collection and running advanced AI models. Thus, the described code snippets show the different aspects of the same code file. Please refer to the code files or the demonstration videos to inspect all interconnected functions in detail.

📁 *HVAC_fault_diagnosis_anomalous_sound.ino*

⭐ Define the required parameters to run an inference with the Edge Impulse Audio MFE neural network model.

⭐ Define the threshold value for the model outputs (predictions).

⭐ Define the anomalous sound (audio) class names.

```
#define buf_multiplier   5
#define audio_buff_size  512
int16_t sample_audio_buffer[audio_buff_size];

// Define the threshold value for the model outputs (predictions).
float threshold = 0.60;

// Define the anomalous sound (audio) class names.
String classes[] = {"defective", "normal"};
```

⭐ In the *run_inference_to_make_predictions* function:

⭐ Summarize the Edge Impulse neural network model (Audio MFE) inference settings and print them on the serial monitor.

⭐ If the I2S microphone generates a raw audio (data) buffer successfully:

⭐ Create a signal object from the resized (scaled) raw data buffer — raw audio buffer.

⭐ Run an inference.

⭐ Print the inference timings on the serial monitor.

⭐ Obtain the prediction results for each label (class).

⭐ Print the model classification results on the serial monitor.

⭐ Get the predicted label (class) explicitly based on the given threshold.

⭐ Print inference anomalies on the serial monitor, if any.

⭐ Release the previously generated raw audio buffer if requested.

```
void run_inference_to_make_predictions(){
  // Summarize the Edge Impulse neural network model (Audio MFE) inference settings (from model_metadata.h):
  ei_printf("\nInference settings:\n");
  ei_printf("\tInterval: "); ei_printf_float((float)EI_CLASSIFIER_INTERVAL_MS); ei_printf(" ms.\n");
  ei_printf("\tFrame size: %d\n", EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE);
  ei_printf("\tSample length: %d ms.\n", EI_CLASSIFIER_RAW_SAMPLE_COUNT / 16);
  ei_printf("\tNo. of classes: %d\n", sizeof(ei_classifier_inferencing_categories) / sizeof(ei_classifier_inferencing_categories[0]));

  // If the I2S microphone generates a raw audio (data) buffer successfully:
  if(microphone_sample(false)){
    // Run inference:
    ei::signal_t signal;
    // Create a signal object from the resized (scaled) audio buffer.
    signal.total_length = EI_CLASSIFIER_RAW_SAMPLE_COUNT;
    signal.get_data = &microphone_audio_signal_get_data;
    // Run the classifier:
    ei_impulse_result_t result = { 0 };
    EI_IMPULSE_ERROR _err = run_classifier(&signal, &result, false);
    if(_err != EI_IMPULSE_OK){
      ei_printf("ERR: Failed to run classifier (%d)\n", _err);
      return;
    }

    // Print the inference timings on the serial monitor.
    ei_printf("\nPredictions (DSP: %d ms., Classification: %d ms., Anomaly: %d ms.): \n",
        result.timing.dsp, result.timing.classification, result.timing.anomaly);

    // Obtain the prediction results for each label (class).
    for(size_t ix = 0; ix &lt; EI_CLASSIFIER_LABEL_COUNT; ix++){
      // Print the prediction results on the serial monitor.
      ei_printf("%s:\t%.5f\n", result.classification[ix].label, result.classification[ix].value);
      // Get the imperative predicted label (class).
      if(result.classification[ix].value >= threshold) predicted_class = ix;
    }
    ei_printf("\nPredicted Class: %d [%s]\n", predicted_class, classes[predicted_class]);  

    // Detect classifier anomalies, if any:
    #if EI_CLASSIFIER_HAS_ANOMALY == 1
      ei_printf("Anomaly: ");
      ei_printf_float(result.anomaly);
      ei_printf("\n");
    #endif 

    // Release the audio buffer.
    //ei_free(sample_audio_buffer);
  }
}
```

⭐ In the *microphone_audio_signal_get_data* function:

⭐ Convert the given microphone (raw audio) data (buffer) to the *out_ptr* format required by the Edge Impulse neural network model (Audio MFE).

```
static int microphone_audio_signal_get_data(size_t offset, size_t length, float *out_ptr){
  // Convert the given microphone (audio) data (buffer) to the out_ptr format required by the Edge Impulse neural network model (Audio MFE).
  numpy::int16_to_float(&sample_audio_buffer[offset], out_ptr, length);
  return 0;
}
```

⭐ If the second option *(Faulty Sound)* is activated:

⭐ Every five seconds, run an inference with the Edge Impulse Audio MFE neural network model.

⭐ If the given model detects anomalous sound originating from the cooling fans:

⭐ Clear the previously assigned buffer operation status indicators.

⭐ Start the four-step CNC positioning sequence to collect thermal imaging buffers and produce a precise thermal image.

:hash: The process is the same for generating a sample thermal image — the third option — except for the passed process type (GET request parameter). This time, the web application utilizes the produced thermal image to run an inference with the Edge Impulse FOMO-AD visual anomaly detection model and generate a model resulting image.

⭐ If the control button D is pressed, redirect the user to the home screen.

![461](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_4.png)

![462](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_xiao_5.png)

## Step 11.b: Setting up the visual anomaly detection model (FOMO-AD) on LattePanda Mu

Since Edge Impulse optimizes and formats signal processing, configuration, and learning blocks into a single EIM file while deploying models as a Linux (x86_64) application, even for complex visual anomaly detection models, I was able to import my advanced FOMO-AD model effortlessly to run inferences in Python on LattePanda Mu (x86 Compute Module).

:hash: After downloading the generated Linux (x86_64) application to the *model* folder under the root folder of the web application, make sure to change the file permissions via the *Properties* tab to be able to execute the model file. As shown earlier, you can also use the terminal (shell) to change file permissions.

![463](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/model_set_1.png)

After importing the generated Linux application successfully, I programmed LattePanda Mu to run inferences to diagnose thermal cooling malfunctions of HVAC system components based on specifically produced thermal images.

Since I described all of the web application features earlier, including the Python script handling thermal image generation, running the visual anomaly detection model, and modifying the resulting image based on the visual anomaly grid with estimated cell anomaly intensity levels, please refer to Step 5.2 to inspect code snippets.

![464](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/code_web_python_1.png)

## Step 11.c: Running both machine learning models consecutively to detect anomalous sound originating from the cooling fans and diagnose ensuing thermal cooling malfunctions of the HVAC system and informing the user of the cooling status via SMS

⚠️🔊♨️🖼️ If the user activates the second menu option provided by XIAO ESP32C6 — *Faulty Sound*:

![465](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_1.jpg)

⚠️🔊♨️🖼️ XIAO ESP32C6 generates a raw audio buffer via the I2S microphone and runs an inference with the Edge Impulse Audio MFE neural network model every five seconds to identify anomalous sound originating from the HVAC system cooling fans.

⚠️🔊♨️🖼️ Then, the device shows the detected audio class and its associated icon on the SSD1306 OLED display.

![466](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_2.jpg)

![467](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_3.jpg)

⚠️🔊♨️🖼️ If the Audio MFE detects anomalous sound, XIAO ESP32C6 initiates the four-step CNC positioning sequence to collect thermal imaging buffers and produce a precise thermal image via the web application.

⚠️🔊♨️🖼️ Except for the passed process type (detection) while making an HTTP GET request to the web application, the process is exactly the same for producing a thermal image sample as explained in Step 8.d.

![468](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_4.jpg)

![469](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_5.jpg)

![470](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_6.jpg)

![471](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_7.jpg)

![472](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_8.jpg)

![473](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_9.jpg)

![474](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_10.jpg)

![475](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_11.jpg)

![476](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_12.jpg)

![477](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_13.jpg)

![478](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_14.jpg)

![479](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_15.jpg)

![480](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_16.jpg)

![481](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/sound_run_17.jpg)

⚠️🔊♨️🖼️ After obtaining the thermal scan (imaging) buffers registered on the Particle Cloud, the web application produces a precise thermal image by running the Python script as shown in Step 8.d.

⚠️🔊♨️🖼️ However, instead of saving the produced image as a sample directly, the web application runs an inference with the Edge Impulse FOMO-AD visual anomaly detection model to diagnose consecutive thermal cooling malfunctions of HVAC system components after anomalous sound detection.

⚠️🔊♨️🖼️ Since the FOMO-AD model categorizes a passed image by individual cells (grids) based on the dichotomy between two predefined classes (anomaly and no anomaly), the web application utilizes the mean visual anomaly value to diagnose overall (high-risk) thermal cooling malfunctions based on the given confidence threshold.

⚠️🔊♨️🖼️ If the mean visual anomaly value is smaller than the given threshold, the web application saves the model resulting image directly by adding the prediction date to the file name.

*normal__2024_06_21_18_08_41.jpg*

![482](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/normal__2024_06_21_18_08_41.jpg)

⚠️🔊♨️🖼️ Otherwise, the web application obtains the visual anomaly grid, consisting of individual cells with coordinates, assigned labels, and anomaly scores.

⚠️🔊♨️🖼️ If a cell's assigned label is anomaly, the web application calculates the cell's anomaly intensity level — Low (L), Moderate (M), High (H) — in relation to the given threshold.

⚠️🔊♨️🖼️ Then, the web application modifies the resulting image with the cells (rectangles) and their intensity levels, emphasizing the risk of component abnormalities.

⚠️🔊♨️🖼️ After modifying the resulting image, the web application saves it by adding the prediction date to the file name.

*malfunction__2024_06_21_18_22_19.jpg*

![483](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/malfunction__2024_06_21_18_22_19.jpg)

![484](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/malfunction__2024_06_21_18_28_16.jpg)

⚠️🔊♨️🖼️ After generating and saving the model resulting image, the web application updates the system log on the MariaDB database accordingly.

![485](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/database_set_5.png)

![486](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/database_set_6.png)

⚠️🔊♨️🖼️ Then, the web application updates its home (index) page automatically to showcase the latest system log entries. In addition to displaying the model resulting images, anomalous sound notifications, thermal cooling malfunction status, and prediction dates, the web application lets the user download modified resulting images individually on the home page.

⚠️🔊♨️🖼️ Furthermore, the web dashboard allows the user to change the system log update category to display only the associated system log entries.

- All
- Cooling Malfunction Detections
- Thermal Image Samples
- Anamolous Sound Samples

![487](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_8.png)

![488](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_app_work_9.png)

⚠️🔊♨️🖼️ Finally, the web application sends an SMS via Twilio to inform the user of anomalous sound detection and the status of the ensuing thermal cooling malfunctions of HVAC system components.

![489](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_sms_1.jpg)

![490](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_sms_2.jpg)

![491](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/twilio_sms_3.jpg)

⚠️🔊♨️🖼️ If the user activates the second menu option provided by Photon 2 — *Inspect:*

⚠️🔊♨️🖼️ Similar to the image sample generation, the device draws each individual data point (color-based indicator) of the registered buffers on the ST7735 TFT display to show an accurate preview (snapshot) thermal image.

![492](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_10.jpg)

⚠️🔊♨️🖼️ Also, XIAO ESP32C6 prints progression notifications on the serial monitor for debugging.

![493](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/serial_xiao_1.png)

While conducting experiments with this HVAC system malfunction detection device, I added an aquarium heater to the water reservoir to artificially increase the temperature of the water circulating in the closed-loop system. In that regard, I was able to simulate and diagnose thermal cooling malfunctions of HVAC system components (aluminum blocks) after identifying anomalous sound originating from the cooling fans.

![494](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/gif_run_models.gif)

![495](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_0.1.jpg)

![496](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_0.2.jpg)

![497](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/thermal_run_0.3.jpg)

![498](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_detection_1.png)

![499](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_detection_2.png)

![500](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_detection_3.png)

![501](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/web_dashboard_img_detection_4.png)

## Further Discussions

By applying advanced AI-powered multi-algorithm detection methods to identify anomalous sound emanating from the cooling fans and diagnose ensuing thermal cooling malfunctions of water-based HVAC system components, we can achieve to:

⚠️🔊♨️🖼️ prevent pernicious cooling aberrations deteriorating heat regulation for industrial facilities,

⚠️🔊♨️🖼️ avert production downtime for demanding industrial processes,

⚠️🔊♨️🖼️ reduce production costs and increase manufacturing efficiency,

⚠️🔊♨️🖼️ obviate excessive energy consumption via real-time (automated) malfunction diagnosis,

⚠️🔊♨️🖼️ extend equipment lifespan by maintaining stable heat transfer,

⚠️🔊♨️🖼️ deter exorbitant overhaul processes due to prolonged negligence, leading to a nosedive in production quality.

![502](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/all_system_assembly_18_completed.jpg)

## Project GitHub Repository

As a developer, if you want to inspect or access code files and custom design files effortlessly, you can visit [the project's GitHub repository](https://github.com/KutluhanAktar/AI-driven-Sound-Thermal-Image-based-HVAC-Fault-Diagnosis/), providing:

- Code files
- Gerber files
- STL files
- Custom libraries
- Edge Impulse machine learning models — Audio MFE and FOMO-AD

## References

[^1] *What is an Industrial Water-Based Cooling System and How Does it Work?*, ChemREADY, *https://www.getchemready.com/water-facts/what-is-an-industrial-water-based-cooling-system-and-how-does-it-work/*.

[^2] *Industrial water cooling systems-chillers*, Atlas Copco, *https://www.atlascopco.com/en-uk/compressors/products/industrial-water-cooling-systems*.

[^3] Jian Bi, Hua Wang, Enbo Yan, Chuan Wang, Ke Yan, Liangliang Jiang, Bin Yang, *AI in HVAC fault detection and diagnosis: A systematic review*, Energy Reviews, Volume 3, Issue 2, 2024, *https://doi.org/10.1016/j.enrev.2024.100071*.

[^4] Herbert W. Stanford III, *HVAC Water Chillers and Cooling Towers: Fundamentals, Application, and Operation*, CRC Press, 2nd edition, March 29, 2017, Page: 16-28, *https://books.google.com.tr/books?hl=en&lr=&id=KDteO_-GaLkC&oi=fnd&pg=PR1#v=onepage&q&f=false*.

## Schematics

![1](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_sound_cnc_0.png)

![2](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_sound_cnc_1.png)

![3](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_sound_cnc_2.png)

![4](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_sound_cnc_3.png)

![5](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_sound_cnc_4.png)

![6](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_sound_cnc_5.png)

![7](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_thermal_cloud_0.png)

![8](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_thermal_cloud_1.png)

![9](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_thermal_cloud_2.png)

![10](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_thermal_cloud_3.png)

![11](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_thermal_cloud_4.png)

![12](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/PCB_hvac_thermal_cloud_5.png)

![13](../.gitbook/assets/multimodal-hvac-failure-anomaly-detection-esp32/xiao_esp32c6_schematic.png)

