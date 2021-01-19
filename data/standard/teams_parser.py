import os
import sys
import pandas as pd


def extract_team_names():
    FILENAME = os.path.join(
        os.getcwd(), "../football-data.co.uk/updated-epl-training.csv"
    )

    def parse_csv():
        teams = set()
        for line in open(FILENAME):
            teams.add(line.split(",")[2])  # home teams
            teams.add(line.split(",")[3])  # away teams
        return sorted(list(teams))

    return parse_csv()


if __name__ == "__main__":
    team_names = {"Standard teamname": extract_team_names()}
    data = pd.DataFrame(data=team_names)

    # give each team a unique ID
    unique_ID = [i for i in range(1, 1 + data["Standard teamname"].count())]
    data.insert(0, "TeamID", unique_ID)

    path = os.path.join(os.getcwd(), "standard.teamnames.csv")
    data.to_csv(path, index=False)
    print(f"Wrote to {path}")
