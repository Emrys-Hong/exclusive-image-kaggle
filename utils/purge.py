import os

file = '/path/to/file.mov'
if os.path.getsize(file) < 100 * 1024:
  os.remove(file)
