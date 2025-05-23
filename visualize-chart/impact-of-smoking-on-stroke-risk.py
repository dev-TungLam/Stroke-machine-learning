import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Calculate the percentage of stroke cases within each smoking status category
smoking_stroke_pct = pd.crosstab(df['smoking_status'], df['stroke'], normalize='index') * 100

# Create a figure
plt.figure(figsize=(10, 6))

# Plot the percentage of stroke cases for each smoking status
smoking_stroke_pct[1].plot(kind='bar', color='crimson')

# Add labels and title
plt.title('Impact of Smoking on Stroke Risk', fontsize=16, pad=20)  # Add padding to the title
plt.xlabel('Smoking Status', fontsize=12)
plt.ylabel('Stroke Rate (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to make more room
max_value = smoking_stroke_pct[1].max()
plt.ylim(0, max_value * 1.3)

# Add percentage labels on top of each bar
for i, v in enumerate(smoking_stroke_pct[1]):
    plt.text(i, v + (max_value * 0.03), f'{v:.1f}%', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('visualize-chart-img/impact-of-smoking-on-stroke.png')
plt.show()

print(f"Stroke Rate by Smoking Status: {smoking_stroke_pct}")
