f = open('input_p15.txt')

for l in f :
    hashes = []
    for s in l[:-1].split(',') :
        curr_val = 0
        for c in s :
            curr_val = ((curr_val + ord(c)) * 17) % 256
        hashes.append(curr_val)

print(sum(hashes))
