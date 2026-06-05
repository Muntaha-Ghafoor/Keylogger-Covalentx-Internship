# ⌨️ Simple Keylogger

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Library](https://img.shields.io/badge/Library-pynput-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
![Internship](https://img.shields.io/badge/CovalentX-Internship%20Task%2003-blueviolet?style=flat-square)
![Ethics](https://img.shields.io/badge/Purpose-Educational%20Only-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> A basic keylogger program that records and logs keystrokes to a file. Built for educational purposes as part of the CovalentX Internship Program.

---

## ⚠️ Ethical Disclaimer

This project is built **strictly for educational purposes** as part of the CovalentX Internship Program.

- ✅ Use only on your **own computer**
- ✅ Use only with **full consent** of the device owner
- ❌ Never use on someone else's device without permission
- ❌ Never use for malicious or illegal purposes

Unauthorized use of keyloggers is **illegal** and unethical.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Author](#author)
- [License](#license)

---

## 📖 About the Project

This project is part of **Task 03** of the **CovalentX Internship Program**. A keylogger is a program that records keystrokes made by a user. This project focuses on understanding how input monitoring works at a system level using Python.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ⌨️ Keystroke Logging | Records every key pressed on the keyboard |
| 💾 File Saving | Saves all keystrokes to `keylog.txt` automatically |
| 🕐 Timestamps | Logs session start and end time |
| 🔑 Special Keys | Handles Enter, Space, Backspace, Shift, Ctrl, Alt |
| ⏹️ Safe Stop | Press ESC key to stop the keylogger safely |

---

## 📁 Project Structure

```
Keylogger-Covalentx-Internship/
│
├── LICENSE                     ← MIT License
├── README.md                   ← Project documentation
└── Task-03-Keylogger/
    ├── keylogger.py            ← Main keylogger program
    └── keylog.txt              ← Auto-created when program runs
```

---

## 🔧 Installation

Make sure Python 3 is installed, then install the required library:

```bash
pip install pynput
```

---

## ▶️ How to Run

```bash
python keylogger.py
```

The program will:
1. Start recording keystrokes immediately
2. Save everything to `keylog.txt`
3. Stop when you press **ESC**

---

## ⚙️ How It Works

```python
# Listen for key press
def on_press(key):
    write_to_file(key.char)  # Save to file

# Stop on ESC key
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener
```

Special keys are logged like this:

| Key Pressed | Logged As |
|-------------|-----------|
| Space | ` ` (space) |
| Enter | `[ENTER]` |
| Backspace | `[BACKSPACE]` |
| Shift | `[SHIFT]` |
| Ctrl | `[CTRL]` |
| ESC | Stops program |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| pynput | Keyboard input monitoring library |
| datetime | Timestamping sessions |
| File I/O | Saving keystrokes to text file |

---

## 👩‍💻 Author

**Muntaha Ghafoor**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Muntaha%20Ghafoor-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/muntaha-ghafoor-2b87a9386)
[![GitHub](https://img.shields.io/badge/GitHub-Muntaha--Ghafoor-black?style=flat-square&logo=github)](https://github.com/Muntaha-Ghafoor)

---

## 🏢 Internship Details

| Detail | Info |
|--------|------|
| Program | CovalentX Internship |
| Task | Task 03 — Implement Simple Keylogger |
| Topic | Keystroke logging and file I/O |
| Technologies | Python, pynput |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Muntaha Ghafoor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

*⭐ If you found this project helpful, consider giving it a star!*
