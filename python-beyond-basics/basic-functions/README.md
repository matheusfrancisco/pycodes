## Basic about functions

#### Callable instances

Callable instances and the dunders-call

use objects like a functions
```

import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


>>>python3
>>>from resolver import Resolver
>>>resolver = Resolver()
>>>resolve('google.com.br')

>>>exit()

import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

>>python3
>>>from resolver import Resolver
>>>resolver = Resolver()
>>>resolve.has_host('google.com.br')
False
>>>resolve('google.com.br')
>>>resolve.has_host('google.com.br')
True
>>>resolve.clear()
>>>resolve.has_host('google.com.br')
False
```

#### Classes are callable

Callable calsses
```

```
#### Conditional Expressions

Conditional statement
```
if condition:
   do_somthing()
else:
   do_something_else()

```
Conditional expression
```
result =  do_somthing() if condition else do_something_else()

```

#### Extended formal argument

```
def hyper(*args):
    print(args)
    print(type(args))

>> hyper(1,3)
(1,3)
<class 'tuple'>


def hyper2(*lengths):
    i = iter(lenths)
    v = next(i)
    for length in i:
        v *= length

    return v

>>hyper2(2,4)
8
>>hyper2(2,4,6)
48

>>hyper2()
Traceback .....
StopInteration


def hyper3(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v
hyper3(3,5,7,9)
945




>>> def tag(name, **attributes):
        result= '<' + name
        for key, value in attributes.items():
            result += '{k}="{v}"'.format(k=key, v=str(value))
        result += '>'
        return result

>>> tag('img', src="xico.jpg", alt="Sunrise by Xico", border=')
<img border="1" alt="Sunrise by Xico" src="xico.jpg">
```

#### Forwarding Arguments

```
>>>def trace(f, *args, **kwargs):
...    result = f(*arg, **kwargs)

>>>int("ff", base=16)
255

>>>trace(int, "ff", base=16)
255
```



