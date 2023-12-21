class Matrix:
    def __init__(self, rows, cols):
        data = []
        for i in range():
            data.append(list(map(int, input().split())))
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return f"матрица {self.rows} //n {self.cols}"

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        return self.matrix() == other.matrix()

    def __add__(self, other):
