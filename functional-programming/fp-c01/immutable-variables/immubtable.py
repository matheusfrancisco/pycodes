
"""
Immutable variables cannot change

Two rules:
    Local variables do not change
    * locals() immutable
    Gobal variables can only change references
    * globlas()

"""


#Wrong away
pi = 3.14

def change_pi(pi):
    pi = 2.71828

print(pi)
change_pi(pi)
print(pi)


#Bad parctices
def change_pi_global(*args, **kwargs):
    global pi
    pi = 2.7

print(pi)
change_pi_global(pi)
print(pi)


