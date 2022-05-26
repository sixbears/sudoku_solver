from Parameter import Parameter
from Individual import Individual
from random import randrange

class Population:
    def __init__(self):
        self.population = []
        self.bestInd = 0
        self.bestFitness = -1
        for i in range(Parameter.nbreIndividus):
            self.population.append(Individual())

    def __str__(self):
        for s in self.population:
            s.__tostr__()

    def evalue_tri(self):
        for s in self.population:
            s.evalue()
        self.population.sort(key=lambda x:x.fitness, reverse=True)
        # for s in self.population:
        #     print(s.sequence, "  --  ", s.fitness)
        # return self.population

    def selection(self):
        totalRanks = len(self.population) * (len(self.population)+1) / 2
        i = randrange(totalRanks)
        indIndex=0
        nbParts=len(self.population)
        totalParts=0
        while(totalParts<i):
            indIndex += 1
            totalParts += nbParts
            nbParts -= 1
        return self.population[indIndex]

    def run(self):
        indGeneration = 1
        while indGeneration<Parameter.generationMaxNb and self.bestFitness < Parameter.maxFitness:
            # self.__str__()
            # self.__str__()
            self.evalue_tri()
            # self.__str__()
            # self.population[0].__tostr__()
            self.bestInd = self.population.pop(0)
            self.bestFitness = self.bestInd.fitness
            # if indGeneration > 1:
            #     print('==', self.population[1].fitness)

            nouvelleGeneration = []
            nouvelleGeneration.append(self.bestInd)
            nouvelleGeneration.append(Individual(self.bestInd))
            # self.bestInd.__tostr__()
            print('== Generation '+ str(indGeneration) + f' == {self.bestFitness}')
            self.bestInd.__tostr__()
            for _ in range(len(self.population)-1):
                father = self.selection()
                mother = self.selection()
                # print('Father:')
                # father.__tostr__()
                # print('Mother:')
                # mother.__tostr__()
                child = Individual(father, mother)
                # child.__tostr__()
                nouvelleGeneration.append(child)
            self.population = nouvelleGeneration

            indGeneration += 1
        # self.__str__()
        print('==== Fin de l\'algorithme ====')
        if (self.bestFitness >= Parameter.maxFitness):
            print('Max Fitness reach')
        if (indGeneration >= Parameter.generationMaxNb):
            print('Max generation reach')
        self.bestInd.__tostr__()

if __name__ == "__main__":
    p = Population()
    p.run()
    # print(p.__str__())
    # print(p.evalue_tri())
    # print(p.__str__())
    # pere = p.selection()
    # mere = p.selection()
    # print(mere, pere)
    # enfant = Sequence(pere, mere)
     