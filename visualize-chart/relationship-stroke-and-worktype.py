import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Calculate the percentage of stroke cases within each work type category
work_stroke_pct = pd.crosstab(df['work_type'], df['stroke'], normalize='index') * 100

plt.figure(figsize=(10, 6))
work_stroke_pct[1].plot(kind='bar', color='SlateBlue')

plt.xlabel('Work Type', fontsize=12)
plt.ylabel('Stroke Rate (%)', fontsize=12)
plt.title('Stroke Rate by Work Type', fontsize=16, pad=20)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = work_stroke_pct[1].max()
plt.ylim(0, max_value * 1.3)  # Extend y-axis to 130% of the maximum value

# Add percentage labels on top of each bar
for i, v in enumerate(work_stroke_pct[1]):
    plt.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('visualize-chart-img/relationship-stroke-and-worktype.png')
plt.show()

# Print useful statistical information
print("\n--- Statistical Information on Work Type and Stroke ---")

# 1. Count of people in each work type category
work_type_counts = df['work_type'].value_counts()
print("\nCount by work type:")
print(work_type_counts)

# 2. Stroke rate by work type
print("\nStroke rate by work type (%):")
print(work_stroke_pct[1])

# 3. Average age by work type
avg_age_by_work = df.groupby('work_type')['age'].mean()
print("\nAverage age by work type:")
print(avg_age_by_work)

# 4. Stroke count by work type
stroke_counts = df.groupby('work_type')['stroke'].sum()
print("\nNumber of strokes by work type:")
print(stroke_counts)
