f = open('input_p16.txt')
lines = [ l[:-1] for l in f ]

start_pos = [ (0, i, (1, 0)) for i in range(len(lines)) ] + [ (len(lines[0]) - 1, i, (-1, 0)) for i in range(len(lines)) ] + [ (i, 0, (0, 1)) for i in range(len(lines[0])) ] + [ (i, len(lines) - 1, (0, -1)) for i in range(len(lines[0])) ]

def energize(start_pos) :
    beams = [ start_pos ]
    energized = [ [ 0 for c in l ] for l in lines ]
    while beams :
        newbeams = beams.copy()
        for b in beams :
            if b[0] < 0 or b[0] >= len(lines[0]) or b[1] < 0 or b[1] >= len(lines) :
                newbeams.remove(b)
                continue
            flag = energized[b[1]][b[0]]
            energized[b[1]][b[0]] = 1
            tile = lines[b[1]][b[0]]
            if tile == '.' :
                newbeams[newbeams.index(b)] = (b[0] + b[2][0], b[1] + b[2][1], b[2])
            elif tile == '-' :
                if b[2][1] == 0 :
                    newbeams[newbeams.index(b)] = (b[0] + b[2][0], b[1] + b[2][1], b[2])
                else :
                    newbeams.remove(b)
                    if not flag :
                        newbeams.append((b[0] - 1, b[1], (-1, 0)))
                        newbeams.append((b[0] + 1, b[1], (1, 0)))
            elif tile == '|' :
                if b[2][0] == 0 :
                    newbeams[newbeams.index(b)] = (b[0] + b[2][0], b[1] + b[2][1], b[2])
                else :
                    newbeams.remove(b)
                    if not flag :
                        newbeams.append((b[0], b[1] - 1, (0, -1)))
                        newbeams.append((b[0], b[1] + 1, (0, 1)))
            elif tile == '/' :
                d = (-b[2][1], -b[2][0])
                newbeams[newbeams.index(b)] = (b[0] + d[0], b[1] + d[1], d)
            elif tile == '\\' :
                d = (b[2][1], b[2][0])
                newbeams[newbeams.index(b)] = (b[0] + d[0], b[1] + d[1], d)
        if beams == newbeams :
            break
        beams = newbeams
    return sum([ sum(l) for l in energized ])

print(max([ energize(s) for s in start_pos ]))
