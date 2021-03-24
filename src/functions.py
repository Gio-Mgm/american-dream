import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Return the mean of salary with paremeters
def get_mean_salary(param, df):
    return round(df.groupby(param)["SalaryUSD"].mean(), 2)

# Function for creating barplot


def make_barplot(title, series, size=(10, 6)):
    plt.figure(figsize=size)
    plt.title(title)
    return sns.barplot(x=series.index, y=series.values)

# Function for formatting salary on "xK $"

def to_k_usd(x):
    return str(int((x / 1000))) + "K $"
