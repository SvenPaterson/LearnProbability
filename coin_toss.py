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
    print(outcome[x-2:])
    return sum(outcome[x-2:])

def main():
    print("Number of tosses before successive tosses: ")
    n = 100000
    outcomes = perform_experiment(n)
    print(outcomes)
    likelihood = [round(x / sum(outcomes), 4) for x in outcomes]
    print(likelihood)

    x = 5
    print("Probability of 4 or more tosses: ")
    print(prob_of_x_tosses(likelihood, x))

    plot_results(likelihood)

    

if __name__ == "__main__":
    main()