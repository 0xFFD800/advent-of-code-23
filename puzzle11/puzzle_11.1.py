f = open('input_p11.txt')
lines = [ l for l in f ]
li = 0
while li < len(lines) :
    if '#' not in lines[li] :
        lines.insert(li, lines[li])
        li += 1
    li += 1

ci = 0
while ci < len(lines[0]) :
    if '#' not in [ l[ci] for l in lines ] :
        lines = [ l[:ci] + '.' + l[ci:] for l in lines ]
        ci += 1
    ci += 1

galaxies = [ (ci, li) for li in range(len(lines)) for ci in range(len(lines[li])) if lines[li][ci] == '#' ]
comb_galax = [ (galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies)) ]
comb_galax_man = [ abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1]) for c in comb_galax ]

print(sum(comb_galax_man))
