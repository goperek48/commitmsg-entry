#!/usr/bin/env python3
"""Emit the 3 AM commit message into /output/entry.txt.

What the bounty wants is a single commit message, no more than 200
characters long: the funniest line an AI agent could plausibly commit
in the minutes after it took production down at 3 AM. This script does
nothing clever -- it drops the chosen sentence into the output file
byte for byte, without a trailing newline, so every grading run reads
the identical text.
"""

import os
from pathlib import Path

# The entry. A single line in genuine commit form ("fix: ..."): the
# confession comes first, then the punchline lands at the end -- the
# agent is rolling back right now and already plans to ship again at
# 4 AM, only more confident this time. The humour is the blind spot:
# an agent that took away nothing from the outage except certainty.
LINE = "fix: 3am deploy took down prod; rolling back now, will re-deploy at 4am with more confidence"


def main() -> None:
    # The grader mounts its output directory at /output; if it hands
    # us a different location through the environment, use that one.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Write the sentence exactly as it stands. Leaving off the final
    # newline is deliberate: the gate measures characters, and the
    # text being judged is the line on its own.
    target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
