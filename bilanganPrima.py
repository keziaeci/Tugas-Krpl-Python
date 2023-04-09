def bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 30):
    if bilangan_prima(i):
        print(i)
