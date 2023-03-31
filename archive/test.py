def fiba(n):
    if n <= 1:
        return n
    seq = [0, 1]

    for i in range(n):
        seq.append(seq[-1]+seq[-2])
        print(seq)

    return seq[n]


def fib_b(n):
    if n <= 1:
        return n

    prev_2 = 0
    prev = 1

    for _ in range(n - 1):
        prev_2,prev = prev, prev + prev_2

    return prev


def fib_c(n):
    if n <= 1:
        return n
    return fib_c(n-1) + fib_c(n - 2)
# fib_b(4)
fib_c(4)
#%%
