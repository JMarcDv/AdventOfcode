import re

numbers = {
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
}

def day1() :
    input = open('Others/Advent_of_Code/day1/inputTest.txt', 'r')
    summList = []
    for lines in input:
        tempList = []
        tempStringList = []
        for string in lines:
            isEndOfString = False
            if (string.isdecimal()):
                tempList.append(string)
                isEndOfString = True
                tempStringList = []
            if (isEndOfString == False):
                tempStringList.append(string)
                result = checkString(tempStringList)
                if (result[0] == True) :
                    tempList.append(findValue(result[1]))
                    tempStringList = []

        first_num = tempList[0]
        last_num = tempList[len(tempList) - 1]
        num = first_num + last_num
        summList.append(num)
    print(summList)
    total = 0
    for number in summList:
        total += int(number)
    print(total)



def checkString(listString) :
    tempString = ''
    for letter in listString :
        tempString += letter
    for numberLitteral in numbers.keys() :
        if re.search(re.escape(numberLitteral), tempString) :
            return (True, numberLitteral)
    return (False, 'nothing')

def findValue(key) :
    for x, y in numbers.items() :
        if x == key : return y

day1()