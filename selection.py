import numpy as np


def resolver(method):
    active_methods = {"elithism": elithism_selection}
    return active_methods[method]

def elithism_selection(fitness_values, population):
    population, second_half_pop = np.split(population, 2)
    fitness_values, second_half_fitval = np.split(fitness_values, 2)
    return population, fitness_values


def selection(fitness_values, population, selection_method = "elithism"):
#todo array with choices , check "if x in array" to select choice of selection method
    selection_method = resolver(selection_method)
    survived_population, survived_fitness_values = selection_method(fitness_values, population)
    return survived_fitness_values, survived_population
