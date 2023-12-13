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

def find_mirror(b, exclude) :
    mirror = None
    # Horizontal
    found = False
    for sp in range(1, ceil(len(b) / 2)) :
        if exclude == (sp, 0) :
            continue
        if found :
            break
        if b[:sp] == list(reversed(b[sp:(sp * 2)])) : 
            mirror = (sp, 0)
            found = True
    for sp in range(ceil(len(b) / 2), len(b)) :
        if exclude == (sp, 0) :
            continue
        if found :
            break
        if b[(len(b) - ((len(b) - sp) * 2)):sp] == list(reversed(b[sp:len(b)])) :
            mirror = (sp, 0)
            found = True
    # Vertical
    for sp in range(1, ceil(len(b[0]) / 2)) :
        if exclude == (0, sp) :
            continue
        if found :
            break
        if extract_columns(b, 0, sp) == extract_columns(b, sp, sp * 2, reverse=True) :
            mirror = (0, sp)
            found = True
    for sp in range(ceil(len(b[0]) / 2), len(b[0])) :
        if exclude == (0, sp) :
            continue
        if found :
            break
        if extract_columns(b, len(b[0]) - ((len(b[0]) - sp) * 2), sp) == extract_columns(b, sp, len(b[0]), reverse=True) :
            mirror = (0, sp)
            found = True
    return mirror

mirrors_old = [ find_mirror(b, (0, 0)) for b in blocks ]
mirrors_new = [ None for m in mirrors_old ]
for bi in range(len(blocks)) :
    for li in range(len(blocks[bi])) :
        done = False
        for ci in range(len(blocks[bi][li])) :
            nb = blocks[bi].copy()
            nb[li] = nb[li][:ci] + ('#' if nb[li][ci] == '.' else '.') + nb[li][ci + 1:]
            m = find_mirror(nb, mirrors_old[bi])
            if m :
                done = True
                mirrors_new[bi] = m
                break
        if done :
            break
        

print(sum([ m[0] * 100 + m[1] for m in mirrors_new ]))
