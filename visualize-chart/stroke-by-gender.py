import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

stroke_counts = df.groupby('gender')['stroke'].sum()

stroke_counts.plot(kind='bar', color=['crimson', 'SlateBlue'])
plt.xlabel('Gender')
plt.ylabel('Number of Strokes')
plt.title('Number of Strokes by Gender')
plt.xticks(ticks=[0, 1], labels=['Female', 'Male'], rotation=0)
plt.grid(axis='y')
plt.show()

plt.savefig('visualize-chart-img/stroke-by-gender.png')

plt.show()