# Annotations about modules and pacakges

Packages are modules that contain other modules.

Packages are generally implmemented as directories containing a special ```__init__.py``` .

The ```__init__.py``` files is executed when the package is imported

Packages can contain sub packages which themselves are implemented with ``` __init__.py ``` in files directories


### Absolut and realtive imports

```
my_package/
|--__init__.py
|--a.py
|__nested/
   |--__init__.py
   |--b.py
   |--c.py

```

In c.py you can use imports realives:
to import A ``` from ..a import A ```
to import B ``` from .b import B ```



In folder [farm](./farm)


```
farm/
|--__init__.py
|__ bird/
|   |--__init__.py
|   |--chicken.py
|   |--turkey.py
|__ bovine/
    |--__init__.py
    |--cow.py
    |--ox.py
    |--comman.py

```

If you want to import comman.py in cow. You can use relative imports ``` from .comman import ruminate ```
or you can use absolute import ``` from farm.bovine.common import ruminate ```.

You can import ``` form . import comman``` use this in which case the ruminate  function would need to be qualified with comman when
you call it. It's easy to see ``` comman.ruminate() ```



Relative imports

1. Can reduce typing in deepl nested package structures
2. Promote certain forms of modifiability
3. Can aid package renaming and refactoring


Dunder-all

Annother topic is dunder-all list of attribute names imported via from module import *
if dunder-all is not specified, then from X  import * imports all public names

for example in [reader](./reader) in compressed dunder-init you add
```
from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']
```

Now when you user
```
>>> from reader.compressed import *
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
'bz2_opener': <function open at 0x7f918b5bee50>, 'gzip_opener': <function open at 0x7f918b591040>}

```
you have two functions bz2 and gzip



Namespace packages (PEP420)

packages split across several directories

Namespace packages have no dunder init.py this avoids complex initialization ordering problems


It means that namespace packages can't have package level initialization code. Nothing  will be executed by the
package when it's imported. The reason for this limitation is primarily that it avoids complex questions of initialization
order when multiple directories contribute to a package. But if namespace packages don't have dunder init.py  ``` __init__.py```.

How does python find namespace packages?
R: Python follows a relatively simple algorithm to detect namespace packages.

When asked to import the name foo, Python scans each of the entries in sys.path in order.

If in any of these directories it finds a directory named foo containing then normal package is imported

If foo.py is found, then it is loaded.

Otherwise, all matching directories in sys.path are considered part of the namespace package.


Example: [splited](./splited)

```
path1/
|____split_farm/
      |__ bovine/
      |--__init__.py
      |--cow.py
      |--ox.py
      |--comman.py

path2/
|___split_farm/
    |__ bird/
        |--__init__.py
        |--chicken.py
        |--turkey.py

```

Now to import farm make sure that both path1 and path2 are in your sys.path

```
>>>python3
>>>import sys
>>>sys.path.extend(['path1', 'path2'])

```
Now you can import split_farm

```
>>> import split_farm
>>> split_farm.__path__
_NamespacePath(['path1/split_farm', 'path2/split_farm'])
>>> import split_farm.bird
>>> import split_farm.bovine
>>> split_farm.bird.__path__
['path2/split_farm/bird']
>>> split_farm.bovine.__path__
['path1/split_farm/bovine']

```
to need more http://www.python.org/dev/peps/pep-0420/




Executable directories

directories containing an entry point for Python execution

in reader dunder-main.py ``` __main__.py ``` when you executed
```
>>> python3  reader test.gz
data compressed with gzip

```

Executable zip file
zip file containing an entry point for Python execution


## Recommended project structure  basics

This directory isn't a package. If you intend to make your package executable included dunder main.py

```
project_name/
|---- __main__.py
|____ project_name/
|     |-- __init__.py
|     |-- more_source.py
|     |-- subpackage1.py
|     |  |-- __init__.py
|     |__ test/
|         |-- __init__.py
|         |-- test_code.py
|____ setup.py
```
