# Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining the function
def bar(dataframe, x, y):
    """
    This function creates a bar plot of total deaths per country.

    Parameters:
    dataframe (pandas dataframe): A dataframe containing COVID-19 data.
    x (pandas series): A series of country names.
    y (pandas series): A series of total deaths per country.

    Returns:
    None
    """
    plt.figure(figsize=(15,12))
    plt.bar(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Country')
    plt.ylabel('Total Deaths')
    plt.title('Top 10 Covid deaths')
    plt.savefig("fig3.png")
    plt.show()

# Main program
if __name__ == '__main__':
    # Loading and preprocessing the data
    df = pd.read_excel("barcovid.xlsx")
    latest_date = df['date'].max()
    df_latest = df[df['date'] == latest_date]
    df_deaths = df_latest.groupby('location')['total_deaths'].sum().reset_index()
    df_deaths = df_deaths.sort_values(by='total_deaths', ascending=False)
    df_deaths1 = df_deaths[9:20]
    # Ploting pie graph
    bar(df_deaths1, df_deaths1['location'], df_deaths1['total_deaths'])
