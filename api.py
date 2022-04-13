from fastapi import FastAPI
from simulator.model import ventricular_action_potential, action_potential_duration, phase_labels

app = FastAPI(title="Cardiac Action Potential Simulator")

@app.get("/action-potential")
def get_action_potential(dt: float = 1.0):
    if dt <= 0 or dt > 10:
        return {"error": "dt should be between 0 and 10 ms"}
    time, voltage = ventricular_action_potential(dt)
    return {
        "time_ms": time,
        "voltage_mv": voltage,
        "duration_ms": action_potential_duration(time, voltage),
        "phases": phase_labels(),
    }
