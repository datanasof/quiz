def down(depth):
    water = depth + 0.5
    depth += 1
    return [WaterCheckDown(water, depth), depth]


def up(depth):
    water = depth - 0.5
    depth -= 1
    return [WaterCheckUp(water, depth), depth]


def hor(depth):
    water = depth
    return [WaterCheckDown(water, depth), depth]


def WaterCheckDown(water, depth):
    if depth > 0:
        return water
    else:
        return 0


def WaterCheckUp(water, depth):
    if depth >= 0:
        return water
    else:
        return 0


commandList = {'d': 'down(depth)', 'u': 'up(depth)', 'h': 'hor(depth)'}

depth = 0
water = 0

command = input('Please define landscape (d,u,h): ')


for ch in command:
    result = eval(commandList[ch])
    depth = result[1]
    water += result[0]

print('Water in the defined terrain equals to {0} litres'.format(int(water * 1000)))
