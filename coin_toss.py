from random import randint

import matplotlib.pyplot as plt
import numpy as np

def coin_toss():
    if randint(0, 1) == 0:
        return "H"
    else:
        return "T"
    
def successive_found():
    count = 0
    while True:
        first_toss = coin_toss()
        if coin_toss() == first_toss:
            return count
        else:
            count += 1

def perform_experiment(n):
    outcomes = np.array([])
    for i in range(n):
        tosses = successive_found()
        if len(outcomes) <= tosses:
            diff = tosses - len(outcomes) + 1
            outcomes = np.append(outcomes, np.zeros(diff)) 
        outcomes[tosses] += 1   
    return outcomes

def plot_results(outcome):
    plt.plot(outcome)
    plt.xlabel("Number of tosses")
    plt.ylabel("Likelihood of successive tosses")
    plt.title("Coin Toss Experiment")
    plt.show()

def prob_of_x_tosses(outcome, x):
    if x < 2:
        return 0
    return sum(outcome[x-2:])

def calc_likelihood(outcomes):
    def normalize(x):
        return np.round(x / np.sum(outcomes), 4)
    return np.apply_along_axis(normalize, 0, outcomes)


def main():
    np.set_printoptions(suppress=True, precision=4)
    print("\nNumber of tosses before successive tosses: ", end="\n\t")
    n = 1000000
    outcomes = perform_experiment(n)
    print(outcomes)

    print("\nLikelihood of successive tosses: ", end="\n\t")
    likelihood = calc_likelihood(outcomes)
    print(likelihood)

    x = 4
    print(f"\nLikelihood of {x} or more tosses, based on {n} experiments: ")
    print(prob_of_x_tosses(likelihood, x))

    plot_results(likelihood)

    

if __name__ == "__main__":
    main()