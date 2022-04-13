def resting_voltage():
    """The cell sits around here before anything exciting happens."""
    return -90.0

def phase_0(v=-90.0):
    """Phase 0: sodium comes in really fast, so voltage shoots up."""
    return 30.0

def phase_1(v=30.0):
    """Phase 1: a tiny early drop after the spike."""
    return 10.0

def phase_2(v=10.0):
    """Phase 2: the plateau. Calcium coming in helps keep voltage up."""
    return 0.0

def phase_3(v=0.0):
    """Phase 3: potassium leaving pulls the voltage back down."""
    return -90.0

def make_action_potential():
    """Makes a simple ventricular action potential from the five phases."""
    times = [0, 50, 70, 250, 300]
    volts = [resting_voltage(), phase_0(), phase_1(), phase_2(), phase_3()]
    return times, volts
