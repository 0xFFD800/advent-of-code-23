f = open('input_p15.txt')

boxes = [ [] for i in range(256) ]
for l in f :
    for s in l[:-1].split(',') :
        h = 0
        for c in s.split('-')[0] if '-' in s else s.split('=')[0] :
            h = ((h + ord(c)) * 17) % 256
        labels = [ b[0] for b in boxes[h] ]
        print(s)
        print(boxes[h])
        if '-' in s and s.split('-')[0] in labels :
            boxes[h].pop(labels.index(s.split('-')[0]))
        elif '=' in s :
            m = s.split('=')
            if m[0] in labels :
                boxes[h][labels.index(m[0])] = (m[0], int(m[1]))
            else :
                boxes[h].append(( m[0], int(m[1]) ))
        print(boxes[h])
focus = sum([ sum([ (bi + 1) * (li + 1) * boxes[bi][li][1] for li in range(len(boxes[bi])) ]) for bi in range(len(boxes)) ])
print(focus)
