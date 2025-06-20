import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

# --- 1. Data Setup ---
# Define the specific risks for the SEBN project.
# Probability and Severity values are assigned based on the risk analysis.
# (e.g., High Severity, Low Probability for GDPR).
risks = {
    'Hybrid Delivery': {'severity': 80, 'prob': 80, 'color': '#d73027', 'size': 250},
    'Coordination': {'severity': 60, 'prob': 70, 'color': '#fee08b', 'size': 250},
    'Speaker Budget': {'severity': 50, 'prob': 50, 'color': '#fee08b', 'size': 250},
    'GDPR Compliance': {'severity': 90, 'prob': 20, 'color': '#fee08b', 'size': 250},
    'Speaker Cancellation': {'severity': 95, 'prob': 15, 'color': '#d73027', 'size': 250},
}

# --- 2. Heatmap and Contour Creation ---
# Create a grid of x (severity) and y (probability) values
severity_ax = np.linspace(0, 100, 100)
probability_ax = np.linspace(0, 100, 100)
X, Y = np.meshgrid(severity_ax, probability_ax)

# Calculate the risk score Z for the heatmap background (Severity * Probability)
Z_heatmap = X * Y

# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 10))

# Display the heatmap background using a Green-Yellow-Red colormap.
im = ax.imshow(Z_heatmap, extent=[0, 100, 0, 100], origin='lower',
               cmap='RdYlGn_r', interpolation='bilinear', alpha=0.9)

# Add contour lines for constant risk levels
levels = np.arange(0, 10001, 1000)
contours = ax.contour(X, Y, Z_heatmap, levels=levels, colors='white', linewidths=0.7)
ax.clabel(contours, inline=True, fontsize=10, fmt='%1.0f')

# --- 3. Plotting Risk Points ---
# Iterate through the risk data to plot each point and its label
for label, data in risks.items():
    ax.scatter(data['severity'], data['prob'], color=data['color'], s=data['size'],
               edgecolors='black', zorder=5)
    # Add the text label with a background for better visibility
    ax.text(data['severity'] + 2.5, data['prob'], label, fontsize=12,
            fontweight='bold', color='black',
            bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'))

# --- 4. Styling and Formatting the Plot ---
# Set titles and labels with increased font size
ax.set_title('Risk Heatmap (Probability-Severity Matrix)', fontsize=20, fontweight='bold')
ax.set_xlabel('Severity', fontsize=16, fontweight='bold')
ax.set_ylabel('Probability', fontsize=16, fontweight='bold')

# Format axes to show percentages
ax.xaxis.set_major_formatter(mticker.PercentFormatter())
ax.yaxis.set_major_formatter(mticker.PercentFormatter())

# Set axis tick font size
ax.tick_params(axis='both', which='major', labelsize=12)

# Set axis limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Add a grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

# Make the plot square
ax.set_aspect('equal', adjustable='box')

# Save the figure instead of showing it
plt.tight_layout()
plt.savefig('updated_risk_heatmap.png')
plt.close()