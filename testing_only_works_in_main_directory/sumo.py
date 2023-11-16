import pandas as pd

results = pd.read_csv("results.csv")
sumo = pd.read_csv("results.csv", dtype={'basho': 'string', 'day': 'string', 'rikishi1_id': 'int64', 'rikishi1_rank': 'string', 'rikishi1_shikona': 'string', 'rikishi1_result': 'string', 'rikishi1_win': 'int64', 'kimarite': 'string', 'rikishi2_id': 'int64', 'rikishi2_rank': 'string', 'rikishi2_shikona': 'string', 'rikishi2_result': 'string', 'rikishi2_win': 'string'})

print(sumo.loc[5, 'rikishi1_id'])