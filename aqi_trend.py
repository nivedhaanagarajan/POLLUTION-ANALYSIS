import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("air_pollution_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Standardize column names
df.rename(columns={
    'city': 'City',
    'date': 'Date',
    'Date': 'Date',
    'datetime': 'Date',
    'Datetime': 'Date',
    'aqi': 'AQI',
    'AQI': 'AQI',
    'AQI Value': 'AQI'
}, inplace=True)

# Convert Date and AQI
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Date", "AQI"])

# Fix scaling
if df["AQI"].max() < 10:
    df["AQI"] = df["AQI"] * 100

# Monthly average
monthly = df.groupby(pd.Grouper(key="Date", freq="M"))["AQI"].mean()

# 🎨 Plot with colors
plt.figure()

monthly.plot(
    marker='o',
    linestyle='-',
    color='red',              # line color
    markerfacecolor='yellow',   # point color
    markeredgecolor='black'
)

plt.title("Monthly AQI Trend (Smoothed)", color='darkblue')
plt.xlabel("Month")
plt.ylabel("AQI")

# Grid for better visibility
plt.grid(True, linestyle='--', alpha=0.6)

# Show values
for i, v in enumerate(monthly):
    plt.text(i, v, str(round(v, 1)), ha='center', fontsize=8)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
