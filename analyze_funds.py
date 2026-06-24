import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/SBI_Bluechip.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True)

df["nav"] = pd.to_numeric(df["nav"])

df = df.sort_values("date")

plt.figure(figsize=(12,6))

plt.plot(df["date"], df["nav"])

plt.title("SBI Bluechip Fund NAV Trend")

plt.xlabel("Date")

plt.ylabel("NAV")

plt.grid()

plt.savefig("reports/nav_trend.png")

print("Graph Saved Successfully")