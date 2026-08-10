# 🃏 Magic Mind Reader

A mind-reading card game web application built with **Python (Flask)**, **HTML5**, **CSS3**, and **JavaScript**.

![Magic Mind Reader Logo](static/joker_logo.png)

---

## 🌟 Overview

**Magic Mind Reader** is an interactive web experience based on the classic 21-card mathematical magic trick. The player chooses any card in their mind from a deck of 21 random cards divided into three groups. By indicating which group contains their chosen card over just 3 quick rounds, the algorithm calculates and reveals the exact card chosen by the user!

---

## ✨ Features

- 🃏 **Custom Joker Badge Logo:** High-resolution custom Joker aesthetic integrated into the glassmorphism UI layout.
- 🔮 **21-Card Mind Reader Algorithm:** Math-based column manipulation that automatically positions the chosen card at the center index after 3 turns.
- ✨ **Interactive Magic Burst Animations:** Clicking **Start Game** triggers a 360° spinning logo badge and a 28-particle sparkle burst transition.
- 🌊 **Floating & Trackpad Parallax Motion:** Smooth floating animations and trackpad/cursor interaction on the result display card.
- 📱 **Responsive Glassmorphism Interface:** Dark glass aesthetic tailored with modern CSS flexbox, grid, and fluid typography (`clamp()`).

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.7+ installed
- Flask (`pip install flask`)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fakruddin-Coder/Magic-Mind-Reader.git
   cd Magic-Mind-Reader
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://127.0.0.1:5000`

---

## 🛠️ Built With

- **Backend:** Python 3 & Flask Web Framework
- **Frontend:** HTML5, Modern CSS3 (Glassmorphism), Vanilla JavaScript
- **Card Images:** Deck of Cards API (`deckofcardsapi.com`)

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
