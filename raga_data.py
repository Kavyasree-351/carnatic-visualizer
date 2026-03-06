"""
raga_data.py
------------
Carnatic music theory data — swaras, talas, and raga definitions.
Currently focused on Mayamalavagowla (Melakarta #15).
"""

# Swara (note) frequencies in Hz — Sa fixed at C4 (261.63 Hz)
SWARA_FREQUENCIES = {
    "Sa":  261.63,   # Shadja       (S)
    "Ri":  277.18,   # Shuddha Ri   (R1) — Mayamalavagowla uses R1
    "Ga":  329.63,   # Antara Ga    (G3) — Mayamalavagowla uses G3
    "Ma":  349.23,   # Shuddha Ma   (M1)
    "Pa":  392.00,   # Panchama     (P)
    "Dha": 415.30,   # Shuddha Dha  (D1) — Mayamalavagowla uses D1
    "Ni":  493.88,   # Kakali Ni    (N3) — Mayamalavagowla uses N3
    "Sa2": 523.25,   # Upper Shadja (octave)
}

# Raga definition
RAGAS = {
    "Mayamalavagowla": {
        "melakarta_number": 15,
        "description": (
            "A fundamental Carnatic raga — the first raga taught to beginners. "
            "It has a distinctive serene and devotional character."
        ),
        "aarohanam": ["Sa", "Ri", "Ga", "Ma", "Pa", "Dha", "Ni", "Sa2"],  # ascending
        "avarohanam": ["Sa2", "Ni", "Dha", "Pa", "Ma", "Ga", "Ri", "Sa"],  # descending
        "vadi": "Sa",        # most important note
        "samvadi": "Pa",     # second most important
        "time": "Early morning",
        "mood": "Devotional, serene, meditative",
        "famous_compositions": [
            "Mahaganapathim (Muthuswami Dikshitar)",
            "Sree Gananatha (Syama Sastri)",
            "Vatapi Ganapathim (Harikesanallur Muthiah Bhagavathar)",
        ],
    }
}

# Tala (rhythm cycle) definitions
TALAS = {
    "Adi": {
        "beats": 8,
        "pattern": [4, 2, 2],       # Laghu(4) + Drutam + Drutam
        "pattern_names": ["Laghu", "Drutam", "Drutam"],
        "description": "Most common tala in Carnatic music. 8-beat cycle.",
    },
    "Rupakam": {
        "beats": 6,
        "pattern": [2, 4],
        "pattern_names": ["Drutam", "Laghu"],
        "description": "6-beat cycle. Commonly used for krithis.",
    },
    "Misra Chapu": {
        "beats": 7,
        "pattern": [3, 2, 2],
        "pattern_names": ["Tisram", "Drutam", "Drutam"],
        "description": "7-beat cycle with an asymmetric feel.",
    },
    "Khanda Chapu": {
        "beats": 5,
        "pattern": [2, 3],
        "pattern_names": ["Drutam", "Tisram"],
        "description": "5-beat cycle. Brisk and energetic.",
    },
}
