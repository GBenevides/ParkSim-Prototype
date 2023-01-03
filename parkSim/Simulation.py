from .Road import Road
from .VehicleGenerator import VehicleGenerator
import time as tm


class Simulation:

    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        self.vehicles = []
        self.nodes = []
        self.current_id = 0
        self.log_level = 0

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0  # Time keeping
        self.frame_count = 0  # Frame count keeping
        self.dt = 1 / 100  # Simulation time step
        self.roads = []  # Array to store roads
        self.generators = []

    def _create_road(self, start, end, name):
        road = Road(start, end, name)
        self.roads.append(road)
        return road

    def tick_next_id(self) -> int:
        self.current_id += 1
        return self.current_id - 1

    def create_roads(self, road_list, nodes):
        self.nodes = nodes
        for road in road_list:
            self._create_road(*road)

    def create_gen(self, config={}):
        gen = VehicleGenerator(self, config)
        self.generators.append(gen)
        return gen

    def run(self, steps):
        for _ in range(steps):
            self.react()

    def road_options_at_coordinates(self, x, y):
        options = []
        for road in self.roads:
            if road.start == x and road.end == y:
                options.append(self.roads.index(road))
        return options

    def insert_vehicle_in_road(self, road, upcomingVehicle):
        road.push_vehicle(upcomingVehicle)
        upcomingVehicle.set_alive(self.t)
        upcomingVehicle.x = 0
        roadIndex = self.roads.index(road)
        upcomingVehicle.current_road = roadIndex

    def get_possible_roads(self, current_road_end):
        possibilities = [self.roads.index(road) for road in self.roads if road.start == current_road_end]
        return possibilities

    def react(self):
        # Update every road
        for road in self.roads:
            road.react(self.dt)

        # Add vehicles if any
        for gen in self.generators:
            if len(self.vehicles) == 0 or True:
                gen.react()

        # Update vehicles
        for vehicle in self.vehicles:
            if vehicle.is_alive():
                current_road = self.roads[vehicle.current_road]
                lead_vehicle = current_road.vehicle_immediately_ahead(vehicle)
                possible_roads_indexes = self.get_possible_roads(current_road.end)
                lead_x = lead_vehicle.x if lead_vehicle is not None else None
                wants_to_change_to = vehicle.react(self.dt, lead_x, current_road.length, current_road.safetyDistance,
                                                   possible_roads_indexes)
                all_roads_avaiable_at_start = all(
                    self.roads[roadWithSpace].space_available_at_start(vehicle.l) for roadWithSpace in
                    possible_roads_indexes)
                if wants_to_change_to is not None and all_roads_avaiable_at_start:  # and CAN change to
                    self.roads[vehicle.current_road].pop_vehicle()
                    self.insert_vehicle_in_road(self.roads[wants_to_change_to], vehicle)

        self.t += self.dt
        self.frame_count += 1
