def find_flags(image_path):
    with open(image_path, "rb") as f:
        data = f.read().decode(errors="ignore")

    flags = []
    start = 0

    while True:
        idx = data.find("CTF{", start)
        if idx == -1:
            break

        end = data.find("}", idx)
        if end != -1:
            flag = data[idx : end + 1]
            flags.append(flag)
            print(f"Found flag: {flag}")

        start = idx + 1

    if not flags:
        print("No flags found.")
