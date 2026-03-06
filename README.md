# 🎵 trials.music — Carnatic Raga Tala Visualizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Audio-013243?style=for-the-badge&logo=numpy&logoColor=white)


*Bringing Carnatic classical music to life through code — visualize ragas, hear swaras, feel the tala.*

</div>

---

## 🌟 What is this?

This project bridges **Carnatic classical music theory** and **Python programming** — generating interactive visualizations and synthesized audio for ragas and talas.

Currently features **Mayamalavagowla** (Melakarta #15) — the foundational raga taught to every Carnatic music student — with its full swara scale, tala cycle diagrams, and playable audio tones.

> 🎧 No external audio files needed. Tones are synthesized in real time using NumPy.

---

## 📸 Demo



| ![Raga Scale]<img width="1785" height="1068" alt="raga_scale" src="https://github.com/user-attachments/assets/538a2153-0a11-41ac-8a03-bbc13c63d7b3"/>
 | ![Tala Cycle]<img width="1035" height="1040" alt="tala_cycle" src="https://github.com/user-attachments/assets/f4892cfd-0d26-48cf-9c60-bc2e8f9f43b2"/>
 | ![Frequencies]<img width="1484" height="732" alt="swara_frequencies" src="https://github.com/user-attachments/assets/596c6d6f-ffaf-4ddc-92ff-bc9bb77e2231"/>
 |

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Kavyasree-351/trials.music.git
cd trials.music

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the visualizer
python main.py

# 4. Save outputs to demo/ folder
python main.py --save
```

### Run in Jupyter Notebook
```bash
jupyter notebook notebooks/exploration.ipynb
```

---

## 📁 Project Structure

```
trials.music/
├── main.py                    ← Entry point — run this!
├── requirements.txt           ← All dependencies
├── src/
│   ├── raga_data.py           ← Raga & tala theory data
│   ├── visualizer.py          ← Matplotlib visualizations
│   └── audio_utils.py         ← Tone synthesis (numpy)
├── notebooks/
│   └── exploration.ipynb      ← Original Colab notebook (dev/reference)
└── demo/
    ├── raga_scale.png
    ├── tala_cycle.png
    └── aarohanam.wav
```

---

## 🎼 Music Theory Background

### Raga — Mayamalavagowla
| Property | Value |
|----------|-------|
| Melakarta # | 15 |
| Aarohanam | Sa Ri Ga Ma Pa Dha Ni Sa |
| Avarohanam | Sa Ni Dha Pa Ma Ga Ri Sa |
| Vadi (key note) | Sa |
| Mood | Devotional, serene, meditative |
| Best time | Early morning |

### Tala — Adi
The most common tala in Carnatic music. An 8-beat cycle divided as:
```
| 1  2  3  4 | 5  6 | 7  8 |
   Laghu(4)    Drutam  Drutam
```

---

## 🔊 Audio Details

Swaras are synthesized using **additive synthesis** — combining the fundamental frequency with its 2nd and 3rd harmonics for a more natural, musical tone (versus a plain sine wave).

```python
wave = 0.6 * sin(2π·f·t)       # fundamental
     + 0.3 * sin(2π·2f·t)      # 2nd harmonic
     + 0.1 * sin(2π·3f·t)      # 3rd harmonic
```

---

## 🛣️ Roadmap

- [ ] Add more Melakarta ragas (72 total!)
- [ ] Interactive Streamlit web app
- [ ] Tala beat metronome with audio
- [ ] Raga mood-to-time-of-day mapping visualization
- [ ] Support for Gamakam (ornamental notes)

---

## 🤝 Contributing

Found a music theory bug or want to add a new raga? Contributions welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/raga-shankarabharanam`)
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

MIT License — free to use, modify, and share.

---

<div align="center">
Made with 🎵 and Python by <a href="https://github.com/Kavyasree-351">Kavyasree</a>
<br><i>"Where code meets classical music"</i>
</div>
