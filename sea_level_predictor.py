import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regres = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = list(range(1880, 2050))
    y = [regres.intercept + regres.slope * year for year in x]
    plt.plot(x, y, 'r', label='1st fitted line')

    # Create second line of best fit
    regres_2 = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    new_x = list(range(2000, 2050))
    new_y = [regres_2.intercept + regres_2.slope * new_year for new_year in new_x]
    plt.plot(new_x, new_y, 'g', label='2nd fitted line')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()