def calc(n : int):
    a = []
    for i in range(0, 1030):
        a.append(0)
    a[0] = 1
    for i in range(0, 2 ** n):
        for j in range(1, 2 ** n - i):
            print(" ", end = "")
        for j in range(i, -1, -1):
            a[j] ^= a[j - 1]
        if( i % 2 == 0):
            for j in range(0, i + 1):
                if(a[j] == 1): print("/\\", end = "")
                else : print("  ", end = "")
        else:
            for j in range(0, i + 1, 2):
                if(a[j] == 1): print("/__\\", end = "")
                else: print("    ", end = "")
        print("")
    print("")

while True:
    n = int(input())
    if(n == 0): break
    calc(n)
    