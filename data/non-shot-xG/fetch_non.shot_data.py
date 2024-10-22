import pandas as pd
import sys
import os


def get_data():
    seasons = [
        "1617",
        "1718",
        "1819",
        "1920",
        "2021",
    ]
    columns = [
        "Date",
        "HomeTeam",
        "AwayTeam",
        "Referee",
        "HC",
        "AC",
        "HF",
        "AF",
        "HY",
        "AY",
        "HR",
        "AR",
        "FTHG",
        "FTAG",
        "FTR",
    ]

    data = [
        pd.read_csv(
            f"https://www.football-data.co.uk/mmz4281/{season}/E0.csv", dtype=str
        )
        for season in seasons
    ]

    # concat data from all seasons
    data = pd.concat([x[columns] for x in data]).dropna(axis=0)

    # give each game a unique ID
    unique_ID = [i for i in range(1, 1 + data["Date"].count())]
    data.insert(0, "GameID", unique_ID)

    return data


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "non_shot_data.csv")
    data = get_data()
    data.to_csv(path, index=False)
    print(f"Wrote to {path}")
