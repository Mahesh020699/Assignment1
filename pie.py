# Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining the function
def generate_pie_chart(dataframe, values_col, labels_col):
    """
    This function produces a pie plot for top 20 companies

    Parameters
    ----------
    dataframe :
        The dataframe containing the data to plot.
    values_col : str
        The column's name containing the values to plot.
    labels_col : str
        The column's name containing the labels.

    Returns
    -------
    None
    """
    plt.figure(figsize=(8,8))
    plt.pie(dataframe[values_col], labels=dataframe[labels_col], autopct='%1.2f%%')
    plt.title('Top 20 companies in the world', fontsize=25)
    plt.savefig('fig2.png')
    plt.show()
    
# Main program
if __name__ == '__main__':
    # Loading and preprocessing the data
    techno_df1 = pd.read_excel("pietechnology.xlsx", sheet_name="Data")
    techno_df1 = techno_df1[4:]
    techno_df1 = techno_df1.iloc[:, 1:3]
    techno_df1.columns = ['Company', 'Market']
    # Ploting pie graph
    company_names = np.array(techno_df1['Company'])
    market_share = np.array(techno_df1['Market'])
    generate_pie_chart(techno_df1, 'Market', 'Company')
