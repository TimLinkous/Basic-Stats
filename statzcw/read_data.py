

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
