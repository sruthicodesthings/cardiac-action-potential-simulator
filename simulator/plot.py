import matplotlib.pyplot as plt
from .model import ventricular_action_potential


def plot_action_potential():
    """Draws the action potential so it is easier to understand."""
    time, voltage = ventricular_action_potential()
    plt.plot(time, voltage)
    plt.xlabel("Time (ms)")
    plt.ylabel("Membrane voltage (mV)")
    plt.title("Simple ventricular action potential")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_action_potential()
