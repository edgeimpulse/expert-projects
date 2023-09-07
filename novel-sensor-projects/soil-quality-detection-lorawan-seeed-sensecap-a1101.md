---
description: >-
  An edge device that can analyze fertilizer contamination and estimate soil
  quality using a Seeed Studio Sensecap A1101 and Edge Impulse.
---

# Sensecap A1101 - Soil Quality Detection Using AI and LoRaWAN

Created By: Kutluhan Aktar

Public Project Link: [https://studio.edgeimpulse.com/public/233660/latest](https://studio.edgeimpulse.com/public/233660/latest)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/finished\_1.jpg)

## Description

To achieve a successful harvest season with prolific plants, farmers utilized a type of fertilizer to increase soil fertility, dating back to the earliest attempts to provide enough food in order to sustain larger populations. Until the industrial revolution, farmers mostly applied organic fertilizers and materials to supply adequate nutrients for plants, including naturally available mineral sources, manure, crop residues, etc. However, due to the evergrowing human population and declining fertile lands, agriculturalists started to utilize organic fertilizers in conjunction with chemical fertilizers to improve crop yield, even to the extent of causing soil contamination.

Chemical fertilizers are synthesized industrially out of estimated proportions of elements like nitrogen, phosphorus, and potassium\[^1], which provide necessary nutrients for plants to flourish vigorously. Due to intensive cultivation and the insufficient replenishment of nutrients, fertilizers mitigate precipitously declining soil fertility. In combination with organic fertilizers, chemical fertilizers can even revitalize arable lands. Although chemical fertilizers are indispensable to sustain soil fertility and avoid food shortages considering the current human population, they can also be noxious without painstaking attention to soil test reports. Since chemical fertilizers directly affect soil integrity and permeate through water bodies, they can contaminate the groundwater and the environment. Also, chemical fertilizers infiltrate the soil and make plants vulnerable to various pathogens by hampering their roots\[^1].

When chemical fertilizers disperse throughout water bodies, they increase macronutrients in the environment, such as nitrogen, potassium, and phosphorus, resulting in contamination and eutrophication (nutrient pollution). These macronutrients can cause serious health problems due to overexposure. For instance, nitrogen can remain in water bodies for several years and cause nitrite (and nitrate) to accumulate exponentially. As a result of the high nitrite accumulation, nitrite-contaminated water can cause a blood disorder called methemoglobinemia (MetHb), also known as Blue Baby Syndrome. Furthermore, chemical reactions between nitrites heavily used in synthetic fertilizers instigate DNA damage, lipid peroxidation, and oxidative stress, which can all result in increased cellular degeneration. As a major health issue caused by the excessive use of chemical (synthetic) fertilizers, cellular degeneration can increase the risk of developing cancer. Forebodingly, a 2009 study by researchers at Rhode Island Hospital has found a substantial link between increased levels of nitrates in our environment and food with increased deaths from diseases, including Alzheimer's, diabetes mellitus, and Parkinson's\[^2].

According to earlier estimations, fertilizers provided approximately 70% of plant nutrients in 2020 at a global level\[^3]. Therefore, at this point, we cannot obviate the need for organic and chemical fertilizers to achieve sustainable crop production. Nevertheless, applying organic fertilizers in conjunction with chemical fertilizers can engender unexpected results and exacerbates the detrimental effects of chemical (synthetic) fertilizers. Since organic fertilizers behave differently depending on their manufacturing conditions, they change the degree of soil permeability of different soil types, such as loamy, peaty, silty, chalky, etc., not only unpredictably but also structurally. Hence, applying chemical fertilizers to the soil structurally altered by organic fertilizers may intensify the mentioned hazardous effects and lead to serious health conditions.

After scrutinizing the recent research papers on the effects of chemical and organic fertilizers, I noticed there are nearly no appliances focusing on detecting the excessive use of chemical fertilizers in the presence of organic fertilizers and providing real-time detection results for further inspection. Therefore, I decided to build a budget-friendly and easy-to-use proof-of-concept device to detect chemical fertilizer contamination levels with object recognition and inform the user of the model detection results simultaneously in the hope of averting the detrimental effects of fertilizer overuse by pre-warning farmers.

To detect chemical fertilizer contamination levels accurately in relation to organic fertilizers, I needed to collect data from a controlled environment manifesting different soil conditions so as to train my object detection model with notable validity. Since utilizing manure as organic fertilizer affects soil acidification, integrity, and structure depending on the manure decomposition stages (fresh, active, mature, and old), I decided to produce my organic fertilizers by composting manure. Fortunately, I am raising quails on my balcony and have experience in utilizing quail manure as organic fertilizer. To change the soil integrity and structure in relation to the applied organic fertilizer, I collected quail manure in different decomposition stages:

* Fresh (1 month)
* Active (3 months)
* Old (6 months)

After producing organic fertilizers in different decomposition stages, I applied them to the soil in three separate flowerpots. Then, I added chemical fertilizers to each flowerpot in the same amount to examine the excessive use of chemical fertilizers depending on the soil integrity and structure. To demonstrate the fertilizer contamination effects on the environment, I sowed different types of tomato seedlings in each flowerpot.

* Calcium Nitrate
* Magnesium Sulphate
* Ammonium Sulphate
* Ammonium Phosphate

Since Wi-Fi and Bluetooth transmissions may not be suitable options for a device operating in farms, I decided to utilize a [SenseCAP A1101 Vision AI](https://www.seeedstudio.com/SenseCAP-A1101-LoRaWAN-Vision-AI-Sensor-p-5367.html) sensor manufactured by Seeed Studio. The SenseCAP A1101 provides a 400Mhz DSP Himax camera for image recognition and a Wio-E5 LoRaWAN module for LoRaWAN long-range transmission. Also, it is compatible with different types of LoRaWAN® gateways and networks, such as the Helium LongFi Network. As shown in the following steps, I explained how to activate a SenseCAP M2 data-only LoRaWAN indoor gateway (EU868) and connect SenseCAP A1101 to the Helium LongFi Network through the SenseCAP M2 data-only gateway. SenseCAP gateways are only required if the Helium network does not cover your surroundings. Since SenseCAP A1101 supports uploading TinyML object detection models as firmware, I was able to run my model without a single line of code. Nevertheless, SenseCAP A1101 does not give you the option to capture images with different labels out of the box. Therefore, I connected three control buttons and an SH1106 OLED screen to Arduino Nano in order to build a simple remote control. Then, I employed LattePanda 3 Delta to program SenseCAP A1101 to capture images according to labels transferred by the remote control via serial communication.

After completing my data set by taking pictures of fertilizer-exerted soils from my three separate flowerpots, I built my object detection model with Edge Impulse to detect chemical fertilizer contamination levels. I utilized Edge Impulse FOMO (Faster Objects, More Objects) algorithm to train my model, which is a novel machine learning algorithm that brings object detection to highly constrained devices. Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I have not encountered any issues while uploading and running my model on SenseCAP A1101.

As labels, I utilized fertilizer contamination levels based on the soil integrity and structure altered by the applied organic fertilizer (manure) decomposition stage:

* Enriched
* Unsafe
* Toxic

After training and testing my object detection (FOMO) model, I deployed and uploaded the model on SenseCAP A1101 as its compatible firmware (UF2). Therefore, the device is capable of detecting fertilizer contamination levels by running the model independently without any additional procedures or latency.

Since I focused on building a full-fledged AIoT appliance detecting fertilizer contamination levels despite utilizing the LoRaWAN network as the primary transmission method, I decided to develop a Python application from scratch informing the user of the recent model detection results via WhatsApp. Plausibly, all SenseCAP AI devices are capable of logging information to the SenseCAP Portal via the LoRaWAN network. Also, Seeed Studio provides the SenseCAP HTTP API to obtain registered data records from the SenseCAP Portal via HTTP GET requests. Therefore, firstly, I utilized the application to get the recent model detection results from the given SenseCAP Portal account.

Then, this complementing application employs Twilio's WhatsApp API to send the latest model detection results to the verified phone number, which SenseCAP A1101 registered to the SenseCAP Portal via the Helium LongFi Network.

Since I decided to capture images with SenseCAP A1101 and run my Python application on LattePanda 3 Delta, I wanted to build a mobile and compact apparatus to access LattePanda 3 Delta in the field without requiring an additional procedure. To improve the user experience, I utilized a high-quality 8.8" IPS monitor from Elecrow. As explained in the following steps, I designed a two-part case (3D printable) in which I placed the Elecrow IPS monitor.

Lastly, to make the device as robust and sturdy as possible while operating outdoors, I designed a plant-themed case providing screw holes to attach the SenseCAP A1101 bracket, a sliding front cover, and a separate section for the remote control compatible with a diagonal top cover with snap-fit joints (3D printable).

So, this is my project in a nutshell 😃

In the following steps, you can find more detailed information on coding, capturing soil images with SenseCAP A1101, building an object detection (FOMO) model with Edge Impulse, running the model on SenseCAP A1101, transferring data to the SenseCAP Portal via the LoRaWAN network, and developing a full-fledged Python application to obtain model detection results and inform the user via WhatsApp.

🎁🎨 Huge thanks to [Elecrow](https://www.elecrow.com/?idd=3) for sending me an [Elecrow 8.8" IPS Monitor (1920\*480)](https://www.elecrow.com/elecrow-8-8-inch-display-1920-480-ips-screen-lcd-panel-raspberry-pi-compatible-monitor.html?idd=3).

🎁🎨 Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sending me a [LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html?tracking=60f546f8002be).

🎁🎨 Also, huge thanks to [Anycubic](https://www.anycubic.com/) for sponsoring a brand-new [Anycubic Kobra 2](https://bit.ly/3Ov2PJh).

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/finished\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_12.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/finished\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_0.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/gif\_collect.gif)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_sample\_collect\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/run\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/whatsapp\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/whatsapp\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/gif\_run.gif)

## Step 1: Designing and printing a plant-themed case

Since I focused on building a budget-friendly and accessible appliance that captures images of fertilizer-exerted soils and runs an object detection model to inform the user of the excessive use of chemical fertilizers over WhatsApp via the LoRaWAN network, I decided to design a modular and compact case allowing the user to place the remote control and position SenseCAP A1101 with LattePanda 3 Delta effortlessly. To avoid overexposure to dust and prevent loose wire connections, I added a sliding front cover. Then, I designed a diagonal top cover for the separate remote control section of the main case, mountable via snap-fit joints. Also, I decided to inscribe the Helium logo and the Arduino symbol on the sliding front cover and the diagonal top cover to highlight the LoRaWAN-enabled fertilizer contamination detection.

Since I needed to attach SenseCAP A1101 to the main case via its bracket, I decided to add compatible screw holes on the top of the main case. Due to the separate section, I was able to fit the remote control and connect it to LattePanda 3 Delta as a single unit.

I designed the main case, its sliding front cover, and the diagonal top cover in Autodesk Fusion 360. You can download their STL files below.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_4.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_6.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_7.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_8.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_9.png)

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_10.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_11.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_12.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_13.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_14.png)

Since I wanted to create a glistening plant structure for the main case and apply a unique verdant theme denoting burgeoning plants, I utilized these PLA filaments:

* eSilk Lime
* Green RAL 6029

Finally, I printed all parts (models) with my brand-new Anycubic Kobra 2 3D Printer.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/printed\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/printed\_2.jpg)

Since Anycubic Kobra 2 is budget-friendly and specifically designed for high-speed printing, I highly recommend Anycubic Kobra 2 if you are a maker or hobbyist needing to print multiple prototypes before finalizing a complex project.

Thanks to its upgraded direct extruder, Anycubic Kobra 2 provides 150mm/s recommended print speed (up to 250mm/s) and dual-gear filament feeding. Also, it provides a cooling fan with an optimized dissipation design to support rapid cooling complementing the fast printing experience. Since the Z-axis has a double-threaded rod structure, it flattens the building platform and reduces the printing layers, even at a higher speed.

Furthermore, Anycubic Kobra 2 provides a magnetic suction platform on the heated bed for the scratch-resistant spring steel build plate allowing the user to remove prints without any struggle. Most importantly, you can level the bed automatically via its user-friendly LeviQ 2.0 automatic bed leveling system. Also, it has a smart filament runout sensor and the resume printing function for power failures.

:hash: First of all, install the gantry and the spring steel build plate.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_2.jpg)

:hash: Install the print head, the touch screen, and the filament runout sensor.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_4.jpg)

:hash: Connect the stepper, switch, screen, and print head cables. Then, attach the filament tube.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_5.jpg)

:hash: If the print head is shaking, adjust the hexagonal isolation column under the print head.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_6.jpg)

:hash: Go to _Prepare➡ Leveling ➡ Auto-leveling_ to initiate the LeviQ 2.0 automatic bed leveling system.

:hash: After preheating and wiping the nozzle, Anycubic Kobra 2 probes the predefined points to level the bed.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_9.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_10.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_11.jpg)

:hash: Finally, fix the filament tube with the cable clips, install the filament holder, and insert the filament into the extruder.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_assembly\_12.jpg)

:hash: Since Anycubic Kobra 2 is not officially supported by Cura yet, download the latest [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer\_424/) version and import the printer profile (configuration) file provided by Anycubic.

:hash: Then, create a custom printer profile on Cura for Anycubic Kobra 2 and change _Start G-code_ and _End G-code_.

:hash: Based on the provided _Start G-code_ and _End G-code_ in the configuration file, I modified new _Start G-code_ and _End G-code_ compatible with Cura.

```
Start G-code:

G90 ; use absolute coordinates
M83 ; extruder relative mode
G28 ; move X/Y/Z to min endstops
G1 Z2.0 F3000 ; lift nozzle a bit 
G92 E0 ; Reset Extruder
G1 X10.1 Y20 Z0.28 F5000.0 ; Move to start position
G1 X10.1 Y200.0 Z0.28 F1500.0 E15 ; Draw the first line
G1 X10.4 Y200.0 Z0.28 F5000.0 ; Move to side a little
G1 X10.4 Y20 Z0.28 F1500.0 E30 ; Draw the second line
G92 E0 ; zero the extruded length again 
G1 E-2 F500 ; Retract a little 
M117
G21 ; set units to millimeters
G90 ; use absolute coordinates
M82 ; use absolute distances for extrusion
G92 E0
M107

End G-code:

M104 S0 ; Extruder off 
M140 S0 ; Heatbed off 
M107    ; Fan off 
G91     ; relative positioning 
G1 E-5 F3000  
G1 Z+0.3 F3000 ; lift print head 
G28 X0  F3000
M84            ; disable stepper motors
```

:hash: Finally, adjust the official printer settings depending on the filament type while copying them from PrusaSlicer to Cura.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_4.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_6.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/kobra\_2\_set\_7.png)

## Step 1.1: Assembling the case and making connections & adjustments

```
// Connections
// Arduino Nano :
//                                SH1106 OLED Display (128x64)
// D11  --------------------------- SDA
// D13  --------------------------- SCK
// D8   --------------------------- RST
// D9   --------------------------- DC
// D10  --------------------------- CS
//                                Control Button (A)
// A0   --------------------------- +
//                                Control Button (B)
// A1   --------------------------- +
//                                Control Button (C)
// A2   --------------------------- +
//                                5mm Common Anode RGB LED
// D3   --------------------------- R
// D5   --------------------------- G
// D6   --------------------------- B
```

Since [SenseCAP A1101](https://files.seeedstudio.com/wiki/SenseCAP-A1101/SenseCAP\_A1101\_LoRaWAN\_Vision\_AI\_Sensor\_User\_Guide\_V1.0.2.pdf) does not support capturing images with different labels out of the box, I decided to build a simple remote control with Arduino Nano to capture pictures easily. Then, I employed LattePanda 3 Delta to program SenseCAP A1101 to capture images according to labels transferred by the remote control via serial communication.

To be able to transfer commands to SenseCAP A1101 via serial communication, I connected Arduino Nano directly to LattePanda 3 Delta via a USB cable. I utilized an SH1106 OLED screen to display ongoing operations and visualize the selected fertilizer contamination classes (levels). Then, I added three control buttons to transfer the user commands to LattePanda 3 Delta via serial communication. Also, I added an RGB LED to inform the user of the device status, indicating serial communication success.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/breadboard\_1.jpg)

After printing all parts (models), I fastened the remote control to the separate section of the main case via a hot glue gun. I also utilized the SenseCAP A1101's screw kit to attach its bracket firmly to the screw holes on the top of the main case.

I placed LattePanda 3 Delta in the main case and attached SenseCAP A1101 to its bracket. Then, I attached the diagonal top cover to the main case via its snap-fit joints.

Finally, I inserted the sliding front cover via the dents on the main case.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_9.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_10.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_11.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_12.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/assembly\_13.jpg)

As mentioned earlier, the diagonal top cover can be utilized to hide the remote control when running the object detection model instead of collecting data.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/finished\_1.jpg)

## Step 1.2: Creating a LattePanda Deck to display the video stream

Since I decided to program SenseCAP A1101 with LattePanda 3 Delta to capture images depending on labels transferred by the remote control via serial communication, I decided to design a unique and compact LattePanda Deck to display the real-time video stream generated by SenseCAP A1101, which is not only compatible with LattePanda but also any single-board computer supporting HDMI.

I decided to employ [Elecrow's 8.8" (1920\*480) high-resolution IPS monitor](https://www.elecrow.com/elecrow-8-8-inch-display-1920-480-ips-screen-lcd-panel-raspberry-pi-compatible-monitor.html?idd=3) as the screen of my LattePanda Deck. Thanks to its converter board, this monitor can be powered via a USB port and works without installing any drivers. Therefore, it is a compact plug-and-play monitor for LattePanda 3 Delta, providing high resolution and up to 60Hz refresh rate.

Due to the fact that I wanted to build a sturdy and easy-to-use deck, I designed a two-part case covering the screen frame and providing a slot for the converter board. To avoid overexposure to dust and provide room for cable management, I added a mountable back cover adorned with the brand logo.

I designed the two-part case and its mountable back cover in Autodesk Fusion 360. You can download their STL files below.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_4.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_6.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_7.png)

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_8.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_9.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/model\_elecrow\_10.png)

After printing all deck parts (models) with my Anycubic Kobra 2 3D Printer, I affixed the two-part case together via the hot glue gun.

Then, I fastened the Elecrow's IPS monitor to the case covering the screen frame and inserted the converter board into its slot.

After attaching the required cables to the converter board, I fixed the mountable back cover via M3 screws.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_0.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_7.jpg)

After connecting the converter board to LattePanda 3 Delta via its USB and HDMI ports, LattePanda recognizes the IPS monitor automatically.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/elecrow\_8.jpg)

## Step 2: Creating an account to utilize Twilio's WhatsApp API

Since I decided to inform the user of the model detection results over WhatsApp via the LoRaWAN network, I needed to utilize Twilio's WhatsApp API. [Twilio](https://www.twilio.com/docs/libraries/python) gives the user a simple and reliable way to communicate with a Twilio-verified phone over WhatsApp via its WhatsApp API for trial accounts. Also, Twilio provides official helper libraries for different programming languages, including Python.

:hash: First of all, sign up for [Twilio](https://www.twilio.com/try-twilio) and create a new free trial account (project).

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_2.png)

:hash: Then, verify a phone number for the account (project) and set the account settings for WhatsApp in Python.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_4.png)

:hash: Go to _Twilio Sandbox for WhatsApp_ and verify your device by sending the given code over WhatsApp, which activates a WhatsApp session.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/whatsapp\_1.jpg)

:hash: After verifying your device, download the [Twilio Python Helper Library](https://github.com/twilio/twilio-python) or directly install it on Thonny. Then, go to _Account ➡ API keys & tokens_ to get the account SID and the auth token under _Live credentials_ so as to communicate with the verified phone over WhatsApp.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_6.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_7.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/twilio\_set\_8.png)

## Step 3: Producing organic fertilizers from quail manure in different decomposition stages

As mentioned earlier, utilizing composted manure as organic fertilizer can affect soil acidification, integrity, and structure depending on the manure decomposition stages (fresh, active, mature, and old). Since I needed a controlled environment manifesting varying soil structure and integrity in order to build a valid object detection model to detect excessive chemical fertilizer use, I decided to produce my organic fertilizers by composting manure.

Fortunately, I am raising quails for egg production on my balcony and have experience in composting quail manure as organic fertilizer. To examine the correlation between the chemical (synthetic) fertilizer contamination and the soil integrity differences due to the applied organic fertilizers, I started to compost quail manure and collected the manure in different decomposition stages:

* Fresh (1 month)
* Active (3 months)
* Old (6 months)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_9.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_10.jpg)

After producing organic fertilizers from manure in different decomposition stages, I applied them to the soil in three separate flowerpots.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_extraction\_11.jpg)

## Step 3.1: Adding chemical fertilizers and sowing tomato seedlings

After adding organic fertilizers to the flowerpots, I ploughed the organic fertilizer-exerted soils and let them rest for a while.

Then, I added chemical (synthetic) fertilizers to each flowerpot in the same amount to examine the excessive use of chemical fertilizers depending on the soil integrity and structure altered by organic fertilizers. I applied some of the most common water-soluble chemical fertilizers:

* Calcium Nitrate
* Magnesium Sulphate
* Ammonium Sulphate
* Ammonium Phosphate

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_0.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_1.jpg)

To demonstrate the detrimental effects of chemical fertilizer contamination on the environment depending on the soil integrity altered by organic fertilizers, I sowed different types of tomato seedlings in each flowerpot.

As demonstrated below, fertilizer contamination killed some tomato seedlings depending on the pollution levels based on the soil integrity and structure altered by the applied organic fertilizer (manure) decomposition stage:

* Enriched
* Unsafe
* Toxic

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_9.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/fertilizer\_chemical\_10.jpg)

## Step 4: Utilizing Arduino Nano as a remote control to send commands via serial communication

As explained earlier, SenseCAP A1101 does not support capturing images and saving them with different labels out of the box. Therefore, I decided to build a simple remote control with Arduino Nano to transfer commands (labels) to SenseCAP A1101 via serial communication, both connected to LattePanda 3 Delta.

You can download the _AIoT\_Fertilizer\_Contamination\_Detector\_remote\_control.ino_ file to try and inspect the code for transferring commands to SenseCAP A1101 via serial communication.

:hash: Firstly, download the required libraries to utilize the SH1106 OLED screen with Arduino Nano:

Adafruit\_SH1106 | [Download](https://github.com/wonho-maker/Adafruit\_SH1106)

Adafruit-GFX-Library | [Download](https://github.com/adafruit/Adafruit-GFX-Library)

⭐ Include the required libraries.

```
#include &lt;SPI.h>
#include &lt;Adafruit_GFX.h>
#include &lt;Adafruit_SH1106.h>
```

⭐ Define the SH1106 OLED display (128x64) settings.

⭐ Define monochrome graphics.

```
#define OLED_MOSI      11  // MOSI (SDA)
#define OLED_CLK       13  // SCK
#define OLED_DC        9
#define OLED_CS        10
#define OLED_RESET     8
Adafruit_SH1106 display(OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);
```

⭐ Define the fertilizer contamination class (label) names and color codes.

```
String classes[] = {"Enriched", "Unsafe", "Toxic"};
int color_codes[3][3] = {{0,255,0}, {255,255,0}, {255,0,0}};
```

⭐ Initialize the default serial port (Serial) to communicate with LattePanda 3 Delta.

```
  Serial.begin(115200);
```

⭐ Initialize the SH1106 OLED display.

```
  display.begin(SH1106_SWITCHCAPVCC);
  display.display();
  delay(1000);
```

⭐ In the _home\_screen_ function, show the menu interface on the SH1106 OLED display, demonstrating classes (labels).

```
void home_screen(){
  display.clearDisplay();   
  display.drawBitmap((128 - 40), 20, _home, 40, 40, WHITE);
  display.setTextSize(1); 
  display.setTextColor(BLACK, WHITE);
  display.setCursor(10,5);
  display.println(" Select Label: ");
  display.setTextColor(WHITE);
  display.setCursor(10,25);
  display.println("A) Enriched");  
  display.setCursor(10,40);
  display.println("B) Unsafe");  
  display.setCursor(10,55);
  display.println("C) Toxic");  
  display.display();
  delay(100);
}
```

⭐ In the _data\_screen_ function, display the selected fertilizer contamination class with its unique icon on the SH1106 OLED screen.

⭐ Then, adjust the RGB LED to the color code of the selected class.

```
void data_screen(int i){
  display.clearDisplay(); 
  if(i==0) display.drawBitmap((128 - 40) / 2, 0, enriched, 40, 40, WHITE);
  if(i==1) display.drawBitmap((128 - 40) / 2, 0, unsafe, 40, 40, WHITE);
  if(i==2) display.drawBitmap((128 - 40) / 2, 0, toxic, 40, 40, WHITE);
  // Print:
  int str_x = classes[i].length() * 11;
  display.setTextSize(2); 
  display.setTextColor(WHITE);
  display.setCursor((128 - str_x) / 2, 48);
  display.println(classes[i]);
  display.display();
  adjustColor(color_codes[i][0], color_codes[i][1], color_codes[i][2]);
  delay(4000);
  adjustColor(255,0,255);
}
```

⭐ If one of the control buttons (A, B, or C) is pressed, transmit the selected fertilizer contamination class (label) to LattePanda 3 Delta via serial communication.

```
  if(!digitalRead(button_A)){ Serial.println("Label: Enriched"); data_screen(0); delay(2000); }
  if(!digitalRead(button_B)){ Serial.println("Label: Unsafe"); data_screen(1); delay(2000); }
  if(!digitalRead(button_C)){ Serial.println("Label: Toxic"); data_screen(2); delay(2000); }
```

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_3.png)

After uploading and running the code for transferring commands to LattePanda 3 Delta via serial communication:

🌱🪴📲 Arduino Nano prints notifications on the serial monitor for debugging.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/serial\_remote\_1.png)

## Step 4.1: Displaying images on the SH1106 OLED screen

To display images (black and white) on the SH1106 OLED screen successfully, I needed to create monochromatic bitmaps from PNG or JPG files and convert those bitmaps to data arrays.

:hash: First of all, download the [LCD Assistant](http://en.radzio.dxp.pl/bitmap\_converter/).

:hash: Then, upload a monochromatic bitmap and select _Vertical_ or _Horizontal_ depending on the screen type.

:hash: Convert the image (bitmap) and save the output (data array).

:hash: Finally, add the data array to the code and print it on the screen.

```
static const unsigned char PROGMEM toxic [] = {
0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x03, 0x00, 0xC0, 0x00, 0x00, 0x06, 0x00, 0x60, 0x00, 0x00,
0x0C, 0x00, 0x30, 0x00, 0x00, 0x18, 0x00, 0x18, 0x00, 0x00, 0x38, 0x00, 0x1C, 0x00, 0x00, 0x30,
0x00, 0x0C, 0x00, 0x00, 0x70, 0x00, 0x0E, 0x00, 0x00, 0x70, 0x00, 0x0E, 0x00, 0x00, 0x70, 0x00,
0x0E, 0x00, 0x00, 0x70, 0x7E, 0x0E, 0x00, 0x00, 0x71, 0xFF, 0x8E, 0x00, 0x00, 0x73, 0xFF, 0xCE,
0x00, 0x00, 0x7B, 0x81, 0xDE, 0x00, 0x00, 0xFD, 0x00, 0xBF, 0x00, 0x01, 0xFC, 0x00, 0x3F, 0x80,
0x07, 0xFF, 0x00, 0xFF, 0xE0, 0x0F, 0xFF, 0xC3, 0xFF, 0xF0, 0x0F, 0xFF, 0xFF, 0xFF, 0xF0, 0x1E,
0x07, 0xE7, 0xE0, 0x78, 0x18, 0x31, 0xC3, 0x8C, 0x18, 0x30, 0x30, 0xC3, 0x0C, 0x0C, 0x30, 0x30,
0x00, 0x0C, 0x0C, 0x20, 0x30, 0x24, 0x0C, 0x04, 0x60, 0x38, 0x3C, 0x1C, 0x06, 0x40, 0x38, 0x3C,
0x1C, 0x02, 0x40, 0x1C, 0x3C, 0x38, 0x02, 0x40, 0x1C, 0x3C, 0x38, 0x02, 0x40, 0x0F, 0x3C, 0xF0,
0x02, 0x00, 0x07, 0xBD, 0xE0, 0x00, 0x00, 0x03, 0xBD, 0xC0, 0x00, 0x00, 0x01, 0x7E, 0x80, 0x00,
0x00, 0x00, 0x7E, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x08, 0x01, 0xFF, 0x80, 0x10, 0x04,
0x03, 0xFF, 0xC0, 0x20, 0x03, 0x9F, 0xE7, 0xF9, 0xC0, 0x00, 0xFF, 0x81, 0xFF, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
};

...

display.clearDisplay(); 
display.drawBitmap((128 - 40) / 2, 0, toxic, 40, 40, WHITE);
display.display();
```

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/img\_convert\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/img\_convert\_2.png)

## Step 5.0: Setting up SenseCAP A1101 on LattePanda 3 Delta

Before proceeding with the following steps, I needed to set up SenseCAP A1101 to program it with LattePanda 3 Delta in Python.

Even though Seeed Studio provides official firmware (UF2) to capture images in Python, I needed to upgrade the BootLoader to the latest version. If your device's BootLoader version is greater than 2.0.0, you do not need to upgrade the BootLoader.

:hash: First of all, connect SenseCAP A1101 to LattePanda 3 Delta via a USB Type-C cable.

:hash: Then, double-click the boot button on SenseCAP A1101 to enter the boot mode and open the storage drive.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_data\_collection\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_data\_collection\_2.png)

:hash: After accessing the storage drive, open the _INFO\_UF2.txt_ file and check for the BootLoader version.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_firmware\_update\_1.png)

:hash: If the BootLoader version is less than 2.0.0, update it with the latest version.

:hash: Download the latest release of the BootLoader:

[_tinyuf2-sensecap\_vision\_ai\_x.x.x.bin_](https://github.com/Seeed-Studio/Seeed\_Arduino\_GroveAI/releases/)

:hash: This firmware controls the BL702 chip that builds the connection between the computer and the Himax chip.

:hash: After downloading the latest BootLoader version, download [the BLDevCube.exe software](https://wiki.seeedstudio.com/Train-Deploy-AI-Model-A1101/#update-bootloader), select _BL702/704/706_, and then click _Finish_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_firmware\_update\_2.png)

:hash: Click _View_, choose _MCU_, and enter the BootLoader firmware path on _Image File_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_firmware\_update\_3.png)

:hash: Select the COM port of SenseCAP A1101. If the port is not recognized by BLDevCube, connect SenseCAP A1101 to LattePanda 3 Delta again while holding the boot button.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_firmware\_update\_4.png)

:hash: Then, click _Open UART_ and set _Chip Erase_ to _True_.

:hash: Finally, click _Create & Program_ and wait until the BootLoader is updated.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_firmware\_update\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_firmware\_update\_6.png)

:hash: After updating the BootLoader, download the official firmware (UF2) for capturing pictures in Python.

[_sensecap\_ai\_capture\_firmware\_vxx-xx.uf2_](https://github.com/Seeed-Studio/Seeed\_Arduino\_GroveAI/releases/)

:hash: Then, open the storage drive and copy the official firmware (UF2) to the drive.

:hash: As soon as the uf2 file is uploaded into the storage drive, it should disappear.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_data\_collection\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_data\_collection\_3.1.png)

:hash: Finally, install the required modules on Thonny.

_pip3 install libusb1_

_pip3 install opencv-python_

_pip3 install numpy_

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/A1101\_data\_collection\_4.png)

## Step 5: Capturing fertilizer-exerted soil images w/ SenseCAP A1101 and communicating with Arduino Nano via serial communication

After setting up SenseCAP A1101 and installing the required libraries, I programmed SenseCAP A1101 via LattePanda 3 Delta to obtain the commands transferred by Arduino Nano via serial communication and capture pictures of fertilizer-exerted soils. As explained in the previous steps, SenseCAP A1101 does not provide the option to capture images with different labels out of the box.

Since I needed to assign fertilizer contamination levels as labels for each image while capturing pictures of fertilizer-exerted soils with altered soil integrity to create a valid data set for my object detection model, I utilized three control buttons connected to Arduino Nano so as to choose among classes and transfer commands via serial communication. After selecting a fertilizer contamination class by pressing a control button, Arduino Nano transmits the selected class to LattePanda 3 Delta via serial communication.

* Control Button (A) ➡ Enriched
* Control Button (B) ➡ Unsafe
* Control Button (C) ➡ Toxic

You can download the _A1101\_data\_img\_collection.py_ file to try and inspect the code for obtaining commands via serial communication and capturing images with SenseCAP A1101.

To decrypt the image buffer generated by SenseCAP A1101, I modified [these functions](https://github.com/Seeed-Studio/Seeed\_Arduino\_GroveAI/blob/master/tools/capture\_images\_script.py) provided by Seeed Studio.

Firstly, I created a class named _A1101\_data\_img\_collection_ to bundle the following functions under a specific structure.

⭐ Include the required modules.

```
import cv2
import serial
from threading import Thread
from time import sleep
import os
from PIL import Image
from io import BytesIO
import usb1
import numpy as np
import datetime
```

⭐ In the _**init**_ function: ⭐ Define the required settings to obtain generated data packets from SenseCAP A1101.

⭐ Get the connected USB device context.

⭐ Initialize serial communication with Arduino Nano to obtain the transferred commands.

⭐ Initialize and test the SenseCAP A1101 USB connection.

```
class A1101_data_img_collection():
    def __init__(self):
        # Define the required settings to obtain information from SenseCAP A1101 LoRaWAN Vision AI Sensor.
        self.WEBUSB_JPEG = (0x2B2D2B2D)
        self.WEBUSB_TEXT = 0x0F100E12
        self.VendorId = 0x2886
        self.ProductId = [0x8060, 0x8061]
        self.img_buff = bytearray()
        self.buff_size = 0
        self.time_out = 1000
        # Get the connected USB device context.       
        self.context = usb1.USBContext()
        # Initialize serial communication with Arduino Nano to obtain the given commands.
        self.arduino_nano = serial.Serial("COM7", 115200, timeout=2000)
        # Initialize and test SenseCAP A1101 connection.
        self.get_rlease_device(False)
        self.disconnect()
```

⭐ In the _read\_data_ function:

⭐ If SenseCAP A1101 is accessible, get the data endpoints and all transferred data objects.

⭐ Check for any submitted data object in the received data packet.

```
    def read_data(self):
        # If SenseCAP A1101 is accessible:
        with self.handle.claimInterface(2):
            # Get the data endpoints.
            self.handle.setInterfaceAltSetting(2, 0)
            self.handle.controlRead(0x01 &lt;&lt; 5, request=0x22, value=0x01, index=2, length=2048, timeout=self.time_out)
            # Get all transferred data objects.
            transfer_list = []
            for _ in range(1):
                transfer = self.handle.getTransfer()
                transfer.setBulk(usb1.ENDPOINT_IN | 2, 2048, callback=self.processReceivedData, timeout=self.time_out)
                transfer.submit()
                transfer_list.append(transfer)
            # Check for any submitted data object in the received data packet.
            while any(x.isSubmitted() for x in transfer_list):
                self.context.handleEvents()
```

⭐ In the _processReceivedData_ function:

⭐ If SenseCAP A1101 generates a data packet successfully, process the received data packet.

⭐ Decrypt the captured image buffer from the processed data packet.

⭐ Resubmit the data packet after processing to avoid errors.

```
    def processReceivedData(self, transfer):
        # If SenseCAP A1101 generates a data packet successfully, process the received information.
        if transfer.getStatus() != usb1.TRANSFER_COMPLETED:
            # transfer.close()
            return
        # Extract the captured image from the processed data packet.
        data = transfer.getBuffer()[:transfer.getActualLength()]
        self.convert_and_show_img(data)
        # Resubmit the data packet after processing to avoid errors.
        transfer.submit()
```

⭐ In the _convert\_and\_show\_img_ function:

⭐ Convert the received data packet to an image buffer.

⭐ If the received data packet is converted to an image buffer successfully, display the generated image on the screen to create a real-time video stream.

⭐ Stop the video stream when requested.

⭐ Store the latest image buffer (frame) captured by SenseCAP A1101.

```
    def convert_and_show_img(self, data: bytearray):
        # Convert the received data packet.
        if (len(data) == 8) and (int.from_bytes(bytes(data[:4]), 'big') == self.WEBUSB_JPEG):
            self.buff_size = int.from_bytes(bytes(data[4:]), 'big')
            self.img_buff = bytearray()
        elif (len(data) == 8) and (int.from_bytes(bytes(data[:4]), 'big') == self.WEBUSB_TEXT):
            self.buff_size = int.from_bytes(bytes(data[4:]), 'big')
            self.img_buff = bytearray()
        else:
            self.img_buff = self.img_buff + data
        # If the received data packet is converted to an image buffer successfully, display the generated image on the screen.
        if self.buff_size == len(self.img_buff):
            try:
                img = Image.open(BytesIO(self.img_buff))
                img = np.array(img)
                cv2.imshow('A1101_data_img_collection', cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
                # Stop the video stream if requested.
                if cv2.waitKey(1) != -1:
                    cv2.destroyAllWindows()
                    print("\nCamera Feed Stopped!")
                # Store the latest frame captured by SenseCAP A1101.
                self.latest_frame = img
            except:
                self.img_buff = bytearray()
                return
```

⭐ In the _connect_ function, connect to SenseCAP A1101 if detected successfully.

```
    def connect(self):
        # Connect to SenseCAP A1101.
        self.handle = self.get_rlease_device(True)
        if self.handle is None:
            print('\nSenseCAP A1101 not detected!')
            return False
        with self.handle.claimInterface(2):
            self.handle.setInterfaceAltSetting(2, 0)
            self.handle.controlRead(0x01 &lt;&lt; 5, request=0x22, value=0x01, index=2, length=2048, timeout=self.time_out)
            print('\nSenseCAP A1101 detected successfully!')
        return True
```

⭐ In the _disconnect_ function, reset the USB connection between SenseCAP A1101 and LattePanda 3 Delta.

```
    def disconnect(self):
        # Reset the SenseCAP A1101 connection.
        try:
            print('Resetting the device connection... ')
            with usb1.USBContext() as context:
                handle = context.getByVendorIDAndProductID(self.VendorId, self.d_ProductId, skip_on_error=False).open()
                handle.controlRead(0x01 &lt;&lt; 5, request=0x22, value=0x00, index=2, length=2048, timeout=self.time_out)
                handle.close()
                print('Device connection has been reset successfully!')
            return True
        except:
            return False
```

⭐ In the _get\_rlease\_device_ function:

⭐ Establish the USB connection between SenseCAP A1101 and LattePanda 3 Delta.

⭐ Retrieve the device information and check if there is a successfully connected device.

⭐ Open or close the SenseCAP A1101 data transmission.

```
    def get_rlease_device(self, get=True):
        # Establish the SenseCAP A1101 connection.
        print('*' * 50)
        print('Establishing connection...')
        # Get the device information. 
        for device in self.context.getDeviceIterator(skip_on_error=True):
            product_id = device.getProductID()
            vendor_id = device.getVendorID()
            device_addr = device.getDeviceAddress()
            bus = '->'.join(str(x) for x in ['Bus %03i' % (device.getBusNumber(),)] + device.getPortNumberList())
            # Check if there is a connected device.
            if(vendor_id == self.VendorId) and (product_id in self.ProductId):
                self.d_ProductId = product_id
                print('\r' + f'\033[4;31mID {vendor_id:04x}:{product_id:04x} {bus} Device {device_addr} \033[0m', end='')
                # Turn on or off SenseCAP A1101.
                if get:
                    return device.open()
                else:
                    device.close()
                    print('\r' + f'\033[4;31mID {vendor_id:04x}:{product_id:04x} {bus} Device {device_addr} CLOSED\033[0m', flush=True)
```

⭐ In the _get\_transferred\_data\_packets_ function, obtain the transferred commands from Arduino Nano via serial communication, including fertilizer contamination classes (labels).

```
    def get_transferred_data_packets(self):
        # Obtain the transferred commands from Arduino Nano via serial communication, including fertilizer hazard classes (labels).
        if self.arduino_nano.in_waiting > 0:
            command = self.arduino_nano.readline().decode("utf-8", "ignore").rstrip()
            if(command.find("Enriched") >= 0):
                print("\nCapturing an image! Label: Enriched")
                self.save_img_sample("Enriched")
            if(command.find("Unsafe") >= 0):
                print("\nCapturing an image! Label: Unsafe")
                self.save_img_sample("Unsafe")
            if(command.find("Toxic") >= 0):
                print("\nCapturing an image! Label: Toxic")
                self.save_img_sample("Toxic")
        sleep(1)
```

⭐ In the _save\_img\_sample_ function, depending on the obtained class name, save the latest stored image buffer (frame) captured by SenseCAP A1101 to the _samples_ folder by appending the current date & time to its file name:

_Enriched\_IMG\_20230530\_165521.jpg_

```
    def save_img_sample(self, _class):    
        date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = './samples/{}_IMG_{}.jpg'.format(_class, date)
        # If requested, save the recently captured image (latest frame) as a sample.
        cv2.imwrite(filename, self.latest_frame)
        print("\nSample Saved Successfully: " + filename)
```

:hash: Since displaying a real-time video stream generated by SenseCAP A1101 and communicating with Arduino Nano to obtain commands via serial communication cannot be executed in a single loop, I utilized the [Python Thread](https://realpython.com/intro-to-python-threading/) class to run simultaneous processes (functions).

```
soil = A1101_data_img_collection()

# Define and initialize threads.
def A1101_camera_feed():
    soil.collect_data()
        
def activate_received_commands():
    while True:
        soil.get_transferred_data_packets()

Thread(target=A1101_camera_feed).start()
Thread(target=activate_received_commands).start()
```

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_img\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_img\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_img\_3.png)

## Step 5.1: Saving the captured images as samples on LattePanda 3 Delta

After uploading and running the code for obtaining commands via serial communication and capturing images with SenseCAP A1101 on LattePanda 3 Delta:

🌱🪴📲 If the device works accurately, the remote control shows the menu interface on the SH1106 OLED display and turns the RGB LED to magenta.

* A) Enriched
* B) Unsafe
* C) Toxic

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_3.jpg)

🌱🪴📲 If the control button (A) is pressed, Arduino Nano adds _Enriched_ as the selected fertilizer contamination class to the command, transfers the modified command to LattePanda 3 Delta via serial communication, displays the selected fertilizer contamination class with its unique monochrome icon on the SH1106 OLED screen, and turns the RGB LED to green.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_4.jpg)

🌱🪴📲 If the control button (B) is pressed, Arduino Nano adds _Unsafe_ as the selected fertilizer contamination class to the command, transfers the modified command to LattePanda 3 Delta via serial communication, displays the selected fertilizer contamination class with its unique monochrome icon on the SH1106 OLED screen, and turns the RGB LED to yellow.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_5.jpg)

🌱🪴📲 If the control button (C) is pressed, Arduino Nano adds _Toxic_ as the selected fertilizer contamination class to the command, transfers the modified command to LattePanda 3 Delta via serial communication, displays the selected fertilizer contamination class with its unique monochrome icon on the SH1106 OLED screen, and turns the RGB LED to red.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_6.jpg)

🌱🪴📲 When LattePanda 3 Delta receives a command transferred by Arduino Nano via serial communication, including the selected fertilizer contamination class, it saves the latest stored image buffer generated by SenseCAP A1101 to the _samples_ folder depending on the selected class name by appending the current date & time to its file name:

_Enriched\_IMG\_20230530\_165528.jpg_

_Unsafe\_IMG\_20230530\_170541.jpg_

_Toxic\_IMG\_20230530\_171326.jpg_

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/collect\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/gif\_collect.gif)

🌱🪴📲 Also, LattePanda 3 Delta shows the real-time video stream generated by SenseCAP A1101 while capturing pictures and prints notifications with the saved image file paths on the shell for debugging.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_sample\_collect\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_sample\_collect\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_sample\_collect\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_sample\_collect\_4.png)

After capturing images of fertilizer-exerted soils in three separate flowerpots for nearly two months, whose soil integrity and structure were altered in relation to the applied organic fertilizer (manure) decomposition stage, I managed to construct my data set with eminent validity and veracity.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_7.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collect\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/data\_collected.png)

## Step 6: Building an object detection (FOMO) model with Edge Impulse

As explained in the previous steps, I needed a controlled environment manifesting varying soil structure and integrity in order to build a valid object detection model. Therefore, I applied composted quail manure collected in different decomposition stages (fresh, active, mature, and old) as organic fertilizers to alter soil acidification, integrity, and structure in three separate flowerpots. Then, I added chemical fertilizers to each flowerpot in the same amount to examine the excessive use of chemical fertilizers.

When I completed capturing images of fertilizer-exerted soils in three separate flowerpots and storing them on LattePanda 3 Delta, I started to work on my object detection (FOMO) model to detect the excessive use of chemical fertilizers in relation to organic fertilizers so as to prevent their hazardous effects on the environment and our health.

Since Edge Impulse supports almost every microcontroller and development board due to its model deployment options, I decided to utilize Edge Impulse to build my object detection model. Also, Edge Impulse provides an elaborate machine learning algorithm (FOMO) for running more accessible and faster object detection models on edge devices such as SenseCAP A1101.

[Edge Impulse FOMO (Faster Objects, More Objects)](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices) is a novel machine learning algorithm that brings object detection to highly constrained devices. FOMO models can count objects, find the location of the detected objects in an image, and track multiple objects in real time, requiring up to 30x less processing power and memory than MobileNet SSD or YOLOv5.

Even though Edge Impulse supports JPG or PNG files to upload as samples directly, each target object in a training or testing sample needs to be labeled manually. Therefore, I needed to follow the steps below to format my data set so as to train my object detection model accurately:

* Data Scaling (Resizing)
* Data Labeling

Since I added fertilizer contamination levels based on the soil integrity and structure altered by the applied organic fertilizer (manure) to the file names while capturing images of soils in the mentioned flowerpots, I preprocessed my data set effortlessly to label each target object on an image sample on Edge Impulse by utilizing the contamination classes:

* Enriched
* Unsafe
* Toxic

Plausibly, Edge Impulse allows building predictive models optimized in size and accuracy automatically and deploying the trained model as a supported firmware (UF2) for SenseCAP A1101. Therefore, after scaling (resizing) and preprocessing my data set to label target objects, I was able to build an accurate object detection model to detect chemical fertilizer overuse, which runs on SenseCAP A1101 without any additional requirements.

You can inspect [my object detection (FOMO) model on Edge Impulse](https://studio.edgeimpulse.com/public/233660/latest) as a public project.

## Step 6.1: Uploading images (samples) to Edge Impulse and labeling objects

After collecting training and testing image samples, I uploaded them to my project on Edge Impulse. Then, I labeled each target object on the image samples.

:hash: First of all, sign up for [Edge Impulse](https://www.edgeimpulse.com/) and create a new project.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_1.png)

:hash: To be able to label image samples manually on Edge Impulse for object detection models, go to _Dashboard ➡ Project info ➡ Labeling method_ and select _Bounding boxes (object detection)_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_2.png)

:hash: Navigate to the _Data acquisition_ page and click the _Upload data_ button.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_3.png)

:hash: Then, choose the data category (training or testing), select image files, and click the _Upload data_ button.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_4.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_6.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_7.png)

After uploading my data set successfully, I labeled each target object on the image samples by utilizing the fertilizer contamination classes. In Edge Impulse, labeling an object is as easy as dragging a box around it and entering a class. Also, Edge Impulse runs a tracking algorithm in the background while labeling objects, so it moves the bounding boxes automatically for the same target objects in different images.

:hash: Go to _Data acquisition ➡ Labeling queue (Object detection labeling)_. It shows all unlabeled items (training and testing) remaining in the given data set.

:hash: Finally, select an unlabeled item, drag bounding boxes around target objects, click the _Save labels_ button, and repeat this process until all samples have at least one labeled target object.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_8.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_9.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_10.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_11.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_12.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_13.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_13.1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_13.2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_14.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_15.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_16.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_17.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_18.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_19.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_20.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_21.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_22.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_23.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_24.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_25.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_set\_26.png)

## Step 6.2: Training the FOMO model on the fertilizer-exerted soil images

After labeling target objects on my training and testing samples successfully, I designed an impulse and trained it on detecting the excessive use of chemical fertilizers in relation to organic fertilizers.

An impulse is a custom neural network model in Edge Impulse. I created my impulse by employing the _Image_ preprocessing block and the _Object Detection (Images)_ learning block.

The _Image_ preprocessing block optionally turns the input image format to grayscale and generates a features array from the raw image.

The _Object Detection (Images)_ learning block represents a machine learning algorithm that detects objects on the given image, distinguished between model labels.

:hash: Go to the _Create impulse_ page and set image width and height parameters to 120. Then, select the resize mode parameter as _Fit shortest axis_ so as to scale (resize) given training and testing image samples.

:hash: Select the _Image_ preprocessing block and the _Object Detection (Images)_ learning block. Finally, click _Save Impulse_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_1.png)

:hash: Before generating features for the object detection model, go to the _Image_ page and set the _Color depth_ parameter as _Grayscale_. Then, click _Save parameters_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_2.png)

:hash: After saving parameters, click _Generate features_ to apply the _Image_ preprocessing block to training image samples.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_4.png)

After conducting preliminary experiments with my object detection model, I noticed some target objects with the _Enriched_ label decreased the model accuracy when being separated while the validation split.

Therefore, I applied a metadata key to the erroneous samples to prevent leaking data between my train and validation sets.

:hash: To add a metadata key, go to _Data acquisition ➡ Dataset ➡ Training_.

:hash: Then, select the faulty sample and click the _Add new metadata_ button.

:hash: Finally, enter the metadata key and value parameters:

* confused\_soil ➡ confused\_soil

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_meta\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_meta\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_meta\_3.png)

:hash: After adding metadata parameters to the faulty samples, navigate to the _Object detection_ page and click _Start training_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_5.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_6.png)

According to my experiments with my object detection model, I modified the neural network settings and architecture to build an object detection model with high accuracy and validity:

📌 Neural network settings:

* Number of training cycles ➡ 90
* Learning rate ➡ 0.052
* Validation set size ➡ 5
* Split train/validation set on metadata key ➡ confused\_soil

📌 Neural network architecture:

* FOMO (Faster Objects, More Objects) MobileNetV2 0.35

After generating features and training my FOMO model with training samples, Edge Impulse evaluated the F1 score (accuracy) as _77.8%_.

The F1 score (accuracy) is approximately _77.8%_ due to the modest volume of training samples of varying fertilizer-exerted soil structures with a similar color scheme, excluding the applied chemical fertilizer colors. Due to this soil color scheme, I noticed the model misinterprets some _Enriched_ and _Toxic_ target objects. Therefore, I am still collecting samples to improve my data set.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_train\_7.png)

## Step 6.3: Evaluating the model accuracy and deploying the model

After building and training my object detection model, I tested its accuracy and validity by utilizing testing image samples.

The evaluated accuracy of the model is _80%_.

:hash: To validate the trained model, go to the _Model testing_ page and click _Classify all_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_test\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_test\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_test\_3.png)

After validating my object detection model, I deployed it as a fully optimized SenseCAP A1101 firmware (UF2) supported by Seeed Studio.

:hash: To deploy the validated model as the supported SenseCAP A1101 firmware (UF2), navigate to the _Deployment_ page and search for _SenseCAP A1101_.

:hash: Then, choose the _Quantized (int8)_ optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click _Build_ to download the model as the supported SenseCAP A1101 firmware — [firmware.uf2](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/seeed-sensecap-a1101#deploy-model-to-sensecap-a1101).

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_deploy\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_deploy\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/edge\_deploy\_3.png)

## Step 7: Connecting SenseCAP A1101 to SenseCAP Mate App and setting up the Edge Impulse FOMO model

After downloading the supported SenseCAP A1101 firmware — _firmware.uf2_, follow the instructions shown in Step 5.0 to upload the Edge Impulse object detection model to the storage drive of SenseCAP A1101.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_model\_set\_1.png)

After uploading the model successfully:

:hash: Install and open the [SenseCAP Mate](https://wiki.seeedstudio.com/One-Stop-Model-Training-with-Edge-Impulse/#configure-your-model-on-the-sensecap-mate) application provided by Seeed Studio.

:hash: Select the server location as _Global_ and create a new account.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_3.jpg)

:hash: Under _Config_ screen, select _Vision AI Sensor_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_4.jpg)

:hash: Press and hold the configuration button on the SenseCAP A1101 for 3 seconds to activate the Bluetooth pairing mode.

:hash: Then, click the _Setup_ button and scan for nearby SenseCAP A1101 devices.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_6.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_7.jpg)

:hash: If the device software version is not the latest release, click the _Update_ button to upgrade the software version.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_8.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_9.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_10.jpg)

:hash: After updating the software version, go to _Setting_ and select:

* Algorithm ➡ Object Detection
* AI Model ➡ User Defined 1
* Score Threshold ➡ 0.6
* Uplink Interval (min) ➡ 5
* Packet Policy ➡ 2C+1N

:hash: Then, select one of the supported frequency plans depending on your region — e.g., EU868.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_11.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_12.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_13.jpg)

:hash: Under _Platform_, select _SenseCAP for Helium_ to utilize the Helium network to transfer data packets to the SenseCAP Portal officially supported by Seeed Studio.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_14.jpg)

:hash: Finally, click _Send ➡ Back to Home_ to complete the device configuration.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_set\_15.jpg)

:hash: After configuring the new device settings, go to _General_ and click _Detect_ under _AI Preview_ so as to inspect the model detection results generated by the uploaded Edge Impulse object detection model.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_model\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_model\_2.jpg)

## Step 8: Transferring the detection results to the SenseCAP Portal via the Helium LongFi Network

After seeing the Edge Impulse model detection results on the SenseCAP Mate application, I needed to bind SenseCAP A1101 as a new device to my account in order to transfer the detection results as data packets to the SenseCAP Portal via the Helium LongFi Network.

:hash: Open the SenseCAP Mate application.

:hash: Under _Device_, click the _Add device_ button.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_add\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_add\_2.jpg)

:hash: Then, scan the QR code on the SenseCAP A1101 to bind it to your account.

:hash: If the QR code sticker is damaged, you can also enter the device EUI manually.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_add\_3.jpg)

:hash: After entering the added device name, SenseCAP A1101 starts sending the model detection results to the SenseCAP Portal via the Helium network.

:hash: SenseCAP A1101 runs the Edge Impulse model and uploads the model detection results to the SenseCAP Portal according to the configured _Uplink Interval_ parameter, in this case, every five minutes.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_add\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_add\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensemate\_add\_6.jpg)

After binding SenseCAP A1101 to the SenseCAP Portal successfully, it finds the nearest Helium gateway and transfers data packets to the SenseCAP Portal automatically.

:hash: To inspect the transferred model detection results on the SenseCAP Portal web dashboard, go to [SenseCAP Portal (web)](https://sensecap.seeed.cc/).

:hash: Then, log in with the same account registered to the SenseCAP Mate App.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_2.png)

:hash: Under _Devices_, select _Sensor Node_ to inspect the bound SenseCAP devices.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_3.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_4.png)

:hash: To see all data packets transferred by the bound devices, go to _Data ➡ Table_.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_5.png)

As explained earlier, Seeed Studio provides the SenseCAP HTTP API to obtain registered data records from the SenseCAP Portal via HTTP GET requests.

:hash: To retrieve the stored model detection results on the SenseCAP Portal via the SenseCAP HTTP API, go to _Security ➡ Access API keys_.

:hash: Then, click the _Create Access Key_ button and copy the generated _API ID_ and _Access API keys_ parameters for further usage.

You can inspect Step 9 to get more detailed information regarding the SenseCAP HTTP API.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_6.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_7.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_web\_set\_8.png)

## Step 8.1: Activating SenseCAP M2 data-only LoRaWAN gateway (EU868)

After binding SenseCAP A1101 to your SenseCAP Portal account, it should automatically connect to the nearest Helium gateway to transfer the model detection results via the Helium LongFi Network.

Nonetheless, if the Helium network does not cover your surroundings, you may need to purchase a Helium gateway.

Since Seeed Studio provides various Helium gateways compatible with the SenseCAP Portal, I wanted to show how to activate one of SenseCAP gateways — SenseCAP M2 data-only LoRaWAN indoor gateway (EU868).

:hash: First of all, go to [Helium Explorer](https://explorer.helium.com/) to check whether a Helium gateway covers your surroundings.

:hash: If so, you do not need to follow the steps below.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_network\_set\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_lorawan\_network\_set\_2.png)

:hash: To activate SenseCAP M2 data-only gateway, follow [the Quick Start instructions](https://www.sensecapmx.com/docs/sensecap-m2-data-only/m2-quick-start/) provided by Seeed Studio.

:hash: After setting up the SenseCAP M2 data-only gateway and connecting it to the Internet via an ethernet cable, you should be able to update the device firmware during the first boot and start transferring data packets in less than 30 minutes.

:hash: Do not forget that Helium Wallet will deduct a $10 onboarding fee and a $5 location asserting fee to activate the M2 data-only gateway to transfer data packets via the Helium LongFi Network.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/m2\_set\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/m2\_set\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/m2\_set\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/m2\_set\_4.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/m2\_set\_5.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/m2\_set\_6.jpg)

## Step 9: Developing a Python application to transfer the model detection results via WhatsApp

To provide an outstanding user experience while informing the user of the model detection results via WhatsApp over LoRaWAN, I developed a full-fledged application from scratch in Python.

This application obtains the model detection results from the SenseCAP Portal by making HTTP GET requests to the SenseCAP HTTP API. Then, the application utilizes Twilio's WhatsApp API to transfer the retrieved model detection results to the verified phone number in order to inform the user of the excessive chemical fertilizer use in relation to organic fertilizers.

You can download the _A1101\_whatsapp\_interface.py_ file to try and inspect the code for obtaining model detection results from the SenseCAP Portal and informing the user of the retrieved detection results via WhatsApp.

:hash: Since Seeed Studio provides the SenseCAP HTTP API for communicating with their various sensors and products, get the correct _Sensor ID_ and _Measurement ID_ parameters from [SenseCAP Document Center](https://sensecap-docs.seeed.cc/sensor\_types\_list.html) so as to obtain the data records that SenseCAP A1101 registered to the SenseCAP Portal via the Helium LongFi Network.

* 2036
* 4175 ➡ AI Detection No.01

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_HTTP\_API\_1.png)

:hash: Since SenseCAP A1101 generates the model detection results in a specific format, I needed to parse the retrieved detection result to obtain the predicted class and the accuracy.

:hash: SenseCAP A1101 stores the predicted class (target number) and the accuracy (confidence level) as a floating point number.

_target number \[1_~~_10], confidence level \[0_~~_99]_

* 🔢0.83
* Predicted Class ➡ 0
* Accuracy ➡ 0.83
* 🔢1.96
* Predicted Class ➡ 1
* Accuracy ➡ 0.96

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_HTTP\_API\_2.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_portal\_data\_collection\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_portal\_data\_collection\_2.png)

⭐ Include the required modules.

```
from twilio.rest import Client
import requests
import json
from time import sleep
```

⭐ Define the Twilio account settings and the client object.

```
twilio_account_sid = '&lt;_SID_>'
twilio_auth_token = '&lt;_TOKEN_>'
twilio_client = Client(twilio_account_sid, twilio_auth_token)
```

⭐ Define the _API ID_ and _Access API keys_ parameters to connect to the SenseCAP Portal, explained in Step 8.

```
API_ID = '&lt;_ID_>'
API_key = '&lt;_KEY_>'
```

⭐ Define the required device information of SenseCAP A1101.

```
device_eui = "2CF7F1C04340004A"
measurement_id = "4175"
channel_index = "1"
```

⭐ Define the host of the SenseCAP HTTP API.

```
host = "https://sensecap.seeed.cc/openapi/"
```

⭐ Depending on the [Device Data API](https://sensecap-docs.seeed.cc/device\_data.html) parameters, define the URL endpoint to obtain the model detection results that SenseCAP A1101 registered to the SenseCAP Portal via the Helium LongFi Network.

_{host}/view\_latest\_telemetry\_data?device\_eui={}\&measurement\_id={}\&channel\_index={}_

```
get_latest_result = "view_latest_telemetry_data?device_eui={}&measurement_id={}&channel_index={}".format(device_eui, measurement_id, channel_index)
```

⭐ In the _send\_WhatsApp\_message_ function:

⭐ Send the given text message with a SenseCAP A1101 image to the verified phone number via Twilio's WhatsApp API to inform the user of the latest model detection results via WhatsApp.

```
def send_WhatsApp_message(_from, _to, _message):
    # Send the given message via WhatsApp to inform the user of the model detection results.
    twilio_message = twilio_client.messages.create(
      from_ = 'whatsapp:'+_from,
      body = _message,
      media_url = 'https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/0/101990962-a1101-first-new-10.17.jpg',
      to = 'whatsapp:'+_to
    )
    print("\nWhatsApp Message Sent: "+twilio_message.sid)
```

⭐ In the _transfer\_latest\_result_ function:

⭐ Make an HTTP GET request to the SenseCAP HTTP API by utilizing the HTTP authentication credentials (_API ID_ and _Access API keys_) provided by the SenseCAP Portal as username and password.

⭐ Decode the received JSON object to obtain the latest model detection results registered by SenseCAP A1101, including the entry date and time.

⭐ Parse the retrieved detection results to get the predicted class and the precision score (accuracy).

⭐ Create a WhatsApp text message from the converted information.

⭐ Transmit the generated text message with the SenseCAP A1101 image to the verified phone number over WhatsApp.

```
def transfer_latest_result():
    # Obtain the latest model detection result via the SenseCAP HTTP API and notify the user of the received information through WhatsApp.
    url = host + get_latest_result
    # Make an HTTP GET request to the SenseCAP Portal by utilizing the provided HTTP authentication credentials (username and password).
    res = requests.get(url, auth = (API_ID, API_key))
    # Decode the received JSON object.
    res = json.loads(res.text)
    detection_digit = res["data"][0]["points"][0]["measurement_value"]
    date = res["data"][0]["points"][0]["time"]
    # Convert the obtained result digits to the detected class and the precision score.
    detected_class = "Nothing!"
    precision = 0
    if(detection_digit > 0 and detection_digit &lt; 1):
        detected_class = "Enriched"
        precision = detection_digit
    if(detection_digit > 1 and detection_digit &lt; 2):
        detected_class = "Toxic"
        precision = detection_digit-1
    if(detection_digit > 2):
        detected_class = "Unsafe"
        precision = detection_digit-2
    # Create a WhatsApp message from the retrieved information.
    message = "📌 Latest Model Detection Result\n\n🕒 {}\n🌱 Class: {}\n💯 Precision: {}".format(date, detected_class, round(precision, 2))
    print(message)
    # Transmit the generated message to the user via WhatsApp.
    send_WhatsApp_message('+_____________', '+_____________', message)
```

⭐ Via WhatsApp, notify the user of the latest model detection results every 10 minutes.

```
while True:
    # Notify the user of the latest model detection result every 10 minutes.
    transfer_latest_result()
    sleep(60*10)
```

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_whatsapp\_1.png)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/code\_whatsapp\_2.png)

## Step 10: Running the model on SenseCAP A1101 and informing the user of the results via WhatsApp

My Edge Impulse object detection (FOMO) model scans a captured image and predicts possibilities of trained labels to recognize a target object on the given picture. The prediction result (score) represents the model's _"confidence"_ that the detected object corresponds to each of the three different labels (classes) \[0 - 2], as shown in Step 6:

* 0 — Enriched
* 1 — Toxic
* 2 — Unsafe

After setting up the Edge Impulse object detection (FOMO) model on SenseCAP A1101 and executing the _A1101\_whatsapp\_interface.py_ file on LattePanda 3 Delta:

🌱🪴📲 As explained in the previous steps, SenseCAP A1101 runs an inference with the Edge Impulse object detection model.

🌱🪴📲 Then, every 5 minutes, it transfers the model detection results as data packets to the SenseCAP Portal via the Helium LongFi Network.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/run\_1.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/run\_2.jpg)

🌱🪴📲 Every 10 minutes, the device executes the Python application to obtain the latest registered model detection results from the SenseCAP Portal by making an HTTP GET request to the SenseCAP HTTP API.

🌱🪴📲 After getting and parsing the latest model detection results, the device utilizes Twilio's WhatsApp API to send the obtained detection results to the verified phone number over WhatsApp in order to inform the user of the excessive chemical fertilizer use in relation to organic fertilizers.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/whatsapp\_2.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/whatsapp\_3.jpg)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/whatsapp\_4.jpg)

🌱🪴📲 Also, LattePanda 3 Delta prints notifications and the generated WhatsApp text messages on the shell for debugging.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/sensecap\_whatsapp\_send\_1.png)

As far as my experiments go, the device detects fertilizer contamination classes accurately, transfers the model detection results to the SenseCAP Portal via the Helium network, and notifies the user of the latest detection results over WhatsApp faultlessly :)

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/gif\_run.gif)

## Videos and Conclusion

[Data Collection | AI-driven LoRaWAN Fertilizer Pollution Detector w/ WhatsApp](https://youtu.be/jqJkfIb0Ow0)

[Experimenting with the model | AI-driven LoRaWAN Fertilizer Pollution Detector w/ WhatsApp](https://youtu.be/9Z4xEuKCFfU)

## Further Discussions

By applying object detection models trained on numerous fertilizer-exerted soil images in detecting the excessive use of chemical fertilizers in relation to organic fertilizers, we can achieve to:

🌱🪴📲 prevent chemical fertilizers from contaminating the groundwater and the environment,

🌱🪴📲 avoid chemical fertilizers from dispersing throughout water bodies and increasing macronutrients in the environment,

🌱🪴📲 mitigate the risk of severe health issues due to nitrite-contaminated water, such as DNA damage, lipid peroxidation, and oxidative stress,

🌱🪴📲 protect wildlife from the execrable effects of excessive chemical fertilizer use.

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/finished\_2.jpg)

## References

\[^1] Devendra Singh, Shobit Thapa, Neelam Geat, Moti Lal Mehriya, Mahendra Vikram Singh Rajawat, _Chapter 12 - Biofertilizers: Mechanisms and application_, Biofertilizers Volume 1: Advances in Bio-Inoculants, Woodhead Publishing, 2021, Pages 151-166, _https://doi.org/10.1016/B978-0-12-821667-5.00024-5_

\[^2] Lifespan, _Nitrates May Be Environmental Trigger For Alzheimer’s, Diabetes And Parkinson's Disease_, ScienceDaily, 6 July 2009, _www.sciencedaily.com/releases/2009/07/090705215239.htm_

\[^3] Ayoub, A.T., _Fertilizers and the environment_, Nutrient Cycling in Agroecosystems 55, 117–121, 1999, _https://doi.org/10.1023/A:1009808118692_

## Schematics

![](../.gitbook/assets/sensecap-a1101-lorawan-soil-quality/SenseCAP\_A1101.jpg)
