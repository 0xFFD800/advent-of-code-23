from functools import reduce
f = open('input_p6.txt')
lines = [ l for l in f ]
times = [ int(n) for n in lines[0][:-1].split(' ')[1:] if n ]
distances = [ int(n) for n in lines[1][:-1].split(' ')[1:] if n ]

w = []
for i in range(len(times)) :
    r = []
    for t in range(times[i]) :
        if t * (times[i] - t) > distances[i] :
            r.append(t)
    w.append(len(r))
   
print(w)
print(reduce(lambda x, y: x * y, w))
