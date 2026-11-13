from pathlib import Path
import sys

script_dir = Path(__file__).resolve().parent
for folder in (script_dir, script_dir.parent, script_dir.parent.parent, Path(r"D:\mod")):
    if (folder / "mahoyo_tools").is_dir():
        sys.path.insert(0, str(folder))
        break

from mahoyo_tools.mzp import MzpImage


def convert(source: Path) -> None:
    destination = source.parent / "png" / f"{source.stem}.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        MzpImage(str(source)).img_write(str(destination))
        print(f"Selesai: {source.name} -> {destination}")
    except Exception as error:
        print(f"Gagal: {source}\n  {error}")


def main() -> None:
    items = [Path(value.strip('"')) for value in sys.argv[1:]]
    for item in items:
        if item.is_file() and item.suffix.lower() == ".mzp":
            convert(item)
        elif item.is_dir():
            for source in sorted(item.rglob("*.mzp")):
                convert(source)
    input("Selesai. Tekan Enter untuk keluar...")


if __name__ == "__main__":
    main()
