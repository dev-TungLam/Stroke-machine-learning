import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='smoking_status', hue='stroke')
plt.title('Impact of Smoking on Stroke Risk')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.legend(title='Stroke Status', loc='upper right')


plt.savefig('visualize-chart-img/impact-of-smoking-on-stroke.png')

plt.show()