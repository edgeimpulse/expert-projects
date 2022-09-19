---
description: Using computer vision to monitor a bird's egg production using an OpenMV Cam.
---

# Counting Eggs with Computer Vision 

Created By:
Kutluhan Aktar

Public Project Link:
[https://studio.edgeimpulse.com/public/134829/latest](https://studio.edgeimpulse.com/public/134829/latest)

![](.gitbook/assets/egg-counting-openmv/sandbox_1.jpg)

## Description

In poultry reproductive flocks, it is essential to achieve a large number of eggs with solid structure, optimal morphological composition, and interior quality. Also, these traits have a significant impact on the egg’s biological value determining the development stages of the embryo. However, the egg quality is determined based on many traits important for global egg production: and depends on many factors, including the diet, age of hens, and the feeding schedule. According to the latest experiments, the best performance by breeder hens is obtained by controlling their body weight by restricting their feed intake. A rationed feed is generally provided in a strict feeding schedule each morning and is expected to be consumed in about 4 hours. Since poultry eating habits and calcium consumption are related to their diurnal rhythm and time of ovulation to a lesser extent, it is crucial to follow a regular feeding schedule to maintain the high poultry health status and maximize egg quality[^1].

Even though there are various nutrition and management factors affecting egg production and quality, the feeding schedule proportional to cage density affects egg production considerably since hens can stop laying eggs intrinsically when they notice a sporadic feeding schedule or paltry feed. Hence, applying a regular and nutritional feeding regimen helps hens lay eggs abundantly.

Furthermore, as the hen’s age increases, the weight of the produced egg usually increases, and the weekly produced egg number decreases. Although each hen has an inveterate laying time, the weekly produced egg number denotes the overall health condition of the hens in the coop. Therefore, tracking unhatched eggs and logging the daily produced egg number assist farmers in determining a potential contagious poultry disease or malnutrition.

However, these processes can be compelling and arduous for small businesses in the poultry industry or people raising domesticated birds in their houses or backyards to produce eggs for profit. Since I am also raising quails as pets on my balcony, I am well aware of the struggles with tracking the poultry feeder status and the produced egg number daily. Hence, I decided to create this budget-friendly and accessible device to track the poultry feeder status and the produced egg number automatically with object detection.

To recognize eggs in the coop (cage) and track the poultry feeder status accurately, I needed to collect data from the coop in order to train my object detection model with notable validity. Since OpenMV Cam H7 is a considerably small high-performance microcontroller board designed for machine vision applications in the real world, I decided to utilize OpenMV Cam H7 in this project. Also, I could easily capture images of my coop and store them on an SD card since OpenMV Cam H7 has a built-in MicroSD card module. Then, I employed a color TFT screen (ST7735) to display a real-time video stream and the prediction (detection) results.

After completing my data set by taking pictures of the produced eggs and the poultry feeder in my quail coop, I built my object detection model with Edge Impulse to recognize (count) the produced eggs and track the poultry feeder status: OK or EMPTY. I utilized [Edge Impulse FOMO](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices) (Faster Objects, More Objects) algorithm to train my model, which is a novel machine learning algorithm that brings object detection to highly constrained devices. Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I had not encountered any issues while uploading and running my model on OpenMV Cam H7. As labels, I appended two main classes to the file names while capturing and storing pictures:

- Egg
- Feeder

After training and testing my object detection (FOMO) model, I deployed and uploaded the model on OpenMV Cam H7 as an OpenMV firmware. Therefore, the device is capable of counting the produced eggs and tracking the poultry feeder status by running the model independently without any additional procedures.

Since I decided to log the detection results on a MySQL database and inform the user of the detection results over WhatsApp, I set an Apache HTTP Server on the [DFRobot LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html) and developed a PHP web application from scratch. To be able to send WhatsApp messages to a verified phone number, I utilized Twilio's API for WhatsApp.

Since OpenMV Cam H7 does not provide Wi-Fi or BLE connectivity, I employed WizFi360-EVB-Pico to communicate with OpenMV Cam H7 and transfer the detection results to the web application. WizFi360-EVB-Pico is a budget-friendly development board based on Raspberry Pi RP2040 and enables Wi-Fi connectivity with the integrated WizFi360 Wi-Fi module. Also, I connected a DHT22 temperature and humidity sensor to WizFi360-EVB-Pico to log and get informed of the current weather condition of my coop (cage) in addition to the detection results.

Lastly, to make the device as robust, sturdy, and compact as possible while experimenting with it in my quail coop (cage), I designed a quail-themed and coop-compatible case with a sliding front cover and a moveable camera handle (3D printable).

So, this is my project in a nutshell 😃

In the following steps, you can find more detailed information on coding, capturing coop images, storing pictures on an SD card, building an object detection (FOMO) model with Edge Impulse, running the model on OpenMV Cam H7, and sending the detection results over WhatsApp via WizFi360-EVB-Pico.

🎁🎨 Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sponsoring these products:

⭐ LattePanda 3 Delta 864 | [Inspect](https://www.dfrobot.com/product-2594.html?tracking=60f546f8002be) 

⭐ DFRobot 8.9" 1920x1200 IPS Touch Display | [Inspect](https://www.dfrobot.com/product-2007.html?tracking=60f546f8002be) 

🎁🎨 Huge thanks to WIZnet for providing me with a [WizFi360-EVB-Pico](https://docs.wiznet.io/Product/Open-Source-Hardware/wizfi360-evb-pico/).

🎁🎨 Also, huge thanks to [Creality](https://store.creality.com/) for sending me a [Creality CR-200B 3D Printer](https://www.creality.com/products/cr-200b-3d-printer).

![image](.gitbook/assets/egg-counting-openmv/home_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/home_4.jpg)

![image](.gitbook/assets/egg-counting-openmv/collect_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/collect_5.jpg)

![image](.gitbook/assets/egg-counting-openmv/gif_collect.gif)

![image](.gitbook/assets/egg-counting-openmv/run_model_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/gif_run.gif)

![image](.gitbook/assets/egg-counting-openmv/app_6.png)

![image](.gitbook/assets/egg-counting-openmv/whatsapp_message_3.jpg)

## Step 1: Designing and printing a quail-themed and coop-compatible case

Since I focused on building a user-friendly and accessible device compatible with a wire quail coop (cage) in this project, I decided to design a robust and compact case allowing the user to attach the device to the wire cage via hooks and capture coop images effortlessly. To avoid overexposure to dust and prevent loose wire connections, I added a sliding front cover to the case. Then, I designed a separate moveable camera handle to capture coop images at different angles with OpenMV Cam H7. Also, I decided to adorn the sliding front cover with a quail logo and the OpenMV icon so as to highlight the poultry theme gloriously.

I designed the main case, its sliding front cover, and the moveable camera handle in Autodesk Fusion 360. You can download their STL files below.

![image](.gitbook/assets/egg-counting-openmv/model_1.png)

![image](.gitbook/assets/egg-counting-openmv/model_2.png)

![image](.gitbook/assets/egg-counting-openmv/model_3.png)

![image](.gitbook/assets/egg-counting-openmv/model_4.png)

![image](.gitbook/assets/egg-counting-openmv/model_5.png)

![image](.gitbook/assets/egg-counting-openmv/model_6.png)

![image](.gitbook/assets/egg-counting-openmv/model_7.png)

![image](.gitbook/assets/egg-counting-openmv/model_8.png)

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

![image](.gitbook/assets/egg-counting-openmv/model_9.png)

![image](.gitbook/assets/egg-counting-openmv/model_10.png)

![image](.gitbook/assets/egg-counting-openmv/model_11.png)

In addition to the mentioned parts, I also designed a complementing sand bath for my quail cage. Since quails usually choose to lay eggs in the sand, I utilized this sand bath to contain the produced eggs while capturing coop images to train my object detection model. You can also download its STL file below.

![image](.gitbook/assets/egg-counting-openmv/model_s_1.png)

![image](.gitbook/assets/egg-counting-openmv/model_s_2.png)

Note: The pictures above are for demonstrating the sliced models: I needed to split some models to make them compatible with the CR-200B build size (200 x 200 x 200 mm).

Since I wanted to create a solid structure conforming with quails' natural habitat and avoid shiny color themes which can trigger quails to attack the case, I utilized these PLA filaments:

- Bone White
- ePLA-Matte Almond Yellow

Finally, I printed all parts (models) with my Creality CR-200B 3D Printer. It is my first fully-enclosed FDM 3D printer, and I must say that I got excellent prints effortlessly with the CR-200B :)

If you are a maker planning to print your 3D models to create more complex projects, I highly recommend the CR-200B. Since the CR-200B is fully-enclosed, you can print high-resolution 3D models with PLA and ABS filaments. Also, it has a smart filament runout sensor and the resume printing option for power failures.

According to my experience, there are only two downsides of the CR-200B: relatively small build size (200 x 200 x 200 mm) and manual leveling. Conversely, thanks to the large leveling nuts and assisted leveling, I was able to level the bed and start printing my first model in less than 30 minutes.

:hash: Before the first use, remove unnecessary cable ties and apply grease to the rails.

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_1.jpg)

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_2.jpg)

:hash: Test the nozzle and hot bed temperatures.

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_3.jpg)

:hash: Go to *Settings ➡ Leveling* and adjust four predefined points by utilizing the leveling nuts.

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_4.jpg)

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_5.jpg)

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_6.jpg)

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_7.jpg)

:hash: Finally, attach the spool holder and feed the extruder with the filament.

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_8.jpg)

:hash: Since the CR-200B is not officially supported by Cura, select the Ender-3 profile and change the build size to 200 x 200 x 200 mm. Also, to compensate for the nozzle placement, set the *Nozzle offset X* and *Y* values to -10 mm on the *Extruder 1* tab.

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_cura_1.PNG)

![image](.gitbook/assets/egg-counting-openmv/cr_200b_set_cura_2.PNG)

## Step 1.1: Assembling the case and making connections & adjustments

```
// Connections
// WizFi360-EVB-Pico :  
//                                DHT22 Temperature and Humidity Sensor
// D28 --------------------------- DATA
// 3.3V -------------------------- VCC
// GND --------------------------- GND
//                                OpenMV Cam H7
// D13 --------------------------- P4
// D12 --------------------------- P5
//
//
//
// OpenMV Cam H7 :
//                                ST7735 1.8" Color TFT Display
// 3.3V -------------------------- LED
// P2  --------------------------- SCK
// P0  --------------------------- SDA
// P8  --------------------------- AO
// P7  --------------------------- RESET
// P3  --------------------------- CS
// GND --------------------------- GND
// 3.3V -------------------------- VCC
//                                Control Button (A)
// P6  --------------------------- +
//                                Control Button (B)
// P1  --------------------------- +
```

First of all, I connected a color TFT screen (ST7735) to [OpenMV Cam H7](https://openmv.io/products/openmv-cam-h7) so as to display the real-time video stream, captured coop images, and the detection results (the produced egg number and the poultry feeder status) after running the object detection (FOMO) model. To append labels to the file names while capturing coop images and storing them on the SD card, I added two control buttons (6x6), as shown in the schematic below.

To be able to transfer the detection results to [WizFi360-EVB-Pico](https://docs.wiznet.io/Product/Open-Source-Hardware/wizfi360-evb-pico/) via serial communication, I connected the hardware serial port of OpenMV Cam H7 (UART 3) to a software serial port of WizFi360-EVB-Pico. Also, I connected a DHT22 temperature and humidity sensor to WizFi360-EVB-Pico to collect the current weather information and send the detection results with the collected weather data to the web application via an HTTP GET request.

To power OpenMV Cam H7 and WizFi360-EVB-Pico via their voltage input pins (VIN and VSYS), I utilized a DC barrel jack adapter connected to my Xiaomi power bank.

After completing breadboard connections and adjustments successfully, I made the breadboard connection points rigid by utilizing a hot glue gun.

![image](.gitbook/assets/egg-counting-openmv/breadboard_1.jpg)

![image](.gitbook/assets/egg-counting-openmv/breadboard_1.jpg)

After printing all parts (models), I fastened all components except OpenMV Cam H7 to their corresponding slots on the main case via the hot glue gun.

Then, I attached OpenMV Cam H7 to the separate moveable handle allowing capturing coop images at different angles.

Finally, I placed the sliding front cover via its dents.

![image](.gitbook/assets/egg-counting-openmv/assembly_1.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_3.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_4.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_5.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_6.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_7.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_8.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_9.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_10.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_11.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_12.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_13.jpg)

![image](.gitbook/assets/egg-counting-openmv/assembly_14.jpg)

After completing assembling, I placed my 3D-printed sand bath in the coop (cage) and hung the main case onto the wire cage via its hooks.

![image](.gitbook/assets/egg-counting-openmv/sandbox_1.jpg)

![image](.gitbook/assets/egg-counting-openmv/home_3.jpg)

![image](.gitbook/assets/egg-counting-openmv/home_4.jpg)

## Step 2: Creating a Twilio account to send messages over WhatsApp

To get notification messages over WhatsApp, I utilized Twilio's API for WhatsApp. [Twilio](https://www.twilio.com/messaging/whatsapp) gives the user a simple and reliable way to send WhatsApp messages to a verified phone number free of charge. Also, Twilio provides official helper libraries for different programming languages, including PHP.

:hash: First of all, sign up for [Twilio](https://www.twilio.com/try-twilio) and create a new free trial account (project).

![image](.gitbook/assets/egg-counting-openmv/twilio_set_1.png)

![image](.gitbook/assets/egg-counting-openmv/twilio_set_2.png)

:hash: Then, verify a phone number for the account (project) and set the account settings for the WhatsApp API in PHP.

![image](.gitbook/assets/egg-counting-openmv/twilio_set_3.png)

![image](.gitbook/assets/egg-counting-openmv/twilio_set_4.png)

:hash: Go to the Twilio Sandbox for WhatsApp to obtain the verification code for joining the verified phone number. Then, send the given verification code to the verified phone number from your phone to activate a WhatsApp session.

![image](.gitbook/assets/egg-counting-openmv/twilio_set_5.png)

![image](.gitbook/assets/egg-counting-openmv/whatsapp_message_1.jpg)

:hash: Finally, download the [Twilio PHP Helper Library](https://github.com/twilio/twilio-php) and go to *Account ➡ API keys & tokens* to get the account SID and the auth token under *Live credentials* so as to send messages with the WhatsApp API.

![image](.gitbook/assets/egg-counting-openmv/twilio_set_6.png)

![image](.gitbook/assets/egg-counting-openmv/twilio_set_7.png)

## Step 3: Developing a web application in PHP to log detection results

To be able to log the detection results with the collected weather data transmitted by WizFi360-EVB-Pico and send WhatsApp messages via the Twilio PHP Helper Library to inform the user of the detection results, I decided to develop a web application in PHP named *poultry_feeder_and_egg_tracker*.

As shown below, the web application consists of one folder and five files:


- /assets
  - class.php
  - icon.png
  - index.css
- get_data.php
- index.php

I also employed the web application to add a timestamp for each data record before appending them to the MySQL database table. Therefore, the application shows these data parameters for each data record:


- Date
- Temperature
- Humidity
- Egg Count
- Feeder Status

You can download and inspect the web application in the ZIP file format below.

📁 *class.php*

In the *class.php* file, in order to run all functions successfully, I created a class named *poultry_feeder*.

⭐ Include the Twilio PHP Helper Library.

```
require_once '/twilio-php-main/src/Twilio/autoload.php'; 
use Twilio\Rest\Client;
```

⭐ Define the *poultry_feeder* class and its functions:

⭐ In the *__init__* function, define the Twilio account information (account SID, auth token, verified and registered phone numbers), the Twilio client object, and the MySQL database server settings.

```
	public function __init__($conn, $table){
		# Define the Twilio account information.
		$this->account = array(	
				"sid" => "[sid]",
				"auth_token" => "[auth_token]",
				"registered_phone" => "+[registered_phone]",
				"verified_phone" => "+14155238886"
		);
		
		# Define the Twilio client object.
		$this->twilio = new Client($this->account["sid"], $this->account["auth_token"]);
		
        # Define the MySQL database server settings.
        $this->conn = $conn;
		$this->table = $table;		
	}
```

⭐ In the *send_message* function, send a WhatsApp message from the verified phone to the registered phone via the Twilio PHP Helper Library.

```
	public function send_message($text){
		$message = $this->twilio->messages 
                  ->create("whatsapp:".$this->account["registered_phone"],
                           array( 
                               "from" => "whatsapp:".$this->account["verified_phone"],       
                               "body" => $text 
                           ) 
                  ); 
 
        echo '&lt;br>&lt;br>WhatsApp Message Send...';	
	}
```

⭐ In the *insert_new_data* function, append the transferred detection results, the collected weather data, and the current date & time to the given database table.

```
	public function insert_new_data($d1, $d2, $d3, $d4, $d5){
		$sql = "INSERT INTO `$this->table`(`date`, `temperature`, `humidity`, `egg_count`, `feeder_status`) VALUES ('$d1', '$d2', '$d3', '$d4', '$d5')";
		if(mysqli_query($this->conn, $sql)){ return true; }
		else{ return false; }
	}
```

⭐ In the *database_create_table* function, create the required database table — *entries*.

```
	public function database_create_table(){
		// Create a new database table.
		$sql_create = "CREATE TABLE `$this->table`(		
							id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
							`date` varchar(255) NOT NULL,
							temperature varchar(255) NOT NULL,
							humidity varchar(255) NOT NULL,
							egg_count varchar(255) NOT NULL,
							feeder_status varchar(255) NOT NULL
					   );";
		if(mysqli_query($this->conn, $sql_create)) echo("&lt;br>&lt;br>Database Table Created Successfully!");
```

⭐ In the *obtain_results* function, get all registered data records (results) from the given database table and return them as an array.

```
	public function obtain_results(){
	    $sql = "SELECT * FROM `$this->table`";
		$result = mysqli_query($this->conn, $sql);
		$check = mysqli_num_rows($result);
		if($check > 0){
			$data_array = array();
			while($row = mysqli_fetch_assoc($result)){
				array_push($data_array, $row);
			}
			return $data_array;
		}else{
			$no_data = array([
					"date" => "X",	
					"temperature" => "X",
					"humidity" => "X",	
					"egg_count" => "X",	
					"feeder_status" => "X"
			]);
			return $no_data;
		}
	} 
```

⭐ Define the required MySQL database connection settings for LattePanda 3 Delta 864.

```
$server = array(
	"name" => "localhost",
	"username" => "root",
	"password" => "",
	"database" => "poultry_feeder",
	"table" => "entries"

);

$conn = mysqli_connect($server["name"], $server["username"], $server["password"], $server["database"]);
```

📁 *get_data.php*

⭐ Include the *class.php* file.

⭐ Define the *feeder* object of the *poultry_feeder* class with its required parameters.

```
include_once "assets/class.php";

# Define a new class object named 'feeder'.
$feeder = new poultry_feeder();
$feeder->__init__($conn, $server["table"]);
```

⭐ Obtain the transferred detection results and weather data from WizFi360-EVB-Pico.

⭐ Then, insert the received information with the current date & time into the given database table — *entries*.

⭐ Finally, send the received information with the current date & time via WhatsApp to the registered phone number so as to inform the user of the detection results.

```
if(isset($_GET["temperature"]) && isset($_GET["humidity"]) && isset($_GET["egg_count"]) && isset($_GET["feeder_status"])){
	// Insert the received information into the given database table.	
	$date = date("Y/m/d_h:i:s");
	if($feeder->insert_new_data($date, $_GET["temperature"], $_GET["humidity"], $_GET["egg_count"], $_GET["feeder_status"])){
		echo("Data received and saved successfully!");
	}else{
		echo("Database error!");
	}
	// Send the received information via WhatsApp to the registered phone so as to notify the user.
	$feeder->send_message(	"⏰ $date\n\n"
	                        ."📌 Object Detection\n🥚 Egg Count: "
							.$_GET["egg_count"]
							."\n🐦 Feeder Status: "
							.$_GET["feeder_status"]
							."\n\n📌 Weather\n🌡️ Temperature: "
							.$_GET["temperature"]
							."°C\n💧 Humidity: "
							.$_GET["humidity"]."%"
		                 );
}else{
	echo("Waiting Data...");
}
```

⭐ If requested, create the required database table — *entries*.

```
if(isset($_GET["create_table"]) && $_GET["create_table"] == "OK") $feeder->database_create_table();
```

📁 *index.php*

⭐ Include the *class.php* file.

⭐ Define the *feeder* object of the *poultry_feeder* class with its required parameters.

```
	include_once "assets/class.php";
	
	# Define a new class object named 'feeder'.
	$feeder = new poultry_feeder();
	$feeder->__init__($conn, $server["table"]);
```

⭐ Get the registered data records and the total entry number from the given database table.

```
	$data_array = $feeder->obtain_results();
	$data_total = count($data_array);
```

⭐ Show all registered data records in a table.

```
  foreach($data_array as $row){
	  if($row["date"] == "X") $data_total = 0;
	  echo '
        &lt;tr>
           &lt;td>'.$row["date"].'&lt;/td>
           &lt;td>'.$row["temperature"].'&lt;/td>
           &lt;td>'.$row["humidity"].'&lt;/td>
           &lt;td>'.$row["egg_count"].'&lt;/td>
           &lt;td>'.$row["feeder_status"].'&lt;/td>
        &lt;/tr>		   
	  ';
  }
```

![image](.gitbook/assets/egg-counting-openmv/code_app_1.png)

![image](.gitbook/assets/egg-counting-openmv/code_app_2.png)

![image](.gitbook/assets/egg-counting-openmv/code_app_3.png)

![image](.gitbook/assets/egg-counting-openmv/code_app_4.png)

![image](.gitbook/assets/egg-counting-openmv/code_app_5.png)

## Step 3.1: Setting and running the web application on LattePanda 3 Delta 864

Since I have got a test sample of the brand-new [LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html), I decided to host my web application on LattePanda 3 Delta. Therefore, I needed to set up a LAMP web server.

LattePanda 3 Delta is a pocket-sized hackable computer that provides ultra performance with the Intel 11th-generation Celeron N5105 processor.

Plausibly, LattePanda 3 Delta can run the XAMPP application. So, it is effortless to create a server and a database with LattePanda 3 Delta.

![image](.gitbook/assets/egg-counting-openmv/lattepanda_show.jpg)

:hash: First of all, install and set up [the XAMPP application](https://www.apachefriends.org/).

:hash: Then, go to the *XAMPP Control Panel* and click the *MySQL Admin* button.

:hash: Once the *phpMyAdmin* tool pops up, create a new database named *poultry_feeder*.

![image](.gitbook/assets/egg-counting-openmv/app_server_set_1.png)

![image](.gitbook/assets/egg-counting-openmv/app_server_set_2.png)

![image](.gitbook/assets/egg-counting-openmv/app_server_set_3.png)

After running the web application by uploading it to the *htdocs* folder:

💻 On the *get_data.php* file:

⭐ If the web application did not receive detection results and the collected weather data from WizFi360-EVB-Pico via an HTTP GET request, it prints: *Waiting Data...*

⭐ Otherwise, the web application saves the received information to the given database table and sends a WhatsApp message to inform the user of the detection results.

*localhost/poultry_feeder_and_egg_tracker/get_data.php*

![image](.gitbook/assets/egg-counting-openmv/app_1.png)

![image](.gitbook/assets/egg-counting-openmv/app_4.png)

⭐ If the *create_table* parameter is set as OK, the web application creates the required database table (entries) and prints: *Database Table Created Successfully!*

![image](.gitbook/assets/egg-counting-openmv/app_2.png)

💻 On the *index.php* file:

⭐ The application interface shows all registered data records in the given database table as a list consisting of these parameters:


- Date
- Temperature
- Humidity
- Egg Count
- Feeder Status

⭐ If there is no data record in the database table, the interface displays *'X'* for each parameter.

![image](.gitbook/assets/egg-counting-openmv/app_3.png)

![image](.gitbook/assets/egg-counting-openmv/app_5.png)

## Step 4: Capturing and storing images of the coop w/ OpenMV Cam H7

Before proceeding with the following steps, I needed to install the OpenMV IDE in order to program OpenMV Cam H7.

Plausibly, the OpenMV IDE includes all required libraries and modules for this project. Therefore, I did not need to download additional modules after installing the OpenMV IDE from [here](https://openmv.io/pages/download).

You can get more information regarding the specific OpenMV MicroPython libraries from [here](https://docs.openmv.io/library/index.html#libraries-specific-to-the-openmv-cam).

After setting up OpenMV Cam H7 on the OpenMV IDE, I programmed OpenMV Cam H7 to capture coop images showing the produced eggs and the poultry feeder in order to store them on the SD card and create appropriately labeled samples for the Edge Impulse object detection (FOMO) model.

Since I needed to assign labels for each captured coop image to create a valid data set for the object detection model, I utilized the control buttons attached to OpenMV Cam H7 so as to choose among two different classes. After selecting a class, OpenMV Cam H7 captures a picture, appends the selected class name (Egg or Feeder) with the current date & time to the file name, and then saves the captured image to the SD card under the *samples* folder.


- Control Button (A) ➡ Egg
- Control Button (B) ➡ Feeder

You can download the *poultry_egg_tracker_data_collect.py* file to try and inspect the code for capturing images and storing them on the SD card via OpenMV Cam H7.

⭐ Include the required modules.

```
import sensor, image, lcd
from pyb import RTC, Pin, LED
from time import sleep
```

⭐ Initialize the camera sensor with its required settings (pixel format and frame size).

```
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2) # Special 128x160 framesize for LCD Shield.
```

⭐ Initialize the ST7735 1.8" color TFT screen.

⭐ Set the built-in RTC (real-time clock).

```
lcd.init()

# Set the built-in RTC (real-time clock).
rtc = RTC()
rtc.datetime((2022, 8, 30, 2, 12, 25, 0, 0))
```

⭐ In the *save_sample* function:

⭐ Get the current date and time.

⭐ Capture an image with OpenMV Cam H7 as a sample in the given frame settings (QVGA).

⭐ Save the captured image in the JPG format and turn the built-in RGB LED to the selected class' unique color.

⭐ Show a glimpse of the captured image on the ST7735 1.8" color TFT screen.

⭐ Also, show the selected class name with its unique color on the screen.

⭐ Finally, turn off the built-in RGB LED.

```
def save_sample(name, color, leds):
    # Get the current date and time.
    date = rtc.datetime()
    date = ".{}_{}_{}_{}-{}-{}".format(date[0], date[1], date[2], date[4], date[5], date[6])
    # Take a picture with the given frame settings (QVGA).
    sensor.set_framesize(sensor.QVGA)
    sample = sensor.snapshot()
    sleep(1)
    # Save the captured image.
    file_name = "/samples/" + name + date + ".jpg"
    sample.save(file_name, quality=20)
    if leds[0]: red.on()
    if leds[1]: green.on()
    if leds[2]: blue.on()
    print("\nSample Saved: " + file_name + "\n")
    # Show a glimpse of the captured image on the ST7735 1.8" color TFT screen.
    sensor.set_framesize(sensor.QQVGA2)
    lcd_img = sensor.snapshot()
    lcd_img.draw_rectangle(0, 0, 128, 30,fill=1, color =(0,0,0))
    lcd_img.draw_string(int((128-16*len(name))/2), 3, name, color=color, scale=2)
    lcd_img.draw_rectangle(0, 130, 128, 160, fill=1, color =(0,0,0))
    lcd_img.draw_string(int((128-16*len("Saved!"))/2), 132, "Saved!", color=color, scale=2)
    lcd_img.draw_cross(64, 80, color=color, size=8, thickness=2)
    lcd.display(lcd_img)
    sleep(5)
    red.off()
    green.off()
    blue.off()
```

⭐ In the *while* loop, display a real-time video stream on the ST7735 1.8" color TFT screen and save image samples of the selected class (Egg or Feeder).

```
while(True):
    # Display a real-time video stream on the ST7735 1.8" color TFT screen.
    sensor.set_framesize(sensor.QQVGA2)
    lcd_img = sensor.snapshot()
    lcd.display(lcd_img)
    # Save samples.
    if(button_a.value() == False):
        save_sample("Egg", (255,0,255), (1,0,1))
    if(button_b.value() == False):
        save_sample("Feeder", (0,255,0), (0,1,0))
```

![image](.gitbook/assets/egg-counting-openmv/code_collect_1.png)

![image](.gitbook/assets/egg-counting-openmv/code_collect_2.png)

## Step 4.1: Saving the captured coop pictures to the SD card as samples

After uploading and running the code for capturing coop pictures and saving them to the SD card on OpenMV Cam H7:

🐤🥚 The device displays a real-time video stream on the ST7735 1.8" color TFT screen.

![image](.gitbook/assets/egg-counting-openmv/collect_1.jpg)

🐤🥚 If the control button (A) is pressed, the device pauses the video stream and captures a picture. If the device captures the picture successfully, it turns the built-in RGB LED to magenta, appends the selected class name (Egg) with the current date & time to the file name, and stores the recently captured image on the SD card.

*Egg.2022_8_30_12-26-11.jpg*

🐤🥚 Then, the device displays the selected class name and the crosshair with the assigned color on the ST7735 1.8" TFT screen.

🐤🥚 Finally, the device resumes the video stream and turns off the RGB LED.

![image](.gitbook/assets/egg-counting-openmv/collect_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/collect_3.jpg)

![image](.gitbook/assets/egg-counting-openmv/collect_4.jpg)

🐤🥚 If the control button (B) is pressed, the device pauses the video stream and captures a picture. If the device captures the picture successfully, it turns the built-in RGB LED to green, appends the selected class name (Feeder) with the current date & time to the file name, and stores the recently captured image on the SD card.

*Feeder.2022_8_30_12-28-46.jpg*

🐤🥚 Then, the device displays the selected class name and the crosshair with the assigned color on the ST7735 1.8" TFT screen.

🐤🥚 Finally, the device resumes the video stream and turns off the RGB LED.

![image](.gitbook/assets/egg-counting-openmv/collect_5.jpg)

![image](.gitbook/assets/egg-counting-openmv/collect_6.jpg)

![image](.gitbook/assets/egg-counting-openmv/collect_7.jpg)

🐤🥚 Also, the device prints notifications and the captured image data on the OpenMV IDE serial monitor for debugging.

![image](.gitbook/assets/egg-counting-openmv/open_serial_collect_1.png)

As far as my experiments go, the device operates faultlessly while capturing coop images and saving them to the SD card :)

![image](.gitbook/assets/egg-counting-openmv/gif_collect.gif)

After capturing numerous coop images depicting the daily produced eggs and the filled poultry feeder, I elicited my data set, including training and testing samples for my object detection (FOMO) model.

![image](.gitbook/assets/egg-counting-openmv/data_collect_1.png)

## Step 5: Building an object detection (FOMO) model with Edge Impulse

When I completed capturing coop images and storing them on the SD card, I started to work on my object detection (FOMO) model to track (count) the daily produced eggs and detect the poultry feeder status.

Since Edge Impulse supports almost every microcontroller and development board due to its model deployment options, I decided to utilize Edge Impulse to build my object detection model. Also, Edge Impulse provides an elaborate machine learning algorithm (FOMO) for running more accessible and faster object detection models on edge devices such as OpenMV Cam H7.

[Edge Impulse FOMO (Faster Objects, More Objects)](https://docs.edgeimpulse.com/docs/edge-impulse-studio/learning-blocks/object-detection/fomo-object-detection-for-constrained-devices) is a novel machine learning algorithm that brings object detection to highly constrained devices. FOMO models can count objects, find the location of the detected objects in an image, and track multiple objects in real time, requiring up to 30x less processing power and memory than MobileNet SSD or YOLOv5.

Even though Edge Impulse supports JPG or PNG files to upload as samples directly, each training or testing sample needs to be labeled manually. Therefore, I needed to follow the steps below to format my data set so as to train my object detection model accurately:


- Data Scaling (Resizing)
- Data Labeling

Since I appended the assigned class names to the file names while capturing and storing coop images, I preprocessed my data set effortlessly to label each image sample on Edge Impulse:


- Egg
- Feeder

Plausibly, Edge Impulse allows building predictive models optimized in size and accuracy automatically and deploying the trained model as an OpenMV firmware. Therefore, after scaling (resizing) and preprocessing my data set to label samples, I was able to build an accurate object detection model to count the daily produced eggs and track the poultry feeder status, which runs on OpenMV Cam H7 without getting memory allocation errors.

You can inspect [my object detection (FOMO) model on Edge Impulse](https://studio.edgeimpulse.com/public/134829/latest) as a public project.

## Step 5.1: Uploading images (samples) to Edge Impulse and labeling samples

After collecting training and testing image samples, I uploaded them to my project on Edge Impulse. Then, I labeled the filled poultry feeder and the daily produced eggs on each sample with egg and feeder classes.

Since I have a plastic ground poultry feeder in my quail cage, I decided to train my object detection model on recognizing the filled feeding holes. If the model cannot detect any feeding holes, which means that the poultry feeder needs to be refilled.

:hash: First of all, sign up for [Edge Impulse](https://www.edgeimpulse.com/) and create a new project.

![image](.gitbook/assets/egg-counting-openmv/edge_set_1.png)

:hash: To be able to label image samples manually on Edge Impulse for object detection models, go to *Dashboard ➡ Project info ➡ Labeling method* and select *Bounding boxes (object detection)*.

![image](.gitbook/assets/egg-counting-openmv/edge_set_2.png)

:hash: Navigate to the *Data acquisition* page and click the *Upload existing data* button.

![image](.gitbook/assets/egg-counting-openmv/edge_set_3.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_4.png)

:hash: Then, choose the data category (training or testing), select image files, and click the *Begin upload* button.

![image](.gitbook/assets/egg-counting-openmv/edge_set_5.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_6.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_7.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_8.png)

After uploading my data set successfully, I labeled the daily produced eggs and the filled feeding holes on each image sample manually with two classes — *egg* and *feeder*. In Edge Impulse, labeling an object is as easy as dragging a box around it and entering a label. Also, Edge Impulse runs a tracking algorithm in the background while labeling objects, so it moves bounding boxes automatically for the same objects in different images.

:hash: Go to *Data acquisition ➡ Labeling queue (Object detection labeling)*. It shows all the unlabeled images (training and testing) remaining in the given data set.

:hash: Finally, select an unlabeled image, drag bounding boxes around objects, click the *Save labels* button, and repeat this process until the whole data set is labeled.

![image](.gitbook/assets/egg-counting-openmv/edge_set_9.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_10.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_11.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_12.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_13.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_14.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_15.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_16.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_17.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_18.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_19.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_20.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_21.png)

![image](.gitbook/assets/egg-counting-openmv/edge_set_22.png)

## Step 5.2: Training the FOMO model on quail eggs and poultry feeder status

After labeling my training and testing samples successfully, I designed an impulse and trained it on detecting the two mentioned classes — *egg* and *feeder*.

An impulse is a custom neural network model in Edge Impulse. I created my impulse by employing the *Image* preprocessing block and the *Object Detection (Images)* learning block.

The *Image* preprocessing block optionally turns the input image format to grayscale and generates a features array from the raw image.

The *Object Detection (Images)* learning block represents a machine learning algorithm that detects objects on the given image, distinguished between model labels *(egg* and *feeder)*.

:hash: Go to the *Create impulse* page and set image width and height parameters to 160. Then, select the resize mode parameter as *Fit shortest axis* so as to scale (resize) given training and testing image samples.

:hash: Select the *Image* preprocessing block and the *Object Detection (Images)* learning block. Finally, click *Save Impulse*.

![image](.gitbook/assets/egg-counting-openmv/edge_train_1.png)

:hash: Before generating features for the object detection model, go to the *Image* page and set the *Color depth* parameter as *Grayscale*. Then, click *Save parameters*.

![image](.gitbook/assets/egg-counting-openmv/edge_train_2.png)

:hash: After saving parameters, click *Generate features* to apply the *Image* preprocessing block to training image samples.

![image](.gitbook/assets/egg-counting-openmv/edge_train_3.png)

![image](.gitbook/assets/egg-counting-openmv/edge_train_4.png)

:hash: Finally, navigate to the *Object detection* page and click *Start training*.

![image](.gitbook/assets/egg-counting-openmv/edge_train_5.png)

![image](.gitbook/assets/egg-counting-openmv/edge_train_6.png)

According to my experiments with my object detection model, I modified the neural network settings and architecture to build an object detection model with high accuracy and validity:

📌 Neural network settings:


- Number of training cycles ➡ 100
- Learning rate ➡ 0.020
- Validation set size ➡ 10

📌 Neural network architecture:


- FOMO (Faster Objects, More Objects) MobileNetV2 0.35

After generating features and training my FOMO model with training samples, Edge Impulse evaluated the F1 score (accuracy) as *100%*.

The F1 score (accuracy) is approximately *100%* due to the modest volume and variety of training samples showing the daily produced eggs and the poultry feeder status. In technical terms, the model trains on limited validation samples. Therefore, I am still collecting data to improve my training data set.

![image](.gitbook/assets/egg-counting-openmv/edge_train_7.png)

If you encounter any memory allocation errors while uploading the model to OpenMV Cam H7 as an OpenMV firmware, try utilizing 80 x 80 or 48 x 48 image resolutions instead of 160 x 160 while creating your impulse. Even though smaller resolutions plummet the model accuracy,  they also reduce the model size.

![image](.gitbook/assets/egg-counting-openmv/edge_train_8.png)

![image](.gitbook/assets/egg-counting-openmv/edge_train_9.png)

## Step 5.3: Evaluating the model accuracy and deploying the model

After building and training my object detection model, I tested its accuracy and validity by utilizing testing image samples.

The evaluated accuracy of the model is *100%*.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

![image](.gitbook/assets/egg-counting-openmv/edge_test_1.png)

![image](.gitbook/assets/egg-counting-openmv/edge_test_2.png)

![image](.gitbook/assets/egg-counting-openmv/edge_test_3.png)

After validating my object detection model, I deployed it as fully optimized OpenMV firmware. This is the preferred method since the deployed firmware contains merely the object detection model and what is necessary to run the impulse. So, it does not consume much memory space and cause running into memory allocation issues.

:hash: To deploy the validated model as an OpenMV firmware, navigate to the *Deployment* page and select *OpenMV firmware*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as an OpenMV firmware in [the generated ZIP folder](https://docs.edgeimpulse.com/docs/deployment/running-your-impulse-openmv#deploying-your-impulse-as-an-openmv-firmware).

![image](.gitbook/assets/egg-counting-openmv/edge_deploy_1.png)

![image](.gitbook/assets/egg-counting-openmv/edge_deploy_2.png)

![image](.gitbook/assets/egg-counting-openmv/edge_deploy_3.png)

## Step 6: Setting up the Edge Impulse FOMO model on OpenMV Cam H7

After building, training, and deploying my object detection (FOMO) model as an OpenMV firmware on Edge Impulse, I needed to flash OpenMV Cam H7 with the generated firmware to run the model directly so as to create an easy-to-use and capable device operating with minimal latency, memory usage, and power consumption.

FOMO object detection models can count objects under the assigned classes and provide the detected object's location using centroids. Therefore, I was able to display all detected objects on the ST7735 color TFT screen with the assigned class colors.


- Egg ➡ Magenta
- Feeder ➡ Green

Since Edge Impulse optimizes and formats preprocessing, configuration, and learning blocks into BIN files for each OpenMV product while deploying models as OpenMV firmware, I was able to flash OpenMV Cam H7 effortlessly to run inferences.

:hash: After downloading the generated OpenMV firmware in the ZIP file format, plug OpenMV Cam H7 into your computer and open the OpenMV IDE.

:hash: Then, go to *Tools ➡ Run Bootloader (Load Firmware)*.

![image](.gitbook/assets/egg-counting-openmv/edge_deploy_4.png)

:hash: Choose the firmware file for OpenMV Cam H7 after extracting the generated ZIP folder.

![image](.gitbook/assets/egg-counting-openmv/edge_deploy_5.png)

:hash: Select *Erase internal file system* and click *Run* to flash OpenMV Cam H7.

![image](.gitbook/assets/egg-counting-openmv/edge_deploy_6.png)

After flashing the firmware successfully via the OpenMV IDE, I programmed OpenMV Cam H7 to run inferences so as to track (count) the daily produced eggs and detect the poultry feeder status.

Also, after running inferences successfully, I employed OpenMV Cam H7 to transmit the detection results to WizFi360-EVB-Pico via serial communication every half an hour.

You can download the *poultry_egg_tracker_run_model.py* file to try and inspect the code for running Edge Impulse neural network models on OpenMV Cam H7.

⭐ Include the required modules.

```
import sensor, image, os, tf, math, uos, gc, lcd
from time import sleep
from pyb import RTC, LED, UART
```

⭐ Initialize the camera sensor with its required settings (pixel format and frame size).

```
sensor.reset()
sensor.set_pixformat(sensor.RGB565)    # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2)    # Special 128x160 framesize for LCD Shield.
sensor.skip_frames(time=2000)          # Let the camera adjust.
```

⭐ Define the required parameters to run an inference with the Edge Impulse FOMO model.

```
net = None
labels = None
min_confidence = 0.7
```

⭐ Load the Edge Impulse FOMO model built-in in the firmware. Then, print errors, if any.

```
try:
    labels, net = tf.load_builtin_model('trained')
except Exception as e:
    raise Exception(e)
```

⭐ Define the unique color codes for each class (egg and feeder). Skip the first index (0) since it is the background class.

```
colors = [
    (255, 255, 255),
    (255, 0, 255),
    (0, 255, 0),
]
```

⭐ Initiate the integrated serial port (UART 3) on the OpenMV Cam H7.

```
uart = UART(3, 115200, timeout_char=1000)
```

⭐ Initialize the ST7735 1.8" color TFT screen.

⭐ Set the built-in RTC (real-time clock).

```
lcd.init()

# Set the built-in RTC (real-time clock).
rtc = RTC()
rtc.datetime((2022, 8, 30, 2, 12, 29, 30, 0))
```

⭐ In the *while* loop:
⭐ Get the current date and time.

⭐ Take a picture with the given frame settings (QQVGA2).

⭐ Run inference to track (count) unhatched eggs in the coop and detect whether the poultry feeder needs to be refilled.

⭐ Via the *detect* function, obtain all detected objects found in the recently captured image, split out per label (class).

⭐ Exclude the class index 0 since it is the background class.

⭐ If the Edge Impulse FOMO model detects objects successfully, clear the egg and feeder detection counters.

⭐ Then, get the prediction (detection) results for each label — *egg* and *feeder*.

⭐ According to the detected object, update the egg or the feeder detection counter.

⭐ Draw a circle in the center of the detected object with its assigned label (class) color.

```
while(True):
    # Get the current date and time.
    date = rtc.datetime()
    m, s = (int(date[5]), int(date[6]))
    date = "{}_{}_{}.{}-{}-{}".format(date[0], date[1], date[2], date[4], date[5], date[6])
    # Take a picture with the given frame settings (QQVGA2).
    img = sensor.snapshot()

    # Run inference to detect unhatched eggs and whether the poultry feeder needs to be refilled.
    # Via the detect function, obtain all detected objects found in the recently captured image, split out per label (class).
    for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
        # Exclude the class index 0 since it is the background class.
        if (i == 0): continue

        # If the Edge Impulse FOMO model predicted a label (class) successfully:
        if (len(detection_list) == 0): continue

        # Clear the egg and feeder detection counters.
        if(i==1): eggs = 0
        feeder = 0

        # Get the prediction (detection) results for each label (class).
        print("\n********** %s **********" % labels[i])
        for d in detection_list:
            # Update the egg and feeder detection counters.
            if(i==1): eggs+=1
            if(i==2): feeder+=1
            # Draw a circle in the center of the detected objects with the assigned label (class) colors.
            [x, y, w, h] = d.rect()
            center_x = math.floor(x + (w / 2))
            center_y = math.floor(y + (h / 2))
            img.draw_circle((center_x, center_y, 12), color=colors[i], thickness=2)
            print('c: (%d, %d)' % (center_x, center_y))
```

⭐ Evaluate the poultry feeder status by utilizing the feeder detection counter to detect whether the feeder needs to be refilled.

```
    if(feeder>0): feeder_status = "OK"
    if(feeder==0): feeder_status = "EMPTY"
```

⭐ Each half an hour, transfer the detection results to WizFi360-EVB-Pico via serial communication (UART) to inform the user of the detection results via WhatsApp. If successful, blink the built-in RGB LED as blue.

```
    if((m,s) == (0,0) or (m,s) == (30,0)):
        query = "&egg_count=%d&feeder_status=%s" % (eggs, feeder_status)
        uart.write(query)
        print("\n\nResults transferred to the WizFi360 module.")
        print(query)
        blue.on()
        sleep(5)
        blue.off()
```

⭐ Display the unhatched egg detection counter, the poultry feeder status, and each detected object with their assigned colors on the ST7735 1.8" TFT screen.

```
    s_eggs = "Egg Count: " + str(eggs)
    s_feeder = "Feeder: " + feeder_status
    img.draw_rectangle(0, 0, 128, 15,fill=1, color =(0,0,0))
    img.draw_string(int((128-8*len(s_eggs))/2), 3, s_eggs, color=(255,0,255), scale=1)
    img.draw_rectangle(0, 145, 128, 160, fill=1, color =(0,0,0))
    img.draw_string(int((128-8*len(s_feeder))/2), 147, s_feeder, color=(0,255,0), scale=1)
    lcd.display(img)
```

![image](.gitbook/assets/egg-counting-openmv/code_run_1.png)

![image](.gitbook/assets/egg-counting-openmv/code_run_2.png)

![image](.gitbook/assets/egg-counting-openmv/code_run_3.png)

## Step 7: Running the FOMO model on OpenMV Cam H7 to track unhatched eggs and the poultry feeder status

My Edge Impulse object detection (FOMO) model scans a captured image and predicts possibilities of trained labels to recognize an object on the given captured image. The prediction result (score) represents the model's *"confidence"* that the detected object corresponds to each of the two different labels (classes) [0 - 1], as shown in Step 5:


- Egg
- Feeder

To run the *poultry_egg_tracker_run_model.py* file on OpenMV Cam H7 when powered up automatically, save it as *main.py*.

🐤🥚 The device displays a real-time video stream on the ST7735 1.8" color TFT screen.

![image](.gitbook/assets/egg-counting-openmv/run_model_0.jpg)

🐤🥚 The device captures a picture and runs an inference with the Edge Impulse object detection (FOMO) model.

🐤🥚 Then, the device draws circles (centroids) on each recognized object with the detected label's assigned color.


- Egg ➡ Magenta
- Feeder ➡ Green

🐤🥚 For each detected *egg* label, the device increments the unhatched egg counter by 1.

🐤🥚 If there is no detected *feeder* label, the device declares the poultry feeder status as EMPTY: Which means that the poultry feeder needs to be refilled. Otherwise, it declares the poultry feeder status as OK.

🐤🥚 Then, the device displays the unhatched egg counter and the evaluated poultry feeder status on the ST7735 1.8" color TFT screen.

![image](.gitbook/assets/egg-counting-openmv/run_model_1.jpg)

![image](.gitbook/assets/egg-counting-openmv/run_model_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/run_model_2.1.jpg)

![image](.gitbook/assets/egg-counting-openmv/run_model_3.jpg)

![image](.gitbook/assets/egg-counting-openmv/run_model_4.jpg)

![image](.gitbook/assets/egg-counting-openmv/run_model_5.jpg)

🐤🥚 Each half an hour, the device transmits the detection results to WizFi360-EVB-Pico via serial communication (UART) to inform the user of the detection results via WhatsApp. Then, the device blinks the built-in RGB LED as blue.

*&egg_count=6&feeder_status=OK*

*&egg_count=8&feeder_status=EMPTY*

![image](.gitbook/assets/egg-counting-openmv/run_model_6.jpg)

![image](.gitbook/assets/egg-counting-openmv/run_model_7.jpg)

🐤🥚 Also, the device prints notifications and the detection results on the OpenMV IDE serial monitor for debugging.

![image](.gitbook/assets/egg-counting-openmv/open_serial_run_1.png)

![image](.gitbook/assets/egg-counting-openmv/open_serial_run_2.png)

As far as my experiments go, the device recognizes objects with different labels (classes) precisely, evaluates the poultry feeder status faultlessly, and shows accurate centroids around the detected objects :)

![image](.gitbook/assets/egg-counting-openmv/gif_run.gif)

## Step 8: Setting up WizFi360-EVB-Pico to collect weather data and communicate w/ OpenMV Cam H7

To inform the user of the detection results via WhatsApp, I needed to transfer the detection results to the PHP web application. Since OpenMV Cam H7 does not support Wi-Fi connectivity, I decided to utilize WizFi360-EVB-Pico to transmit the detection results. WizFi360-EVB-Pico is a budget-friendly development board based on the RP2040 microcontroller and pin-compatible with Raspberry Pi Pico. WizFi360-EVB-Pico enables Wi-Fi connectivity with the integrated WizFi360, an industrial-grade Wi-Fi module.

Also, I connected a DHT22 temperature and humidity sensor to WizFi360-EVB-Pico to collect the current weather information and send the detection results with the collected weather data to the web application.

Before proceeding with the following steps, I needed to set up WizFi360-EVB-Pico on the Arduino IDE and install the required libraries for this project.

:hash: To add [the WizFi360-EVB-Pico board package](https://github.com/earlephilhower/arduino-pico/) to the Arduino IDE, navigate to *File ➡ Preferences* and paste the URL below under *Additional Boards Manager URLs*.

*https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json*

![image](.gitbook/assets/egg-counting-openmv/set_wiz_pico_1.png)

:hash: Then, to install the required core, navigate to *Tools ➡ Board ➡ Boards Manager* and search for *rp2040*.

![image](.gitbook/assets/egg-counting-openmv/set_wiz_pico_2.png)

:hash: After installing the core, navigate to *Tools > Board > Raspberry Pi RP2040 Boards* and select *WIZnet WizFi360-EVB-Pico*.

![image](.gitbook/assets/egg-counting-openmv/set_wiz_pico_3.png)

:hash:  Finally, download the required library for the DHT22 temperature and humidity sensor:

DHT-sensor-library | [Download](https://github.com/adafruit/DHT-sensor-library) 

After setting up WizFi360-EVB-Pico and installing the required libraries, I programmed WizFi360-EVB-Pico to collect weather data and transmit the detection results with the collected weather data when OpenMV Cam H7 transfers the detection results via serial communication.

You can download the *Poultry_Feeder_and_Unhatched_Egg_Tracker.ino* file to try and inspect the code on WizFi360-EVB-Pico.

⭐ Include the required libraries.

```
#include "WizFi360.h"
#include "SoftwareSerial.h"
#include "DHT.h"
```

⭐ Define the Wi-Fi network settings and the web application path.

```
char ssid[] = "[SSID]";       // your network SSID (name)
char pass[] = "[PASSWORD]";   // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;             // your network key Index number (needed only for WEP)

// Change the server below before running the code.
IPAddress server(192, 168, 1, 22);

// Define the web application path.
String application = "/poultry_feeder_and_egg_tracker/get_data.php";
```

⭐ Define a software serial port to communicate with the integrated WizFi360 module.

⭐ Define a software serial port to communicate with OpenMV Cam H7.

```
SoftwareSerial WizFi360(5, 4); // RX, TX

SoftwareSerial OpenMV(13, 12); // RX, TX
```

⭐ Initialize the Ethernet client object.

⭐ Define the DHT22 temperature and humidity sensor settings and the DHT object.

```
WiFiClient client;

#define DHTPIN 28
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
```

⭐ Initialize the integrated WizFi360 module.

⭐ Check the connection status of the integrated WizFi360 module.

⭐ Attempt to connect to the given Wi-Fi network.

⭐ Initialize the DHT22 sensor.

```
  WiFi.init(&WizFi360);

  // Check the connection status of the integrated WizFi360 module.
  if(WiFi.status() == WL_NO_SHIELD){
    Serial.println("Error: The WizFi360 module is not found!");
    while (true);
  }
  // Attempt to connect to the WiFi network:
  while(status != WL_CONNECTED){
    Serial.print("Attempting to connect to the given network (SSID): "); Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);
  }

  // If connected to the network successfully:
  Serial.println("WizFi360 module connected to the network successfully!");

  // Initialize the DHT22 sensor.
  dht.begin();
```

⭐ In the *get_detection_results* function, obtain the detection results transferred by OpenMV Cam H7 via serial communication.

```
void get_detection_results(){
  // Obtain the detection results from the OpenMV Cam H7.
  if(OpenMV.available() > 0){
    Serial.println("\nTransferred results from the OpenMV Cam H7:");
    OpenMV_data = "";
    OpenMV_data = OpenMV.readString();
    Serial.println(OpenMV_data); 
  }
}
```

⭐ In the *collect_weather_data* function, get the evaluated temperature and humidity measurements from the DHT22 sensor.

```
void collect_weather_data(){
  delay(2000);
  humidity = dht.readHumidity();
  temperature = dht.readTemperature(); // Celsius
  // Compute the heat index in Celsius (isFahreheit = false).
  hic = dht.computeHeatIndex(temperature, humidity, false);

  Serial.print(F("\nHumidity: ")); Serial.print(humidity); Serial.println("%");
  Serial.print(F("Temperature: ")); Serial.print(temperature); Serial.println(" °C");
  Serial.print("Heat Index: "); Serial.print(hic); Serial.println(" °C");
  Serial.println("\n");
}
```

⭐ In the *make_a_get_request* function:

⭐ Connect to the web application named *poultry_feeder_and_egg_tracker*.

⭐ Create the query string with the collected weather data and the received detection results from OpenMV Cam H7.

⭐ Make an HTTP GET request with the query string to the web application.

⭐ If there is a response from the server, print it on the serial monitor.

```
void make_a_get_request(String detection){
  // Connect to the web application named poultry_feeder_and_egg_tracker. Change '80' with '443' if you are using SSL connection.
  if (client.connect(server, 80)){
    // If successful:
    Serial.println("\nWizFi360 module connected to the given server successfully!\n");
    delay(2000);
    // Create the query string:
    String query = application 
                   + "?temperature=" + String(temperature)
                   + "&humidity=" + String(humidity)
                   + detection
                 ;
    // Make an HTTP Get request:
    client.println("GET " + query + " HTTP/1.1");
    client.println("Host: 192.168.1.22");
    client.println("Connection: close");
    client.println();
  }else{
    Serial.println("\nError: WizFi360 module cannot connect to the given server! \n");
  }
  delay(150);
  // If there are incoming bytes available, get the response from the web application.
  String response = "\nData transferred successfully!\n";
  while (client.available()) { char c = client.read(); response += c; }
  Serial.println(response);
}
```

⭐ If the prediction (detection) results are received from OpenMV Cam H7 successfully, make an HTTP GET request to the given web application to inform the user of the detection results and the collected weather data via WhatsApp.

```
  if(OpenMV_data != ""){
    make_a_get_request(OpenMV_data);
    OpenMV_data = "";
  }
```

![image](.gitbook/assets/egg-counting-openmv/code_wiz_1.png)

![image](.gitbook/assets/egg-counting-openmv/code_wiz_2.png)

![image](.gitbook/assets/egg-counting-openmv/code_wiz_3.png)

![image](.gitbook/assets/egg-counting-openmv/code_wiz_4.png)

## Step 8.1: Logging the detection results and notifying the user over WhatsApp

After running the *Poultry_Feeder_and_Unhatched_Egg_Tracker.ino* file on WizFi360-EVB-Pico:

🐤🥚 The device transmits the detection results and the collected weather data to the PHP web application when WizFi360-EVB-Pico receives the detection results from OpenMV Cam H7 via serial communication every half an hour.

🐤🥚 As explained in Step 3, when the web application obtains the detection results and the collected weather data via an HTTP GET request, the application appends the current date & time and logs the received data to the given MySQL database table.

🐤🥚 Then, the application shows all registered data records as a list on the home page.

![image](.gitbook/assets/egg-counting-openmv/app_6.png)

🐤🥚 Also, the web application sends the detection results and the weather data with the current date & time over WhatsApp via Twilio's API in order to inform the user of the latest unhatched egg number and the poultry feeder status in the coop.

![image](.gitbook/assets/egg-counting-openmv/whatsapp_message_2.jpg)

![image](.gitbook/assets/egg-counting-openmv/whatsapp_message_3.jpg)

🐤🥚 Finally, the device prints notifications and sensor measurements on the Arduino IDE serial monitor for debugging.

![image](.gitbook/assets/egg-counting-openmv/wiznet_serial_1.png)

![image](.gitbook/assets/egg-counting-openmv/wiznet_serial_2.png)

## Videos and Conclusion

{% embed url="https://www.youtube.com/embed/cCYl11kxo3o" %}

{% embed url="https://www.youtube.com/embed/QNmQuXRQtWs" %}

## Further Discussions

By applying object detection models trained on captured coop images in tracking unhatched eggs and detecting the poultry feeder status automatically, we can:

🐤🥚 mitigate strenuous workload while logging the daily produced eggs and applying a regular feeding schedule,

🐤🥚 maintain a high poultry health status,

🐤🥚 maximize egg quality and quantity,

🐤🥚 determine a potential contagious poultry disease or malnutrition.

![image](.gitbook/assets/egg-counting-openmv/home_2.jpg)

## References

[^1] Soltanmoradi MG, Seidavi A, Dadashbeiki M, Laudadio V, Centoducati G, Tufarelli V., *Influence of Feeding Frequency and Timetable on Egg Parameters and Reproductive Performance in Broiler Breeder Hens*, Avian Biology Research, vol. 7, no. 3, Aug. 2014, pp. 153–159, *https://doi.org/10.3184/175815514X14025828753279*

