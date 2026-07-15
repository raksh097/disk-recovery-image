import os

from utils.logger import error, info


def extract_partition_simple(image_path, offset, fs_type, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    out_file = os.path.join(output_dir, f"{fs_type}_{offset}.bin")

    try:
        with open(image_path, "rb") as f:
            f.seek(offset)
            data = f.read(1024 * 1024)

        with open(out_file, "wb") as out:
            out.write(data)

        info(f"Saved: {out_file}")

    except Exception as exc:
        error(str(exc))
