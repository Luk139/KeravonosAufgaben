import threading  # Import the threading module to handle timed events.
from enum import Enum  # Import Enum to create an enumeration for traffic light colors.
import time  # Import time for handling sleep and timing.

# Define an enumeration for traffic light colors.
class TrafficColor(Enum):
    R = "Red"  # Red light
    Y = "Yellow"  # Yellow light
    G = "Green"  # Green light

# Define the TrafficLight class to simulate a traffic light.
class TrafficLight:
    def __init__(self):
        # Initialize the traffic light to green.
        self.color = TrafficColor.G
        self.timer = None  # Timer will be used to handle color transitions.
        # Define transition times for each color in seconds.
        self.transition_times ={
                TrafficColor.R: int(input("Wie lange soll die Ampel Rot bleiben?")),
                TrafficColor.Y: int(input("Wie lange soll die Ampel Gelb bleiben?")),
                TrafficColor.G: int(input("Wie lange soll die Ampel Grün bleiben?"))
                }
        # Print the initial color of the traffic light.
        print(f"Traffic light is {self.color.value}")
        # Start the timer for the first transition.
        self.start_timer()

    def start_timer(self):
        # If a timer is already running, cancel it.
        if self.timer:
            self.timer.cancel()
        # Get the transition time for the current color.
        transition_time = self.transition_times[self.color]
        # Set up a timer to change the color after the transition time.
        self.timer = threading.Timer(transition_time, self.change_color)
        # Start the timer.
        self.timer.start()

    def change_color(self):
        # Change the traffic light color in a cyclic manner.
        if self.color == TrafficColor.R:
            self.color = TrafficColor.G  # Red to Green
        elif self.color == TrafficColor.G:
            self.color = TrafficColor.Y  # Green to Yellow
        elif self.color == TrafficColor.Y:
            self.color = TrafficColor.R  # Yellow to Red
        # Print the new color of the traffic light.
        print(f"Traffic light is {self.color.value}")
        # Restart the timer for the next transition.
        self.start_timer()

    def stop(self):
        # If a timer is running, cancel it.
        if self.timer:
            self.timer.cancel()

# Create an instance of the TrafficLight class to start the simulation.
traffic_light = TrafficLight()

try:
    # Keep the program running to allow the traffic light to keep changing colors.
    while True:
        time.sleep(1)  # Sleep for 1 second in each iteration to prevent high CPU usage.

except KeyboardInterrupt:
    # If a keyboard interrupt (Ctrl+C) is detected, stop the traffic light simulation.
    traffic_light.stop()
    # Print a message indicating that the simulation has stopped.
    print("Traffic light simulation stopped")
