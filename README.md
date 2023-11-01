# CfgBinEditor
Python editor for level 5 files in .cfg.bin format

**What is a cfg.bin files ?**<br>
.cfg.bin files are binary files in a specific format developed by level 5 for the Nintendo 3DS, they act as a tag and most often contain text or values.<br>

**What is this tool for?**<br>
As its name suggests, this tool is used to modify the textual content of these files, this can be useful for translating a game for example.<br>

# Modify the code<br>
To modify the code and add operations to be performed on the text you will need to modify the main.py file. I advise you not to touch other files which are intended for loading .cfg.bin files<br>
In the main.py file you will need to modify the name of the file you want to open :

`ttbin_file = "ev01_0230_ja.cfg.bin"`

#Credits<br>
Thanks to the developers of kuriimu for publishing their code in C#, I adjusted it in python and its structure easily allows any modification to be applied to the text contained in the files.<br>
