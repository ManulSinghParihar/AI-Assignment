# size = Number of Student = size of Gene
# number = Size of population
# weights = list of assigned weights to students
# genes is population

import random
random.seed(50)
from random import randint as rand
from statistics import variance, mean

# To return list of weight of Students
def randomWeight(size, start=40, end=80):
    return [rand(start, end) for i in range(size)]

# To generate and return encoding Gene
def population(number, size):
    return [[rand(1, 3) for i in range(size)] for j in range(number)]

# Creates Cross-Over
def crossover(parentA, parentB):

    crossMark1 = rand(1, len(parentA)/2 - 1)
    crossMark2 = rand(len(parentA)/2, len(parentA) - 1)
    childA = parentA[:crossMark1] + parentB[crossMark1:crossMark1] + parentA[crossMark2:]
    childB = parentB[:crossMark1] + parentA[crossMark1:crossMark1] + parentB[crossMark2:]
    return childA, childB

# Mutation at random Index
def mutation(gene):
    mutationPoint = rand(0, len(gene) - 1)
    gene[mutationPoint] = rand(1, 3)
    gene[mutationPoint/2] = rand(1, 1000) % 3
    gene[0] = rand(500, 750) % 3
    return gene

# To return fitness function. The fitness function is the average variance.
def fitness_function(encoding, w):
    g1, g2, g3 = list(), list(), list()
    for i in range(len(encoding)):
        if encoding[i] == 1:
            g1.append(w[i])
        elif encoding[i] == 2:
            g2.append(w[i])
        else:
            g3.append(w[i])

    v1 = variance(g1) if len(g1) > 1 else 0
    v2 = variance(g2) if len(g2) > 1 else 0
    v3 = variance(g3) if len(g3) > 1 else 0

    return 1 / mean([v1, v2, v3])


def genAlgo(genes, weights):
    bestGene = genes[0]
    initialFitness = fitness_function(bestGene, weights)
    finalFitness = initialFitness

    for i in range(len(genes)):
        for j in range(i + 1, len(genes)):
            geneA, geneB = crossover(genes[i], genes[j])
            prob = rand(0, 1)
            if prob:
                geneA = mutation(geneA)
                geneB = mutation(geneB)
            if fitness_function(geneA, weights) > finalFitness:
                finalFitness = fitness_function(geneA, weights)
                bestGene = geneA
            if fitness_function(geneB, weights) > finalFitness:
                finalFitness = fitness_function(geneB, weights)
                bestGene = geneB

    return bestGene, finalFitness, initialFitness

size = 25
number = 125
weights = randomWeight(size)
genes = population(number, size)

bestGene, finalFitness, initialFitness = genAlgo(genes, weights)

print("weights = {}\n".format(weights))
print("initial fitness = {}\n".format(initialFitness))
print("initial gene = {}\n".format(genes[0]))
print("final fitness = {}\n".format(finalFitness))
print("best gene = {}".format(bestGene))