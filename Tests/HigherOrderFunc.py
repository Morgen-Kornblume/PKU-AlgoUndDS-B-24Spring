def square(x):
    return x * x
def inc(x):
    return x + 1
def combine(f,g,x):
    return f(g(x))
print(combine(square,inc, 4)) #>>25
print(combine(inc,square, 4)) #>>17
def combineFunctions(f,g):
    return lambda x: f(g(x)) #lambda 表达式，函数的返回值是一个函数，又是FP东西
print(combineFunctions(square,inc)(4))	#>>25
