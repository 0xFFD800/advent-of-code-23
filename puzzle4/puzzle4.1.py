f = open('input_p4.txt')

points = []
for l in f :
    ci, c = l.split(':')
    nh, wn = c.split('|')
    nhs = { int(n) for n in nh.split(' ') if n }
    wns = { int(n) for n in wn.split(' ') if n }
    nn = nhs.intersection(wns)
    print(nn)
    if nn :
        points.append(2 ** (len(nn) - 1))

print(points)
print(sum(points))
