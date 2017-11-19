#   Reading in CSV data
#   Google stock prices for 10 years
#   using import csv
#   Parsing csv with Python
#   Parse date with method datetime.strptime
#   strptime = string parse time
#   first arg is string, 2nd is expected format
#   This file will convert the string datatype in the csv to appropriate floats, doubles, int or w/e
#   Stock return = % change in price
#   Common; daily return is % change from 1 day to the next

import csv
from datetime import datetime

path = "/Users/shan203x/Desktop/SocraticaPython/Google Stock Market Data - google_stock_data.csv.csv"

file = open( path, newline='' )

reader = csv.reader(file)

header = next( reader ) # the first line is the header

#   improve our code by converting
#   data to appropriate types

#   Parsing
data = []
for row in reader:
    # row = [ Date, Open, High, Low, Close, Volume, Adj.Close ]
    date = datetime.strptime( row[0], '%m/%d/%Y' )
    # Float conversion
    open_price = float( row[1] ) # can't use 'open' bc it's a built in func
    high = float( row[2] )
    low = float( row[3] )
    close = float( row[4] )
    volume = int( row[5] )
    adj_close = float( row[6] )

#   Append a list containing these values to our data list
    data.append( [date, open_price, high, low, close, adj_close] )

#   Print first row to see all data are appropriate type
print( data[0] )

#   Compute and store daily stock returns
#   This creates csv file as well - IMPORTANT
returns_path = "/Users/shan203x/Desktop/SocraticaPython/google_returns.csv"
file = open( returns_path, 'w' )
writer = csv.writer(file)
writer.writerow( ["Date", "Return"] )

#   loop to calculate all the returns
#   *Dates are in decreasing order!*
for i in range( len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1] # dates in descending order
    yesterdays_row = data[i + 1]  # dates in descending order
    yesterdays_price = yesterdays_row[-1]

    daily_return = ( todays_price - yesterdays_price ) / yesterdays_price
    # string format time func - to format date
    formatted_date = todays_date.strftime('%m/%d/%Y')

    writer.writerow( [formatted_date, daily_return] )
    
#   we stop at the 2nd to last row
#   bc for the first day, there is no prev day return to compare to
#   use index 'i' to get today's data
