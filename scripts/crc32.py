#!/usr/bin/env python3.6
import sys
import zlib
import textwrap


CRC32_LEN = 0x4

def extract(data):
    return "0x" + data[:CRC32_LEN].hex()


def calculate(data):
    crc32 = hex(zlib.crc32(data[CRC32_LEN:]) & 0xffffffff).lstrip("0x")
    reversed_crc32 = "".join(reversed(textwrap.wrap(crc32.zfill(8), 2)))
    return "0x" + reversed_crc32


def get_data(path):
    with open(path, "rb") as f:
        return f.read(0xffff + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <PATH>")
        sys.exit(1)

    data = get_data(sys.argv[1])

    print(f"new:      {calculate(data)}")
    print(f"original: {extract(data)}")