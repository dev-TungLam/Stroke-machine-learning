import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric (ensuring it's the right type)
df['stroke'] = pd.to_numeric(df['stroke'])

# Calculate the percentage of stroke cases for each residence type
residence_stroke_pct = pd.crosstab(df['Residence_type'], df['stroke'], normalize='index') * 100

# Plot the percentage of stroke cases for each residence type
plt.figure(figsize=(10, 6))
residence_stroke_pct[1].plot(kind='bar', color=['forestgreen', 'darkblue'])

# Add labels and title
plt.xlabel('Residence Type', fontsize=12)
plt.ylabel('Stroke Rate (%)', fontsize=12)
plt.title('Stroke Rate by Residence Type (Urban vs. Rural)', fontsize=16, pad=20)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = residence_stroke_pct[1].max()
plt.ylim(0, max_value * 1.3)  # Extend y-axis to 130% of the maximum value

# Add percentage labels on top of each bar
for i, v in enumerate(residence_stroke_pct[1]):
    plt.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=10)

# Calculate the relative risk
rural_stroke_rate = residence_stroke_pct.loc['Rural', 1]
urban_stroke_rate = residence_stroke_pct.loc['Urban', 1]
relative_risk = rural_stroke_rate / urban_stroke_rate

# Add statistical annotation
plt.annotate(f'Relative Risk (Rural/Urban): {relative_risk:.2f}x', 
             xy=(0.5, 0.85), xycoords='axes fraction',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
             ha='center', fontsize=12)

# Add counts as text below the x-axis
residence_counts = df['Residence_type'].value_counts()
for i, residence in enumerate(residence_stroke_pct.index):
    plt.annotate(f'n={residence_counts[residence]}', xy=(i, -0.05), xytext=(i, -20), 
                 textcoords='offset points', ha='center', va='top')

plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-residence-type.png')
plt.show()

print(f"Relative Risk (Rural/Urban): {relative_risk:.2f}x")
print(f"Stroke Rate - Rural: {rural_stroke_rate:.2f}%")
print(f"Stroke Rate - Urban: {urban_stroke_rate:.2f}%")
