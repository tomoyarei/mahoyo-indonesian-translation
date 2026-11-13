from pathlib import Path
import shutil
import sys

script_dir = Path(__file__).resolve().parent

for folder in (
    script_dir,
    script_dir.parent,
    script_dir.parent.parent,
    Path(r"D:\mod"),
):
    if (folder / "mahoyo_tools").is_dir():
        sys.path.insert(0, str(folder))
        break

from mahoyo_tools.cbg import CompressedBG


def convert_file(source: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"{source.stem}.png"
    try:
        image = CompressedBG(str(source))
        image.img_write(str(destination))
        print(f"Selesai: {source.name} -> {destination}")
    except Exception as error:
        print(f"Gagal: {source}\n  {error}")


def main() -> None:
    dropped = [Path(item.strip('"')) for item in sys.argv[1:]]
    if not dropped:
        print("Tarik file CBG atau folder ke script ini.")
        input("Tekan Enter untuk keluar...")
        return

    for item in dropped:
        if item.is_file() and item.suffix.lower() == ".cbg":
            convert_file(item, item.parent / "png")
        elif item.is_dir():
            files = sorted(item.rglob("*.cbg"))
            output_dir = item / "png"
            for source in files:
                convert_file(source, output_dir)
            print(f"Total diproses dari folder: {len(files)}")
        else:
            print(f"Dilewati: {item}")

    input("Selesai. Tekan Enter untuk keluar...")


if __name__ == "__main__":
    main()
