---
description: This tutorial involves invoking an Edge Impulse ML model from within a publisher node in MicroROS. An Arduino Portenta H7 is used for demonstration.
---

# ROS2 + Edge Impulse [Part 2]: MicroROS

Created By:
Avi Brown 

Public Project Link:
[https://studio.edgeimpulse.com/public/124223/latest](https://studio.edgeimpulse.com/public/124223/latest)

{% embed url="https://www.youtube.com/watch?v=_M7Wv-3yFLA" %}

### Full code for this project can be found [here](https://github.com/avielbr/micro_ros_ei)

### Background

By popular demand following [Part 1](https://docs.edgeimpulse.com/experts/ros2-part1-pubsub-node) I've decided to change the focus of Part 2 to something that I am particularly excited about, and that is [MicroROS](https://micro.ros.org/). According to their site, MicroROS' mission is -

> Bridging the gap between resource-constrained microcontrollers and larger processors in robotic applications that are based on the Robot Operating System.

They go on to note -

> Microcontrollers are used in almost every robotic product. Typical reasons are:
>
> - Hardware access
> - Hard, low-latency real-time
> - Power saving

So where does AI fit in here? It may seem perhaps an unusual approach - to take something that has traditionally been reserved for high powered processors (running neural networks) and use a tool specifically designed for low-level, memory constrained devices (MicroROS) - but these are precisely the presuppositions TinyML seeks to challenge.

By combining MicroROS and Edge Impulse, the path to creating your own plug-and-play AI-driven peripherals for ROS2 systems becomes much more straightforward. This enables experimentation with a "distributed" approach to AI in robotics, wherein neural networks are run much closer to the sensors, and the central ROS2 computer can enjoy the benefits of model inferences without being bogged down by running many neural networks simultaneously.



________________

## Equipment and software

- Arduino Portenta H7 + vision shield
- Linux computer running ROS2


### Getting started

You'll need to install a few things in order to follow along with this tutorial:


#### MicroROS Arduino library

Clone the library from [this](https://github.com/micro-ROS/micro_ros_arduino) repository and add the .ZIP folder to your Arduino IDE. This library comes precompiled, but we'll need to rebuild it after we add the custom Edge Impulse ROS2 message types (to be discussed).


#### Custom Edge Impulse message types

To ease the process of interfacing Edge Impulse with MicroROS two custom message types were created:

- `EIClassification`: Contains a label and value, like `{'label': 'cat', 'value': 0.75}`. One classification contains one class name and the probability given to that class by the neural network.
- `EIResult`: Contains multiple classifications - as many as your neural network needs. A full result looks like this: `[{'label': 'cat', 'value': 0.75}, {'label': 'dog', 'value': 0.25}]`.

In order to use these message types they need to be added to both your ROS2 and MicroROS environments. Clone the MicroROS + Edge Impulse repository [here](https://github.com/avielbr/micro_ros_ei) and copy the `ei_interfaces` directory. This folder contains everything you need to build the custom message types. 


**To add it to your ROS2 system, navigate to:**

`ros2_ws/src`

and paste the `ei_interfaces` directory inside. `cd` back to your main `ros2_ws` directory and from the terminal run `colcon build`.

You can confirm the message types were added by running the following from the terminal:

`ros2 interface list | grep EI`

You should see:

```
ros2 interface list | grep EI
    ei_interfaces/msg/EIClassification
    ei_interfaces/msg/EIResult
```


To add it to your MicroROS environment, navigate to the MicroROS Arduino library (that you cloned added to the Arduino IDE). You need to paste the same `ei_interfaces` directory inside the special `extra_packages` directory in the Arduino library. For me the path is:

```
~/Arduino/libraries/micro_ros_arduino-2.0.5-humble/extras/library_generation/extra_packages
```

Paste the directory there, **return to the main** `micro_ros_arduino-2.0.5-humble` **directory,** and use the docker commands from [this part](micro_ros_arduino-2.0.5-humble) of the MicroROS Arduino readme:

```
docker pull microros/micro_ros_static_library_builder:humble

docker run -it --rm -v $(pwd):/project --env MICROROS_LIBRARY_FOLDER=extras microros/micro_ros_static_library_builder:humble -p portenta-m7
```

Note the `-p` flag at the end - it significantly reduces the build time if you specify your target. You can also run the command without this flag to build for all available targets, but it'll take a while.

____________


### Arduino code

Now it's time to export your Edge Impulse vision project as an Arduino library, and be sure to add the .ZIP folder to the Arduino IDE.

As for the example code for this project, find it [here](https://github.com/avielbr/micro_ros_ei/tree/main/examples/arduino/ei_micro_ros_portenta). Compile and upload the `.ino` file to your Arduino Portenta, and make sure the `.h` header file is in the same directory. I won't be writing a line-by-line explanation of the code here - but here is some info on key points that make this all work.

**Make sure to change the name of the included Edge Impulse library to the name of your own project:**

```c++
// Replace this with <name_of_your_ei_library_inferencing.h>
#include <micro_ros_ei_inferencing.h>
```


#### MicroROS publisher

Inside the `ei_result_publisher` file, note that we include the two message types we added before:

```c++
#include <ei_interfaces/msg/ei_result.h>
#include <ei_interfaces/msg/ei_classification.h>
```

The reason we need to add both is because `EIResult` is a sequence (array) of `EIClassification` messages, and in MicroROS you need to allocate memory for your message when setting everything up. Even if your neural network has more labels than than the 2 that I have for this project (human, background), the code will still work fine as it will automatically allocate enough memory for however many labels (and hence classifications) your `EIResult` message needs to support. You can see the section where the memory is allocated here:

```c++
msg.result.capacity = LABEL_COUNT;
msg.result.data = (ei_interfaces__msg__EIClassification*) malloc(msg.result.capacity * sizeof(ei_interfaces__msg__EIClassification));
msg.result.size = 0;

// Allocate memory to message
for (int32_t ix = 0; ix < LABEL_COUNT; ix++) {
	// If 20 characters isn't enough - increase this value
	msg.result.data[ix].label.capacity = 20;
	msg.result.data[ix].label.data = (char*) malloc(msg.result.data[ix].label.capacity * sizeof(char));
	msg.result.data[ix].label.size = 0;
	msg.result.size++;
}
```


Note that our `msg ` is initialized as type:

```c++
ei_interfaces__msg__EIResult msg;
```


You can see the names of the node and publisher:

```c++
RCCHECK(rclc_node_init_default(&node, "ei_micro_ros_node", "", &support));
...
RCCHECK(rclc_publisher_init_default(
	&publisher,
	&node,
	ROSIDL_GET_MSG_TYPE_SUPPORT(ei_interfaces, msg, EIResult),
	"/ei_micro_ros_publisher"));
```

These names are what will appear on your ROS2 system once the MicroROS agent detects your MicroROS publisher.


#### Main Portenta code

In the `.ino` file, you'll see that a lot of the code is taken directly from the Edge Impulse `ei_camera` example code [here](https://github.com/edgeimpulse/firmware-arduino-portenta-h7/blob/main/src/sensors/ei_camera.cpp). Let's focus on the moment that the `ei_impulse_result_t` object is transferred to the MicroROS publisher:

```c++
// Run the classifier
ei_impulse_result_t result = { 0 }; // Initialize result

EI_IMPULSE_ERROR err = run_classifier(&signal, &result, debug_nn); // Run classifier
	if (err != EI_IMPULSE_OK) {
		return;
}

fill_result_msg(result); // Store result data in MicroROS message
publish_msg(); // Publish message
```

---


### Putting everything together

#### MicroROS agent

OK, now it's time to run the MicroROS agent and see if our node is publishing as expected. The agent runs on your main ROS2 computer and serves as a middle man to allow your MicroROS device to communicate with your main ROS2 system. It's recommended to use the docker command for the agent. When you run this command be sure and use paste in your board port - in my case the Portenta H7 connects to `/dev/ttyACM0`.

```
docker run -it --rm -v /dev:/dev --privileged --net=host microros/micro-ros-agent:humble serial --dev [YOUR BOARD PORT] -v6
```

> Since you'll probably be using this command a bunch, you might find it convenient to make an alias for it :)

After starting the agent, you may have to reset your Arduino (with the reset button, or just unplug and reconnect).


In a separate terminal, check if the topic is listed. You should see the name of your topic:

```
ros2 topic list
    /ei_micro_ros_publisher 
    ...

```


To see the result messages, echo the topic:

```
ros2 topic echo /ei_micro_ros_publisher
```


And if everything worked you should see the result messages:

```
.
.
.
result:
- label: background
  value: 0.75390625
- label: human
  value: 0.24609375
---
result:
- label: background
  value: 0.69140625
- label: human
  value: 0.30859375
---
result:
- label: background
  value: 0.71875
- label: human
  value: 0.28125
---
.
.
.
```

Now you can subscribe to this topic as you would any other ROS2 topic!

---


### To Summarize

In this tutorial we looked at running a neural network and publishing its inferences from within a MicroROS node. Please note that the repository associated with this tutorial will be growing and support for additional boards (incl. non-Arduino boards) will be added. In the meantime your constructive feedback is warmly invited!

