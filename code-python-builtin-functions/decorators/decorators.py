def outside_function():
    def inside_function():
        print("I am the inside function")

    print("Hey, I am the outside function")
    print("Above inside function")
    inside_function()
    print("Below inside function")


# outside_function()

def addition(a, b):
    def add(x,y):
        return x + y

    sum = f'the Sum of two no,s is {add(a,b)}'

    return sum

# print(addition(2, 3))


def x(func):
    print("I am the function x")

def y():
    print("Hi I am the function y")


#x(y())


def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function


z = outer_function(2)
v = outer_function(2)

ans1 = z(4)
ans2 = v(5)

print(ans1, ans2)

