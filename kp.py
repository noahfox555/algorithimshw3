import sys

def dynamicKnapSack(weights, values, c):
    # create an array that has a position for every calculated weight remaining
    dp = []
    for i in range(c):
        dp.append([])
        for j in range(len(values)):
            dp[i].append(([], -1))
    
    # printList(dp)
    numItems = len(values)
    # i = current max weight
    for i in range(c):
        curC = i + 1
        for j in range(numItems):
            curWeight = weights[j]
            curValue = values[j]
            if curC - curWeight == 0:
                dp[i][j] =  ([j+1], curValue)
            elif curC - curWeight > 0:
                
                maxValue = ([], -1)
                for subList in dp[curC - curWeight - 1]:
                    if subList[1] > maxValue[1]:
                        maxValue = (subList[0][:], subList[1])
                if (maxValue[1] >= 0) and (j+1) not in maxValue[0]:
                        maxValue[0].append(j+1)
                        maxValue = (maxValue[0], maxValue[1] + curValue)
                dp[i][j] = maxValue
          
    # printList(dp)
    maxValue = ([], -1)
    for subList in dp[c-1]:
        if maxValue[1] < subList[1]:
            maxValue = subList
    maxValue[0].sort()
    return maxValue


def main():
    inTxt = sys.argv[1]
    outTxt = sys.argv[2]
    with open(inTxt, 'r') as inFile:
        lines = inFile.readlines()
    
    c = int(lines[0].strip())
    weights = []
    values = []
    for i in range(1, len(lines)):
        line = lines[i].split(',')
        weights.append(int(line[1]))
        values.append(int(line[2]))

    with open(outTxt, 'w') as outFile:
        outFile.write(str(dynamicKnapSack(weights, values, c))[1:-1] + ' total value')

main()