import numpy as np
import random


class Vehicle:

    safety_space = 1

    def __init__(self, id, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.alive = False
        self.id = id

    def set_default_config(self):
        self.l = 4
        self.current_road = 0
        self.x = 0
        self.stopped = False
        self.activityDuration = 60  # minutes ?
        self.stdVel = 0.1  # m/s ?

    def react(self, lead_x, currentRoadLength, currentRoadSafetyDistance, possible_roads):
        choice = None
        if self.alive:
            front_of_vehicle = self.x + self.l
            if front_of_vehicle < currentRoadLength:  # Vehicle NOT reached end of current stretch
                if lead_x is None or front_of_vehicle + currentRoadSafetyDistance < lead_x:
                    self.x += self.stdVel
                # print("Car %s x: %.2f , front: %.2f " % (self.id, self.x, front_of_vehicle))
            elif possible_roads is not None and len(possible_roads) > 0:
                choice = random.choice(possible_roads)
        return choice
