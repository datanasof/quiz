import re


text = input('Enter your string for decoding: ')


def countChar(ch, text):
    char_occur = text.count(ch)
    return char_occur


def charNumbered(text):
    charList = {}
    for ch in set(text):
        charList[ch] = countChar(ch, text)
    return charList


'''def sortGenerator():
    chardict = charNumbered(text)
    sortChGen = (k for k in sorted(
        chardict, key=chardict.get, reverse=True))
    return sortChGen'''


def sortDic():
    chardict = charNumbered(text)
    sortedKeys = sorted(chardict, key=chardict.get, reverse=True)
    return sortedKeys


def valueAssign():
    charList = {}
    i = 9
    for ch in sortDic():
        charList[ch] = i
        i -= 1
        if i < 0:
            break
    return charList


def charExchange(text):
    charlist = valueAssign()
    for ch in charlist:
        text = text.replace(ch, str(charlist[ch]))
    return text


def splitNumbers():
    result = [int(s) for s in re.findall(r'\d+', charExchange(text))]
    return result


def total(numbersList):
    return sum(numbersList)


#print (charExchange(text))
#print (splitNumbers())
print ('The sum of decoded numbers equals to {}'.format(total(splitNumbers())))
