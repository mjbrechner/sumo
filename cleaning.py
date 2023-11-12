import pandas as pd
from sqlite3 import connect

sumo = pd.read_csv(
    "data/results.csv",
    dtype={
        "basho": "string",
        "day": "string",
        "rikishi1_id": "int64",
        "rikishi1_rank": "string",
        "rikishi1_shikona": "string",
        "rikishi1_result": "string",
        "rikishi1_win": "int64",
        "kimarite": "string",
        "rikishi2_id": "int64",
        "rikishi2_rank": "string",
        "rikishi2_shikona": "string",
        "rikishi2_result": "string",
        "rikishi2_win": "string",
    },
)
banzuke = pd.read_csv(
    "data/banzuke.csv",
    dtype={
        "basho": "string",
        "day": "string",
        "rikishi1_id": "int64",
        "rikishi1_rank": "string",
        "rikishi1_shikona": "string",
        "rikishi1_result": "string",
        "rikishi1_win": "int64",
        "kimarite": "string",
        "rikishi2_id": "int64",
        "rikishi2_rank": "string",
        "rikishi2_shikona": "string",
        "rikishi2_result": "string",
        "rikishi2_win": "string",
    },
)

# Calculate BMI
bmi_list = []

for i in range(len(banzuke)):
    bmi = round(banzuke.loc[i, "weight"] / ((banzuke.loc[i, "height"] / 100) ** 2), 1)
    bmi_list.append(bmi)
bmi_list

banzuke["bmi"] = bmi_list
# Finished calculating BMI

connection = connect(":memory:")
sumo.to_sql("sumo", connection)
banzuke.to_sql("banzuke", connection)


def sql(a_string):
    return pd.read_sql(a_string, connection)


combined_sql_query = pd.read_sql_query(
    """SELECT sumo.basho AS 'basho', sumo.rikishi1_id AS 'id', sumo.rikishi1_shikona, banzuke.rikishi as 'rikishi', 
    sumo.rikishi1_rank AS 'rank', banzuke.height AS 'height', banzuke.weight AS 'weight', banzuke.bmi AS 'bmi', banzuke.heya AS 'heya',
    banzuke.shusshin AS 'shusshin', sumo.rikishi1_win as 'outcome', sumo.kimarite AS 'kimarite', sumo.rikishi2_id AS 'opponent id',
    sumo.rikishi2_shikona AS 'opponent'
    FROM sumo 
    JOIN banzuke 
    ON sumo.rikishi1_shikona = banzuke.rikishi 
    AND sumo.basho = banzuke.basho""",
    connection,
)

combined_sql_query
combined_df = pd.DataFrame(combined_sql_query)
combined_df = combined_df.drop(["rikishi1_shikona"], axis=1)


combined_df["rank"] = combined_df["rank"].astype(str)

combined_df.to_csv("data/cleaned.csv", index=False)
