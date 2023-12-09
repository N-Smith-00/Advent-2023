import math
f = open('input.txt')
games = {}

for line in f:
    game = line.split(':')[0].strip()
    res = [d.split(', ') for d in line.split(': ')[1].strip('\n').split('; ')]
    games[game] = res

sum = 0
pow = 0
total_cubes = {'red':12,'green':13,'blue':14}


for game in games.keys():
    imp = False
    red = 0
    blue = 0
    green = 0
    for draw in games[game]:
        for blocks in draw:
            blocks = blocks.split()
            if total_cubes[blocks[1]] < int(blocks[0]):
                imp = True
            match blocks[1]:
                case 'red':
                    red = max([int(blocks[0]), red])
                case 'blue':
                    blue = max([int(blocks[0]), blue])
                case 'green':
                    green = max([int(blocks[0]), green])
    
    if not imp:
        sum += int(game.split()[1])
    pow += math.prod([red, blue, green])

print('part 1 '+str(sum))
print('part 2 '+str(pow))