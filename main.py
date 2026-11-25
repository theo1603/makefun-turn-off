#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun entry.

Writes one funny single line a hopeless tech support agent says to a
desperate customer, to /output/entry.txt.

The joke: the agent opens with the classic "turn it off and on again",
then cheerfully admits it is the last line of his script - and that if
it fails, neither of them has a plan. The twist is his cheerful
uselessness, not the customer's problem: the customer is not the butt of
it, they are in the same boat, and the agent says so with total
confidence. The desperation is felt, not explained: the script has run
out and there is nowhere left to escalate to.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? "
    "It's the last line of my script, and if it doesn't work, "
    "neither of us has a plan."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
