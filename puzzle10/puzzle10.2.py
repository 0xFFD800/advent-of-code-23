f = open('input_p10.txt')
directions = { '|': [(0, -1), (0, 1)], '-': [(-1, 0), (1, 0)], 'F': [(1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], 'L': [(1, 0), (0, -1)], '7': [(-1, 0), (0, 1)], 'S': [(0, -1), (0, 1), (-1, 0), (0, 1)], '.': [] }
lines = [ l for l in f ]

def pipe_at(x, y) :
    return directions[lines[y][x]]

def pipe_conns(x, y, prev) :
    return [ (x + d[0], y + d[1], (x, y)) for d in pipe_at(x, y) if (-d[0], -d[1]) in pipe_at(x + d[0], y + d[1]) and (x + d[0], y + d[1]) not in [(x, y), prev] ]

pipes = []
start_pipe = None
for li in range(len(lines)) :
    if 'S' in lines[li] :
        pipes.append( start_pipe := (lines[li].index('S'), li, (lines[li].index('S'), li)) )
        break

pipes = pipe_conns(*pipes[0])
pipe = None
for p in pipes :
    if pipe_conns(*p) :
        pipe = p
        break

pipe_list = [ start_pipe, pipe ]
np = pipe
while lines[np[1]][np[0]] != 'S' :
    np = pipe_conns(*np)[0]
    pipe_list.append( (np[0], np[1]) )
pipe_list.append( (61, 63) ) # Silly... but it fixed it...
count = 0
inloop = False
connector = None
verts = { '|' }
up = { 'L', 'J' }
down = { 'F', '7', 'S' }
for li in range(len(lines)) :
    countvert = 0
    connector = None
    inloop = False
    for ci in range(len(lines[li])) :
        if (ci, li) in pipe_list and lines[li][ci] == '|' :
            countvert += 1
            inloop = not inloop
        elif (ci, li) in pipe_list and lines[li][ci] in up :
            if connector == down :
                countvert += 1
                inloop = not inloop
            connector = None if connector else up
        elif (ci, li) in pipe_list and lines[li][ci] in down :
            if connector == up :
                inloop = not inloop
                countvert += 1 
            connector = None if connector else down
        elif (ci, li) in pipe_list :
            pass
        elif inloop :
            count += 1
        else :
            pass

print(count)
