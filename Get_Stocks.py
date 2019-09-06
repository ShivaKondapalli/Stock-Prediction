import argparse
import pandas_datareader.data as web
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("startdate", help="The Start Date - format YYYY-MM-DD",
                    type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
parser.add_argument("enddate",
    help="The End Date format YYYY-MM-DD (Inclusive)",
    type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))
args = parser.parse_args()


# get "AAPL" stock form yahoo finance
df = web.DataReader('AAPL', 'yahoo', args.startdate, args.enddate)

df.to_csv("data/stock_date.csv")
