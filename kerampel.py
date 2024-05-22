import threading 
from enum import Enum
import time

class TrafficColor(Enum):
    R = "Red"
    Y = "Yellow"
    G = "Green"

class TrafficLight:
    def __init__(self):
        self.color = TrafficColor.G
        self.timer = None
        self.transition_times ={
                TrafficColor.R: 3,
                TrafficColor.Y: 3,
                TrafficColor.G: 3
    
                }
        print(f"Traffic light is {self.color.value}")
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
        print(f"Traffic light is {self.color.value}")
        self.start_timer()

    def stop(self):
        if self.timer:
            self.timer.cancel()


traffic_light = TrafficLight()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
        traffic_light.stop()
        print("Traffic light simulation stopped")
