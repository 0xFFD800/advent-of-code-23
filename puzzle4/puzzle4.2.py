f = open('input_p4.txt')
cards = [ l for l in f ]
copies = [ 1 for i in range(len(cards)) ]
for li in range(len(cards)) :
    l = cards[li]
    ci, c = l.split(':')
    nh, wn = c.split('|')
    nhs = { int(n) for n in nh.split(' ') if n }
    wns = { int(n) for n in wn.split(' ') if n }
    nn = nhs.intersection(wns)
    print(nn)
    for i in range(1, len(nn) + 1) :
        copies[li + i] += copies[li]

print(copies)
print(sum(copies))
