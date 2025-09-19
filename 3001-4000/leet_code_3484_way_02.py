# Faster than way 01
# Faster than way 01
# Faster than way 01


class Spreadsheet:
    def __init__(self, rows: int):
        self.data = {}

    def setCell(self, cell: str, value: int):
        self.data[cell] = value

    def resetCell(self, cell: str):
        self.data.pop(cell, None)

    def getValue(self, fomula: str):
        fomula = fomula[1:].split('+')
        result = 0

        if fomula[0].isnumeric():
            result += int(fomula[0])
        else:
            if fomula[0] in self.data:
                result += self.data[fomula[0]]

        if fomula[1].isnumeric():
            result += int(fomula[1])
        elif fomula[1] in self.data:
            result += self.data[fomula[1]]

        return result





a = Spreadsheet(3)
print(a.getValue('=5+7'))
a.setCell("A1", 10)
print(a.getValue("=A1+6"))
a.setCell("B2", 15)
print(a.getValue("=A1+B2"))
a.resetCell("A1")
print(a.getValue("=A1+B2"))

