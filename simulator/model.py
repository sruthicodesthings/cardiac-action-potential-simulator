import math


def smooth_step(start, end, points):
    """Makes the line less blocky between two voltages."""
    values = []
    for i in range(points):
        x = i / max(points - 1, 1)
        s = x * x * (3 - 2 * x)
        values.append(start + (end - start) * s)
    return values

def ventricular_action_potential(dt=1.0):
    """A simple shape model of a ventricular action potential.

    This is for learning the phases, not for predicting a real ECG or patient.
    """
    pieces = [
        (-90, -90, 50),
        (-90, 30, 4),
        (30, 10, 12),
        (10, 0, 160),
        (0, -90, 80),
        (-90, -90, 70),
    ]
    voltage = []
    for start, end, duration in pieces:
        count = max(2, int(duration / dt))
        voltage.extend(smooth_step(start, end, count))
    time = [i * dt for i in range(len(voltage))]
    return time, voltage

def phase_labels():
    return {
        0: "fast depolarization (Na+ in)",
        1: "early repolarization",
        2: "plateau (Ca2+ in and K+ out)",
        3: "repolarization (K+ out)",
        4: "resting membrane potential",
    }

def action_potential_duration(time, voltage, cutoff=-70):
    """Rough AP duration: from the upstroke until voltage falls below cutoff."""
    peak_i = voltage.index(max(voltage))
    for i in range(peak_i, len(voltage)):
        if voltage[i] <= cutoff:
            return time[i] - time[peak_i]
    return None
