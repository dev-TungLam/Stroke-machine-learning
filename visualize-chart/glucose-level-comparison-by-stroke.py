import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric (ensuring it's the right type)
df['stroke'] = pd.to_numeric(df['stroke'])

# Calculate mean glucose levels for each group
stroke_glucose = df[df['stroke'] == 1]['avg_glucose_level']
no_stroke_glucose = df[df['stroke'] == 0]['avg_glucose_level']

mean_stroke = stroke_glucose.mean()
mean_no_stroke = no_stroke_glucose.mean()
values = [mean_no_stroke, mean_stroke]

# Create a simple bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(['No Stroke', 'Stroke'], values, color=['SlateBlue', 'crimson'], width=0.6)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{height:.1f} mg/dL', ha='center', va='bottom', fontsize=12)

# Add labels and title
plt.title('Average Blood Glucose Level by Stroke Status', fontsize=16)
plt.ylabel('Average Glucose Level (mg/dL)', fontsize=12)
plt.ylim(0, max(values) * 1.2)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Calculate and show the percentage increase
pct_increase = ((mean_stroke - mean_no_stroke) / mean_no_stroke) * 100
plt.annotate(f"Stroke patients have {pct_increase:.1f}% higher\naverage glucose levels", 
             xy=(0.5, 0.8), xycoords='axes fraction',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
             ha='center', fontsize=12)

# Add statistical significance information
t_stat, p_value = ttest_ind(stroke_glucose, no_stroke_glucose, equal_var=False)
significance = "statistically significant" if p_value < 0.05 else "not statistically significant"

# Add sample sizes
plt.annotate(f"n={len(no_stroke_glucose)}", xy=(0, -0.05), xytext=(0, -20), 
             textcoords='offset points', ha='center', va='top')
plt.annotate(f"n={len(stroke_glucose)}", xy=(1, -0.05), xytext=(1, -20), 
             textcoords='offset points', ha='center', va='top')

plt.tight_layout()
plt.savefig('visualize-chart-img/glucose-level-by-stroke-status.png')
plt.close()

print(f"The average glucose level for stroke patients is {mean_stroke:.1f} mg/dL, which is {pct_increase:.1f}% higher than the average for non-stroke patients ({mean_no_stroke:.1f} mg/dL).")
print(f"The difference in glucose levels between stroke and non-stroke patients is statistically {significance} (p-value: {p_value:.4f}).")

