gameResult = input('Please enter game results: ').lower()


def count(coin):
    H = coin.count('h')
    T = coin.count('t')
    if H > T:
        return 'H wins!'
    elif H < T:
        return 'T wins'
    else:
        return 'Draw!'

print (count(gameResult))




