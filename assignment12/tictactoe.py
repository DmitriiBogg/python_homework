class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        index = Board.valid_moves.index(move_string)
        row, col = index // 3, index % 3
        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][col] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
        if cat:
            return (True, "Cat's Game.")

        for i in range(3):
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                return (True, f"{self.board_array[i][0]} wins!")

        for i in range(3):
            if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                return (True, f"{self.board_array[0][i]} wins!")

        if self.board_array[1][1] != " ":
            if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                return (True, f"{self.board_array[1][1]} wins!")
            if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                return (True, f"{self.board_array[1][1]} wins!")

        return (False, f"{self.turn}'s turn.")

if __name__ == "__main__":
    board = Board()
    while True:
        print(board)
        move = input(f"{board.turn}'s move: ").strip().lower()
        try:
            board.move(move)
        except TictactoeException as e:
            print(e.message)
            continue

        game_over, status = board.whats_next()
        if game_over:
            print(board)
            print(status)
            break
