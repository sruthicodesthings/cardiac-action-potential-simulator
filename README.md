# Cardiac Action Potential Simulator

This is a simple simulator for the **ventricular cardiac action potential**. I made it mostly to understand why the voltage across a heart cell changes shape during one beat. It has a Python model, a little graph, a FastAPI API, and a React page.

## The theory behind it

A heart muscle cell has a voltage across its membrane because ions are not spread equally inside and outside the cell. The membrane also has ion channels that can open and close. When different channels open, charged ions move across the membrane and the membrane potential changes.

A ventricular myocyte action potential is usually split into **phases 0 to 4**.

### Phase 4 - resting

Before the cell is excited, its membrane potential is roughly **-90 mV**. Potassium permeability is important for keeping this resting membrane potential stable. The cell is polarized: the inside is electrically negative compared with the outside.

### Phase 0 - rapid depolarization

An electrical stimulus opens fast voltage-gated **Na+ channels**. Sodium moves into the cell very quickly. Because positive charge is entering, the membrane potential rises sharply from around -90 mV to a positive value. This makes the steep upstroke of the graph.

### Phase 1 - early repolarization

The fast sodium channels inactivate. There is a short outward potassium current, so the voltage drops a little after the peak.

### Phase 2 - plateau

This is the really distinctive part of a ventricular action potential. **L-type Ca2+ channels** allow calcium to enter while potassium is also leaving through potassium channels. The inward and outward currents partly balance each other, so the voltage stays near the same level for a while instead of immediately falling.

The calcium entering the cell is also important because it helps trigger more calcium release inside the myocyte, which is part of excitation-contraction coupling and eventually causes contraction.

### Phase 3 - repolarization

Calcium current decreases while outward **K+ current** becomes more important. Positive charge leaves the cell, so the membrane potential falls back toward its resting value near -90 mV.

### Why the plateau matters

Cardiac muscle has a much longer action potential than a typical neuron. The long plateau produces a long refractory period. That helps stop ventricular muscle from being repeatedly stimulated so quickly that it goes into a sustained tetanic contraction. The heart needs to relax between contractions so the chambers can fill again.

## What this simulator actually models

This is deliberately a **shape-based educational model**, not a detailed ionic model. It joins smooth voltage changes together to make something that looks like a normal ventricular action potential. The labels explain which ion currents are mainly associated with each phase.

A more serious electrophysiology simulator would calculate individual ionic currents using channel conductances, reversal potentials, gating variables and differential equations. Models such as Hodgkin-Huxley-style formulations and later cardiac-cell models do this. This project does **not** claim that its generated voltages predict a real person's cardiac electrophysiology.

## Running the Python graph

```bash
pip install -r requirements.txt
python -m simulator.plot
```

## Running the tests

```bash
pytest
```

## Running the API

```bash
uvicorn api:app --reload
```

Then the action-potential data is available from `/action-potential`.

## Running the React page

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local Vite address it prints. The API should be running on port 8000.

## Files

```text
simulator/
  action_potential.py   first simple phase functions
  model.py              smoother action-potential model
  currents.py           ion notes for each phase
  plot.py               matplotlib graph
api.py                   FastAPI server
frontend/                React page
 tests/                  a few basic tests
```

## Important

This is an educational coding project, not medical software. It should not be used for diagnosis, treatment decisions, ECG interpretation, or patient-specific predictions.
