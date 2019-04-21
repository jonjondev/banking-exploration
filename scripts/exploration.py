import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def correlation_matrix(df):

    # Remove the row id from the data frame
    df = df.drop('row id', 1)

    # Set up the matrix plot
    f, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax)

    # Display the matrix
    plt.show()
