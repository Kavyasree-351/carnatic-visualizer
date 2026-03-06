"""
visualizer.py
-------------
Visualize Carnatic raga scales and tala patterns using matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from typing import Optional


# Color palette — warm, Indian-classical inspired
SWARA_COLORS = {
    "Sa":  "#E63946",
    "Ri":  "#F4A261",
    "Ga":  "#E9C46A",
    "Ma":  "#2A9D8F",
    "Pa":  "#457B9D",
    "Dha": "#6A4C93",
    "Ni":  "#C77DFF",
    "Sa2": "#E63946",
}

TALA_COLORS = {
    "Laghu":  "#E63946",
    "Drutam": "#457B9D",
    "Tisram": "#2A9D8F",
}


def plot_raga_scale(raga_name: str, raga_data: dict, save_path: Optional[str] = None):
    """
    Plot the aarohanam (ascending) and avarohanam (descending) of a raga.

    Args:
        raga_name: Name of the raga
        raga_data: Dict with keys 'aarohanam', 'avarohanam', 'description', etc.
        save_path: If provided, saves the figure to this path
    """
    aarohanam = raga_data["aarohanam"]
    avarohanam = raga_data["avarohanam"]

    fig, axes = plt.subplots(2, 1, figsize=(12, 7))
    fig.patch.set_facecolor("#1a1a2e")

    for ax, swaras, title in zip(
        axes,
        [aarohanam, avarohanam],
        ["⬆ Aarohanam (Ascending)", "⬇ Avarohanam (Descending)"],
    ):
        ax.set_facecolor("#16213e")
        positions = list(range(len(swaras)))

        # Draw connecting line
        ax.plot(positions, positions, color="#ffffff22", linewidth=1, zorder=1)

        # Draw each swara as a colored circle
        for i, swara in enumerate(swaras):
            color = SWARA_COLORS.get(swara, "#ffffff")
            ax.scatter(i, i, s=500, color=color, zorder=3, edgecolors="white", linewidths=1.5)
            ax.text(i, i + 0.35, swara, ha="center", va="bottom",
                    fontsize=11, fontweight="bold", color="white")

        ax.set_title(title, color="white", fontsize=13, pad=10)
        ax.set_xlim(-0.5, len(swaras) - 0.5)
        ax.set_ylim(-0.5, len(swaras) + 0.5)
        ax.axis("off")

    # Main title
    fig.suptitle(
        f"🎵 Raga {raga_name}  |  Melakarta #{raga_data.get('melakarta_number', '?')}",
        color="white", fontsize=16, fontweight="bold", y=1.01,
    )

    # Description subtitle
    fig.text(
        0.5, 0.98,
        raga_data.get("description", ""),
        ha="center", color="#aaaaaa", fontsize=9, style="italic",
    )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"✅ Saved raga plot to: {save_path}")

    return fig


def plot_tala_cycle(tala_name: str, tala_data: dict, save_path: Optional[str] = None):
    """
    Plot a tala cycle as a circular beat diagram.

    Args:
        tala_name: Name of the tala (e.g., "Adi")
        tala_data: Dict with 'beats', 'pattern', 'pattern_names', 'description'
        save_path: Optional file path to save the figure
    """
    beats = tala_data["beats"]
    pattern = tala_data["pattern"]
    pattern_names = tala_data["pattern_names"]

    fig, ax = plt.subplots(figsize=(7, 7))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    angles = np.linspace(0, 2 * np.pi, beats, endpoint=False)
    radius = 1.0

    # Assign colors to each beat based on its tala section
    beat_colors = []
    for section, name in zip(pattern, pattern_names):
        color = TALA_COLORS.get(name, "#888888")
        beat_colors.extend([color] * section)

    # Draw beats as circles around a ring
    for i, (angle, color) in enumerate(zip(angles, beat_colors)):
        x = radius * np.cos(angle - np.pi / 2)
        y = radius * np.sin(angle - np.pi / 2)
        ax.scatter(x, y, s=800, color=color, zorder=3, edgecolors="white", linewidths=2)
        ax.text(x * 1.25, y * 1.25, str(i + 1), ha="center", va="center",
                fontsize=11, color="white", fontweight="bold")

    # Center label
    ax.text(0, 0, f"{beats}\nbeats", ha="center", va="center",
            fontsize=14, color="white", fontweight="bold")

    # Legend
    legend_patches = [
        mpatches.Patch(color=TALA_COLORS.get(name, "#888"), label=f"{name} ({count} beats)")
        for name, count in zip(pattern_names, pattern)
    ]
    ax.legend(handles=legend_patches, loc="lower center", bbox_to_anchor=(0.5, -0.12),
              ncol=len(pattern_names), facecolor="#16213e", labelcolor="white",
              edgecolor="white", fontsize=10)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.axis("off")
    ax.set_title(
        f"🥁 Tala: {tala_name}  |  {tala_data.get('description', '')}",
        color="white", fontsize=13, pad=15,
    )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"✅ Saved tala plot to: {save_path}")

    return fig


def plot_swara_frequencies(swara_frequencies: dict, save_path: Optional[str] = None):
    """Bar chart of swara frequencies for the raga."""
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    swaras = list(swara_frequencies.keys())
    freqs = list(swara_frequencies.values())
    colors = [SWARA_COLORS.get(s, "#888") for s in swaras]

    bars = ax.bar(swaras, freqs, color=colors, edgecolor="white", linewidth=0.8)

    for bar, freq in zip(bars, freqs):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3,
                f"{freq:.0f} Hz", ha="center", color="white", fontsize=9)

    ax.set_facecolor("#16213e")
    ax.tick_params(colors="white")
    ax.spines[:].set_color("#444")
    ax.set_title("Swara Frequencies — Mayamalavagowla",
                 color="white", fontsize=14, pad=12)
    ax.set_ylabel("Frequency (Hz)", color="white")
    ax.set_xlabel("Swara", color="white")
    ax.set_ylim(0, max(freqs) * 1.2)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"✅ Saved frequency plot to: {save_path}")

    return fig
