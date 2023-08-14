import random
import os

from matplotlib import pyplot

import pandas as pd


class Agent(object):
    '''
    An agent class representing individuals with traits in a simulation.

    An agent has two traits - one instrumental, 'trait', which is directly
    related to reputation within the community and 'trait_2' which is neutral 
    with regard to reputation. These traits are linked with a probability of
    0.5 such that there is a 50% chance that if they have trait=A they
    have trait_2=X, otherwise underlying chance of trait_2=X is 0.1
    
    The 'payoff' function represents the reputation of an agent within the 
    community 
    '''
    def __init__(self, trait=None):
        
        '''
        Initializes an Agent instance with traits.

        :param trait: The initial trait of the agent.
        '''
          
        if trait:
            self.trait = trait
        else:
            #probability of trait = 'A' for a new agent is 0.05
            self.trait = 'A' if random.random() < 0.05 else 'B'
        self.trait_2 = 'N/A'        
        if random.random()  < 0.5:
            if self.trait == 'A':
                self.trait_2 = 'X'
            else:
                self.trait_2 = 'Y'
        else:
            self.trait_2 = 'X' if random.random() < 0.1 else 'Y'
                
        
    @property
    def payoff(self):
        
        '''
        Calculates and returns the payoff value of the agent.
        :return: The calculated payoff value.
        '''
        #payoff in any epoch for the productive trait=A is 11 reputation
        #points compared to a baseline of 10 reputation points
        if self.trait == 'A':
            return 11
        else:
            return 10

    def reproduce(self, population, strategy = 'unbiased_mutation'):
        
        '''
        Creates a new agent as an offspring with a specific strategy.

        :param population: The population containing the agents.
        :param strategy: The reproduction strategy to use.
        :return: The newly created offspring agent.
        '''
        offspring = Agent(trait=self.trait)
        if strategy == 'unbiased_transmission':
            #agents behave essentially at random in similar proportions
            #to in the previous period
            offspring.trait = random.choice(population.agents).trait
        if strategy == 'unbiased_mutation':
            #agents will stick with their behaviour from the previous
            #period, except for a 0.05 chance of switching to the alternate
            #behaviour
            #rate of unbiased mutation is 0.05
            if random.random() < 0.05:
                offspring.trait = 'B' if self.trait == 'A' else 'A'
        if strategy == 'biased_mutation':
            #agents never switch from the more productive to less productive
            #behaviour, but will switch from B to A with a probability of 0.05
            if self.trait == 'B':
                #rate of biased mutation is 0.05
                if random.random() < 0.05:
                    offspring.trait = 'A'
        if strategy == 'direct_biased_transmission':
            #agents encounter a single random 'demonstrator' agent in the
            #previous period and will copy their behaviour, if it's trait A
            #with a probability of 0.1
            demonstrator = random.choice(population.agents)
            if demonstrator.trait == 'A':
                #rate of direct biased transmission is 0.1
                if random.random() < 0.1:
                    offspring.trait = 'A'
        if strategy == 'indirect_biased_transmission':
             #agents will choose a single random demonstrator from the previous
             #period, preferentially selecting agents relative to their payoff
             #compared with other agents
             demonstrator = random.choices(population.agents, weights = population.payoffs, k=1)[0]    
             offspring.trait = demonstrator.trait
             offspring.trait_2 = demonstrator.trait_2

        return offspring
    

class Population(object):

    '''
    A population class containing a collection of agents in a simulation.
    '''
    def __init__(self):

        '''
        Initializes a Population instance and creates a set of agents.
        '''
        # create a population of 1000 agents
        self.agents = [Agent() for i in range(1, 1000)]
        self.period = 1
        self.proportion_of_as = []
        self.proportion_of_xs = []
        self.payoffs = []
        self.proportion_of_as.append(self.calc_output())
        self.proportion_of_xs.append(self.calc_output_2())
        #self.unbiased_mutation_rate = unbiased_mutation_rate
        #self.biased_mutation_rate = biased_mutation_rate
        
    def calc_output(self):

        '''
        Calculates and returns the proportion of agents with trait 'A'.

        :return: The calculated proportion.
        '''
        # gives the number of agents with trait=A in the current period
        output = 0
        for agent in self.agents:
            if agent.trait == 'A':
                output += 1
        output = output / len(self.agents)
        return output

    def calc_output_2(self):

        '''
        Calculates and returns the proportion of agents with trait_2 'X'.

        :return: The calculated proportion.
        '''
        # gives the number of agents with trait_2=X in the current period
        output = 0
        for agent in self.agents:
            if agent.trait_2 == 'X':
                output += 1
        output = output / len(self.agents)
        return output


    def learning_epoch(self):
        
        '''
        Advances the simulation by one epoch, updating agents' traits.
        '''
        # increase the period by one, and have the agents update
        # their traits according to selected strategy
        self.period += 1
        self.payoffs = [agent.payoff for agent in self.agents]
        new_agents = []
        for agent in self.agents:
            new_agents.append(agent.reproduce(self,strategy="indirect_biased_transmission"))
        self.agents = new_agents
        self.proportion_of_as.append(self.calc_output())
        self.proportion_of_xs.append(self.calc_output_2())



def main(population_size, trait_prob, trait_2_prob, trait_link, payoff_bonus):

    '''
    The main function to run the simulation with given parameters.

    :param population_size: The size of the population.
    :param trait_prob: Probability of trait 'A' for a new agent.
    :param trait_2_prob: Probability of trait_2 'X' for a new agent.
    :param trait_link: Probability of the link between trait 'A' and trait_2 'X'.
    :param payoff_bonus: Additional payoff for trait 'A'.
    :return: A dictionary containing simulation results.
    '''
    population = Population()
    # Run for a fixed number of periods
    num_periods = 150
    for i in range(num_periods):
        population.learning_epoch()
        
    # Create the Output directory if it doesn't exist
    output_dir = "Output"
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Plot and save the output figures in the output directory
    output_filename = f"output_{population_size}_{trait_prob}_{trait_2_prob}_{trait_link}_{payoff_bonus}.svg"
    output_path = os.path.join(output_dir, output_filename)
    pyplot.plot(population.proportion_of_as)
    pyplot.plot(population.proportion_of_xs)
    pyplot.ylim([0, 1])
    pyplot.savefig(output_path, format="svg")
    pyplot.close()

    return {
        'population_size': population_size,
        'trait_prob': trait_prob,
        'trait_2_prob': trait_2_prob,
        'trait_link': trait_link,
        'payoff_bonus': payoff_bonus,
        'filename': output_filename
    }


if __name__ == "__main__":
    # Read the parameters from the CSV file
    parameters_df = pd.read_csv('paramaters.csv')

    # os.makedirs('Output', exist_ok=True)

    # Iterate over the parameter combinations and run simulations
    results = []
    for _, row in parameters_df.iterrows():
        population_size = int(row['n_agents'])
        trait_prob = float(row['trait_p'])
        trait_2_prob = float(row['trait_2_p'])
        trait_link = float(row['link'])
        payoff_bonus = int(row['additional_payoff'])

        result = main(population_size, trait_prob, trait_2_prob, trait_link, payoff_bonus)
        results.append(result)

    # Save the results to a CSV file within the 'Output' directory
    results_df = pd.DataFrame(results)
    output_path = os.path.join('Output', 'simulation_results.csv')
    results_df.to_csv(output_path, index=False)