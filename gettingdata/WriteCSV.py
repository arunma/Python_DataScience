import csv

today_prices={'AAPL':90.81, 'FB':91.0, "GOOGL": 81.28}

def writeToFile(file):
    with open (file, 'wb') as f:
        writer=csv.writer(f, delimiter=',')
        for ticker, close in today_prices.items():
            writer.writerow([ticker, close])


writeToFile("writtenstockprices.txt")
print ("Written to file")