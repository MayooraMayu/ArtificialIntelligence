import string
import itertools
inListNumsAsStringArray = [ ['FIRST', 'FIRST'], 
                            ['SEND', 'MORE'] ]
inResultsArray = [ 'THIRD',
                'MONEY' ]
inPossibleNumsAsStr = '0123456789'
def getNumberFromStringAndMappingInfo(inStr, inDictMapping):
    numAsStr = ''
    for ch in inStr:
        numAsStr = numAsStr + inDictMapping[ch] 
    return int(numAsStr)

def solveCryptarithmeticBruteForce(inListNumsAsString, inResultStr, inPossibleNumsAsStr):
    nonZeroLetters = []
    strFromStrList = ''
    for numStr in inListNumsAsString:
        nonZeroLetters.append(numStr[0])
        strFromStrList = strFromStrList + numStr
    nonZeroLetters.append(inResultStr[0])
    strFromStrList = strFromStrList + inResultStr  
    uniqueStrs = ''.join(set(strFromStrList))
    for tup in itertools.permutations(inPossibleNumsAsStr, len(uniqueStrs)):
        dictCharAndDigit = {}
        for i in range(len(uniqueStrs)):
            dictCharAndDigit[uniqueStrs[i]] = tup[i]            
        nonZeroLetterIsZero = False
        for letter in nonZeroLetters:
            if(dictCharAndDigit[letter] == '0'):
                nonZeroLetterIsZero = True
                break
        if(nonZeroLetterIsZero == True):
            continue
        result = getNumberFromStringAndMappingInfo(inResultStr, dictCharAndDigit)     
        testResult = 0
        for numStr in inListNumsAsString:
            testResult = testResult + getNumberFromStringAndMappingInfo(numStr, dictCharAndDigit)        

        if(testResult == result):
            strToPrint = ''
            for numStr in inListNumsAsString:
                strToPrint = strToPrint + numStr + '(' + str(getNumberFromStringAndMappingInfo(numStr, dictCharAndDigit)) + ')' + ' + '
            strToPrint = strToPrint[:-3]
            strToPrint = strToPrint + ' = ' + inResultStr + '(' + str(result) + ')'
            print(strToPrint)
            break

for i in range(len(inResultsArray)):
    solveCryptarithmeticBruteForce(inListNumsAsStringArray[i], inResultsArray[i], inPossibleNumsAsStr)
