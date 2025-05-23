import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

plt.figure(figsize=(10, 6))
sns.kdeplot(data=df[df['stroke'] == 1], x='age', label='Stroke', shade=True)
sns.kdeplot(data=df[df['stroke'] == 0], x='age', label='No Stroke', shade=True)
plt.title('Age Distribution by Stroke Occurrence', fontsize=18, fontweight='bold', fontname='Sans')
plt.xlabel('Age', fontsize=20, fontname="Sans", labelpad=10)
plt.ylabel('Density', fontsize=20, fontname="Sans", labelpad=10)
plt.legend()

plt.tight_layout(pad=2.0) 

plt.savefig('visualize-chart-img/age-distribution-by-stroke.png')

plt.show()
print(f"Age distribution by stroke occurrence: {df['age'].describe()}")
print
