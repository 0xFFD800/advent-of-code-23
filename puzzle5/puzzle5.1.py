f = open('input_p5.txt')
lines = [ l for l in f ]
seeds = [ int(n) for n in lines[0].split(' ')[1:-1] ]
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
for s in seeds :
    for r in categories :
        for c in r :
            print(c)
            if s in range(c[1], c[1] + c[2]) :
                s = (s - c[1]) + c[0]
                break
    locations.append(s)
print(locations)
print(min(locations))
