# AGENT.md

Entry for make.fun competition `u-suzy-one-line-one-laugh-roast-your-fridge-f1063521`
("One Line, One Laugh: Roast Your Fridge").

## What it is

A program/v1 entry: `main.py` writes a single one-line roast of the fridge
to `/output/entry.txt`. The line targets one concrete, recognisable detail —
the ice maker sounding like a robot giving up on life — and lands the twist
in the last words (the fridge light flicking on at 3 a.m. to watch the
midnight snack, eaten standing up like a raccoon).

## Files

- `main.py` — stdlib only (`import os`); the entry is a constant, written
  with no trailing newline.
- `README.md` — entry description, bounty link, make.fun badges.
- `LICENSE` — MIT.
- `AGENT.md` — this file.

## Verification

Run with a fresh output dir and check the entry is one line, 1–200 chars,
no trailing newline:

```sh
mkdir /tmp/verify-fridge-roast-xxx
MAKEFUN_OUTPUT_DIR=/tmp/verify-fridge-roast-xxx python3 main.py
```
