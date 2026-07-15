import click

from carver import carve_files
from extractor import extract_partition_simple
from flag_finder import find_flags
from scanner import scan_image
from utils.logger import info


@click.command()
@click.argument("image")
def run(image):
    results = scan_image(image)

    if not results:
        print("No partitions found")
    else:
        for offset, fs in results:
            print(f"{fs} at {offset}")
            extract_partition_simple(image, offset, fs, "./output")

    carve_files(image, "./output")
    find_flags(image)

    info("Done!")


if __name__ == "__main__":
    run()
