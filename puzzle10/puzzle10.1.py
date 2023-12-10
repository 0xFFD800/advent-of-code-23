f = open('input_p10.txt')
directions = { '|': [(0, -1), (0, 1)], '-': [(-1, 0), (1, 0)], 'F': [(1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], 'L': [(1, 0), (0, -1)], '7': [(-1, 0), (0, 1)], 'S': [(0, -1), (0, 1), (-1, 0), (0, 1)], '.': [] }
lines = [ l for l in f ]

def pipe_at(x, y) :
    return directions[lines[y][x]]

def pipe_conns(x, y, prev) :
    return [ (x + d[0], y + d[1], (x, y)) for d in pipe_at(x, y) if (-d[0], -d[1]) in pipe_at(x + d[0], y + d[1]) and (x + d[0], y + d[1]) not in [(x, y), prev] ]

pipes = []
for li in range(len(lines)) :
    if 'S' in lines[li] :
        pipes.append( (lines[li].index('S'), li, (lines[li].index('S'), li)) )
        break

pipes = pipe_conns(*pipes[0])
pipe = None
for p in pipes :
    if pipe_conns(*p) :
        pipe = p
        break
st = 1
while lines[pipe[1]][pipe[0]] != 'S' :
    pipe = pipe_conns(*pipe)[0]
    st += 1

print(st / 2)
