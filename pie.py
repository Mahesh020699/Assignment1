# Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining the function
def pie(dataframe, x, y):
    """
    Generate a pie chart from a pandas dataframe.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataframe containing the data to plot.
    x : str
        The name of the column containing the values to plot.
    y : str
        The name of the column containing the labels.

    Returns
    -------
    None
    """
    plt.figure(figsize=(8,8))
    plt.pie(dataframe[x], labels=dataframe[y], autopct='%1.2f%%')
    plt.title('Top 20 companies in the world', fontsize=25)
    plt.savefig('fig2.png')
    plt.show()
    
# Main program
if __name__ == '__main__':
    # Loading and preprocessing the data
    df = pd.read_excel("pietechnology.xlsx", sheet_name="Data")
    df = df[4:]
    df = df.iloc[:, 1:3]
    df.columns = ['Company', 'Market']
    # Ploting pie graph
    names = np.array(df['Company'])
    market = np.array(df['Market'])
    pie(df, 'Market', 'Company')
