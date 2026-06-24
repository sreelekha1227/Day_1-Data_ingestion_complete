import requests
import pandas as pd
import os

funds = {
    "SBI_Bluechip": 119551,
    "Axis_Bluechip": 120503,
    "HDFC_Top100": 119063,
    "ICICI_Bluechip": 120586,
    "Kotak_Bluechip": 120828
}

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{fund_name}.csv"

    df.to_csv(file_name, index=False)

    print(f"{fund_name} Saved Successfully")

print("All Funds Downloaded")