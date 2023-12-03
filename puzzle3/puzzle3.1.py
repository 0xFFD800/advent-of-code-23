f = open('input_p3.txt')
lines = [ l for l in f ]
digits = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }
symbols = { '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '-', '_', ';', ':', '[', ']', '{', '}', '/', '\\', '\'', '"', '?', ',', '<', '>' }
parts = []
for li in range(len(lines)) :
    l = lines[li]
    num = ''
    for ci in range(len(l)) :
        if l[ci] in digits :
            num += l[ci]
        else :
            if num :
                n = int(num)
                slice1 = max(ci - (len(num) + 1), 0)
                slice2 = min(ci + 1, len(l) - 1)
                candidates = l[slice1:slice2] + (lines[li - 1][slice1:slice2] if li > 0 else '') + (lines[li + 1][slice1:slice2] if li < len(lines) - 1 else '')
                for s in symbols :
                    if s in candidates :
                        parts += [n]
                        print('n: ' + str(n) + '; s: ' + s)
                        break;
            num = ''
print(parts)
print(sum(parts))
