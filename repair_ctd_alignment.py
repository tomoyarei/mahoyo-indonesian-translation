from __future__ import annotations

import difflib
import sys
from pathlib import Path


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def main() -> int:
    if len(sys.argv) != 4:
        print("Pemakaian: repair_ctd_alignment.py ASLI REVISI HASIL")
        return 2

    original_path, revised_path, output_path = map(Path, sys.argv[1:])
    original = read_lines(original_path)
    revised = read_lines(revised_path)
    matcher = difflib.SequenceMatcher(None, original, revised, autojunk=False)

    repaired: list[str] = []
    restored = 0
    unequal_blocks = 0

    for tag, original_start, original_end, revised_start, revised_end in matcher.get_opcodes():
        original_block = original[original_start:original_end]
        revised_block = revised[revised_start:revised_end]

        if tag == "equal" or len(original_block) == len(revised_block):
            repaired.extend(revised_block)
            continue

        unequal_blocks += 1
        if len(original_block) > len(revised_block):
            missing = len(original_block) - len(revised_block)
            repaired.extend(original_block[:missing])
            repaired.extend(revised_block)
            restored += missing
        else:
            repaired.extend(revised_block)

    output_path.write_text("\r\n".join(repaired) + "\r\n", encoding="utf-8", newline="")

    print(f"Baris asli   : {len(original)}")
    print(f"Baris revisi : {len(revised)}")
    print(f"Baris hasil  : {len(repaired)}")
    print(f"Baris dipulihkan: {restored}")
    print(f"Blok berbeda: {unequal_blocks}")
    print(f"Hasil: {output_path}")

    if len(repaired) != len(original):
        print("PERINGATAN: jumlah baris belum sama dengan file asli.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
