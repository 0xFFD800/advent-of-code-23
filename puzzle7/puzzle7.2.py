from functools import cmp_to_key

f = open('input_p7.txt')
chars = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J' ]
lines = [ ( l.split(' ')[0], int(l[:-1].split(' ')[1]) ) for l in f ]

def key(t, s) :
    x = t[0]
    y = s[0]
    countsxr = [ x.count(c) for c in chars[:-1] ]
    countsyr = [ y.count(c) for c in chars[:-1] ]
    jx = x.count('J')
    jy = y.count('J')
    mx = (max(countsxr) + jx) * 2
    my = (max(countsyr) + jy) * 2
    if len([ c for c in countsxr if c == 2 or c == 3]) == 2 :
        mx += 1
    if len([ c for c in countsyr if c == 2 or c == 3]) == 2 :
        my += 1
    if mx < my :
        return -1
    if mx > my :
        return 1
    for ci in range(len(x)) :
        if chars.index(x[ci]) > chars.index(y[ci]) :
            return -1
        if chars.index(x[ci]) < chars.index(y[ci]) :
            return 1
    return 0

sort = sorted(lines, key=cmp_to_key(key))
print(sort)
vals = [ sort[ci][1] * (ci + 1) for ci in range(len(sort)) ]
print(vals)
print(sum(vals))
