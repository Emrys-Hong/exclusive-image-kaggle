import os
import glob

files = glob.glob("train90_size/*")
for file in files:
    if os.path.getsize(file) < 4.1 * 1024:
        os.remove(file)
