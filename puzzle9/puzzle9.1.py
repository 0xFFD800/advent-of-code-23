f = open("input_p9.txt")
seqs = [ [ int(c) for c in l[:-1].split(' ') ] for l in f ]
vals = [ ]
for s in seqs :
    dxm = [ s ]
    dx = s.copy()
    while (dx := [ dx[i] - dx[i - 1] for i in range(1, len(dx)) ]) != [ 0 for d in dx ] :
        dxm.append(dx)
    for ri in reversed(range(1, len(dxm))) :
        dxm[ri - 1] += [ dxm[ri - 1][-1] + dxm[ri][-1] ]
    vals += [ dxm[0][-1] ]
print(sum(vals))
