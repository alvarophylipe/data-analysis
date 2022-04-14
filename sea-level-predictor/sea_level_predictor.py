import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x = 'Year', y = 'CSIRO Adjusted Sea Level', data = df)

    # Create first line of best fit
    res = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.intercept + res.slope*(x_pred)
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    df_2 = df[df['Year'] >= 2000]
    res2 = linregress(x = df_2['Year'], y = df_2['CSIRO Adjusted Sea Level'])
    x_pred_2 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2 = res2.intercept + res2.slope*(x_pred_2)
    plt.plot(x_pred_2, y_pred_2, 'y')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()