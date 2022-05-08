WHITE = 1
BLACK = 2
 
 
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE
 
 
def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()
 
 
def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8
 
 
r1 = [False, 0, 0]
r2 = [False, 0, 7]
r3 = [False, 7, 0]
r4 = [False, 7, 7]
kw = [False, 0, 4]
kb = [False, 7, 4]
 
        
class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]
 
    def current_player_color(self):
        return self.color
 
    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()
 
    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None
 
    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(self, row, col, row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True
 
    def move_and_promote_pawn(self, row, col, row1, col1, char):
        p = Pawn
        if not isinstance(self.field[row][col], p):
            return False
        if self.field[row1][col1] is None:
            if not self.field[row][col].can_move(self, row, col, row1, col1):
                return False   
        else:
            if not self.field[row][col].can_attack(self, row, col, row1, col1):
                return False
        p = self.field[row][col]
        self.field[row][col] = None
        if char == 'Q':
            self.field[row1][col1] = Queen(p.color)
        elif char == 'R':
            self.field[row1][col1] = Rook(p.color)
        elif char == 'B':
            self.field[row1][col1] = Bishop(p.color)
        else:
            self.field[row1][col1] = Knight(p.color)
        self.color = opponent(self.color)
        return True
 
    def king_is_under_attack(self, row2, col2, color, field, board):
        for i in range(8):
            for j in range(8):
                if field[i][j] is not None:
                    piece = field[i][j]
                    if piece.can_move(board, i, j, row2, col2):
                        if piece.get_color() == color:
                            return True
        return False
 
    def castling0(self):
        global r1, r2, r3, r4, kw, kb
        if self.color == WHITE:
            if r1[0] is False and kw[0] is False and self.field[0][0].__class__.__name__ == 'Rook':
                if self.field[0][1] is None and self.field[0][4].__class__.__name__ == 'King':
                    if self.field[0][2] is None:
                        if self.field[0][3] is None:
                            if not self.king_is_under_attack(0, 2, BLACK, self.field, self):
                                self.field[0][2] = King(WHITE)
                                self.field[0][2].set_position(0, 2)
                                self.field[0][4] = None
                                kw[0] = True 
                                self.field[0][3] = Rook(WHITE)
                                self.field[0][3].set_position(0, 3)
                                self.field[0][0] = None
                                r1[0] = True
                                self.color = BLACK
                                return True
                            return False
                        return False
                    return False
                return False
            return False
        else:
            if r3[0] is False and kb[0] is False and self.field[7][0].__class__.__name__ == 'Rook':
                if self.field[7][1] is None and self.field[7][4].__class__.__name__ == 'King':
                    if self.field[7][2] is None:
                        if self.field[7][3] is None:
                            if not self.king_is_under_attack(7, 2, WHITE, self.field, self):
                                self.field[7][2] = King(BLACK)
                                self.field[7][2].set_position(7, 2)
                                self.field[7][4] = None
                                kb[0] = True 
                                self.field[7][3] = Rook(BLACK)
                                self.field[7][3].set_position(7, 3)
                                self.field[7][0] = None
                                r3[0] = True
                                self.color = WHITE
                                return True
                            return False
                        return False
                    return False
                return False
            return False
 
    def castling7(self):
        global r1, r2, r3, r4, kw, kb
        if self.color == WHITE:
            if r2[0] is False and kw[0] is False and self.field[0][7].__class__.__name__ == 'Rook':
                if self.field[0][5] is None and self.field[0][4].__class__.__name__ == 'King':
                    if self.field[0][6] is None:
                        if not self.king_is_under_attack(0, 6, BLACK, self.field, self):
                            self.field[0][6] = King(WHITE)
                            self.field[0][6].set_position(0, 6)
                            self.field[0][4] = None
                            kw[0] = True 
                            self.field[0][5] = Rook(WHITE)
                            self.field[0][5].set_position(0, 5)
                            self.field[0][7] = None
                            r2[0] = True
                            self.color = BLACK
                            return True
                        return False
                    return False
                return False
            return False
        else:
            if r4[0] is False and kb[0] is False and self.field[7][7].__class__.__name__ == 'Rook':
                if self.field[7][5] is None and self.field[7][4].__class__.__name__ == 'King':
                    if self.field[7][6] is None:
                        if not self.king_is_under_attack(7, 6, WHITE, self.field, self):
                            self.field[7][6] = King(BLACK)
                            self.field[7][6].set_position(7, 6)
                            self.field[7][4] = None
                            kb[0] = True 
                            self.field[7][5] = Rook(BLACK)
                            self.field[7][5].set_position(7, 5)
                            self.field[7][7] = None
                            r4[0] = True
                            self.color = WHITE
                            return True
                        return False
                    return False
                return False
            return False
 
 
class Pawn:
    def __init__(self, color):
        self.color = color
 
    def set_position(self, row, col):
        self.row, self.col = row, col
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'P'
 
    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if row + direction == row1:
            return True
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        if board.get_piece(row1, col1).get_color() == self.color:
            return False
        if board.cell(row1, col1) == '  ':
            return False
        if self.color == WHITE:
            direction = 1
        else:
            direction = -1
        return row + direction == row1 and abs(col1 - col) == 1
        
 
class Rook:
    def __init__(self, color):
        self.color = color
  
    def set_position(self, row, col):
        self.row, self.col = row, col
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'R'
 
    def can_move(self, board, row, col, row1, col1):
        global r1, r2, r3, r4
        if row != row1 and col != col1:
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        if [row, col] == [0, 0]:
            r1 = [True, row1, col1]
        elif [row, col] == [0, 7]:
            r2 = [True, row1, col1] 
        elif [row, col] == [7, 0]:
            r3 = [True, row1, col1]
        elif [row, col] == [7, 7]:
            r4 = [True, row1, col1]
        return True
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
 
 
class Knight:
    def __init__(self, color):
        self.color = color
    
    def set_position(self, row, col):
        self.row, self.col = row, col
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'N'
 
    def can_move(self, board, row, col, row1, col1):
        field = board.field
        if 0 <= row1 < 8 and 0 <= col1 < 8:
            if abs(row - row1) == 2 and abs(col - col1) == 1:
                if self.check_move(row1, col1, field, self.color):
                    return True
                return False
            elif abs(row - row1) == 1 and abs(col - col1) == 2:
                if self.check_move(row1, col1, field, self.color):
                    return True
                return False
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)
 
    def check_move(self, row1, col1, field, color):
        if field[row1][col1] is None:
            return True
        elif field[row1][col1].color != color:
            return True
        return False
 
 
class King(Board):
    def __init__(self, color):
        self.color = color
    
    def set_position(self, row, col):
        self.row, self.col = row, col
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'K'
 
    def can_move(self, board, row, col, row1, col1):
        global kw, kb
        field = board.field
        if 0 <= row1 < 8 and 0 <= col1 < 8:
            if abs(row - row1) <= 1 and abs(col - col1) <= 1:
                if self.check_move(row1, col1, field, self.color):
                    if not self.king_is_under_attack(row, col, opponent(self.color), field, board):
                        if self.color == WHITE:
                            kw = [True, row1, col1]
                        else:
                            kb = [True, row1, col1]
                        return True
                    return False
                return False
            return False
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)
    
    def check_move(self, row1, col1, field, color):
        if field[row1][col1] is None:
            return True
        elif field[row1][col1].color != color:
            return True
        return False
    
 
class Queen(Board):
    def __init__(self, color):
        self.color = color
    
    def set_position(self, row, col):
        self.row, self.col = row, col
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'Q'
 
    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        piece = board.get_piece(row1, col1)
        if piece is not None and piece.get_color() == self.color:
            return False
        if row == row1 or col == col1:
            if row1 > row:
                step = 1
            else:
                step = -1
            for i in range(row + step, row1, step):
                if board.get_piece(i, col) is not None:
                    return False
            if col1 >= col:
                step = 1
            else:
                step = -1
            for i in range(col + step, col1, step):
                if board.get_piece(row, i) is not None:
                    return False
            return True
        if row - col == row1 - col1:
            step = 1 if (row1 >= row) else -1
            for i in range(row + step, row1, step):
                if board.get_piece(i, col - row + i) is not None:
                    return False
            return True
        if row + col == row1 + col1:
            step = 1 if (row1 >= row) else -1
            for i in range(row + step, row1, step):
                if board.get_piece(i, row + col - i) is not None:
                    return False
            return True
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)
 
 
class Bishop(Board):
    def __init__(self, color):
        self.color = color
    
    def set_position(self, row, col):
        self.row, self.col = row, col
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'B'
 
    def can_move(self, board, row, col, row1, col1):
        field = board.field
        if 0 <= row1 < 8 and 0 <= col1 < 8:
            if abs(row1 - row) == abs(col1 - col):
                if self.check_move(row1, col1, field, self.color):
                    if row1 > row and col1 > col:
                        a, b = row + 1, col + 1
                        while a < row1 and b < col1:
                            if field[a][b] is not None:
                                return False
                            else:
                                a += 1
                                b += 1
                        return True
                    elif row1 > row and col1 < col:
                        a, b = row + 1, col - 1
                        while a < row1 and b > col1:
                            if field[a][b] is not None:
                                return False
                            else:
                                a += 1
                                b -= 1
                        return True  
                    elif row1 < row and col1 > col:
                        a, b = row - 1, col + 1
                        while a > row1 and b < col1:
                            if field[a][b] is not None:
                                return False
                            else:
                                a -= 1
                                b += 1
                        return True     
                    else:
                        a, b = row - 1, col - 1
                        while a > row1 and b > col1:
                            if field[a][b] is not None:
                                return False
                            else:
                                a -= 1
                                b -= 1
                        return True
                return False
            return False
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)
 
    def check_move(self, row1, col1, field, color):
        if field[row1][col1] is None:
            return True
        elif field[row1][col1].color != color:
            return True
        return False
