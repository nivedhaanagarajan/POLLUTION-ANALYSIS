import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("air_pollution_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# 🔍 Detect pollutant columns automatically
pollutants = [col for col in df.columns if "pm" in col.lower() or "no" in col.lower()]

# Convert to numeric
for col in pollutants:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=pollutants)

# Calculate average
avg = df[pollutants].mean()

print("\nAverage Pollutants:\n", avg)

# 🎨 Vibrant colors
colors = ['#FF5733', '#33FF57', '#3380FF', '#FF33A8', '#FFD700', '#00FFFF']

# Plot
plt.figure()

avg.plot(
    kind="bar",
    color=colors[:len(avg)],  # match number of pollutants
    edgecolor='black'
)

plt.title("Average Pollutant Levels", fontsize=14, color='purple')
plt.xlabel("Pollutants")
plt.ylabel("Concentration")

# Add grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show values on bars
for i, v in enumerate(avg):
    plt.text(i, v, str(round(v, 1)), ha='center', fontsize=10, fontweight='bold')

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
