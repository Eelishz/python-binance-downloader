# python-binance-downloader
Simple utility for downloading data from the binance api and getting pandas DataFrames

## Installing

```console
$ curl https://raw.githubusercontent.com/Eelishz/python-binance-downloader/main/binance_downloader.py -o binance_downloader.py
$ curl https://raw.githubusercontent.com/Eelishz/python-binance-downloader/main/requirements.txt -o requirements.txt
$ pip install -r requirements.txt
```

## Usage

```python
In [1]: from binance_downloader import download

In [2]: df = download('BTCUSDT')

In [3]: df.head()
Out[3]:
                Open      High       Low     Close         Volume
2020-11-04  14023.53  14259.00  13525.00  14144.01   93016.988262
2020-11-05  14144.01  15750.00  14093.56  15590.02  143741.522673
2020-11-06  15590.02  15960.00  15166.00  15579.92  122618.197695
2020-11-07  15579.93  15753.52  14344.22  14818.30  101431.206553
2020-11-08  14818.30  15650.00  14703.88  15475.10   65547.178574
```
