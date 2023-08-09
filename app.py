import requests
import pandas as pd

api_key = '64d3556704d662.16437540'

def get_upcoming_earnings(start_report_date, end_report_date,currency, api_key, n_limit):

    url =  f'https://eodhistoricaldata.com/api/calendar/earnings?api_token={api_key}&fmt=json&from={start_report_date}&to={end_report_date}'
    u_earnings =  requests.get(url).json()

    u_earnings_df = pd.DataFrame(u_earnings['earnings']).drop('before_after_market', axis = 1).fillna(0)
    u_earnings_df = u_earnings_df[u_earnings_df.currency == f'{currency}']
    u_earnings_df = u_earnings_df[u_earnings_df.actual != 0]
    u_earnings_df = u_earnings_df.rename(columns={'code':'stock'})
    u_earnings_df = u_earnings_df.iloc[-n_limit:]
    u_earnings_df.index = range(len(u_earnings_df))

    return u_earnings_df

us_stocks_u_earnings =  get_upcoming_earnings('2021-11-23', '2021-11-26', 'USD', api_key, 10)
us_stocks_u_earnings