import pandas as pd
import matplotlib.pyplot as plt
import movie_analysis as mv
import statsmodels.api as sm
import numpy as np

col = ["average_gross", "movie_count", "years_active", "budget", "bin_young_old", ]
log_col = ['log_average',  'log_years',  'log_count',  'log_budget',  "bin_young_old"]


def linear_fit(data, col=col):

    X = sm.add_constant(data[col])
    y = data[col[0]]
    model = sm.OLS(y, X)
    results = model.fit()
    print results.summary()
    return results


def plot_linear_fit(data, col=col):

    X = sm.add_constant(data[col])
    results = linear_fit(data, col)
    plt.plot(X[col], data.log_average, 'bo')
    plt.plot(X[col], results.fittedvalues, 'r')
    plt.show()


def split_data(df):
    df = df.reindex(np.random.permutation(df.index))
    size = int(len(df)*.75)
    train = df[:size]
    test = df[size+1:]
    return [train, test]


def linear_regression_random_train_test(data, col='log_budget'):
    train, test = split_data(data)

    X_train = train[col]
    X_train = sm.add_constant(X_train)
    y_train = train.log_average

    X_test = test[col]
    X_test = sm.add_constant(X_test)
    y_test = test.log_average
    model = sm.OLS(y_train, X_train)
    results = model.fit()

    print results
    return results, X_test, y_test


def plot_random_test_train(data, col='log_budget'):

    results, X_test, y_test = linear_regression_random_train_test(data, col)

    plt.plot(X_test[col], y_test, 'bo')
    plt.plot(X_test[col], results.predict(X_test), 'r')
    plt.show()


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
