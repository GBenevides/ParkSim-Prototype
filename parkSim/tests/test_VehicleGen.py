from unittest import TestCase

from parkSim import *

class TestVehicleGenerator(TestCase):

    def setUp(self):
        self.sim = Simulation()

    def test_init_config(self):
        props = {
            'vehicle_rate': 60,
            'vehicles': [
                [1, {"current_road": 4, "l": 18}],
                [1, {"current_road": 0}],
                [1, {"current_road": 1}],
                [1, {"current_road": 6}],
                [1, {"current_road": 4, "l": 8}]
            ]
        }
        gen = VehicleGenerator(self.sim, props)
        self.assertTrue(gen.vehicle_rate is 60)

    def test_react(self):
        vehicleGen1 = VehicleGenerator(self.sim)
        self.assertEqual(0.01, vehicleGen1.vehicle_rate)

