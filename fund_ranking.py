import pandas as pd

funds = [
    "SBI_Bluechip",
    "Axis_Bluechip",
    "HDFC_Top100",
    "ICICI_Bluechip",
    "Kotak_Bluechip"
]

results = []

for fund in funds:
    try:
        df = pd.read_csv(f"data/raw/{fund}.csv")

        df["nav"] = pd.to_numeric(df["nav"])

        latest_nav = df["nav"].iloc[0]
        highest_nav = df["nav"].max()
        lowest_nav = df["nav"].min()
        average_nav = df["nav"].mean()

        results.append([
            fund,
            latest_nav,
            highest_nav,
            lowest_nav,
            average_nav
        ])

    except Exception as e:
        print(f"Error in {fund}: {e}")

ranking_df = pd.DataFrame(
    results,
    columns=[
        "Fund",
        "Latest_NAV",
        "Highest_NAV",
        "Lowest_NAV",
        "Average_NAV"
    ]
)

ranking_df = ranking_df.sort_values(
    by="Average_NAV",
    ascending=False
)

print("\n===== FUND RANKING =====\n")
print(ranking_df)

ranking_df.to_csv(
    "data/processed/fund_ranking.csv",
    index=False
)

print("\nFund Ranking Saved Successfully!")