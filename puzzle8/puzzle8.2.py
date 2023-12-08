from math import lcm
f = open('input_p8.txt')
inst = [] # array of ints
maps = dict() # dict of str -> (str, str)
for l in f :
    if '=' in l :
        h1, h2 = [ s.strip() for s in l.split('=') ]
        maps[h1] = tuple(s.strip() for s in h2[1:-1].split(','))
    elif l.strip() :
        inst = [ 0 if c == 'L' else 1 for c in l[:-1] ]
p = [ s for s in maps.keys() if s[2] == 'A' ]
st = [ 0 for s in range(len(p)) ]
for pi in range(len(p)) :
    while p[pi][2] != 'Z' :
        p[pi] = maps[p[pi]][inst[st[pi] % len(inst)]]
        st[pi] += 1
stm = [ s for s in st ]

print(lcm(*stm))
