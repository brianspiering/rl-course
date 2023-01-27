import numpy as np

class Bandit:
    "Implements a online, learning strategy to solve the Multi-Armed Bandit problem."

    def __init__(self, p_array, choice_function):
        self.p_array   = p_array                  # Array of probabilities for each bandit
        self.n_bandits = len(p_array)
        self.optimal   = np.argmax(p_array)       # Index of the optimal bandit
        self.wins      = np.zeros(self.n_bandits)
        self.trials    = np.zeros(self.n_bandits)
        self.N         = 0                        # The cumulative number of samples
        self.choices   = []                       # The historical choices 
        self.score     = []                       # The historical score 
        self.choice_function = choice_function    # Should return an index, an int between 0 and n-1
                                               
    def pull(self, index):
        "Sample from a given bandit"
        return np.random.random() < self.p_array[index] # Boolean indicating whether the bandit returned a reward or not

    def sample_bandits(self, n=1):
        "Simulate n rounds of running the bandit process."
        score = np.zeros(n)
        choices = np.zeros(n)

        for k in range(n):
            # Sample from the bandits's priors, and select the largest sample
            choice = self.choice_function(self)

            # Sample the chosen bandit
            result = self.pull(choice)

            # Update priors and score
            self.wins[choice] += result
            self.trials[choice] += 1
            score[k] = result
            self.N += 1
            choices[k] = choice

        self.score = np.r_[self.score, score]
        self.choices = np.r_[self.choices, choices]

    def regret(self, probabilities):
        """Take an array of the true probabilities for each machine and 
        an array of the indices of the machine played at each round.
        Return an array giving the total regret after each round."""
        p_opt = np.max(probabilities)
        return np.cumsum(p_opt - probabilities[self.choices.astype(int)]) # Total Regret

    def optimum_choices(self, probabilities):
        """Take an array of the true probabilities for each machine and 
        an array of the indices of the machine played at each round.
        Return an array giving the total regret after each round."""
        p_opt = np.argmax(probabilities)
        return np.cumsum(np.select([self.choices==p_opt], [1]))

    def max_mean(self):
        "Pick the bandit with the current best observed proportion of winning."
        if len(self.trials.nonzero()[0]) < self.n_bandits: # Make sure to play each bandit at least once
            return np.random.randint(0, self.n_bandits)
        return np.argmax(self.wins / (self.trials + 1)) # Return the index of the winning bandit.

def print_results(bandit):
    assert len(bandit.p_array) == 4, "Expecting 4 options"
    print("Options: \t  {:>6} {:>6} {:>6} {:>6}".format(*"A B C D".split()))
    print("Probablities: \t  {:>6.2f} {:>6.2f} {:>6.2f} {:>6.2f}".format(*bandit.p_array))
    print("Number of wins:   {:>6} {:>6} {:>6} {:>6}".format(*[int(_) for _ in bandit.wins]))
    print("Number of trials: {:>6} {:>6} {:>6} {:>6}".format(*[int(_) for _ in bandit.trials]))
    rates = [bandit.wins / bandit.trials]
    print("Conversion rates: {:>6.2f} {:>6.2f} {:>6.2f} {:>6.2f}".format(*rates[0]))
    print()
    print(f"A total of {bandit.wins.sum():,.0f} wins out of {bandit.trials.sum():,.0f} trials.")
    