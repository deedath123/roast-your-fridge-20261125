"""One Line, One Laugh: Roast Your Fridge.

Writes a single-line roast of the fridge's crisper drawer to /output/entry.txt.
"""

import os

ENTRY = "My fridge's crisper drawer has kept the same lettuce for 47 days, and yesterday the carrots held a funeral while the celery read the eulogy for a salad that never happened."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if "  " in ENTRY:
        raise ValueError("entry must not contain double spaces")
    if not ENTRY[0].isupper():
        raise ValueError("entry must start with a capital letter")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
