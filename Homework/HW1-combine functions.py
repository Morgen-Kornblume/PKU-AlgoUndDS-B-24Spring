def combine(f,g):
    return lambda x: g(f(x))
def inc(x):
    return x + 1
def square(x):
    return x * x
c  = int(input())
fx = combine(inc,square)
print(fx(c))