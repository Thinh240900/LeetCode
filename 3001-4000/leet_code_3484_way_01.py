class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.sheet = [[0] * self.cols for _ in range(self.rows)]
        self.set_name = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
            'U': 20,
            'V': 21,
            'W': 22,
            'X': 23,
            'Y': 24,
            'Z': 25,
        }

    def setCell(self, cell: str, value: int):
        self.sheet[int(cell[1:]) - 1][self.set_name[cell[0]]] = value

    def resetCell(self, cell: str):
        self.sheet[int(cell[1:]) - 1][self.set_name[cell[0]]] = 0

    def getValue(self, fomula: str):
        arr = fomula[1:].split('+')
        value_1 = 0
        value_2 = 0
        if arr[0][0] in self.set_name:
            value_1 = self.sheet[int(arr[0][1:]) - 1][self.set_name[arr[0][0]]]
        else:
            value_1 = int(arr[0])

        if arr[1][0] in self.set_name:
            value_2 = self.sheet[int(arr[1][1:]) - 1][self.set_name[arr[1][0]]]
        else:
            value_2 = int(arr[1])
        return value_1 + value_2



a = Spreadsheet(3)
print(a.getValue('=5+7'))
a.setCell("A1", 10)
print(a.getValue("=A1+6"))
a.setCell("B2", 15)
print(a.getValue("=A1+B2"))
a.resetCell("A1")
print(a.getValue("=A1+B2"))

