import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric (ensuring it's the right type)
df['stroke'] = pd.to_numeric(df['stroke'])

# Calculate the percentage of stroke cases for each hypertension status
hypertension_stroke_pct = pd.crosstab(df['hypertension'], df['stroke'], normalize='index') * 100

# Plot the percentage of stroke cases for each hypertension status
plt.figure(figsize=(10, 6))
hypertension_stroke_pct[1].plot(kind='bar', color=['SlateBlue', 'crimson'])

# Add labels and title
plt.xlabel('Hypertension', fontsize=12)
plt.ylabel('Stroke Rate (%)', fontsize=12)
plt.title('Stroke Rate in Individuals with vs without Hypertension', fontsize=16, pad=20)
plt.xticks(ticks=[0, 1], labels=['No Hypertension', 'Hypertension'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = hypertension_stroke_pct[1].max()
plt.ylim(0, max_value * 1.3)  # Extend y-axis to 130% of the maximum value

# Add percentage labels on top of each bar
for i, v in enumerate(hypertension_stroke_pct[1]):
    plt.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=10)

# Calculate the relative risk
no_hypertension_stroke_rate = hypertension_stroke_pct.loc[0, 1]
hypertension_stroke_rate = hypertension_stroke_pct.loc[1, 1]
relative_risk = hypertension_stroke_rate / no_hypertension_stroke_rate

# Add statistical annotation
plt.annotate(f'Relative Risk: {relative_risk:.2f}x', 
             xy=(0.5, 0.85), xycoords='axes fraction',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
             ha='center', fontsize=12)

# Add counts as text below the x-axis
hypertension_counts = df['hypertension'].value_counts()
plt.annotate(f'n={hypertension_counts[0]}', xy=(0, -0.05), xytext=(0, -20), 
             textcoords='offset points', ha='center', va='top')
plt.annotate(f'n={hypertension_counts[1]}', xy=(1, -0.05), xytext=(1, -20), 
             textcoords='offset points', ha='center', va='top')

plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-hypertension.png')
plt.show()

# Additional statistical analysis
print(f"Stroke rate in patients without hypertension: {no_hypertension_stroke_rate:.2f}%")
print(f"Stroke rate in patients with hypertension: {hypertension_stroke_rate:.2f}%")
print(f"Relative risk of stroke with hypertension: {relative_risk:.2f}x")
