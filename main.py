import csv
from statzcw.stats import zcount, zmean, zmode, zmedian, zvariance, zstddev, zstderr, zcorr


def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data

datasets = ['dataZero.csv', 'dataOne.csv', 'dataTwo.csv', 'dataThree.csv']
data = readDataSets([f'{dataset}' for dataset in datasets])

for dataset in datasets:
    x, y = data[f'{dataset}']
    print(f"From {dataset}:")
    print(f"Count of X: {zcount(x)}")
    print(f"Count of Y: {zcount(y)}")
    print(f"Mean of X: {zmean(x)}")
    print(f"Mean of Y: {zmean(y)}")
    print(f"Median of X: {zmedian(x)}")
    print(f"Median of Y: {zmedian(y)}")
    print(f"Mode of X: {zmode(x)}")
    print(f"Mode of Y: {zmode(y)}")
    print(f"Variance of X: {zvariance(x)}")
    print(f"Variance of Y: {zvariance(y)}")
    print(f"Standard Deviation of X: {zstddev(x)}")
    print(f"Standard Deviation of Y: {zstddev(y)}")
    print(f"Standard Error of X: {zstderr(x)}")
    print(f"Standard Error of Y: {zstderr(y)}")
    print(f"Correlation between X and Y: {zcorr(x,y)}")
    