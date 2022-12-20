from .Vehicle import Vehicle
from numpy.random import randint
from random import random


class VehicleGenerator:

    def __init__(self, sim, config={}):
        self.upcoming_vehicle = None
        self.last_added_time = None
        self.sim = sim

        self.set_default_config()

        for attr, val in config.items():
            setattr(self, attr, val)

        self.init_properties()

    def set_default_config(self):
        self.vehicle_rate = 0.01  # minutes/vehicle
        self.last_added_time = 0
        self.vehiclePossibilities = [
            [1, {"current_road": 4}],
            [1, {"current_road": 4, "l":8}],
            [1, {"current_road": 1, "l": 2}],
            [1, {"current_road": 3}],

        ]

    def init_properties(self):
        self.upcoming_vehicle = self.generate_vehicle()

    def generate_vehicle(self):
        total = sum(pair[0] for pair in self.vehiclePossibilities)
        r = randint(1, total + 1)
        for (weight, config) in self.vehiclePossibilities:
            r -= weight
            if r <= 0:
                return Vehicle(self.sim.tick_next_id(), config)

    def react(self):
        deltaT = self.sim.t - self.last_added_time
        if deltaT >= self.vehicle_rate + random()*5:
            # If time elasped after last added vehicle is
            # greater than vehicle_period; generate a vehicle
            road = self.sim.roads[self.upcoming_vehicle.current_road]
            if road.get_vehicles_len() == 0 or road.space_available_at_start(self.upcoming_vehicle.l):
                # If there is space for the generated vehicle; add it
                if self.sim.log_level > 0:
                    print("Adding vehicle: ", road)
                self.upcoming_vehicle.time_added = self.sim.t
                self.sim.vehicles.append(self.upcoming_vehicle)
                self.sim.insert_vehicle_in_road(road, self.upcoming_vehicle)
                # Reset last_added_time and  generate a new upcoming_vehicle
                self.last_added_time = self.sim.t
                self.upcoming_vehicle = self.generate_vehicle()
