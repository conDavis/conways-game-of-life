import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick


df = pd.read_csv("heuristic_evaluation_data.csv")

num_infinite_rows = len(df.loc[df['is_infinite_without_interference'] == True])


def evaluate_heuristic(heuristic_name):
    """
    Runs calculations to evaluate the effectiveness of the given heuristic in comparison to a game running with no
    agent interference. Textually renders the results as they are calculated.
    """
    print('-------------------------------------------')
    print(f'Evaluating {heuristic_name} heuristic:')

    # comparing game final scores after 20 generations
    df[f'final_score_natural_vs_{heuristic_name}_20_gen'] = \
        df.apply(
            lambda row: row[f'{heuristic_name}_agent_final_score_20_gen'] - row['without_agent_final_score_20_gen'],
            axis=1)
    score_effect_after_20_gens = df[f'final_score_natural_vs_{heuristic_name}_20_gen'].mean()
    print('Average effect on final score after 20 generations:', '{0:+}'.format(score_effect_after_20_gens))
    effect_on_score_after_20_gens.append(score_effect_after_20_gens)

    # ... and after 50 generations
    df[f'final_score_natural_vs_{heuristic_name}_50_gen'] = \
        df.apply(
            lambda row: row[f'{heuristic_name}_agent_final_score_50_gen'] - row['without_agent_final_score_50_gen'],
            axis=1)
    score_effect_after_50_gens = df[f'final_score_natural_vs_{heuristic_name}_50_gen'].mean()
    print('Average effect on final score after 50 generations:', '{0:+}'.format(score_effect_after_50_gens))
    effect_on_score_after_50_gens.append(score_effect_after_50_gens)

    # calculating the number of "naturally" infinite board configs killed by agent interference using the given
    # heuristic after 20 generations
    killed_infinite_life_in_20_gens = df.apply(lambda row: row['is_infinite_without_interference']
                                                           and row[f'{heuristic_name}_agent_final_score_20_gen'] == 0,
                                               axis=1)
    num_infinite_life_killed_in_20_gens = len(
        killed_infinite_life_in_20_gens[killed_infinite_life_in_20_gens == True].index)
    print('Killed', '{:.1%}'.format(num_infinite_life_killed_in_20_gens / num_infinite_rows),
          'of infinite board configurations after 20 gens.')
    perc_infinite_configs_killed_after_20_gens.append(num_infinite_life_killed_in_20_gens / num_infinite_rows)

    # ... and after 50 generations
    killed_infinite_life_in_50_gens = df.apply(lambda row: row['is_infinite_without_interference']
                                                           and row[f'{heuristic_name}_agent_final_score_50_gen'] == 0,
                                               axis=1)
    num_infinite_life_killed_in_50_gens = len(
        killed_infinite_life_in_50_gens[killed_infinite_life_in_50_gens == True].index)
    print('Killed', '{:.1%}'.format(num_infinite_life_killed_in_50_gens / num_infinite_rows),
          'of infinite board configurations after 50 gens.')
    perc_infinite_configs_killed_after_50_gens.append(num_infinite_life_killed_in_50_gens / num_infinite_rows)


# evaluate heuristics, collect data to graphically compare them
heuristics = ['random', 'maximizing_neighbors', 'minimizing_neighbors', 'idealizing_neighbors']
effect_on_score_after_20_gens = []
effect_on_score_after_50_gens = []
perc_infinite_configs_killed_after_20_gens = []
perc_infinite_configs_killed_after_50_gens = []

print('\nEvaluating heuristic performance on 10,000 randomly generated board configurations:')
print('Total number of infinite life sustaining boards in our sample', num_infinite_rows)
for heuristic in heuristics:
    evaluate_heuristic(heuristic)

# prepping data to graphically compare heuristics
graph_df = pd.DataFrame(heuristics, columns=['heuristic'])
graph_df['effect_on_score_after_20_gens'] = effect_on_score_after_20_gens
graph_df['effect_on_score_after_50_gens'] = effect_on_score_after_50_gens
graph_df['perc_infinite_configs_killed_after_20_gens'] = perc_infinite_configs_killed_after_20_gens
graph_df['perc_infinite_configs_killed_after_50_gens'] = perc_infinite_configs_killed_after_50_gens

# ------------- Graphically comparing heuristics ------------------

# bar plot comparing agent play effects after 20 generations
ax = sns.barplot(data=graph_df, x="heuristic", y="effect_on_score_after_20_gens")
ax.set(xlabel='Heuristic', ylabel='Average Effect on Score at 20 Generations', yticks=np.arange(-10, 12, step=2))
ax.axhline(0)
ax.set(title='Analysis of Agent Play Using Heuristics over 10,000 Board Configs')
plt.show()

# bar plot comparing agent play effects after 50 generations
ax = sns.barplot(data=graph_df, x="heuristic", y="effect_on_score_after_50_gens")
ax.set(xlabel='Heuristic', ylabel='Average Effect on Score at 50 Generations', yticks=np.arange(-10, 12, step=2))
ax.axhline(0)
ax.set(title='Analysis of Agent Play Using Heuristics over 10,000 Board Configs')
plt.show()

# bar plot comparing agent play effects on "naturally" infinite configurations after 20 generations
graph_df['perc_infinite_configs_killed_after_20_gens'] = graph_df['perc_infinite_configs_killed_after_20_gens'] * 100
ax = sns.barplot(data=graph_df, x="heuristic", y="perc_infinite_configs_killed_after_20_gens")
ax.set(xlabel='Heuristic', ylabel='Infinite Life Sustaining Boards Killed in 20 Generations',
       yticks=np.arange(0, 110, step=10))
ax.set(title='Analysis of Agent Play Using Heuristics on Infinite Life Sustaining Boards')
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()

# bar plot comparing agent play effects on "naturally" infinite configurations after 50 generations
graph_df['perc_infinite_configs_killed_after_50_gens'] = graph_df['perc_infinite_configs_killed_after_50_gens'] * 100
ax = sns.barplot(data=graph_df, x="heuristic", y="perc_infinite_configs_killed_after_50_gens")
ax.set(xlabel='Heuristic', ylabel='Infinite Life Sustaining Boards Killed in 50 Generations',
       yticks=np.arange(0, 110, step=10))
ax.set(title='Analysis of Agent Play Using Heuristics on Infinite Life Sustaining Boards')
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()






