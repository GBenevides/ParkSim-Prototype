import unittest
from unittest import TestCase
from parkSim import Simulation
from parkSim import Vehicle
from parkSim import Road

import random

def generateRandomCoordinates():
    x1 = random.uniform(-150, 150)
    y1 = random.uniform(-150, 150)
    x2 = random.uniform(-150, 150)
    y2 = random.uniform(-150, 150)
    return x1, y1, x2, y2


def generateRandomRoad(name):
    x1, y1, x2, y2 = generateRandomCoordinates()
    return Road((x1, y1), (x2, y2), name)


class TestSimulation(TestCase):
    def test_set_default_config(self):
        sim1 = Simulation()
        self.assertTrue(len(sim1.vehicles) + len(sim1.roads) == 0)
        self.assertEqual(0, sim1.current_id)
        self.assertEqual(0, sim1.log_level)
        sim2 = Simulation({"log_level": 2, "current_id": 5, "bla": 321})
        self.assertEqual(5, sim2.current_id)
        self.assertEqual(2, sim2.log_level)

    def test_create_road(self):
        sim1 = Simulation()
        x1, y1, x2, y2 = generateRandomCoordinates()
        road = sim1._create_road((x1, y1), (x2, y2), "DummyRoad")
        self.assertIsNotNone(road)

    def test_get_next_id(self):
        sim1 = Simulation()
        next_id = sim1.current_id + 1
        self.assertTrue(next_id, sim1.tick_next_id())
        Vehicle(sim1.tick_next_id(), {})
        self.assertTrue(next_id + 1, sim1.current_id)

    def test_create_roads(self):
        sim1 = Simulation()
        x1, y1, x2, y2 = generateRandomCoordinates()
        r1 = ((x1, y1), (x2, y2), "DummyRoad")
        r2 = ((x1, y1), (x2, y2), "DummyRoad")
        with self.assertRaises(TypeError) as cm:
            sim1.create_roads([None, r2], None)
        self.assertEqual('parkSim.Simulation.Simulation._create_road() argument after * must be an iterable, '
                         'not NoneType', str(cm.exception))
        sim1.create_roads([r1, r2], [])

    def test_insert_vehicle_in_road(self):
        sim1 = Simulation()
        road = generateRandomRoad("Road 1")
        sim1.roads.append(road)
        v1 = Vehicle(0)
        sim1.insert_vehicle_in_road(road, v1)
        self.assertTrue(v1.is_alive())

    @unittest.skip
    def test_get_possible_roads(self):
        self.fail()

    @unittest.skip
    def test_update(self):
        self.fail() # actual integration test todo

    @unittest.skip
    def test_road_options_at_coordinates(self):
        self.fail()
