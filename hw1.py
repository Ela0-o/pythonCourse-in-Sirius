# import math as m
def get_seq_len(a0):
    if isinstance(a0, int) and a0 > 0:
        n = 1
        while a0 > 1:
            if a0 % 2 == 0:
                a0 = a0 // 2
            else:
                a0 = 3 * a0 + 1
            n += 1
        return n
    else:
        return None

def get_longest_seq(L, U):
    if isinstance(L,int) and isinstance(U,int) and U > L > 0:
        lenMax = 0
        for a0 in range(L, U + 1):
            x = get_seq_len(a0)
            if x > lenMax:
                lenMax = x
                aMax = a0
    else:
        return None
    # maxF = lenMax-m.log2(a0)
    return aMax, lenMax

print(get_longest_seq(1, 1000))