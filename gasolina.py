import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_df = pd.read_csv("gasolina.csv", index_col=0, parse_dates=True)
data_df.head(10)

data_df.plot.line()
plt.savefig('gasolina.png', format='png')