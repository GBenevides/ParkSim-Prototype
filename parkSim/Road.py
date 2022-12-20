from scipy.spatial import distance
from collections import deque
import numpy as np


class Road:
    def __init__(self, start, end, name="Unkown"):
        self.start = start
        self.end = end
        self.name = name
        self.__vehicles = deque()
        self.safetyDistance = 5  # 3m

        self.init_properties()

    def init_properties(self):
        self.length = distance.euclidean(self.start, self.end)
        dy = (self.end[1] - self.start[1])
        dx = (self.end[0] - self.start[0])
        self.angle_sin = dy / self.length
        self.angle_cos = dx / self.length
        self.angle = np.arctan2(dy, dx)

        self.has_traffic_signal = False

    def react(self, dt):
        # traffic signal stuff one day, parking stuff one day
        pass

    def vehicle_immediately_ahead(self, refV):
        vehicle_ahead_if_any = None
        if refV is None: return None
        for vehicle in self.__vehicles:
            if vehicle != refV:
                if vehicle.x > refV.x:  # That is, the vehicle is ahead of the reference
                    if vehicle_ahead_if_any is None or vehicle_ahead_if_any.x > vehicle.x:
                        vehicle_ahead_if_any = vehicle
        return vehicle_ahead_if_any

    def get_last_vehicle(self):
        last = None
        if len(self.__vehicles) != 0:
            last = self.__vehicles[-1]
        return last

    def __str__(self):
        return "Road %s start/end: % s - % s -> length: %.2f m" % (self.name, self.start, self.end, self.length)

    def space_available_at_start(self, upcoming_vehicle_length):
        last_vehicle = self.get_last_vehicle()
        if last_vehicle is None:
            space_available = True
        else:
            space_available = last_vehicle.x > upcoming_vehicle_length + self.safetyDistance
        return space_available

    def push_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)
    def pop_vehicle(self):
        self.__vehicles.popleft()

    def get_vehicles_len(self):
        return len(self.__vehicles)


