def main_ion_for_phase(phase):
    """Very simplified list of the main ions to remember for each phase."""
    ions = {
        0: "Na+ inward",
        1: "K+ outward",
        2: "Ca2+ inward + K+ outward",
        3: "K+ outward",
        4: "K+ conductance keeps resting voltage stable",
    }
    return ions.get(phase, "unknown phase")
