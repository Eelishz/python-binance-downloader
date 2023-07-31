import pandas as pd
from binance import Client
from datetime import datetime
import numpy as np

def download(symbol: str, interval='1d', start_date=None, end_date=None) -> pd.DataFrame:
    client = Client()
    candles = client.get_historical_klines(symbol, interval, start_date, end_date)
    candles = np.asarray(candles)

    df = pd.DataFrame()
    df.index = pd.to_datetime(candles[:, 0].astype('int64'), unit='ms')
    df['Open'] = candles[:, 1].astype('float64')
    df['High'] = candles[:, 2].astype('float64')
    df['Low'] = candles[:, 3].astype('float64')
    df['Close'] = candles[:, 4].astype('float64')
    df['Volume'] = candles[: ,5].astype('float64')

    return df

if __name__ == '__main__':
    df = download('BTCUSDT')
    print(df)
