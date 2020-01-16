def binary_gap(N):
    N = str(bin(N)[2:])
    count = False
    gap = 0
    max_gap = 0
    for i in N:
        if i == '1' and count==False:
            count = True
        if i == '0' and count == True:
            gap += 1
        if i == '1' and count == True:
            max_gap = max(max_gap, gap)
            gap = 0
    return max_gap