import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
import matplotlib.patches as patches

# Create a precision-recall visualization
plt.figure(figsize=(8, 6))

# Define the coordinate system
x_min, x_max = 0, 1
y_min, y_max = 0, 1

# Plot F1 curves using quadratic Bezier curves to match the SVG style
f1_values = [0.2, 0.4, 0.8]
colors = ['#ea4335', '#fbbc05', '#34a853']  # Red, Yellow, Green
y_positions = [0.2, 0.4, 0.8]  # Positions where curves reach the right edge

for f1, color, y_pos in zip(f1_values, colors, y_positions):
    # Create a quadratic Bezier curve
    verts = [
        (0.0, 0.0),  # Start at origin
        (0.5, y_pos),  # Control point
        (1.0, y_pos),  # End point
    ]
    
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3,
    ]
    
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor=color, linestyle='--', alpha=0.7)
    plt.gca().add_patch(patch)
    
    # Add F1 score label
    plt.text(0.25, y_pos/2, f'F1={f1}', fontsize=10, color=color)

# Plot model points
plt.scatter(0.10, 0.14, s=100, color='#4285f4', alpha=0.7, label='XGBoost') 
plt.scatter(0.81, 0.17, s=100, color='#ea4335', alpha=0.7, label='Logistic Regression')
plt.scatter(1.0, 1.0, s=50, color='#34a853', alpha=0.7, label='Ideal Model')

# Add labels and formatting
plt.xlabel('Recall (Sensitivity)')
plt.ylabel('Precision')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.legend()
plt.title('Precision-Recall Trade-off Between Models')

# Save the figure
plt.savefig('visualize-chart-img/precision-recall-tradeoff.png', dpi=300, bbox_inches='tight')
plt.close()
