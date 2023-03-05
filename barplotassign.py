# Necessary modules were imported 
import pandas as pd
import matplotlib.pyplot as plt

# Defining the function
def bar_plot(dataframe, x, y):
    """
    This function creates a bar plot of total deaths per country.

    Parameters:
    dataframe : A dataframe containing COVID-19 data.
    x : A series of country names.
    y : A series of total deaths per country.

    Returns:
    None
    """
    plt.figure(figsize=(15,12))
    plt.bar(x, y)
    plt.title('Top 10 Covid deaths', fontsize=25)
    plt.xticks(rotation=45)
    plt.xlabel('Country')
    plt.ylabel('Total Deaths')
    plt.savefig("fig3.png")
    plt.show()

# Main program
if __name__ == '__main__':
    # Loading and preprocessing the data
    df1 = pd.read_excel("barcovid.xlsx")
    new_date = df1['date'].max()
    df_new = df1[df1['date'] == new_date]
    df_deaths = df_new.groupby('location')['total_deaths'].sum().reset_index()
    df_deaths = df_deaths.sort_values(by='total_deaths', ascending=False)
    df_deaths1 = df_deaths[9:20]
    # Ploting pie graph
    bar_plot(df_deaths1, df_deaths1['location'], df_deaths1['total_deaths'])
