from pathlib import Path
import shutil
import sys
import argparse


SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Menyisipkan CTD terjemahan ke arsip HFA.")
    parser.add_argument("source_hfa", type=Path, help="Arsip HFA asli sebagai sumber.")
    parser.add_argument("translation_ctd", type=Path, help="File CTD terjemahan yang sudah disejajarkan.")
    parser.add_argument("output_hfa", type=Path, help="Nama file HFA hasil.")
    parser.add_argument(
        "--tools-dir",
        type=Path,
        default=SCRIPT_DIR,
        help="Folder yang berisi package mahoyo_tools.",
    )
    args = parser.parse_args()

    source_hfa = args.source_hfa.resolve()
    translation_ctd = args.translation_ctd.resolve()
    output_hfa = args.output_hfa.resolve()

    if not source_hfa.is_file():
        raise FileNotFoundError(f"HFA sumber tidak ditemukan: {source_hfa}")
    if not translation_ctd.is_file():
        raise FileNotFoundError(f"CTD revisi tidak ditemukan: {translation_ctd}")

    sys.path.insert(0, str(args.tools_dir.resolve()))
    from mahoyo_tools.hfa import HfaArchive

    shutil.copy2(source_hfa, output_hfa)
    with HfaArchive(str(output_hfa), "rw") as archive:
        archive["script_text_en.ctd"].inject(str(translation_ctd))

    print(f"HFA selesai dibuat: {output_hfa}")


if __name__ == "__main__":
    main()
