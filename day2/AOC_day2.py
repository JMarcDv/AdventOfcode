import re

def day2_1() :
    input = open('./input.txt', 'r')
    tabId = []
    for line in input :
        tab = line.split(':')
        gameId = tab[0].split(' ')[1]
        setsSplitTab = tab[1].split(';')
        isGamePossible = True
        for item in setsSplitTab :
            # print('SET' + str(item))
            for item2 in item.split(',') :
                # print('TIRAGE' + str(item2))
                res = isPossible(item2)
                if res == False :
                    isGamePossible = False
        if isGamePossible :
            tabId.append(gameId)
    total = 0
    for id in tabId :
        total += int(id)
    # print(tabId)
    print('DAY 2-1 ANSWER : ' + str(total))

def isPossible(item) :
    count = item.split(' ')[1]
    color = item.split(' ')[2]
    if re.search('blue', color):
        if int(count) > 14 :
            # print(gameId + 'blue')
            return False
    if re.search('red', color) :
        if int(count) > 12 :
            # print(gameId + 'red')
            return False
    if re.search('green', color) :
        if int(count) > 13 :
            # print(gameId + 'green')
            return False
    return True

def day2_2() :
    input = open('./input.txt', 'r')
    cubesTab = []
    for line in input :
        tab = line.split(':')
        setsSplitTab = tab[1].split(';')
        blueList = []
        redList = []
        greenList = []
        for item in setsSplitTab :
            # print('SET' + str(item))
            for item2 in item.split(',') :
                # print('TIRAGE' + str(item2))
                res = countingList(item2, blueList, redList, greenList)
                blueList, redList, greenList = res
        blueMax = max(blueList)
        redMax = max(redList)
        greenMax = max(greenList)
        cubesTab.append(int(blueMax) * int(redMax) * int(greenMax))
    # print(len(cubesTab))
    # print(cubesTab)
    total = 0
    for cube in cubesTab :
        total += int(cube)
    print('DAY 2-2 ANSWER : ' + str(total))


def countingList(item, blueList, redList, greenList) :
    count = item.split(' ')[1]
    color = item.split(' ')[2]
    if re.search('blue', color):
        blueList.append(int(count))
        
    if re.search('red', color) :
        redList.append(int(count))
        
    if re.search('green', color) :
        greenList.append(int(count))
        
    return blueList, redList, greenList


day2_1()
day2_2()