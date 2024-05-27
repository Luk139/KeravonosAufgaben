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
    def __init__(self, name, initial_color=TrafficColor.R):
        self.name = name
        self.color = initial_color
        self.timer = None  # Timer will be used to handle color transitions.
        self.transition_times = {
            TrafficColor.R: 3,
            TrafficColor.Y: 1,
            TrafficColor.G: 3
        }
        print(f"{self.name} traffic light is {self.color.value}")
        self.start_timer()

    def start_timer(self):
        if self.timer:
            self.timer.cancel()
        transition_time = self.transition_times[self.color]
        self.timer = threading.Timer(transition_time, self.change_color)
        self.timer.start()

    def change_color(self):
        if self.color == TrafficColor.R:
            self.color = TrafficColor.G
        elif self.color == TrafficColor.G:
            self.color = TrafficColor.Y
        elif self.color == TrafficColor.Y:
            self.color = TrafficColor.R
        print(f"{self.name} traffic light is {self.color.value}")
        self.start_timer()

    def stop(self):
        if self.timer:
            self.timer.cancel()

# Define the TrafficControl class to coordinate multiple traffic lights at a crossing.
class TrafficControl:
    def __init__(self):
        # Create traffic lights for all lanes
        self.right_right = TrafficLight("RightRight", TrafficColor.G)
        self.left_right = TrafficLight("LeftRight", TrafficColor.G)
        self.bottom_right = TrafficLight("BottomRight", TrafficColor.R)
        self.top_right = TrafficLight("TopRight", TrafficColor.R)
        self.cycle_time = 3  # Time for each green light cycle in seconds

    def start(self):
        try:
            while True:
                time.sleep(self.cycle_time)
                self.change_lights()

        except KeyboardInterrupt:
            self.stop_all()
            print("Traffic light simulation stopped")

    def change_lights(self):
        if self.right_right.color == TrafficColor.G and self.left_right.color == TrafficColor.G:
            self.right_right.color = TrafficColor.R
            self.left_right.color = TrafficColor.R
            self.bottom_right.color = TrafficColor.G
            self.top_right.color = TrafficColor.G
        elif self.bottom_right.color == TrafficColor.G and self.top_right.color == TrafficColor.G:
            self.bottom_right.color = TrafficColor.R
            self.top_right.color = TrafficColor.R
            self.right_right.color = TrafficColor.G
            self.left_right.color = TrafficColor.G

        # Print the new state of all traffic lights
        print(f"RightRight traffic light is {self.right_right.color.value}")
        print(f"LeftRight traffic light is {self.left_right.color.value}")
        print(f"BottomRight traffic light is {self.bottom_right.color.value}")
        print(f"TopRight traffic light is {self.top_right.color.value}")

    def stop_all(self):
        self.right_right.stop()
        self.left_right.stop()
        self.bottom_right.stop()
        self.top_right.stop()

# Create an instance of TrafficControl to start the simulation.
traffic_control = TrafficControl()
traffic_control.start()
