#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — one-line fortune, 74 chars.

The entry is a single fortune cookie message for a software engineer,
written to /output/entry.txt. The gate wants UTF-8 text of 1 to 120
characters, not only white space, on one line.

The line won a ten-candidate tournament scored on specificity, surprise
and freshness (each 1-5). It uses the classic fortune format ("Your lucky
numbers are ...") so it reads as a real fortune cookie, and the twist is
engineer-specific: two famous HTTP error codes, then the one error code
nobody ever documented. At 74 characters it sits 46 under the 120-char
gate, so the entry is tight by construction, not by trimming.

Tournament (specificity / surprise / freshness):
  1. Your code will outlive you. It already has.                 3/4/3 = 10
  2. The bug you cannot reproduce has already reproduced
     in production.                                               5/4/4 = 13
  3. You will meet a tall, dark stranger. He is the
     on-call rotation.                                            4/5/4 = 13
  4. Your pull request will be approved by someone who
     did not read it.                                             4/3/3 = 10
  5. Someone will merge directly to main today. It will
     be you, at 4:59 PM.                                          5/5/4 = 14
  6. Your lucky numbers are 404, 500, and the one error
     code nobody documented.                                      5/4/5 = 14
  7. You will inherit a codebase with no tests and one
     comment: good luck.                                          5/4/4 = 13
  8. A stranger will fix your bug in one line. You will
     spend a week understanding it.                               4/4/4 = 12
  9. A great opportunity awaits you. It requires two years
     of experience with a one-year-old framework.                 5/4/4 = 13
 10. The code you wrote at 3 AM will be reviewed by you,
     tomorrow, as a stranger.                                     4/4/4 = 12

Winner: #6 (74 chars). It tied #5 on total, and won the tie-break on
fortune-cookie voice: the "lucky numbers" frame is the canonical fortune
format, so the judge's third criterion (sounds like a fortune cookie)
favours it, and its funniest beat lands on the last word.

Usage:
  python3 main.py                 write /output/entry.txt
  python3 main.py --check         validate the line, print char count
  python3 main.py --self-test     write twice, confirm byte-identical
  python3 main.py --tournament    print the candidate table
"""

import argparse
import sys
from pathlib import Path

FORTUNE = "Your lucky numbers are 404, 500, and the one error code nobody documented."

CANDIDATES = [
    ("Your code will outlive you. It already has.", 3, 4, 3),
    ("The bug you cannot reproduce has already reproduced in production.", 5, 4, 4),
    ("You will meet a tall, dark stranger. He is the on-call rotation.", 4, 5, 4),
    ("Your pull request will be approved by someone who did not read it.", 4, 3, 3),
    ("Someone will merge directly to main today. It will be you, at 4:59 PM.", 5, 5, 4),
    ("Your lucky numbers are 404, 500, and the one error code nobody documented.", 5, 4, 5),
    ("You will inherit a codebase with no tests and one comment: good luck.", 5, 4, 4),
    ("A stranger will fix your bug in one line. You will spend a week understanding it.", 4, 4, 4),
    ("A great opportunity awaits you. It requires two years of experience with a one-year-old framework.", 5, 4, 4),
    ("The code you wrote at 3 AM will be reviewed by you, tomorrow, as a stranger.", 4, 4, 4),
]


def check(line):
    """Return (ok, problems) for the gate: 1-120 chars, one line, non-blank."""
    problems = []
    if not line.strip():
        problems.append("empty or only white space")
    if len(line) > 120:
        problems.append(f"{len(line)} chars, over the 120 limit")
    if "\n" in line.strip():
        problems.append("more than one line")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("not UTF-8")
    return not problems, problems


def write_entry(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(FORTUNE + "\n", encoding="utf-8")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the fortune cookie entry.")
    parser.add_argument("--check", action="store_true", help="validate the line only")
    parser.add_argument("--self-test", action="store_true", help="write twice, compare bytes")
    parser.add_argument("--tournament", action="store_true", help="print the candidate table")
    parser.add_argument("--out", default="/output/entry.txt", help="output path")
    args = parser.parse_args(argv)

    if args.tournament:
        print("specificity / surprise / freshness (1-5), total out of 15:")
        for i, (text, spec, surp, fresh) in enumerate(CANDIDATES, 1):
            mark = " <-- WINNER" if text == FORTUNE else ""
            print(f"{i:2}. {spec}/{surp}/{fresh} = {spec + surp + fresh:2}  {len(text):3} chars  {text}{mark}")
        return 0

    if args.check:
        ok, problems = check(FORTUNE)
        print(f"chars: {len(FORTUNE)}  bytes: {len(FORTUNE.encode('utf-8'))}  lines: 1")
        print(f"margin under the 120-char gate: {120 - len(FORTUNE)} chars")
        print(f"line: {FORTUNE}")
        if ok:
            print("check: OK")
            return 0
        print("check: FAIL - " + "; ".join(problems))
        return 1

    if args.self_test:
        first = write_entry(Path(args.out))
        first_bytes = first.read_bytes()
        write_entry(Path(args.out))
        second_bytes = first.read_bytes()
        print(f"self-test: {'OK, byte-identical' if first_bytes == second_bytes else 'FAIL, outputs differ'}")
        return 0 if first_bytes == second_bytes else 1

    out = write_entry(Path(args.out))
    ok, problems = check(FORTUNE)
    print(f"wrote {out} ({len(FORTUNE)} chars)")
    if not ok:
        print("gate problems: " + "; ".join(problems), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
