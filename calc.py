import pandas as pd

shows = pd.read_csv("criteria.csv")

episode_vals = []
for value in shows['episodes']:
    if value < 10:
        episode_vals.append(5)
    elif 10 <= value < 20:
        episode_vals.append(3)
    elif 28 <= value < 100:
        episode_vals.append(-3)
    elif value >= 100:
        episode_vals.append(-5)
    else:
        episode_vals.append(0)
shows['episode_BP'] = episode_vals

season_vals = []
for value in shows['seasons']:
    if value == 0:
        season_vals.append(3)
    elif value > 2:
        season_vals.append(-3)
    else:
        season_vals.append(0)
shows['season_BP'] = season_vals

total_episodes_vals = []
for value in shows['total_episodes']:
    if 10 <= value < 20:
        total_episodes_vals.append(2)
    elif 20 <= value < 100:
        total_episodes_vals.append(-2)
    elif value >= 100:
        total_episodes_vals.append(-5)
    else:
        total_episodes_vals.append(0)
shows['total_episodes_BP'] = total_episodes_vals

essen_vals = []
for value in shows['essential']:
    if value == 'yy':
        essen_vals.append(10)
    elif value == 'y':
        essen_vals.append(4)
    elif value == 'm':
        essen_vals.append(2)
    else:
        essen_vals.append(0)
shows['essential_BP'] = essen_vals

genre_vals = []
for value in shows['like_genre']:
    if value == 'y':
        genre_vals.append(3)
    elif value == 'n':
        genre_vals.append(-3)
    else:
        genre_vals.append(0)
shows['genre_BP'] = genre_vals

rec_vals = []
for value in shows['rec']:
    if value == 'y':
        rec_vals.append(3)
    else:
        rec_vals.append(0)
shows['rec_BP'] = rec_vals

best_vals = []
for value in shows['best']:
    if value == 'y':
        best_vals.append(2)
    else:
        best_vals.append(0)
shows['best_BP'] = rec_vals

other_vals = []
for value in shows['other']:
    if value > 0 or value < 0:
        other_vals.append(int(value))
    else:
        other_vals.append(0)
shows['other_BP'] = other_vals

shows['BP'] = shows['episode_BP'] + shows['season_BP'] + shows['total_episodes_BP'] + shows['essential_BP']\
              + shows['genre_BP'] + shows['rec_BP'] + shows['best_BP'] + shows['other_BP']

calculated = pd.DataFrame()
calculated['show'] = shows['title']
calculated['point_value'] = shows['BP']
calculated = calculated.sort_values('point_value', ascending=False)
print(calculated)
calculated.to_csv('calculated.csv', index=False)
