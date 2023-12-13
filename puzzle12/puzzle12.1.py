from itertools import combinations_with_replacement

f = open('input_p12.txt')

lines = [ l for l in f ]
comb = []

def create_groupings(group, pr1, pr2, in1, in2) :
    if not pr1 or not pr2 :
        return [ group ]

    groupings = []
    offset = 0

    while sum(pr2[:offset]) + len(pr2[:offset]) - 1 <= pr1[0] and offset <= len(pr2) :
        groupings += create_groupings(group + [ (in2[:offset], in1[0]) ], pr1[1:], pr2[offset:], in1[1:], in2[offset:])
        offset += 1

    return groupings

def perm_valid(r1, st, ti) :
    st2 = st.copy()
    i = 0
    for tii in ti :
        st2.insert(tii + i, '.')
        i += 1
    string2 = ''.join(st2)
    for ci in range(len(string2)) :
        if r1[ci] == '#' and string2[ci] == '.' or r1[ci] == '.' and string2[ci] == '#' :
            return False
    return True

total = 0
for li in range(len(lines)) :
    l = lines[li]
    r1, r2 = l[:-1].split(' ')
    pr1 = [ len(r) for r in r1.split('.') if r ]
    pr2 = [ int(n) for n in r2.split(',') ]
    
    groupings = [ g for g in create_groupings([], pr1, pr2, [ i for i in range(len(pr1)) ], [ i for i in range(len(pr2)) ]) if sum([ len(x[0]) for x in g ]) == len(pr2) ]

    for g in groupings :
        for t in g :
            if len(t[0]) > 0 :
                wh = pr1[t[1]] - (sum([ pr2[i] for i in t[0] ]) + len(t[0]) - 1)
                st = [ '#'*pr2[t[0][ii]] + ('.' if ii != len(t[0]) - 1 else '') for ii in range(len(t[0])) ]
                for ti in combinations_with_replacement(range(len(st) + 1), wh) :
                    if perm_valid(r1, st, ti) :
                        total += 1

print(total)
