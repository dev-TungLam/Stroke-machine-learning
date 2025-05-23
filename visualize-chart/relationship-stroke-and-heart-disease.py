import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric
df['stroke'] = pd.to_numeric(df['stroke'])

# Calculate stroke rate by heart disease status
stroke_rate = df.groupby('heart_disease')['stroke'].mean() * 100 

# Plot the stroke rate
stroke_rate.plot(kind='bar', color=['SlateBlue', 'crimson'])

# Add labels and formatting
plt.xlabel('Heart Disease', fontsize=14, fontname="Sans", labelpad=10)
plt.ylabel('Stroke Rate (%)', fontsize=14, fontname="Sans", labelpad=10)
plt.title('Stroke Rate in Individuals with vs without Heart Disease', fontsize=10, fontweight='bold', fontname='Sans')
plt.xticks(ticks=[0, 1], labels=['No Heart Disease', 'Heart Disease'], rotation=0)
plt.ylim(0, stroke_rate.max() + 5)
plt.grid(axis='y')

# Get counts for each heart disease category
heart_disease_counts = df['heart_disease'].value_counts()

# Add annotations for sample sizes
plt.annotate(f'n={heart_disease_counts[0]}', xy=(0, -0.05), xytext=(0, -20),
             textcoords='offset points', ha='center', va='top')
plt.annotate(f'n={heart_disease_counts[1]}', xy=(1, -0.05), xytext=(1, -20),
             textcoords='offset points', ha='center', va='top')


# Add values on top of bars
for i, v in enumerate(stroke_rate):
    plt.text(i, v + 0.5, f'{v:.2f}%', ha='center')

plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-heart-disease.png')
plt.show()

print(f"Stroke Rate in Individuals with Heart Disease: {stroke_rate[1]:.2f}%")
print(f"Stroke Rate in Individuals without Heart Disease: {stroke_rate[0]:.2f}%")
