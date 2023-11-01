from ttbin import TTBIN

def main():
    ttbin_file = "ev01_0230_ja.cfg.bin" # Your CFG file
    ttbin = TTBIN(ttbin_file)
    total_entries = len(ttbin.entries)  # Total number of entries in the TTBIN
    texts = ["List", "For", "Write text in differnt entry"] # I presented how to write entries in the form of a list but you can modify it very well. For example with a pyhton modue "from collections import deque"

    # Lists to store text before and after modification
    text_before_modification = []
    text_after_modification = []

    with open(ttbin_file, 'r+b') as file:
        for i, entry in enumerate(ttbin.entries[1:-1]):  # Exclude the first and last entry
            if entry.meta_info:
                for meta in entry.meta_info:
                    if meta["type"] == 0:
                        file.seek(ttbin.cfgHeader.dataOffset + int(meta["value"]))
                        text_before = file.read(0x400).decode('utf-8', errors='ignore')
                        if '\x00' in text_before:
                            text_before = text_before.split('\x00', 1)[0]
                        text_before_modification.append(text_before)
                        if i < len(texts):
                            text = texts[i].encode('utf-8')
                        else:
                            # If the `texts` list is shorter, use a default text
                            text = "Default text".encode('utf-8')

                        entry_length = len(text_before)
                        file.seek(ttbin.cfgHeader.dataOffset + int(meta["value"]))
                        file.write(b'\x00' * entry_length)
                        file.seek(ttbin.cfgHeader.dataOffset + int(meta["value"]))
                        file.write(text)  # Write the new text
                        text_after_modification.append(text.decode('utf-8'))

    print("Text before modification:")
    for i, text in enumerate(text_before_modification):
        print(f"Entry {i} : {text}")

    print("\nText after modification:")
    for i, text in enumerate(text_after_modification):
        print(f"Text in entry {i} modified: {text}")

    print("\nLoading completed successfully.")
    print(f"Number of entries in the CFG file: {total_entries - 2}")

if __name__ == "__main__":
    main()
