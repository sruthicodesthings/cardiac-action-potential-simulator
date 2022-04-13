from simulator.model import ventricular_action_potential, action_potential_duration


def test_voltage_range():
    t, v = ventricular_action_potential()
    assert min(v) >= -91
    assert max(v) <= 31


def test_time_and_voltage_same_size():
    t, v = ventricular_action_potential()
    assert len(t) == len(v)


def test_duration_exists():
    t, v = ventricular_action_potential()
    assert action_potential_duration(t, v) is not None
