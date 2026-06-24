import pandas as pd
import matplotlib.pyplot as plt

funds = [
    "SBI_Bluechip",
    "Axis_Bluechip",
    "HDFC_Top100",
    "ICICI_Bluechip",
    "Kotak_Bluechip"
]

plt.figure(figsize=(12,6))

for fund in funds:
    df = pd.read_csv(f"data/raw/{fund}.csv")

    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df["nav"] = pd.to_numeric(df["nav"])

    df = df.sort_values("date")

    plt.plot(df["date"], df["nav"], label=fund)

plt.title("Mutual Fund NAV Comparison")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.legend()

plt.grid()

plt.savefig("reports/fund_comparison.png")

print("Fund Comparison Graph Saved")