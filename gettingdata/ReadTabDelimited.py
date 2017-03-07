import csv

fileName = "stockprices.txt"


def readDelimited(file):
    with open(file, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            date = row[0]
            ticker = row[1]
            close = float(row[2])
            print ("Date %s Ticker %s Close %f " % (date, ticker, close))


#readDelimited(fileName)


def readDelimitedAsMap(file):
    """
    some help docs
    """
    with open (file, 'rb') as f:
        reader=csv.DictReader(f, delimiter=':')
        for row in reader:
            date=row["date"]
            ticker=row["ticker"]
            close=float(row["close"])
            print ("Date %s Ticker %s Close %f " % (date, ticker, close))

readDelimitedAsMap("stockprices_semicolon.txt")

help (readDelimitedAsMap)