import pandas as pd
import matplotlib.pyplot as plt
import movie_analysis as mv


def show_hist(data):
    pd.DataFrame.hist(data)


def show_scatter(data, col):

    if col:
        pd.scatter_matrix(data, figsize=(10, 10))
    else:
        pd.scatter_matrix(data, figsize=(10, 10))


def main():
    data_dir, data_act = mv.get_data()
    data_dir = mv.create_dataframe(data_dir)
    data_act = mv.create_dataframe(data_act)


if __name__ == '__main__':
    main()
