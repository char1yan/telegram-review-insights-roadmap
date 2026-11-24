"""Shared chart style so every figure in the project looks consistent.

Usage:
    from style import apply_style, C, save
    apply_style()
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

# Categorical colours, always assigned in this order (colour-blind-safe sequence)
C = {
    "blue": "#2a78d6",
    "orange": "#eb6834",
    "aqua": "#1baf7a",
    "yellow": "#eda100",
    "magenta": "#e87ba4",
    "green": "#008300",
    "violet": "#6250d6",
    "red": "#e34948",
    "grey": "#a3a29d",
    "ink": "#0b0b0b",
    "ink2": "#52514e",
    "surface": "#fcfcfb",
}
SERIES = [C[k] for k in ["blue", "orange", "aqua", "yellow", "magenta", "green", "violet", "red"]]
# Single-hue sequential ramp (light -> dark) for magnitude
BLUES = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#2a78d6", "#1c5cab", "#104281", "#0d366b"]


def apply_style():
    mpl.rcParams.update({
        "figure.facecolor": C["surface"],
        "axes.facecolor": C["surface"],
        "savefig.facecolor": C["surface"],
        "figure.dpi": 110,
        "savefig.dpi": 160,
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelcolor": C["ink2"],
        "axes.edgecolor": "#d6d5d0",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": "#ebeae6",
        "grid.linewidth": 0.8,
        "axes.axisbelow": True,
        "xtick.color": C["ink2"],
        "ytick.color": C["ink2"],
        "text.color": C["ink"],
        "legend.frameon": False,
        "lines.linewidth": 2,
        "axes.prop_cycle": mpl.cycler(color=SERIES),
    })


def save(fig, name, folder="../reports/figures"):
    path = Path(folder)
    path.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path / f"{name}.png", bbox_inches="tight")
    return path / f"{name}.png"
