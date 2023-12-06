from functools import reduce
f = open('input_p6.txt')
lines = [ l for l in f ]
time = int(reduce(lambda x, y: x + y, [ n for n in lines[0][:-1].split(' ') if n ][1:]))
distance = int(reduce(lambda x, y: x + y, [ n for n in lines[1][:-1].split(' ') if n ][1:]))

w = 0
for t in range(time) :
    if t % 1000000 == 0 :
        print(str(t) + " of " + str(time))
    if t * (time - t) > distance :
        w += 1
print(w) 
