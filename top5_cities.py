import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("air_pollution_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Standardize column names
df.rename(columns={
    'city': 'City',
    'City': 'City',
    'aqi': 'AQI',
    'AQI': 'AQI',
    'AQI Value': 'AQI'
}, inplace=True)

# If AQI not present → create it
if "AQI" not in df.columns:
    df["AQI"] = (df["PM2.5"] + df["PM10"]) / 2

# Convert AQI to numeric
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["City", "AQI"])

# Fix scaling issue (if values are like 4.7)
if df["AQI"].max() < 10:
    df["AQI"] = df["AQI"] * 100

# 🔥 Top 5 polluted cities
top5 = df.groupby("City")["AQI"].mean().sort_values(ascending=False).head(5)

print("\nTop 5 Polluted Cities:\n")
print(top5)

# 📈 LINE GRAPH (dotted with markers)
plt.figure()

top5.plot(marker='o', linestyle='--')

plt.title("Top 5 Polluted Cities (Line Graph)")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)

# Show AQI values on graph
for i, v in enumerate(top5):
    plt.text(i, v, str(round(v, 1)), ha='center')

plt.tight_layout()
plt.show()
