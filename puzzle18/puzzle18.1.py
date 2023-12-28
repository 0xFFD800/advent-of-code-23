f = open('input_p18.txt')

curr = (0, 0)
points = [ (0, 0) ]
for l in f :
    d, s, u = l.split(' ')
    for i in range(int(s)) :
        curr = (curr[0] + 1 if d == 'R' else curr[0] - 1 if d == 'L' else curr[0], curr[1] + 1 if d == 'D' else curr[1] - 1 if d == 'U' else curr[1])
        points.append(curr)

xs = [ p[0] for p in points ]
ys = [ p[1] for p in points ]

matrix = []
for j in range(max(ys) - min(ys) + 1) :
    s = []
    flag1 = 0
    flag2 = 0
    prevflag1 = 0
    for i in range(max(xs) - min(xs) + 1) :
        r = False
        if (i + min(xs), j + min(ys)) in points :
            if (i + min(xs), j + 1 + min(ys)) in points :
                flag1 += 1
                flag2 -= 1
            if (i + min(xs), j - 1 + min(ys)) in points :
                flag1 += 1
                flag2 += 1
            r = True
        elif flag2 :
            flag1 = prevflag1
            flag2 = 0
        else :
            prevflag1 = flag1
        s.append('#' if r or (flag1 % 4 and not flag2) else ' ')
    matrix.append(''.join(s))
for m in matrix :
    print(m)

l = []
for m in matrix :
    l.append(m.count('#'))

print(l)
print(sum(l))
