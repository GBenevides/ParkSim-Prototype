from parkSim.Simulation import *
from parkSim.Window import *

if __name__ == '__main__':
    # Create simulation
    sim = Simulation({"simu_slow_down": 10})

    a = 300
    b = 100
    c = 0
    d = 180
    e = 60
    f = 450
    g = f + 50

    A = (a, b)
    B = (c, b)
    C = (a, c)
    D = (c, c)
    E = (f, c)
    F = (f, b)
    G = (d, b)
    H = (f, b)  # (f+50, b)

    ROAD_GRAPH_NODES = [A, B, C, D, E, F, G, H]

    sim.create_roads([
        (A, B, "Road A"),
        (C, A, "Road B"),
        (A, D, "Road C"),
        (E, F, "Road D"),
        (H, A, "Road E"),
        (B, D, "Road F"),
        (D, C, "Road G"),
    ], ROAD_GRAPH_NODES)

    sim.create_gen({})

    # Start simulation
    win = Window(sim)
    win.run(10)
