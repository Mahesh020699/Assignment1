#Imported the required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Defining the function
def line_plot(dataframe, country1, country2, country3, country4, line_label_x, line_label_y):
    """
    This function plots a line graph for the given data.

    Parameters:
        dataframe : The input data.
        country1 (str): The name of the first country to plot.
        country2 (str): The name of the second country to plot.
        country3 (str): The name of the third country to plot.
        country4 (str): The name of the fourth country to plot.
        pie_label_x (str): The label for the x-axis.
        pie_label_y (str): The label for the y-axis.

    Returns:
        None.
    """
    plt.figure(figsize=(10,5))
    plt.plot(dataframe["Year"], dataframe[country1], label=country1)
    plt.plot(dataframe["Year"], dataframe[country2], label=country2)
    plt.plot(dataframe["Year"], dataframe[country3], label=country3)
    plt.plot(dataframe["Year"], dataframe[country4], label=country4)
    plt.xlabel(line_label_x)
    plt.ylabel(line_label_y)
    plt.legend()
    plt.title("Incidence of Malaria per 1000 people")
    plt.xticks(np.arange(2000,2021,2.0))
    plt.xlim(2000,2020)
    plt.savefig("fig1.png")
    plt.show()


# Main program
if __name__ == "__main__":
    # Loading and preprocessing the data
    malaria_df = pd.read_excel("linemalaria.xls")
    malaria_df = malaria_df.T
    h = malaria_df.iloc[0].values.tolist()
    malaria_df.columns = h
    malaria_df = malaria_df[4:]
    malaria_df = malaria_df.rename(columns={"Country Name": "Year"})
    # Ploting line graph
    line_plot(malaria_df, "Africa Western and Central", "India", "Nigeria", "Angola", 'Year', 'Malaria cases per 1,000 population at risk')

