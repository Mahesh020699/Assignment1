# Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Defining the function
def line(dataframe, con1, con2, con3, con4, x1, y1):
    """
    Plot a line graph for the given data.

    Parameters:
        dataframe (pandas.DataFrame): The input data.
        con1 (str): The name of the first country to plot.
        con2 (str): The name of the second country to plot.
        con3 (str): The name of the third country to plot.
        con4 (str): The name of the fourth country to plot.
        x1 (str): The label for the x-axis.
        y1 (str): The label for the y-axis.

    Returns:
        None.
    """
    plt.figure(figsize=(10,5))
    plt.plot(dataframe["Year"], dataframe[con1], label=con1)
    plt.plot(dataframe["Year"], dataframe[con2], label=con2)
    plt.plot(dataframe["Year"], dataframe[con3], label=con3)
    plt.plot(dataframe["Year"], dataframe[con4], label=con4)
    plt.xlabel(x1)
    plt.ylabel(y1)
    plt.legend()
    plt.title("Incidence of Malaria per 1000 people")
    
    plt.xticks(np.arange(2000,2021,2.0))
    plt.xlim(2000,2020)
    plt.savefig("fig1.png")
    plt.show()


# Main program
if __name__ == "__main__":
    # Loading and preprocessing the data
    df = pd.read_excel("linemalaria.xls")
    df = df.T
    h = df.iloc[0].values.tolist()
    df.columns = h
    df = df[4:]
    df = df.rename(columns={"Country Name": "Year"})
    # Ploting line graph
    line(df, "Africa Western and Central", "India", "Nigeria", "Angola", 'Year', 'Malaria cases per 1,000 population at risk')
