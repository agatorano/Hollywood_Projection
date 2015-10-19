import pandas as pd
#import seaborn as sns
#from patsy import dmatrices
#import statsmodels.api as sm
import movie_analysis as mv


def show_hist(data):
    pd.DataFrame.hist(data)


def main():
    data_dir, data_act = mv.get_data()
    data_dir = mv.create_dataframe(data_dir)
    data_act = mv.create_dataframe(data_act)


if __name__ == '__main__':
    main()
