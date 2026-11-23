🌈 BaziGarr QR Generator

<p align="center">
  <pre>
██████╗  █████╗ ███████╗██╗ ██████╗  █████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗╚══███╔╝██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║  ███╔╝ ██║██║  ███╗███████║██████╔╝██████╔╝
██╔══██╗██╔══██║ ███╔╝  ██║██║   ██║██╔══██║██╔══██╗██╔══██╗
██████╔╝██║  ██║███████╗██║╚██████╔╝██║  ██║██║  ██║██║  ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
  </pre>
  <b>QR CODE GENERATOR</b>
  <br>
  <i>Generate • Customize • Scan</i>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Linux-Kali%20%7C%20Debian-black?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Output-PNG-orange?style=for-the-badge">
</p><p align="center">
  <b>Stylish Gradient QR Code Generator for Termux, Android and Linux.</b>
</p>---

📌 About

BaziGarr QR Generator is a Python-based interactive QR code generation tool.

It creates beautiful QR codes with a modern Green → Cyan → Blue gradient, displays QR previews directly in the terminal, and saves generated QR images as PNG files.

It also supports custom filenames, optional image saving, and generating multiple QR codes in one session.

Simple. Stylish. Powerful. 🔥

✨ Features

Feature| Description
🎨 Gradient QR| Green → Cyan → Blue design
🖥️ Terminal Preview| Display QR directly in terminal
🌈 Gradient Text| Colorful filename rendering
🖼️ PNG Output| Save QR codes as PNG images
💾 Save Option| Choose Y/N before saving
🔗 URL Support| Automatically adds HTTPS when needed
🔄 Multiple QR| Generate multiple QR codes
📝 Custom Filename| Choose your own image name
🛡️ Error Correction| High QR error correction (Level H)
📂 Auto Directory| Automatically creates output folder
🎭 FIGlet Banner| Stylish terminal banner

---

⚡ One-Line Quick Install

📱 Termux (Android)

pkg update && pkg install git python figlet -y && termux-setup-storage && git clone https://github.com/csrb4zzigar-07/QR-CODE-GENERETOR.git && cd QR-CODE-GENERETOR && pip install -r requirements.txt && python3 "qr-code genretor"

🐉 Kali Linux

sudo apt update && sudo apt install git python3 python3-pip python3-venv figlet -y && git clone https://github.com/csrb4zzigar-07/QR-CODE-GENERETOR.git && cd QR-CODE-GENERETOR && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python3 "qr-code genretor"

---

📲 Installation Guide

📱 Termux — Android

Step 1 — Update Packages

pkg update && pkg upgrade -y

Step 2 — Install Required Packages

pkg install git python figlet -y

Step 3 — Allow Storage Permission

termux-setup-storage

Step 4 — Clone Repository

git clone https://github.com/csrb4zzigar-07/QR-CODE-GENERETOR.git

Step 5 — Open Project Directory

cd QR-CODE-GENERETOR

Step 6 — Install Python Dependencies

pip install -r requirements.txt

Step 7 — Run BaziGarr QR Generator

python3 "qr-code genretor"

---

🐉 Linux — Kali / Debian / Ubuntu

Step 1 — Update System

sudo apt update && sudo apt upgrade -y

Step 2 — Install Required Packages

sudo apt install git python3 python3-pip python3-venv figlet -y

Step 3 — Clone Repository

git clone https://github.com/csrb4zzigar-07/QR-CODE-GENERETOR.git

Step 4 — Open Project Directory

cd QR-CODE-GENERETOR

Step 5 — Create Virtual Environment

python3 -m venv .venv

Step 6 — Activate Virtual Environment

source .venv/bin/activate

Step 7 — Install Dependencies

pip install -r requirements.txt

Step 8 — Run BaziGarr QR Generator

python3 "qr-code genretor"

---

📸 Terminal Preview

<p align="center">
  <img src="terminal-preview.jpg" alt="BaziGarr QR Generator Preview" width="90%">
</p><p align="center">
  <b>Beautiful gradient QR codes directly from your terminal.</b>
</p>---

🎯 How to Use

1. Enter Your URL

Enter Link/URL: https://github.com

2. Enter Image Filename

Enter Name of the QR-Image: GitHub

3. Preview Your QR Code

The generated QR code will appear directly in your terminal.

4. Save Your QR Image

SAVE THIS IMAGE? (y/n):

- "y" — Save the QR image.
- "n" — Skip saving the QR image.

5. Generate Another QR Code

1. Next Link
2. Exit

Choose "1" to generate another QR code or "2" to exit.

---

📂 Output Location

Generated QR images are saved in:

/storage/emulated/0/Pictures/QR_CODE

Example

Pictures/
└── QR_CODE/
    ├── GitHub.png
    ├── YouTube.png
    └── Website.png

Note: The default output directory is configured for Android shared storage. On Linux, configure "SAVE_DIR" in the Python script to use a suitable directory.

---

⚙️ Customization

You can customize the QR gradient and appearance by editing these values in the Python script:

GREEN = (0, 200, 115)
CYAN = (0, 185, 180)
BLUE = (0, 155, 225)

MODULE_SIZE = 12
BORDER = 4

---

📦 Requirements

Python Libraries

The project uses:

- "qrcode[pil]"
- "Pillow"

Install all Python dependencies:

pip install -r requirements.txt

System Dependency

FIGlet is required for the terminal banner.

Termux:

pkg install figlet -y

Kali / Debian / Ubuntu:

sudo apt install figlet -y

---

🛠️ Built With

Technology| Purpose
Python 3| Main programming language
qrcode| QR code generation
Pillow| Image processing
FIGlet| Terminal ASCII banner

---

📁 Project Structure

QR-CODE-GENERETOR/
│
├── README.md
├── requirements.txt
├── terminal-preview.jpg
└── qr-code genretor

---

👨‍💻 Developer

<p align="center">
  <b>BAZIGARR</b>
  <br>
  Python Developer
  <br>
  Made with ❤️
</p>⭐ Support the Project

If you like this project:

- ⭐ Star this repository.
- 🍴 Fork the repository.
- 🐛 Report bugs through Issues.
- 💡 Suggest new features.
- 🤝 Contributions are welcome.

<p align="center">
  <b>🔥 BAZIGARR QR GENERATOR 🔥</b>
  <br>
  <i>Generate. Customize. Scan.</i>
  <br><br>
  Made with ❤️ by BaziGarr
</p>
