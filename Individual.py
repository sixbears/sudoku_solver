from Parameter import Parameter
from Sudoku import Sudoku
import random
import pprint

class Individual:
    def __init__(self, father = '', mother= ''):
        if isinstance(father, Individual) :
            self.genome = Sudoku()
            if Parameter.crossOverRate < random.random() and isinstance(mother, Individual):
                rand = random.randint(4,5)
                # print(father.genome.sudoku[:rand], ' --- ',mother.genome.sudoku[rand:])
                self.genome.sudoku[:rand] = father.genome.sudoku[:rand]
                self.genome.sudoku[rand:] = mother.genome.sudoku[rand:]
            else:
                self.genome.sudoku = father.genome.sudoku[:]
            self.evalue()
            self.mutation()
        elif len(father) == 0: # création du sudoku a partir grille vide
            self.genome = Sudoku()
            seq = [1,2,3,4,5,6,7,8,9]
            for x in range(9):
                new_line = random.sample(seq[:], len(seq))
                for e in self.genome.empty_sudoku[x]:
                    if e != 0:
                        new_idx, old_idx = new_line.index(e), self.genome.empty_sudoku[x].index(e)
                        new_line[new_idx] , new_line[old_idx] = new_line[old_idx], new_line[new_idx]
                    self.genome.sudoku[x] = new_line
            self.evalue()

    def evalue(self):
        self.fitness = 81
        # error_by_column = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
        self.error_by_line_on_column_and_box = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
        for x in range(9):
            for y in range(9):
                if self.genome.empty_sudoku[x][y] != 0:
                    # print(self.genome.empty_sudoku[x][y])
                    # break
                    continue
                    
                # print(self.genome.empty_sudoku[x][y])
                # error_by_column[y] = 0
                # if self.genome.getLine(x).count(self.genome.sudoku[x][y]) > 1:
                #     self.fitness -= 1
                # if self.genome.isOnImmutableLine(x,y):
                if self.genome.isOnImmutableColumn(x,y):
                    # print('empty sudoku', self.genome.empty_sudoku)
                    self.error_by_line_on_column_and_box[x] += 5
                if self.genome.isOnImmutableBox(x,y):
                    self.error_by_line_on_column_and_box[x] += 5
                if self.genome.getColumn(y).count(self.genome.sudoku[x][y]) > 1:
                    self.fitness -= 1
                    # self.error_by_line_on_column_and_box[x] += 1
                if self.genome.getBox(x,y).count(self.genome.sudoku[x][y]) > 1:
                    self.fitness -= 1
                    # self.error_by_line_on_column_and_box[x] += 1

        # number_error_by_column = dict()
        # for pos in error:
            # number_error_by_column.update(str(pos)) += 1
        # print(self.error_by_line_on_column_and_box)
        # dic2=dict(sorted(self.error_by_line_on_column_and_box.items(),key= lambda x:x[1], reverse=False))
        # print(dic2,dic2.popitem()[0])

    def __tostr__(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(self.genome.sudoku)
        print('Fitness : {}'.format(self.fitness))
        print('error : {}'.format(self.error_by_line_on_column_and_box))


    def mutation(self):
        chanceOfMut = random.random()
        if chanceOfMut < Parameter.mutationRate:
            chanceOfChoosingGenome = random.random()
            if chanceOfChoosingGenome < Parameter.choosingGenomeRate:
                # x = random.randint(0,8)
                # for _ in range(4):
                x = dict(sorted(self.error_by_line_on_column_and_box.items(),key= lambda x:x[1], reverse=False)).popitem()[0]
                # print('x',x)
            else:
                x = random.randrange(9)
            seq = [1,2,3,4,5,6,7,8,9]
            new_line = random.sample(seq[:], len(seq))
            for e in self.genome.empty_sudoku[x]:
                if e != 0:
                    # print(self.genome.empty_sudoku)
                    new_idx, old_idx = new_line.index(e), self.genome.empty_sudoku[x].index(e)
                    new_line[new_idx] , new_line[old_idx] = new_line[old_idx], new_line[new_idx]
                    # print(new_idx, old_idx)
                self.genome.sudoku[x] = new_line
        self.evalue()
            


if __name__ == "__main__":
    t = Individual()
    # print(Sudoku().sudoku)
    (t.__tostr__())
    # t.evalue()
    # (t.__tostr__())
    t.mutation()
    # (t.__tostr__())
    # print(t.error)
    