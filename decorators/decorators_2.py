def poly(a,b,c):
    def pol(x):
        return a*x**2 + b*x + c
    return pol



ans = poly(1, 2, 3)
ans1 = ans(1)
print(ans1)
