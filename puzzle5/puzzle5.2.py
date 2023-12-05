f = open('input_p5.txt')
lines = [ l for l in f ]
seedsraw = lines[0][:-1].split(' ')[1:]
seeds = [ (int(seedsraw[i]), int(seedsraw[i + 1])) for i in range(0, len(seedsraw), 2) ]
categories = []
li = 3
while li in range(len(lines)) :
    c = []
    while li in range(len(lines)) and lines[li] != '\n' :
        c.append([ int(n) for n in lines[li][:-1].split(' ') ])
        li += 1
    if c :
        categories.append(c)
    li += 2

locations = []
for ri in range(len(categories)) :
    r = categories[ri]
    ac = []
    print("Beginning category " + str(ri) + " of " + str(len(categories)))
    for s in seeds :
        worklist = [ s ]
        while worklist :
            w = worklist[0]
            flag = False
            for ci in range(len(r)) :
                c = r[ci]
                wr = (w[0], w[0] + w[1])
                cr = (c[1], c[1] + c[2])
                # Endpoint is inclusive, then exclusive.
                inter = cr if wr[0] <= cr[0] and wr[1] >= cr[1] else wr if cr[0] <= wr[0] and cr[1] >= wr[1] else ( wr[0], cr[1] ) if wr[0] >= cr[0] and wr[0] < cr[1] else ( cr[0], wr[1] ) if cr[0] >= wr[0] and cr[0] < wr[1] else (-1, -1)
                if inter != (-1, -1) :
                    ac.append( ((inter[0] - c[1]) + c[0], (inter[1] - inter[0])) )
                    worklist = worklist[1:]
                    if w[0] < inter[0] :
                        worklist.append( (w[0], inter[0] - w[0]) )
                    if w[0] + w[1] > inter[1] :
                        worklist.append( (inter[1], (w[0] + w[1]) - inter[1]) )
                    flag = True
                    break
            if worklist and not flag :
                ac.append(worklist[0])
                worklist = worklist[1:]
    seeds = ac

results = [s for s in sorted(seeds, key=lambda x: x[0])]
print(results)
print(results[0][0])
