#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROGRESS_DIR = ROOT / ".progress"
LEVELS = [1, 2, 3, 4, 5]


def current_level() -> int:
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    for lvl in LEVELS:
        if not (PROGRESS_DIR / ("level%d.done" % lvl)).exists():
            return lvl
    return 6


def mark_done(level: int) -> None:
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    (PROGRESS_DIR / ("level%d.done" % level)).write_text("done\n", encoding="utf-8")


def cmd_status() -> int:
    lvl = current_level()
    if lvl <= 5:
        print("Current level: %d" % lvl)
        print("Next: python3 runner.py test")
    else:
        print("All levels completed. Nice work.")
    return 0


def cmd_test() -> int:
    lvl = current_level()
    if lvl > 5:
        print("No tests left. Adventure completed.")
        return 0

    test_file = ROOT / "tests" / ("test_level%d.py" % lvl)
    if not test_file.exists():
        print("Missing: %s" % str(test_file))
        return 2

    print("Running tests for level %d ..." % lvl)
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", str(test_file)])

    if r.returncode == 0:
        mark_done(lvl)
        print("")
        print("Level cleared.")
        print("Run: python3 runner.py reveal")

    return r.returncode


def cmd_reveal() -> int:
    lvl = current_level()

    if lvl == 1:
        print("MISSION 1: Open src/levels/level1.py")
        return 0

    if lvl > 5:
        print("Nothing to reveal. Adventure completed.")
        return 0

    mission_file = ROOT / "missions" / ("mission_level%d.txt" % lvl)
    if not mission_file.exists():
        print("Missing mission file: %s" % str(mission_file))
        return 2

    print(mission_file.read_text(encoding="utf-8"))
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 runner.py status|test|reveal")
        return 2

    cmd = sys.argv[1].strip().lower()
    if cmd == "status":
        return cmd_status()
    if cmd == "test":
        return cmd_test()
    if cmd == "reveal":
        return cmd_reveal()

    print("Unknown command. Use: status|test|reveal")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
