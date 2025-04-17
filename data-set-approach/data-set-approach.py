# %%
import pandas as pd
from IPython.display import Markdown, display


# Load dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')
display(df.head())


# Describe the dataset
display(df.describe().T)



#Null value count
display(Markdown("## Count all null value"))
df.isnull().sum()



    # %%
