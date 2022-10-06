def inc(x):
    return x*2
def dec(x):
    return x/2
def opt(func,x):
    rst=func(x)
    return rst
print(opt(inc,4))
print(opt(dec,4))            