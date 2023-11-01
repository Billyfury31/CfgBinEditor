import struct

class Label:
    def __init__(self, name, text_id, text_offset, text):
        self.name = name
        self.text_id = text_id
        self.text_offset = text_offset
        self.text = text

class Header:
    def __init__(self, entryCount, dataOffset, dataLength, unk1):
        self.entryCount = entryCount
        self.dataOffset = dataOffset
        self.dataLength = dataLength
        self.unk1 = unk1

class CfgEntry:
    def __init__(self, input_stream):
        data = input_stream.read(5)  
        if len(data) != 5:
            raise ValueError("Invalid data length")
        self.hash, self.entry_count = struct.unpack("<IB", data)
        
        self.meta_info = [] 
        types_data = input_stream.read(self.get_bytes_to_read(self.entry_count))
        types = list(types_data[::-1])  
        
        scanned_types = 0
        for type_chunk in types:
            for i in range(4):
                type_val = (type_chunk >> (i * 2)) & 0x03
                if type_val != 0x03:
                    value = None
                    if type_val in (0, 1):
                        value_data = input_stream.read(4)
                        value = struct.unpack("<i", value_data)[0]
                    elif type_val == 2:
                        value_data = input_stream.read(4)
                        value = struct.unpack("<f", value_data)[0]
                    
                    self.meta_info.append({
                        "type": type_val,
                        "value": value
                    })
                    scanned_types += 1
                    
                if scanned_types >= self.entry_count:
                    break

    def get_bytes_to_read(self, entry_count):
        if entry_count <= 12:
            return 3
        else:
            longer_entry = entry_count - 12
            bytes_to_read = (longer_entry // 16) * 4 + 3
            return bytes_to_read + 4 if longer_entry % 16 != 0 else bytes_to_read
