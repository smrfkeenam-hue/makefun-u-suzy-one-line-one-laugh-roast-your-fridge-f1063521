import os

# One-line roast of my fridge for make.fun "Roast Your Fridge".
# The ice maker is the star: it sounds like a robot giving up on life,
# and the light still comes on at 3 a.m. to watch me eat standing up
# like a raccoon. One concrete detail, twist in the last words.
ENTRY = "My fridge's ice maker sounds like a robot giving up on life, and the light still flicks on at 3 a.m. just to watch me eat standing up like a raccoon."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)
