import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric (ensuring it's the right type)
df['stroke'] = pd.to_numeric(df['stroke'])

# Define glucose level categories
glucose_bins = [0, 70, 100, 126, 200, 300]
glucose_labels = ['Low (<70)', 'Normal (70-100)', 'Prediabetic (100-126)', 
                 'Diabetic (126-200)', 'High Diabetic (>200)']

df['glucose_category'] = pd.cut(df['avg_glucose_level'], bins=glucose_bins, labels=glucose_labels)

# Calculate stroke rate by glucose category
glucose_stroke_pct = pd.crosstab(df['glucose_category'], df['stroke'], normalize='index') * 100

# Create a figure
plt.figure(figsize=(10, 6))

# Plot the stroke rate by glucose category with a color gradient
bars = plt.bar(range(len(glucose_stroke_pct.index)), glucose_stroke_pct[1], 
        color=plt.cm.YlOrRd(np.linspace(0.3, 0.9, len(glucose_stroke_pct.index))))

# Add labels and title
plt.title('Stroke Risk Increases with Blood Glucose Levels', fontsize=16, pad=20)
plt.xlabel('Glucose Level Category', fontsize=12)
plt.ylabel('Stroke Rate (%)', fontsize=12)
plt.xticks(range(len(glucose_stroke_pct.index)), glucose_labels, rotation=30, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = glucose_stroke_pct[1].max()
plt.ylim(0, max_value * 1.3)

# Add percentage labels on top of each bar
for i, v in enumerate(glucose_stroke_pct[1]):
    plt.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=10)

# Add sample sizes below the x-axis
glucose_counts = df['glucose_category'].value_counts(sort=False)
for i, category in enumerate(glucose_stroke_pct.index):
    plt.annotate(f'n={glucose_counts[category]}', xy=(i, -0.5), xytext=(i, -5), 
                 textcoords='offset points', ha='center', va='top', fontsize=9)

# Add a trend line to emphasize the relationship
x = np.arange(len(glucose_stroke_pct.index))
z = np.polyfit(x, glucose_stroke_pct[1], 1)
p = np.poly1d(z)


# Calculate normal glucose stroke rate for reference
normal_rate = glucose_stroke_pct.loc['Normal (70-100)', 1] if 'Normal (70-100)' in glucose_stroke_pct.index else 0

# Add annotation about risk increase
highest_rate = glucose_stroke_pct[1].max()
risk_increase = highest_rate / normal_rate if normal_rate > 0 else float('inf')
plt.annotate(f"High glucose levels increase stroke risk by {risk_increase:.1f}x\ncompared to normal levels", 
             xy=(0.45, 0.85), xycoords='axes fraction',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
             ha='center', fontsize=11)

plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-by-glucose-category.png')
plt.close()

# Print statistical summary
print("Stroke rate by glucose level category:")
for category in glucose_stroke_pct.index:
    count = glucose_counts[category]
    rate = glucose_stroke_pct.loc[category, 1]
    print(f"{category}: {rate:.2f}% (n={count})")

print("\nOdds ratios compared to normal glucose level:")
for category in glucose_stroke_pct.index:
    if category != 'Normal (70-100)':
        category_rate = glucose_stroke_pct.loc[category, 1]
        odds_ratio = category_rate / normal_rate if normal_rate > 0 else float('inf')
        print(f"{category}: {odds_ratio:.2f}x")