import os

from utils.logger import info


def carve_files(image_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    signatures = {
        "jpg": (b"\xFF\xD8\xFF", b"\xFF\xD9"),
        "png": (b"\x89PNG", b"IEND"),
        "pdf": (b"%PDF", b"%%EOF"),
    }

    with open(image_path, "rb") as f:
        data = f.read()

    found_any = False

    for ext, (start_sig, end_sig) in signatures.items():
        start = 0
        count = 0

        while True:
            idx = data.find(start_sig, start)

            if idx == -1:
                break

            end = data.find(end_sig, idx)

            if end == -1:
                break

            end += len(end_sig)
            recovered = data[idx:end]
            filename = os.path.join(output_dir, f"recovered_{count}.{ext}")

            with open(filename, "wb") as out:
                out.write(recovered)

            info(f"Recovered {ext} at offset {idx}")

            found_any = True
            count += 1
            start = end

    if not found_any:
        info("No recoverable files found.")
