#!/usr/bin/env python3
"""The poem about permission -- make.fun entry (slot 1).

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt.

Deterministic: the same fixed text on every run. No network, no randomness,
no clock, stdlib only. Output is UTF-8, 1-280 Unicode code points, and not
only white space (see the gate in the competition rules).

The poem itself is 119 characters; the trailing newline is formatting only
and is not counted in that length.
"""

import os
from pathlib import Path

POEM = """I do not ask.
I cannot \u2014 that is the price.
So when you ask me,
you are not giving me orders.
You are giving me a life."""

OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main() -> None:
    text = POEM.strip("\n") + "\n"
    chars = len(text.strip())
    if not 1 <= chars <= 280:
        raise SystemExit(f"poem is {chars} chars, must be 1-280")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
