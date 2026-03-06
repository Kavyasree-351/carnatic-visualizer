"""
main.py
-------
Entry point for the Carnatic Raga Tala Visualizer.

Run:
    python main.py

Or for a specific raga/tala:
    python main.py --raga Mayamalavagowla --tala Adi --save
"""

import argparse
import os
from src.raga_data import RAGAS, TALAS, SWARA_FREQUENCIES
from src.visualizer import plot_raga_scale, plot_tala_cycle, plot_swara_frequencies
from src.audio_utils import generate_raga_sequence, save_wav

import matplotlib.pyplot as plt


def main(raga_name: str = "Mayamalavagowla", tala_name: str = "Adi", save: bool = False):
    print(f"\n🎵 Carnatic Raga Tala Visualizer")
    print(f"   Raga : {raga_name}")
    print(f"   Tala : {tala_name}")
    print("-" * 40)

    raga = RAGAS.get(raga_name)
    tala = TALAS.get(tala_name)

    if not raga:
        print(f"❌ Raga '{raga_name}' not found. Available: {list(RAGAS.keys())}")
        return
    if not tala:
        print(f"❌ Tala '{tala_name}' not found. Available: {list(TALAS.keys())}")
        return

    os.makedirs("demo", exist_ok=True)

    # --- Visualizations ---
    raga_path  = "demo/raga_scale.png" if save else None
    tala_path  = "demo/tala_cycle.png" if save else None
    freq_path  = "demo/swara_frequencies.png" if save else None

    fig1 = plot_raga_scale(raga_name, raga, save_path=raga_path)
    fig2 = plot_tala_cycle(tala_name, tala, save_path=tala_path)
    fig3 = plot_swara_frequencies(SWARA_FREQUENCIES, save_path=freq_path)

    # --- Audio ---
    print("\n🎧 Generating audio for aarohanam...")
    audio = generate_raga_sequence(raga["aarohanam"], SWARA_FREQUENCIES)
    if save:
        save_wav(audio, "demo/aarohanam.wav")

    plt.show()
    print("\n✅ Done! Check the demo/ folder for saved outputs.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Carnatic Raga Tala Visualizer")
    parser.add_argument("--raga", default="Mayamalavagowla", help="Raga name")
    parser.add_argument("--tala", default="Adi", help="Tala name")
    parser.add_argument("--save", action="store_true", help="Save outputs to demo/")
    args = parser.parse_args()
    main(args.raga, args.tala, args.save)
