import numpy as np
import random

def genematrix(list_of_individuals,list_of_genes,zero_matrix):
    for i in list_of_individuals:
        for a in list_of_genes:
            zero_matrix[i][a] = 1
    return zero_matrix

def randn(size=1, m=0, s=1, seed=None):
    if isinstance(size, (int, float)): size = [size, size]
    np.random.seed(seed=seed)
    r = np.random.normal(loc=m, scale=s, size=size)
    return r

def resolver(method):
    active_methods = {"value":value_changing_mutation, 'gaussian':gausian}

    return active_methods[method]

def mutation_diversity(gene, percent_mutation_diversity, seed,limits):
    random.seed(seed)
    seed = seed+1
    if random.choice([-1, 1]) == [1]:
        tmp = int(gene + randn(m=0, s=percent_mutation_diversity, seed=seed+gene))
        seed= seed+1
    else:
        tmp = int(gene - random.randint())
        seed = seed + 1
    if tmp > limits[1]:
        tmp = int(tmp - limits[1])
    if tmp < limits[0]:
        tmp = int(tmp + limits[1])
    gene = tmp
    return gene, seed

def gausian(pop,gene_count,number_of_pop_to_mutate,seed,limits,count_of_genes_to_mutate,percent_mutation_diversity):
    random.seed(seed)
    list_to_mutate = random.sample(range(0, len(pop)), number_of_pop_to_mutate)
    list_of_genes = random.sample(range(0,4),count_of_genes_to_mutate)
    list_of_genes = genematrix(list_to_mutate,list_of_genes,np.zeros((len(pop),4)))
    seed += 1
    list_of_genes_to_mutate = randn((len(pop),4))
    seed+=1
    list_of_genes = list_of_genes_to_mutate*list_of_genes

    return (pop+list_of_genes),seed

def value_changing_mutation(pop,gene_count, number_of_pop_to_mutate, seed, limits, count_of_genes_to_mutate, percent_mutation_diversity):
    random.seed(seed)
    list_to_mutate = random.sample(range(0, len(pop)), number_of_pop_to_mutate)
    seed += 1
    list_of_genes_to_mutate = random.sample(range(0, gene_count), count_of_genes_to_mutate)
    seed += 1
    for x in list_to_mutate:
        for y in list_of_genes_to_mutate:
            random.seed(seed);
            seed+=1
            pop[x][y] = int(round(pop[x][y] + random.choice([-pop[x][y], pop[x][y]])*percent_mutation_diversity*0.01))
    return pop, seed


#pop, seed = mutation.mutate(pop, mutation_method, number_of_pop_to_mutate, seed, count_of_genes_to_mutate, percent_mutation_diversity)


def mutate(pop, gene_count, mutation_method, number_of_pop_to_mutate, seed, limits, count_of_genes_to_mutate = None, percent_mutation_diversity = None):
    mutation_method = resolver(mutation_method)
    pop, seed = mutation_method(pop, gene_count, number_of_pop_to_mutate, seed, limits, count_of_genes_to_mutate, percent_mutation_diversity)

    return pop, seed