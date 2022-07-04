import numpy as np


def mask_generator(number_of_arguments, seed, crossover_points=None):
    np.random.seed(seed)
    if crossover_points is None:
        #todo return uniform mask
        mask = np.random.randint(0, 2, (number_of_arguments, 1))
    if crossover_points is not None:
        point = 0
        if np.random.randint(0,2,(1,1)) == [1]:
            val = 1
        else: val =0
        crossover_points.append([number_of_arguments])
        mask = np.zeros(number_of_arguments)
        for x in crossover_points:
            if x == number_of_arguments: break
            if val == 1:
                mask[point:x] = 1
                val = 0
                point = x
            else:
                mask[point:x]
                val = 1
                point = x
    seed = seed+1
    return mask, seed


def uniform_co(parent_1, parent_2, number_of_arguments, seed, cutpoints=None):
    #mask = np.array([])
    mask, seed = mask_generator(number_of_arguments, seed, cutpoints)
    child_1 = np.zeros(number_of_arguments, dtype=type(parent_1[0]))
    child_2 = np.zeros(number_of_arguments, dtype=type(parent_1[0]))
    k = 0
    for x in mask:
        if x == 1:
            child_1[k] = parent_1[k]
            child_2[k] = parent_2[k]
        if x == 0:
            child_1[k] = parent_2[k]
            child_2[k] = parent_1[k]
        k=k+1
    return child_1, child_2, seed

def resolver(method):
    active_methods = {"uniform":uniform_co,"scramble":scramble}
    return active_methods[method]

def scramble(parent_1, parent_2, number_of_arguments, seed, cutpoints=None):
    mask, seed = mask_generator(number_of_arguments, seed, cutpoints)
    child_1 = np.zeros(number_of_arguments, dtype=type(parent_1[0]))
    child_2 = np.zeros(number_of_arguments, dtype=type(parent_1[0]))
    k = 0
    for x in mask:
        if x == 1:
            child_1[k] = parent_1[k]
            child_2[k] = parent_2[k]
        if x == 0:
            child_1[k] = parent_2[k]
            child_2[k] = parent_1[k]
        k = k + 1
    child_1=np.random.choice(child_1,4)
    child_2=np.random.choice(child_2,4)
    return child_1, child_2, seed

def mating(population, crossover_type, number_of_arguments, seed,return_parents=False, co_cut_points_number_and_genes=None):
    count_of_iters = range(0, len(population) - 1, 2)
    offspring = np.empty([0,number_of_arguments], dtype=type(population[0][0]))
    for iter in count_of_iters:
        child_1, child_2, seed = crossover_type(population[iter], population[iter + 1], number_of_arguments, seed,
                                                co_cut_points_number_and_genes)
        if return_parents:
            population = np.vstack((population, child_1))
            population = np.vstack((population, child_2))
        else:
            offspring = np.vstack((offspring,child_1))
            offspring = np.vstack((offspring,child_2))
    if return_parents:
        return population, seed
    else:
        return offspring, seed

def crossover(population, crossover_type, number_of_args, seed,return_parents=False, co_cut_points_number_and_genes=None):
    crossover_type = resolver(crossover_type)
    offspring, seed = mating(population, crossover_type, number_of_args, seed,return_parents, co_cut_points_number_and_genes)

    return offspring, seed



