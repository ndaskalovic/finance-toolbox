import json
import requests
from fredapi import Fred  # https://mortada.net/python-api-for-fred.html
import pandas as pd
import os

BLS_API_KEY = os.environ.get("BLS_API_KEY")
# https://data.bls.gov/PDQWeb/jt (jolts)
# https://data.bls.gov/PDQWeb/ci (eci)
# https://www.bls.gov/data/

FRED_API_KEY = os.environ.get("FRED_API_KEY")
BLS_ENDPOINT = os.environ.get("BLS_ENDPOINT")


fred = Fred(api_key=FRED_API_KEY)


def format_bls_data(df):
    if df.period.str.contains('Q').sum() > 0:
        df['period'] = ((df.period.str.replace('Q', '').astype(int)
                        - 1) * 3 + 1).astype(str)  # handle quarterly data
    df['date'] = pd.to_datetime(
        df.year + '/' + df.period.str.replace('M|Q', '') + '/01')
    df['value'] = df['value'].astype(float)
    df = df.set_index('date').value.sort_index()
    return df


def scrape_bls(series_id, start_year=2004, end_year=2023):
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": [series_id],
                       "startyear": str(start_year),
                       "endyear": str(end_year),
                       "registrationkey": BLS_API_KEY})
    p = requests.post(BLS_ENDPOINT, data=data, headers=headers)
    json_data = json.loads(p.text)
    df = pd.DataFrame(json_data['Results']['series'][0]['data'])
    return format_bls_data(df)
