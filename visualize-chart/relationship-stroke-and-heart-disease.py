import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric
df['stroke'] = pd.to_numeric(df['stroke'])


stroke_rate = df.groupby('heart_disease')['stroke'].mean() * 100 

stroke_rate.plot(kind='bar', color=['SlateBlue', 'crimson'])


plt.xlabel('Heart Disease')
plt.ylabel('Stroke Rate (%)')
plt.title('Stroke Rate in Individuals with vs without Heart Disease')
plt.xticks(ticks=[0, 1], labels=['No Heart Disease', 'Heart Disease'], rotation=0)
plt.ylim(0, stroke_rate.max() + 5)
plt.grid(axis='y')


plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-heart-disease.png')
plt.show()
