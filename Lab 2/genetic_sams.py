import random
from tkinter.font import names
Batsman = 5
Target = 240
genome = '10101010'
Size = 100
input_list = [('Bradman', 120), ('Tendulkar', 90), ('Sangakkara ', 70), ('Kallis', 65), ('Lara', 80)]

class Genome(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        fitness = 0
        for index, names in enumerate(input_list):
            if genome[index] == '1':
                fitness = fitness + names[1]

        if fitness > Target:
            return 0
        return fitness

    @classmethod
    def mutated_genome(self):
        sequence = random.choices(['0', '1'])
        return sequence

    @classmethod
    def create_genome(self):
        global Batsman
        return [self.mutated_genome() for _ in range(Batsman)]

    def crossover(self, sp2):
        cross_point = random.randint(0, Target)
        new_child1 = self.chromosome[:cross_point] + sp2.chromosome[cross_point:]

        new_child2 = self.chromosome[cross_point:] + sp2.chromosome[:cross_point]


    def mutation(self, sp2):
        new_child = []
        for gene1, gene2 in zip(self.chromosome, sp2.chromosome):
            probability = random.random()
    
            if probability < 0.49:
                new_child.append(gene1)
    
            elif probability < 0.82:
                new_child.append(gene2)

            else:
                new_child.append(self.mutated_genome)
    
        return Genome(new_child)



def main():
    number_sequence = []
    global Size
    is_number = False
    run_time = 1

    for _ in range(Size):
        sequences = Genome.create_genome()
        number_sequence.append(Genome(sequences))

    while not is_number:
        number_sequence = sorted(number_sequence, key=lambda fit:fit.fitness)

        if number_sequence[0].fitness == 240:
            print(number_sequence[0])
            is_number = True
            break

        new_number_sequence = []

        n = int((10 * Size)/100)
        new_number_sequence.extend(number_sequence[:n])

        n = int((90 * Size) / 100)

        for _ in range(n):
            spouce1 = random.choice(number_sequence[:50])
            spouce2 = random.choice(number_sequence[:50])
            new_gen1 = spouce1.mutation(spouce2)



if __name__ == '__main__':
    main()