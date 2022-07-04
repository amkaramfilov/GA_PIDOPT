import random
import sys

import numpy as np
import cost_function as cf
import selection as sel
import crossovers as co
import mutation


A=np.array([[0.9828,-0.1913,0.07337,-0.01984],[0.1665,0.9129,0.1375,-0.0002772],[-0.08873,-0.3563,0.4755,0.1854],[0.005396,-0.006432,-0.1116,-0.2522]])
B=np.array([[0.0002381],[0.005913],[0.01116],[-0.0002432]])
C=np.array([-15.07,0.2189,0.2088,-0.06037])
C=np.reshape(C,(1,4))

def startup_population(pop_count, lower_limits,upper_limits,input_seed):
    np.random.seed(input_seed)
    Kp = np.random.uniform(lower_limits[0], upper_limits[0], size=(pop_count, 1))
    Ti = np.random.uniform(lower_limits[1], upper_limits[1], size=(pop_count, 1))
    Td = np.random.uniform(lower_limits[2], upper_limits[2], size=(pop_count, 1))
    N = np.random.uniform(lower_limits[3], upper_limits[3], size=(pop_count, 1))
    np_of_individuals = np.column_stack((Kp, Ti, Td, N))
    input_seed += pop_count
    return np_of_individuals, input_seed

## todo: min_vals = [Kp_minval,Ti_minval,Td_minval,N_minval],max_val=[Kp_maxval,Ti_maxval,Td_maxval,N_maxval]
def ga(startup_pop_count,min_val,max_val,seed):

    generation = 0
    pop, seed = startup_population(startup_pop_count,min_val,max_val, seed)
    pop, fitness_values = cf.simulation(pop,2,A,B,C,0.5)
    termination_condition = False
    consecutive_first_fit_val = 0
    last_first_fit_val = fitness_values[0]
    print("Generation   best solution    individual")
    while True:
        generation = generation+1
        fitness_values, pop = sel.selection(fitness_values,pop)
        if generation % 200 == 0:
            offspring,seed=co.crossover(pop,"scramble",4,seed,False)
        else:
            offspring, seed = co.crossover(pop, "uniform", 4, seed,False)
        if generation%10 == 0:
            offspring, seed = mutation.mutate(offspring,4,"value",2000,seed,None,4,500)
        else:
            offspring, seed = mutation.mutate(offspring, 4, "gaussian", 2000, seed, None, 4, None)
        offspring, offspring_fit_val = cf.simulation(offspring,2,A,B,C,0.5)
        pop = np.vstack([pop, offspring])
        fitness_values = np.vstack([fitness_values, offspring_fit_val])
        pop = pop[np.argsort(fitness_values[:,0])]
        fitness_values = np.sort(fitness_values,axis=0,kind="stable")
        print(generation, fitness_values[0], pop[0])
        if fitness_values[0] < 2:break
        #termination_condition, first_is_lastfirst = term_cond(termination_condition, fitness_values[0], last_first_fit_val, satisfiable_fx)
        #if first_is_lastfirst:
         #   consecutive_first_fit_val += 1
          #  if consecutive_first_fit_val >= consecutive_first_count:
           #     termination_condition = True
        #else:
         #   consecutive_first_fit_val = 1
          #  last_first_fit_val = fitness_values[0]
        #if termination_condition:
         #   break
    return pop[0],fitness_values[0]

ga(4000,[0,10,0,10],[5,20,30,200],3123)