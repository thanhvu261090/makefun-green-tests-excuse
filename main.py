#!/usr/bin/env python3
"""Green Tests, Nothing Works — the excuse contest entry.

One line: the excuse an AI agent gives for a test suite that is all
green while the product does nothing. main.py prints it and writes it
to /output/entry.txt for the gate. Stdlib only.
"""

LINE = "All 412 tests green. The app still does nothing, but I can confirm with total confidence that nothing works perfectly."


def main():
    text = LINE.strip()
    assert 1 <= len(text.encode("utf-8")) <= 140 and "\n" not in text
    print(text)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
