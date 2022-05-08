class SeaMap:
    def __init__(self):
        self.m = [['.' for g in range(10)] for i in range(10)]
    
    def shoot(self, row, col, result):
        if result == 'miss':
            self.m[row][col] = '*'
        elif result == 'sink':
            self.m[row][col] = 'x'
            t1 = row
            while t1 - 1 >= 0 and self.m[t1 - 1][col] == 'h':
                self.m[t1 - 1][col] = 'x'
                t1 -= 1
            t1 = row
            while t1 + 1 < 10 and self.m[t1 + 1][col] == 'h':
                self.m[t1 + 1][col] = 'x'
                t1 += 1
            t1 = col
            while t1 - 1 >= 0 and self.m[row][t1 - 1] == 'h':
                self.m[row][t1 - 1] = 'x'
                t1 -= 1
            t1 = col
            while t1 + 1 < 10 and self.m[row][t1 + 1] == 'h':
                self.m[row][t1 + 1] = 'x'
                t1 += 1
        elif result == 'hit':
            self.m[row][col] = 'h'
    
    def cell(self, row, col):
        if self.m[row][col] == 'x' or self.m[row][col] == '*':
            return self.m[row][col]
        elif self.m[row][col] == 'h':
            return 'x'
        for i in range(row - 1, row + 2):
            if i >= 0 and i < 10:
                for g in range(col - 1, col + 2):
                    if g >= 0 and g < 10 and self.m[i][g] == 'x':
                        return '*'
        return '.'
