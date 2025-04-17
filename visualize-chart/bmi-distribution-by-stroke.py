import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Remove rows with missing BMI values
df = df.dropna(subset=['bmi'])


bmi_bins = [0, 18.5, 24.9, 29.9, 39.9, 100]
bmi_labels = ['Underweight', 'Normal', 'Overweight', 'Obese', 'Severely Obese']
df['bmi_category'] = pd.cut(df['bmi'], bins=bmi_bins, labels=bmi_labels)


bmi_stroke_rate = df.groupby('bmi_category')['stroke'].mean() * 100

# Plot
bmi_stroke_rate.plot(kind='bar', color='teal')
plt.title('Stroke Rate by BMI Category', loc='center', pad=15, fontsize=14)  # Title styling
plt.xlabel('BMI Category')
plt.ylabel('Stroke Rate (%)')
plt.xticks(rotation=0) 
plt.grid(axis='y')


plt.tight_layout()
plt.savefig('visualize-chart-img/stroke-rate-bmi-category.png')
plt.show()
