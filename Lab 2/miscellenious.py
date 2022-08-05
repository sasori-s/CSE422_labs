Target = 330
chromosome = '10101010'
input_list = [('Tamim', 68), ('Shoumyo', 25), ('Shakib', 70), ('Afif', 53), ('Mushfiq', 71), ('Liton', 55), ('Mahmadullah', 66), ('Shanto', 29)]

def calc_fitness(chromosome):
    fitness = 0
    for i, val in enumerate(input_list):
        if chromosome[i] == '1':
            fitness = fitness + val[1]

    if fitness > Target:
        return 0
    return fitness

print(calc_fitness(chromosome))