from functools import cmp_to_key

f = open('input_p7.txt')
chars = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]
lines = [ ( l.split(' ')[0], int(l[:-1].split(' ')[1]) ) for l in f ]

def key(t, s) :
    x = t[0]
    y = s[0]
    countsx = [ x.count(c) for c in chars ]
    countsy = [ y.count(c) for c in chars ]
    mx = max(countsx) * 2
    my = max(countsy) * 2
    if len([ c for c in countsx if c == 2]) == 2 :
        mx += 1
    if len([ c for c in countsy if c == 2]) == 2 :
        my += 1
    if max(countsx) == 3 and 2 in countsx:
        mx += 1
    if max(countsy) == 3 and 2 in countsy:
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
