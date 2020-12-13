import os


class StlFile:
    def __init__(self, path):
        self.path = path

    def format(self):
        textchars = bytearray(
            {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F}
        )
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        if is_binary_string(open(self.path, "rb").read(1024)):
            return "Binary"
        else:
            return "Ascii"

    def content(self):
        if self.format() == "Binary":
            return open(self.path, "rb").read()
        else:
            return open(self.path, "r").read()

    def mesh(self):
        if self.format() == "Ascii":
            ## Partie à coder
            pass
        else:
            ## Partie à coder
            pass
