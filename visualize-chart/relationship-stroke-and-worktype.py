import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')
plt.figure(figsize=(10, 6))
stroke_counts = df.groupby('work_type')['stroke'].sum()
stroke_counts.plot(kind='bar', color='SlateBlue')
plt.xlabel('Work Type')
plt.ylabel('Number of Strokes')
plt.title('Number of Strokes by Work Type')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()


plt.savefig('visualize-chart-img/relationship-stroke-and-worktype.png')

plt.show()