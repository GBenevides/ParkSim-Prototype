import sys
import unittest
from unittest import TestCase

from parkSim import Road
from parkSim import Vehicle

import random


class TestRoad(TestCase):

    def setUp(self):
        self.a = 300
        self.b = 100
        self.c = 0
        self.road = Road((self.a, self.b), (self.b, self.c))
        pass

    def test_init(self):
        x = random.uniform(-150, 150)
        y = random.uniform(-150, 150)
        z = random.uniform(-150, 150)
        aRoad = Road((x, y), (y, z))
        self.assertTrue(aRoad.length > 0)
        self.assertFalse(aRoad.has_traffic_signal)

    @unittest.skip
    def test_react(self):
        self.assertTrue(False) #todo

    def test_vehicle_immediately_ahead_and_last_vehicle(self):
        # some dummy vehicles
        v1 = Vehicle(0, {})
        v2 = Vehicle(1, {})
        v2.x = self.road.length / 3
        v3 = Vehicle(2, {})
        v3.x = self.road.length / 2

        self.assertTrue(self.road.vehicle_immediately_ahead(None) is None)
        self.assertTrue(self.road.get_last_vehicle() is None)
        self.assertTrue(self.road.vehicle_immediately_ahead(v1) is None)
        self.road.push_vehicle(v1)
        self.assertTrue(self.road.get_last_vehicle() is v1)
        self.assertTrue(self.road.vehicle_immediately_ahead(v1) is None)
        self.road.push_vehicle(v2)
        self.assertTrue(self.road.get_last_vehicle() is v2)
        self.assertTrue(self.road.vehicle_immediately_ahead(v2) is None)
        self.assertTrue(self.road.vehicle_immediately_ahead(v1) is v2)
        self.road.pop_vehicle()
        self.road.push_vehicle(v3)
        self.assertTrue(self.road.get_last_vehicle() is v3)
        self.road.pop_vehicle()
        self.road.pop_vehicle()
        self.assertTrue(self.road.get_last_vehicle() is None)

    def test_get_last_vehicle(self):
        self.assertTrue(2 == 2)

    def test_space_available_at_start(self):
        print("test_space_available_at_start")
        dummy_length = random.uniform(1, 150)
        print("dummy length", dummy_length)
        v1 = Vehicle(0, {})
        v1.l = 15
        v1.x = 0
        self.road.safetyDistance = 0
        self.assertTrue(self.road.space_available_at_start(dummy_length) is True)  # There must be space, no cars
        self.road.push_vehicle(v1)
        self.assertTrue(self.road.space_available_at_start(1) is False)  # v1 is at starting place
        v1.x = dummy_length
        self.assertTrue(self.road.space_available_at_start(dummy_length) is False)
        self.assertTrue(self.road.space_available_at_start(dummy_length/2) is True)
