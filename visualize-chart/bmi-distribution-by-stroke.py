import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Remove rows with missing BMI values
df = df.dropna(subset=['bmi'])

# Create BMI categories
bmi_bins = [0, 18.5, 24.9, 29.9, 39.9, 100]
bmi_labels = ['Underweight', 'Normal', 'Overweight', 'Obese', 'Severely Obese']
df['bmi_category'] = pd.cut(df['bmi'], bins=bmi_bins, labels=bmi_labels)

# Calculate stroke rate by BMI category
bmi_stroke_rate = df.groupby('bmi_category')['stroke'].mean() * 100

# Get sample counts for each BMI category
bmi_counts = df['bmi_category'].value_counts().sort_index()

# Plot
ax = bmi_stroke_rate.plot(kind='bar', color='teal')
plt.title('Stroke Rate by BMI Category', loc='center', pad=15, fontsize=14, fontweight='bold')  # Title styling
plt.xlabel('BMI Category', fontsize=12, labelpad = 10)
plt.ylabel('Stroke Rate (%)', fontsize=12, labelpad = 10)
plt.xticks(rotation=0) 
plt.grid(axis='y')

plt.tight_layout(pad=2.0)

# Set y-axis limit to make room for annotations
plt.ylim(0, bmi_stroke_rate.max() * 1.2)

# Add percentage labels on top of each bar
for i, v in enumerate(bmi_stroke_rate):
    plt.text(i, v + 0.2, f'{v:.2f}%', ha='center', fontsize=9)

plt.savefig('visualize-chart-img/stroke-rate-bmi-category.png')
plt.show()

print(f"Stroke Rate by BMI Category: {bmi_stroke_rate}")
