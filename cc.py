import sys

def dynamic(amount, coins):
    if amount == 0:
        return ([0] * len(coins), 0)
        
    dp = []
    for i in range(amount):
        dp.append([])
        for j in range(len(coins)):
            dp[i].append(([sys.maxsize] * len(coins), sys.maxsize))        

    for i in range(amount):
        for j in range(len(coins)):
            currentAmount = i + 1
            currentCoin = coins[j]
            if currentAmount - currentCoin == 0:
                temp = ([0] * len(coins), 1)
                temp[0][j] = 1
                dp[i][j] = temp
            elif currentAmount - currentCoin > 0:
                minimumList = ([sys.maxsize] * len(coins), sys.maxsize)
                for subList in dp[currentAmount-currentCoin-1]:
                    if (subList[1] < minimumList[1]):
                        minimumList = (subList[0][:], subList[1])
                if (minimumList[1] < sys.maxsize):
                    minimumList[0][j] += 1
                    minimumList = (minimumList[0], minimumList[1]+1)

                dp[i][j] = minimumList


    minimumList = ([0] * len(coins), sys.maxsize)
    for subList in dp[amount-1]:
        if minimumList[1] > subList[1]:
            minimumList = subList
    
    return minimumList

def main():
    inTxt = sys.argv[1]
    outTxt = sys.argv[2]
    with open(inTxt, 'r') as inFile:
        lines = inFile.readlines()
    
    c = int(lines[0].strip())

    coinsString = lines[1][1:-1]
    coins = []
    for num in coinsString.split(','):
        coins.append(int(num))

    with open(outTxt, 'w') as outFile:
        outFile.write(str(dynamic(c, coins))[1:-1] + ' total coins')
main()