import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Convert 'stroke' to numeric (ensuring it's the right type)
df['stroke'] = pd.to_numeric(df['stroke'])

# Create more evenly distributed age groups with proper ordering
age_bins = [0, 20, 40, 60, 82]
age_labels = ['0-20', '21-40', '41-60', '61-82']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First subplot: Stroke rate by marital status
marital_stroke_pct = pd.crosstab(df['ever_married'], df['stroke'], normalize='index') * 100
marital_stroke_pct[1].plot(kind='bar', color=['SlateBlue', 'crimson'], ax=ax1)

# Add labels and title
ax1.set_xlabel('Marital Status', fontsize=12)
ax1.set_ylabel('Stroke Rate (%)', fontsize=12)
ax1.set_title('Stroke Rate by Marital Status', fontsize=14)
ax1.set_xticklabels(['Never Married', 'Ever Married'], rotation=0)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = marital_stroke_pct[1].max()
ax1.set_ylim(0, max_value * 1.3)

# Add percentage labels on top of each bar
for i, v in enumerate(marital_stroke_pct[1]):
    ax1.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=14)

# Add counts as text below the x-axis
marital_counts = df['ever_married'].value_counts()
for i, status in enumerate(['No', 'Yes']):
    ax1.annotate(f'n={marital_counts[status]}', xy=(i, -0.05), xytext=(i, -20), 
                 textcoords='offset points', ha='center', va='top')

# Add average age annotation
avg_age_by_marital = df.groupby('ever_married')['age'].mean()
ax1.annotate(f'Avg age (Never Married): {avg_age_by_marital["No"]:.1f} years\nAvg age (Ever Married): {avg_age_by_marital["Yes"]:.1f} years', 
             xy=(0.5, 0.85), xycoords='axes fraction',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
             ha='center', fontsize=10)

# Second subplot: Stroke rate by marital status, stratified by age group
# Calculate stroke rates by marital status within each age group
age_marital_stroke = pd.crosstab([df['age_group'], df['ever_married']], df['stroke'], normalize='index') * 100

# Prepare data for grouped bar chart
age_groups = age_labels  # Use our predefined labels to ensure correct order
x = np.arange(len(age_groups))
width = 0.35

# Plot bars for never married
never_married_rates = []
for age in age_groups:
    if (age, 'No') in age_marital_stroke.index and 1 in age_marital_stroke.loc[(age, 'No')]:
        never_married_rates.append(age_marital_stroke.loc[(age, 'No'), 1])
    else:
        never_married_rates.append(0)

rects1 = ax2.bar(x - width/2, never_married_rates, width, label='Never Married', color='SlateBlue')

# Plot bars for ever married
ever_married_rates = []
for age in age_groups:
    if (age, 'Yes') in age_marital_stroke.index and 1 in age_marital_stroke.loc[(age, 'Yes')]:
        ever_married_rates.append(age_marital_stroke.loc[(age, 'Yes'), 1])
    else:
        ever_married_rates.append(0)

rects2 = ax2.bar(x + width/2, ever_married_rates, width, label='Ever Married', color='crimson')

# Add labels and title
ax2.set_xlabel('Age Group', fontsize=12, labelpad=15)
ax2.set_ylabel('Stroke Rate (%)', fontsize=12)
ax2.set_title('Stroke Rate by Marital Status and Age Group', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(age_groups, fontsize = 12)
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Add percentage labels on top of each bar
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:  # Only add label if there's a value
            ax2.annotate(f'{height:.1f}%',
                        xy=(rect.get_x() + rect.get_width()/2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=9)

add_labels(rects1)
add_labels(rects2)

# Add sample sizes below each bar
age_marital_counts = df.groupby(['age_group', 'ever_married']).size()
for i, age in enumerate(age_groups):
    for j, married in enumerate(['No', 'Yes']):
        if (age, married) in age_marital_counts.index:
            count = age_marital_counts[(age, married)]
            x_pos = i + (j*2-1)*width/2
            ax2.annotate(f'n={count}', xy=(x_pos, 0), xytext=(0, -15), 
                        textcoords='offset points', ha='center', va='top', fontsize=8)

plt.tight_layout(pad=4.0)
plt.savefig('visualize-chart-img/stroke-rate-marital-status-with-age.png')
plt.close()

# Save the age-stratified chart separately for clarity
plt.figure(figsize=(10, 6))
x = np.arange(len(age_groups))
width = 0.35

rects1 = plt.bar(x - width/2, never_married_rates, width, label='Never Married', color='SlateBlue')
rects2 = plt.bar(x + width/2, ever_married_rates, width, label='Ever Married', color='crimson')

plt.xlabel('Age Group', fontsize=16, labelpad=25)
plt.ylabel('Stroke Rate (%)', fontsize=16, labelpad=25)
plt.title('Stroke Rate by Marital Status and Age Group', fontsize=16)
plt.xticks(x, age_groups, fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Function to add labels on top of bars
def add_labels_plt(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:  # Only add label if there's a value
            plt.annotate(f'{height:.1f}%',
                        xy=(rect.get_x() + rect.get_width()/2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=9)

add_labels_plt(rects1)
add_labels_plt(rects2)

# Add sample sizes below each bar
for i, age in enumerate(age_groups):
    for j, married in enumerate(['No', 'Yes']):
        if (age, married) in age_marital_counts.index:
            count = age_marital_counts[(age, married)]
            x_pos = i + (j*2-1)*width/2
            plt.annotate(f'n={count}', xy=(x_pos, 0), xytext=(0, -25), 
                        textcoords='offset points', ha='center', va='top', fontsize=10)

plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-by-age-and-marital-status.png')
plt.close()

# Print statistical analysis
print(f"Average age by marital status:")
print(avg_age_by_marital)

print("\nStroke rate by marital status:")
print(marital_stroke_pct[1])

print("\nStroke rate by marital status and age group:")
print(age_marital_stroke[1])
