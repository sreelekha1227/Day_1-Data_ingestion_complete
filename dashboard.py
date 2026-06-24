import pandas as pd
import plotly.express as px

ranking_df = pd.read_csv("data/processed/fund_ranking.csv")

fig = px.bar(
    ranking_df,
    x="Fund",
    y="Average_NAV",
    title="Mutual Fund Average NAV Ranking",
    text="Average_NAV"
)

fig.write_html("reports/dashboard.html")

print("Dashboard Saved Successfully")