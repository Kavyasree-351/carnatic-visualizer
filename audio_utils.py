"""
audio_utils.py
--------------
Generate audio tones for Carnatic swaras using numpy + scipy.
No external audio files needed — synthesizes tones on the fly.
"""

import numpy as np

try:
    from scipy.io import wavfile
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

try:
    import IPython.display as ipd
    IPYTHON_AVAILABLE = True
except ImportError:
    IPYTHON_AVAILABLE = False


SAMPLE_RATE = 44100  # Hz


def generate_tone(frequency: float, duration: float = 0.5, volume: float = 0.5) -> np.ndarray:
    """
    Generate a sine wave tone for a given frequency.

    Args:
        frequency: Frequency in Hz
        duration:  Duration in seconds
        volume:    Amplitude (0.0 to 1.0)

    Returns:
        numpy array of audio samples
    """
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    # Add harmonics for a more musical, less robotic sound
    wave = (
        volume * 0.6 * np.sin(2 * np.pi * frequency * t) +        # fundamental
        volume * 0.3 * np.sin(2 * np.pi * frequency * 2 * t) +    # 2nd harmonic
        volume * 0.1 * np.sin(2 * np.pi * frequency * 3 * t)       # 3rd harmonic
    )
    # Apply fade-in/fade-out to avoid clicks
    fade_samples = int(SAMPLE_RATE * 0.01)
    wave[:fade_samples] *= np.linspace(0, 1, fade_samples)
    wave[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    return wave.astype(np.float32)


def generate_raga_sequence(
    swara_names: list,
    swara_frequencies: dict,
    duration_per_note: float = 0.6,
    pause: float = 0.05,
) -> np.ndarray:
    """
    Generate an audio sequence for a list of swara names.

    Args:
        swara_names:       List of swara names e.g. ["Sa", "Ri", "Ga"]
        swara_frequencies: Dict mapping swara name -> Hz
        duration_per_note: Seconds per note
        pause:             Silence between notes in seconds

    Returns:
        numpy array of the full audio sequence
    """
    silence = np.zeros(int(SAMPLE_RATE * pause), dtype=np.float32)
    segments = []
    for name in swara_names:
        freq = swara_frequencies.get(name)
        if freq:
            tone = generate_tone(freq, duration=duration_per_note)
            segments.append(tone)
            segments.append(silence)
    return np.concatenate(segments) if segments else np.array([], dtype=np.float32)


def save_wav(audio: np.ndarray, filepath: str) -> None:
    """Save audio array as a .wav file."""
    if not SCIPY_AVAILABLE:
        raise ImportError("scipy is required to save WAV files. Run: pip install scipy")
    audio_int16 = (audio * 32767).astype(np.int16)
    wavfile.write(filepath, SAMPLE_RATE, audio_int16)
    print(f"✅ Saved audio to: {filepath}")


def play_in_notebook(audio: np.ndarray) -> None:
    """Play audio inline in a Jupyter notebook."""
    if not IPYTHON_AVAILABLE:
        raise EnvironmentError("IPython is required for notebook playback.")
    return ipd.Audio(audio, rate=SAMPLE_RATE, autoplay=False)
