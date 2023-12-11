f = open('input_p11.txt')
lines = [ l for l in f ]
c_sizes = [ [ 1 for c in l ] for l in lines ]

for li in range(len(lines)) :
    if '#' not in lines[li] :
        c_sizes[li] = [ c * 1000000 for c in c_sizes[li] ]
        
for ci in range(len(lines[0])) :
    if '#' not in [ l[ci] for l in lines ] :
        c_sizes = [ c_sizes[li][:ci] + [ (c_sizes[li][ci] * 1000000) ] + c_sizes[li][(ci + 1):] for li in range(len(lines)) ]

galaxies = [ (ci, li) for li in range(len(lines)) for ci in range(len(lines[li])) if lines[li][ci] == '#' ]
comb_galax = [ (galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies)) ]
comb_galax_man = [ sum(c_sizes[c[0][1]][c[0][0]:c[1][0]] if c[0][0] <= c[1][0] else c_sizes[c[0][1]][c[1][0]:c[0][0]]) + sum([s[c[0][0]] for s in (c_sizes[c[0][1]:c[1][1]] if c[0][1] <= c[1][1] else c_sizes[c[1][1]:c[0][1]])]) for c in comb_galax ]

print(sum(comb_galax_man))
