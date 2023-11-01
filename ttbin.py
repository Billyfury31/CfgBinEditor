import struct
from tkinter import messagebox
from ttbinsuport import *

import struct

class TTBIN:
    def __init__(self, filename):
        self.cfgHeader = None
        self.entries = []

        with open(filename, 'rb') as file:
            self.load_header(file)
            self.load_entries(file)

    def load_header(self, file):
        header_data = file.read(struct.calcsize('I I I I'))
        if len(header_data) < 16:
            raise ValueError("Invalid header data length")
        header_data = struct.unpack('I I I I', header_data)
        self.cfgHeader = Header(*header_data)

    def load_entries(self, file):
        for _ in range(self.cfgHeader.entryCount):
            entry = CfgEntry(file)
            self.entries.append(entry)
