from math import floor, ceil

f = open('input_p13.txt')
lines = [ l for l in f ]
blocks = []
bi = 0
while bi < len(lines) :
    if '\n' in lines[bi:] :
        nbi = lines[bi:].index('\n') + bi
    else :
        nbi = len(lines)
    blocks.append([ l[:-1] for l in lines[bi:nbi] ])
    bi = nbi + 1

def extract_columns(block, start, stop, reverse=False) :
    return [ [ l[i] for i in (reversed(range(start, stop)) if reverse else range(start, stop)) ] for l in block ]

horizontals = []
verticals = []
for b in blocks :
    # Horizontal
    found = False
    for sp in range(1, ceil(len(b) / 2)) :
        if found :
            break
        if b[:sp] == list(reversed(b[sp:(sp * 2)])) : 
            horizontals.append(sp)
            found = True
    for sp in range(ceil(len(b) / 2), len(b)) :
        if found :
            break
        if b[(len(b) - ((len(b) - sp) * 2)):sp] == list(reversed(b[sp:len(b)])) :
            horizontals.append(sp)
            found = True
    # Vertical
    for sp in range(1, ceil(len(b[0]) / 2)) :
        if found :
            break
        if extract_columns(b, 0, sp) == extract_columns(b, sp, sp * 2, reverse=True) :
            verticals.append(sp)
            found = True
    for sp in range(ceil(len(b[0]) / 2), len(b[0])) :
        if found :
            break
        if extract_columns(b, len(b[0]) - ((len(b[0]) - sp) * 2), sp) == extract_columns(b, sp, len(b[0]), reverse=True) :
            verticals.append(sp)
            found = True
    if not found :
        print("I... don't think this should happen...")
        for l in b :
            print(l)

print(sum(verticals) + (100 * sum(horizontals)))
