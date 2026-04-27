def fitness(chromosome, weights, benefits, capacity):
    total_weight = sum(chromosome[i] * weights[i]  for i in range(len(chromosome)))
    total_benefit = sum(chromosome[i] * benefits[i] for i in range(len(chromosome)))
    if total_weight> capacity:
        return 0
    return total_benefit
def population(pop_size, n_items):
    return [[random.randint(0, 1) for _ in range(n_items)] for _ in range(pop_size)]
def tournament(population, weights, benefits, capacity, k=3):
    contestants = random.sample(population, k)
    return max(contestants, key=lambda c: fitness(c, weights, benefits, capacity))
def crossover(parent1, parent2):
    point =random.randint(1, len(parent1) - 1)
    child1 = parent1[:point]+ parent2[point:]
    child2 = parent2[:point]+ parent1[point:]
    return child1, child2
def mutation(chromosome, mutation_rate=0.01):
    return [1 - gene if random.random() < mutation_rate else gene for gene in chromosome]
def main_algo(weights, benefits, capacity, pop_size=50, n_generations=200, mutation_rate=0.01):
    n_items = len(weights)
    population = init_population(pop_size, n_items)
    best_chromosome = max(population, key=lambda c: fitness(c, weights, benefits, capacity))
    best_fitness = fitness(best_chromosome, weights, benefits, capacity)
    for _ in range(n_generations):
        new_population =[best_chromosome[:]]
        while len(new_population)<pop_size:
            p1 = tournament_selection(population, weights, benefits, capacity)
            p2 = tournament_selection(population, weights, benefits, capacity)
            c1, c2 = single_point_crossover(p1, p2)
            c1 = bit_flip_mutation(c1, mutation_rate)
            c2 = bit_flip_mutation(c2, mutation_rate)
            new_population.extend([c1, c2])
        population=new_population[:pop_size]
        gen_best = max(population, key=lambda c: fitness(c, weights, benefits, capacity))
        gen_fit= fitness(gen_best, weights, benefits, capacity)
        if gen_fit > best_fitness:
            best_fitness = gen_fit
            best_chromosome= gen_best[:]
    return best_chromosome, best_fitness
np.random.seed(111)
np.random.seed(111)
test_cases = [
              {'n_items': 5,  'capacity': 10, 'items': [(4,5),(3,4),(5,3),(2,3),(1,1)]},
              {'n_items': 6,  'capacity': 15, 'items': [(5,10),(4,40),(3,30),(2,50),(6,35),(7,20)]},
              {'n_items': 8,  'capacity': 20, 'items': [(3,4),(4,5),(5,6),(6,7),(2,3),(7,8),(1,2),(8,9)]},
              ]

Len = len(test_cases)
print(Len)
print()
for case_id, tc in enumerate(test_cases, 1):
    solve_knapsack(case_id, tc['n_items'], tc['capacity'], tc['items'])
    print()
