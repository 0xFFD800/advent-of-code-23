import numpy as np
f = open('input_p1.txt')
s = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
r = []
for l in f :
    ls1 = sorted([ (c, l.find(c)) for c in s if l.find(c) != -1 ], key=lambda x: x[1])
    ls2 = sorted([ (c, l.rfind(c)) for c in s if l.rfind(c) != -1 ], key=lambda x: x[1])
    #c1 = s[ls1[0]]
    #c2 = s[ls2[-1]]
    print('c1: ' + ls1[0][0] + ', c2: ' + ls2[-1][0])
    r.append((s.index(ls1[0][0]) % 10) * 10 + (s.index(ls2[-1][0]) % 10))
#r = [ int(s[np.argmin([ l.find(c) for c in s if l.find(c) != -1 ])]) * 10 + int(s[np.argmax([ l.rfind(c) for c in s if l.rfind(c) != -1 ])]) for l in f ]
print(r)
print('sum: ' + str(sum(r)))
