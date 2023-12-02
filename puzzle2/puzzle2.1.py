maxes = { 'red': 12, 'green': 13, 'blue': 14 }
f = open('input_p2.txt')

possible = []
i = 0
for lr in f :
    p = True
    gr, l = [t.strip() for t in lr.split(':')]
    g = int(gr.split(' ')[1])
    sets = [s.strip() for s in l.split(';')]
    for s in sets :
        colors = [c.strip() for c in s.split(',')]
        for c in colors :
            n, co = c.split(' ')
            if int(n) > maxes[co] :
                p = False
    if p :
        possible.append(g)
    i += 1
print(possible)
print(sum(possible))
