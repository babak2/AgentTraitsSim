# AgentTraitsSim

AgentTraitsSim is a Python program for simulating the evolution of agent traits in a social media community. It explores how different structural characteristics of the environment affect the transmission of behaviors among customer communities. The simulation is based on agent-based modeling and allows for varying population sizes, trait probabilities, trait links, payoff bonuses, and reproduction strategies.

ats (Agent Traits Sim) program reads parameter values from a CSV file, iterates over the combinations, performs simulations, plots and saves output figures, and finally stores the simulation results in another CSV file (all output files are stored in the Output directory).

This model of customer engagement in the social media industry looks at how cultural norms evolve within different social media structures, utilizing empirical data collected from various observational studies. The simulation runs a series of experiments altering the structural characteristics of the environment to examine their impact on the transmission of behaviors within customer communities.

In particular, the simulations vary across the following aspects:

- The number of agents in the population, including levels of 100, 1,000, 5,000, 50,000, 100,000, 250,000, and 1,000,000. (For testing purposes, it's recommended to limit populations to 100 and 1,000 to ensure reasonable execution time.)
- Probabilities of a new agent having trait == 'A', with increments of 0.05 from 0 to 1.
- Probabilities of a new agent having trait_2 == 'X', with increments of 0.05 from 0 to 1.
- The linkage between trait == 'A' and trait_2 == 'X', adjusted in increments of 0.05 from 0 to 1.
- Additional payoff for trait=='A', incremented by 1 from 0 to 10.
    The reproduction strategy, which remains constant as "indirect_biased_transmission".


## Installation

Clone the repository to your local machine:

`git clone https://github.com/babak2/AgentTraitsSim.git  `

or if you have the program as a ZIP file, simply extract the zip file to a directory of your choice.

Change your working directory to AgentTraitsSim:

`cd AgentTraitsSim`


## Program Requirements

AgentTraitsSim requires Python 3 and the following libraries:
    pandas
    matplotlib

Install these libraries using the following command:

`pip install pandas matplotlib`


## Input File Format

The program reads input parameters from a CSV file named parameters.csv. The CSV file should have the following columns:

- `n_agents`: Number of agents in the population.
- `trait_p`: Probability of trait 'A' for a new agent.
- `trait_2_p`: Probability of trait_2 'X' for a new agent.
- `link`: Probability of the link between trait 'A' and trait_2 'X'.
- `additional_payoff`: Additional payoff for trait 'A'.

## Input File Format

The program reads input parameters from a CSV file named `parameters.csv`. The CSV file should have the following columns:

| n_agents | trait_p | trait_2_p | link | additional_payoff |
|----------|---------|-----------|------|-------------------|
| 100      | 0.1     | 0.1       | 0.05 | 1                 |
| 100      | 0.1     | 0.1       | 0.5  | 1                 |
| 100      | 0.1     | 0.5       | 0.05 | 10                |
| 100      | 0.1     | 0.5       | 0.5  | 1                 |
| 100      | 0.5     | 0.1       | 0.05 | 1                 |
| 100      | 0.5     | 0.1       | 0.5  | 10                |


An example is located in the current directory.

## Output Format

Output Files:
- The simulation results are saved in SVG format. Each output file includes plots showing the proportion of agents with trait 'A' and the proportion of agents with trait_2 'X' over time.
- simulation_results.csv:  A CSV file containing svarious parameter combinations.

All the output files are stored in the `Output` directory.

## Output File Format

After running the simulation for various parameter combinations, the program generates an output CSV file named `simulation_results.csv` in the `Output` directory. The CSV file will have the following columns:

|population_size|trait_prob|trait_2_prob|trait_link|payoff_bonus| filename                     |
|---------------|----------|------------|----------|------------|------------------------------|
| 100           | 0.1      | 0.1        | 0.05     | 1          |output_100_0.1_0.1_0.05_1.svg |
| 100           | 0.1      | 0.1        | 0.5      | 1          |output_100_0.1_0.1_0.5_1.svg  |
| 100           | 0.1      | 0.5        | 0.05     | 10         |output_100_0.1_0.5_0.05_10.svg|
| 100           | 0.1      | 0.5        | 0.5      | 1          |output_100_0.1_0.5_0.5_1.svg  |
| 100           | 0.5      | 0.1        | 0.05     | 1          |output_100_0.5_0.1_0.05_1.svg |
| 100           | 0.5      | 0.1        | 0.5      | 10         |output_100_0.5_0.1_0.5_10.svg |
| 100           | 0.5      | 0.5        | 0.05     | 1          |output_100_0.5_0.5_0.05_1.svg |

The `filename` column indicates the name of the SVG file that corresponds to the output plot generated for each parameter combination.

An example is located in the `Output` directory.

## Usage

To use ats, run the ats.py script with the following command:

`python3 ats.py`


## License

ats is licensed under the GNU GENERAL PUBLIC LICENSE. See LICENSE for more information.


## Author 

Babak Mahdavi Aresetani

babak.m.ardestani@gmail.com

