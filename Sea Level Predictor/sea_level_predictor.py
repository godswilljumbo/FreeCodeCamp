import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    daf = pd.read_csv("epa-sea-level.csv").rename(
        columns={
            "CSIRO Adjusted Sea Level": "sea",
            "Year": "year"
        }
    )

    # Create scatter plot
    plt.figure(1, figsize=(20, 10))
    plt.scatter(daf.year, daf.sea)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(daf.year, daf.sea)
    x_values = pd.Series(range(1880, 2051))
    y_values = slope * x_values + intercept 
    plt.plot(x_values, y_values, 'r')

    # Create second line of best fit
    df_recent = daf[daf.year >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(daf.year, daf.sea)
    x_values_recent = pd.Series(range(2000, 2051))
    y_values_recent = slope_recent * x_values_recent + intercept_recent 
    plt.plot(x_values_recent, y_values_recent, 'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()