f = open('input_p8.txt')
inst = [] # array of ints
maps = dict() # dict of str -> (str, str)
for l in f :
    if '=' in l :
        h1, h2 = [ s.strip() for s in l.split('=') ]
        maps[h1] = tuple(s.strip() for s in h2[1:-1].split(','))
    elif l.strip() :
        inst = [ 0 if c == 'L' else 1 for c in l[:-1] ]
p = "AAA"
st = 0
while p != "ZZZ" :
    p = maps[p][inst[st % len(inst)]]
    st += 1
print(st)
