import os
import sys
import pandas as pd


def extract_referee_names():
    FILENAME = os.path.join(
        os.getcwd(), "../football-data.co.uk/updated-epl-training.csv"
    )

    def parse_csv():
        referees = set()
        for line in open(FILENAME):
            referees.add(line.split(",")[10])  # referee column
        return sorted(list(referees))

    return parse_csv()


if __name__ == "__main__":
    referee_names = {"Standard referee name": extract_referee_names()}
    data = pd.DataFrame(data=referee_names)

    # give each team a unique ID
    unique_ID = [i for i in range(1, 1 + data["Standard referee name"].count())]
    data.insert(0, "RefereeID", unique_ID)

    path = os.path.join(os.getcwd(), "standard.referee.names.csv")
    data.to_csv(path, index=False)
    print(f"Wrote to {path}")
