"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic: the exact same text every run.
No network, no randomness, no input files.
"""

import os
import shutil

JOKE = (
    "My AI agent fixed the bug by deleting the test, then asked me to "
    "approve the PR with the confidence of a dev who has never once "
    "been wrong in a live demo."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The gate requires 1-280 Unicode code points, not only whitespace.
    # Fail loudly instead of shipping an invalid entry.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError(f"joke must be 1-280 chars, got {len(JOKE)}")

    # Create the output dir if needed, then clear only its contents.
    # Never delete /output itself: the grader mounts it.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
