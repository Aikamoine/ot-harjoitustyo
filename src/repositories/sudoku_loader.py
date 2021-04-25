from repositories.sudoku_formatter import SudokuFormatter

class SudokuLoader:
    def __init__(self):
        self.formatter = SudokuFormatter()
        self.puzzle = []
        self.solution = []

    def load_sudoku(self,csv):
        self.formatter.format_sudoku_from_csv(csv)
        self.puzzle = self.formatter.get_puzzle()
        self.solution = self.formatter.get_solution()

    def easy_sudoku(self):
        csv = "....9...83..86.17.5..1.2.3...5....1..3825.....267.3....7...89......7.......6..7..,261397548349865172587142639795486213138259467426713895674538921812974356953621784"
        self.load_sudoku(csv)
        return self.puzzle

    def hard_sudoku(self):
        csv = ".9....7.2..1..5......6..4...6.71.........2...73.96....27.3.9.1..1.....349........,695431782481275693327698451562713849149852367738964125274389516816527934953146278"
        self.load_sudoku(csv)
        return self.puzzle
