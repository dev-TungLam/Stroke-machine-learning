import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Calculate the percentage of stroke cases within each gender
gender_stroke_pct = pd.crosstab(df['gender'], df['stroke'], normalize='index') * 100

# Plot the percentage of stroke cases for each gender
gender_stroke_pct[1].plot(kind='bar', color=['crimson', 'SlateBlue'])

plt.xlabel('Gender', fontsize=12)
plt.ylabel('Stroke Rate (%)', fontsize=12)
plt.title('Stroke Rate by Gender', fontsize=16, pad=20)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = gender_stroke_pct[1].max()
plt.ylim(0, max_value * 1.3)  # Extend y-axis to 130% of the maximum value

# Add percentage labels on top of each bar
for i, v in enumerate(gender_stroke_pct[1]):
    plt.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-by-gender.png')
plt.show()

print(f"Stroke rate by gender: {gender_stroke_pct[1]}")