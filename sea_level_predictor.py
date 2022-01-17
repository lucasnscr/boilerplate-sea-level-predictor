import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col='Year')
    # Create scatter plot
    plt.scatter(df.index, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin = linregress(x=df.index, y=df['CSIRO Adjusted Sea Level'])
    fit_2050 = pd.Series([int(i) for i in range(df.index.min(), 2051)])
    plt.plot(fit_2050, lin.intercept + lin.slope * fit_2050)

    # Create second line of best fit
    mask = df.index >= 2000
    # ! x and y have shapes diff????
    # x = np.array(df.index[mask])
    # y = np.array(df['CSIRO Adjusted Sea Level'][mask])
    # print(x, y)
    lin2000 = linregress(x=df.index[mask], y=df['CSIRO Adjusted Sea Level'][mask])
    fit_2000 = pd.Series([int(i) for i in range(2000, 2051)])

    plt.plot(fit_2000, lin2000.intercept + lin2000.slope * fit_2000)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
