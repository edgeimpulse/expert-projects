# This script controls a Dobot conveyor belt, reads real-time serial data, visualizes nut sizes using Tkinter, and displays a live video feed using OpenCV.
# Date: 2024-09-29 15:30:00
# Author: Thomas Vikström

import tkinter as tk
from tkinter import ttk
from serial import Serial
from serial.tools import list_ports
import threading
import time
import cv2  # OpenCV for video capture and display

# Dobot-related imports (assuming these are present in the working environment)
from dobot_extensions import Dobot

# Initialize Dobot
port = list_ports.comports()[0].device  # Selects the first available port
port = 'COM18'  # You may need to update this if the port changes
device = Dobot(port=port)

# Serial port setup for OpenMV Cam (modify to your specific settings)
serial_port = Serial(port='COM21', baudrate=115200, timeout=1)

# Tkinter setup
root = tk.Tk()
root.title("Nut Count Visualization")

# Create the main frame for the GUI
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dictionary to keep track of nut sizes and counts
nut_counts = {}

# Tkinter variables for display
total_count_var = tk.StringVar()
total_count_var.set("Total Count: 0")

# Create labels for the total count
ttk.Label(mainframe, textvariable=total_count_var, font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Placeholder labels for individual nut counts (to be updated dynamically)
nut_labels = {}

# Global variable to track video feed status
video_feed_ready = threading.Event()

# Function to parse the serial string with error handling
def parse_serial_string(serial_string):
    try:
        if ',' not in serial_string:
            return 0, {}
        parts = serial_string.split(", ")
        if len(parts) < 1 or not parts[0].isdigit():
            return 0, {}
        total_count = int(parts[0])
        counts = {}
        for item in parts[1:]:
            if ": " in item:
                nut, count = item.split(": ")
                counts[nut] = int(count)
        return total_count, counts
    except Exception as e:
        print(f"Error parsing serial string '{serial_string}': {e}")
        return 0, {}

# Function to update the GUI with the new counts
def update_gui(total_count, counts):
    total_count_var.set(f"Total Count: {total_count}")
    for nut_label in nut_labels:
        nut_labels[nut_label].set("0")
    for nut, count in counts.items():
        if nut not in nut_labels:
            nut_labels[nut] = tk.StringVar()
            row = len(nut_labels)
            ttk.Label(mainframe, text=f"{nut}: ", font=("Helvetica", 14)).grid(row=row, column=0, sticky=tk.E, padx=5)
            ttk.Label(mainframe, textvariable=nut_labels[nut], font=("Helvetica", 14)).grid(row=row, column=1, sticky=tk.W, padx=5)
        nut_labels[nut].set(f"{count}")

# Function to read from the serial port and update counts
def read_serial_data():
    while True:
        try:
            if serial_port.in_waiting > 0:
                line = serial_port.readline().decode("utf-8").strip()
                if line:
                    total, counts = parse_serial_string(line)
                    update_gui(total, counts)
        except Exception as e:
            print(f"Error reading serial data: {e}")
        time.sleep(0.1)

# Function to control the conveyor belt in a loop
def control_conveyor_belt():
    # Wait until the video feed is ready
    video_feed_ready.wait()
    print("Video feed is active. Starting the conveyor belt.")
    while True:
        device.conveyor_belt_distance(10, 15, 1, 0)
        time.sleep(0.5)

# Function to show live video feed using OpenCV
def show_video_feed():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return
    
    print("Starting video feed...")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Live Video Feed", frame)
            video_feed_ready.set()  # Set the event when the first frame is successfully shown

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Thread to handle the Dobot movements
dobot_thread = threading.Thread(target=control_conveyor_belt, daemon=True)
dobot_thread.start()

# Thread to handle reading and updating serial data
serial_thread = threading.Thread(target=read_serial_data, daemon=True)
serial_thread.start()

# Thread to show live video feed using OpenCV
video_thread = threading.Thread(target=show_video_feed, daemon=True)
video_thread.start()

# Run the Tkinter main event loop
root.mainloop()

# Cleanup after exiting the GUI
device.close()
serial_port.close()
