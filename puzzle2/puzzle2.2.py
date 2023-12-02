f = open('input_p2.txt')

powers = []

for lr in f :
    p = True
    gr, l = [t.strip() for t in lr.split(':')]
    g = int(gr.split(' ')[1])
    sets = [s.strip() for s in l.split(';')]
    maxC = { 'red': 0, 'green': 0, 'blue': 0 }
    for s in sets :
        colors = [c.strip() for c in s.split(',')]
        for c in colors :
            n, co = c.split(' ')
            if int(n) > maxC[co] :
                maxC[co] = int(n)
    powers.append(maxC['red'] * maxC['green'] * maxC['blue'])
print(powers)
print(sum(powers))
