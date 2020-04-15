## Closures and Decorators


#### Functoin from Functions

Functions can be treated like any other object, pass to another function HOF


#### Closures and Nested Scopes

Closures essentially remembers the objects from the
enclosing scope the local functinos needs. It then
keeps them alive so that when local function is
executed they can still be used.


See [here](./enclosing.py)

#### Function Factories

A very common use for closures is in so-called function
factories. These factories are functions that return other
functions where the returned functions are specialized in some
way based on argumentsa. It then creates a local function,
which takes its own arguments, but also uses the arguments
passed to the factory. The combination of runtime function definition
enclosures makes this possible. A typical example of this
kind of factory creates a functions, which raises numbers to
a particular power.
Here's how the factory looks.

```
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


square = raise_to(2)
square.__closure___
(<cell at 0x1064e2b40: int object at 0x10604f030>)

square(5)
25

```

#### The Nonlocal keyword

nonlocal introduce names from the enclosing namespace..

See [here](./enclosing.py)
See [here](./make_timer.py)

#### Decorators

At a hihg level decorators are a way to modify or
enhance existing functions in a nonintrusive and
maintanable way.

In python a decorator is a callable object that takes
in a callable and returns a callable. If that sounds a
a bit abstract, it might be a simpler for now


```
@my_decorator
def my_functions(x, y):
    return x + y
```
My functions is a functions object. Python then passes
this functinos (my_function object to the) my_decorator

```
my_decorator(f):
  ...
  return new_f

```

* Replace, enhance, or modify existing functions
* Does not change the original function definition
* Calling code does not need to change
* Decorator mechanism uses the modified function' to original name

```

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city():
    return 'Tromsø'

```

```
class MyDec:
    def __init__(self, func):
        ....

    def __call___(sefl):
        ....

@MyDec
def func():
    ....


```

```

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello, {}'.format(name))

hello('xico')
hello('xico')
hello('xico')

hello.count
3

```

Another example is class instance

```
class AnthoerDec:
      def __call__(self, f):
          def wrap():
              ...
          return wrap

@AnotherDec()
def func():
    ...

```

example

```

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = rotate_list()
l

tracer.enabled = False
```

multiple decorators

```
@decorator1
@decorator2
@decorator3
def some_function():
    ...
```


See [here an example](./island_maker.py)



functools.wrap()

See [here an example](./noop.py)


#### decorators use to validate args
```
def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size
```

####
