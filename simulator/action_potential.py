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
