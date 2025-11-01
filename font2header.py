# font2header.py

with open("SourceSans3-Regular.ttf", "rb") as f:
    data = f.read()

with open("SourceSans3-Regular.h", "w") as h:
    h.write("unsigned char SourceSans3_Regular_ttf[] = {")
    for i, b in enumerate(data):
        if i % 12 == 0:
            h.write("\n    ")
        h.write(f"0x{b:02x}, ")
    h.write("\n};\n")
    h.write(f"unsigned int SourceSans3_Regular_ttf_len = {len(data)};\n")