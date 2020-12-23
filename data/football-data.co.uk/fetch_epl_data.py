import pandas as pd

def get_data():
    seasons = ['0809', '0910', '1011', '1112', '1213', '1314', '1415', '1516', '1617', '1718', '1819', '1920', '2021']
    columns = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']

    data = [pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{season}/E0.csv', dtype=str) for season in seasons]
    data = [x[columns] for x in data]
    return pd.concat(data).dropna(axis=0)

if __name__ == '__main__':
    get_data().to_csv('updated-epl-training.csv', index=False)