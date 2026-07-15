def read_little_endian(data, offset, size):
    return int.from_bytes(data[offset : offset + size], "little")
