import sys
from unittest import TestCase

from parkSim import Vehicle
import random


class TestVehicle(TestCase):

    def test_set_default_config(self):
        aVehicle = Vehicle(0)
        self.assertFalse(aVehicle.is_alive())
        self.assertEqual(0, aVehicle.id)
        self.assertEqual(0, aVehicle.current_road)
        aVehicle2 = Vehicle(1, {"current_road": 2})
        self.assertEqual(1, aVehicle2.id)
        self.assertEqual(2, aVehicle2.current_road)

    def test_react(self):
        aVehicle = Vehicle(0)
        aVehicle.x = 10
        aVehicle.current_road = 0
        self.assertIsNone(aVehicle.react(1, None, None, None, [1]))
        aVehicle.set_alive(0)
        self.assertIsNone(aVehicle.react(1, aVehicle.x + 5, 100, 10, [1]))
        self.assertEqual(10, aVehicle.x)  # car did not move
        self.assertIsNone(aVehicle.react(1, aVehicle.x + 11, 100, 10, [1]))
        self.assertEqual(10, aVehicle.x)
        self.assertIsNone(aVehicle.react(1, aVehicle.x + 20, 100, 10, [1]))
        self.assertEqual(10 + aVehicle.stdVel, aVehicle.x)  # car moved
        self.assertIsNone(aVehicle.react(1, None, 100, 10, [1]))
        self.assertEqual(10 + aVehicle.stdVel * 2, aVehicle.x)  # car moved, no one ahead
        aVehicle.x = 100
        self.assertEqual(1, aVehicle.react(1, None, 100, 10, [1]))
        self.assertEqual(aVehicle.stdVel * 2, aVehicle.distance_driven)
