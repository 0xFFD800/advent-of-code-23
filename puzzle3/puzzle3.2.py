f = open('input_p3.txt')
lines = [ l for l in f ]
digits = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }
ratios = []
for li in range(len(lines)) :
    l = lines[li]
    for ci in range(len(l)) :
        if l[ci] == '*' :
            slice1 = max(ci - 1, 0)
            slice2 = min(ci + 2, len(l))
            candidates = [ (lines[li - 1][slice1:slice2] if li > 0 else ''), l[slice1:slice2], (lines[li + 1][slice1:slice2] if li < len(lines) - 1 else '') ]
            nums = []
            for cni in range(len(candidates)) :
                candle = candidates[cni]
                fline = lines[li + cni - 1 if li + cni - 1 in range(len(lines)) else '']
                cn = 0
                while cn in range(len(candle) - 1) :
                    num = ''
                    while fline[cn + slice1] in digits and cn + slice1 >= 0 :
                        cn -= 1
                    cn += 1
                    while cn + slice1 < len(fline) and fline[cn + slice1] in digits :
                        num += fline[cn + slice1]
                        cn += 1
                    if num :
                        nums += [int(num)]
            print(nums)
            if len(nums) == 2 :
                ratios += [nums[0] * nums[1]]
#print(ratios)
print(sum(ratios))
