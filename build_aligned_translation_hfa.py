from pathlib import Path
import shutil
import sys


TOOLS_DIR = Path(r"D:\mod")
SOURCE_HFA = Path(r"C:\Users\nuran\Documents\Codex\2026-11-10\referenced-chatgpt-conversation-this-is-an\data00200.hfa")
TRANSLATION_CTD = Path(__file__).with_name("script_text_en.ctd")
OUTPUT_HFA = Path(__file__).with_name("data00200_TomoyaRei_aligned.hfa")


def main() -> None:
    if not SOURCE_HFA.is_file():
        raise FileNotFoundError(f"HFA sumber tidak ditemukan: {SOURCE_HFA}")
    if not TRANSLATION_CTD.is_file():
        raise FileNotFoundError(f"CTD revisi tidak ditemukan: {TRANSLATION_CTD}")

    sys.path.insert(0, str(TOOLS_DIR))
    from mahoyo_tools.hfa import HfaArchive

    shutil.copy2(SOURCE_HFA, OUTPUT_HFA)
    with HfaArchive(str(OUTPUT_HFA), "rw") as archive:
        archive["script_text_en.ctd"].inject(str(TRANSLATION_CTD))

    print(f"HFA selesai dibuat: {OUTPUT_HFA}")


if __name__ == "__main__":
    main()
