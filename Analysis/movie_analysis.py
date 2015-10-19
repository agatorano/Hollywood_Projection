import json
import pandas as pd
import numpy as np
import seaborn as sns
from patsy import dmatrices
import statsmodels.api as sm


def get_data():
    with open('directors.json') as data_file:
        data_dir = json.load(data_file)
    with open('actors.json') as data_file:
        data_act = json.load(data_file)
    return data_dir, data_act


def create_dataframe(data_in):

    data_p = [(x['average_gross'], x['movie_count'], x['years_active'], x['budgets']) for x in data_in]

    data = pd.DataFrame.from_records(data_p)

    col = ["average_gross", "movie_count", "years_active", "budget", "bin_young_old"]
    data.columns = col[0:4]
    data[col[0:4]] = data[col[0:4]].astype(int)

    data = handle_log_columns(data)
    data = create_young_old_bin(data)

    return data


def handle_log_columns(data):

    log_col = ['log_average',  'log_years',  'log_count',  'log_budget']

    data[log_col[0]] = np.log(data.average_gross)
    data[log_col[1]] = np.log(data.movie_count)
    data[log_col[2]] = np.log(data.years_active)
    data[log_col[3]] = np.log(data.budget)

    return data


def create_young_old_bin(data):

    f = lambda x: 1 if x > 13 else 0
    data['bin_young_old'] = data.applymap(f).years_active

    return data


def main():
    data_dir, data_act = get_data()
    data_dir = create_dataframe(data_dir)
    data_act = create_dataframe(data_act)


if __name__ == '__main__':
    main()
