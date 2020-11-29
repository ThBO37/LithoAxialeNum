def stlFormat(path):
    # Fonction renvoyant le format du fichier STL (Binaire ou ASCII)
    file = open(path, "rb")
    textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

    if is_binary_string(file.read(1024)):
        return "Binary"
    else:
        return "ASCII"


def parseBinary(path):
    # Fonction transformant les données d'un fichier STL (binaire) en tableau numpy
    # A coder
    print("Parse Binary")


def parseAscii(path):
    # Fonction transformant les données d'un fichier STL (ASCII) en tableau numpy
    # A coder
    print("Parse Ascii")


def parse(path):
    # Fonction transformant les données d'un fichier STL en tableau numpy
    if stlFormat(path) == "Binary":
        parseBinary(path)
    else:
        parseAscii(path)
