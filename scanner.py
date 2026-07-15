import os

from tqdm import tqdm

from utils.logger import info, warn


SIGNATURES = {
    "FAT32": [b"\xEB\x58\x90", b"\xEB\x5A\x90", b"\xEB\x76\x90"],
    "NTFS": [b"\xEB\x52\x90NTFS"],
    "EXT4": [b"\x53\xEF"],
}

BLOCK_SIZE = 512


def scan_image(image_path: str) -> list:
    if not os.path.exists(image_path):
        warn(f"File not found: {image_path}")
        return []

    file_size = os.path.getsize(image_path)
    found = []

    info(f"Scanning: {image_path}")

    with open(image_path, "rb") as f:
        with tqdm(total=file_size, unit="B", unit_scale=True) as pbar:
            offset = 0

            while True:
                block = f.read(BLOCK_SIZE)
                if not block:
                    break

                for fs, sigs in SIGNATURES.items():
                    for sig in sigs:
                        if block[: len(sig)] == sig:
                            info(f"Found {fs} at {offset}")
                            found.append((offset, fs))

                offset += BLOCK_SIZE
                pbar.update(BLOCK_SIZE)

    return found
