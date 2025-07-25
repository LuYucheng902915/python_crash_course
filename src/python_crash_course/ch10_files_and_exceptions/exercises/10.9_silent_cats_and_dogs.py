# 10-9. Silent Cats and Dogs:
# Modify your except block in Exercise 10-7 to fail silently if either file is missing.

from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
