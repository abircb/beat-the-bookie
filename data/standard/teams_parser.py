import os
import sys
import pandas as pd


def extract_team_names():
    FILENAME = "../football-data.co.uk/updated-epl-training.csv"

    def parse_csv():
        teams = set()
        for line in open(FILENAME):
            teams.add(line.split(",")[2])
        return sorted(list(teams))

    return parse_csv()


if __name__ == "__main__":
    team_names = {"Standard teamname": extract_team_names()}
    data = pd.DataFrame(data=team_names)

    path = os.path.join(os.getcwd(), "standard.teamnames.csv")
    data.to_csv(path, index=False)
    print(f"Wrote to {path}")
