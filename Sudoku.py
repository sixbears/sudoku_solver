import math


class Sudoku:

    def __init__(self) -> None:
        # https://www.e-sudoku.fr/grille-de-sudoku.php n°228598 niveau moyen
        self.sudoku = [
                [0,0,2,0,8,0,1,4,0],
                [1,0,0,0,7,3,2,0,5],
                [0,0,0,1,0,0,3,0,0],
                [7,0,0,0,9,0,0,0,6],
                [0,0,6,8,0,5,4,0,0],
                [5,0,0,0,1,0,0,0,3],
                [0,0,7,0,0,2,0,0,0],
                [2,0,3,7,5,0,0,0,4],
                [0,5,9,0,4,0,7,0,0]
                ]
        self.empty_sudoku = [
                [0,0,2,0,8,0,1,4,0],
                [1,0,0,0,7,3,2,0,5],
                [0,0,0,1,0,0,3,0,0],
                [7,0,0,0,9,0,0,0,6],
                [0,0,6,8,0,5,4,0,0],
                [5,0,0,0,1,0,0,0,3],
                [0,0,7,0,0,2,0,0,0],
                [2,0,3,7,5,0,0,0,4],
                [0,5,9,0,4,0,7,0,0]
                ]
        # self.sudoku = [
        #             [0,0,2,5,8,6,1,4,9],
        #             [1,9,8,4,7,3,2,6,5],
        #             [4,6,5,1,2,9,3,7,8],
        #             [7,3,1,2,9,4,8,5,6],
        #             [9,2,6,8,3,5,4,1,7],
        #             [5,8,4,6,1,7,9,2,3],
        #             [8,4,7,9,6,2,5,3,1],
        #             [2,1,3,7,5,8,6,9,4],
        #             [6,5,9,3,4,1,7,8,2]
        #             ]
        # self.solved_sudoku = [
        #             [3,7,2,5,8,6,1,4,9],
        #             [1,9,8,4,7,3,2,6,5],
        #             [4,6,5,1,2,9,3,7,8],
        #             [7,3,1,2,9,4,8,5,6],
        #             [9,2,6,8,3,5,4,1,7],
        #             [5,8,4,6,1,7,9,2,3],
        #             [8,4,7,9,6,2,5,3,1],
        #             [2,1,3,7,5,8,6,9,4],
        #             [6,5,9,3,4,1,7,8,2]
        #             ]
        # self.immutable_numbers = []
        # self.getImmutableNumbers()

    def getBox(self,x,y):
        x,y = self.getBoxOrigin(x,y)
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.sudoku[x+i][y+j])
        return box
    
    def isOnImmutableBox(self, x,y):
        x,y = self.getBoxOrigin(x,y)
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.sudoku[x+i][y+j])
        if box.count(self.sudoku[x][y]) > 0:
            return True
        else:
            return False

    def getLine(self,x):
        return self.sudoku[x]
    
    def isOnImmutableLine(self,x,y):
        if self.empty_sudoku[x].count(self.sudoku[x][y]) > 0:
            return True
        else:
            return False

    def getColumn(self,y):
        column = []
        for line in self.sudoku:
            column.append(line[y])
        return column

    def isOnImmutableColumn(self,x, y):
        column = []
        for line in self.empty_sudoku:
            column.append(line[y])
        # print('immutable column ',column)
        if column.count(self.sudoku[x][y]) > 0:
            return True
        else:
            return False

    def getBoxOrigin(self,x,y):
        return math.floor(x/3)*3,math.floor(y/3)*3

    # def getImmutableNumbers(self):
    #     for x in range(9):
    #         for y in range(9):
    #             if self.sudoku[x][y] != 0:
    #                 self.immutable_numbers.append([x,y])

if __name__ == "__main__":
    t = Sudoku()
    print(t.immutable_numbers)
