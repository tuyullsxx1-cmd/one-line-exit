from pathlib import Path

LETTER = "I hereby resign. My notice period is two weeks, my patience ran out in March, and the office plant is the only thing I'll miss."

def send_letter():
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(LETTER, encoding="utf-8")

send_letter()
