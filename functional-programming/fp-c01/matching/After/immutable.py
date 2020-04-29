import abc

class Immutable(metaclass=abc.ABCMeta):
    __slots__ = ('__attrs__',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__attrs__ = frozenset()

    def __setattr__(self, name, value):
        if name == '__attrs__':
            super().__setattr__(name, value)
            return

        if name in self.__attrs__:
            raise AttributeError('Attempt to modify immutable attribute "%s".' % name)
        else:
            super().__setattr__(name, value)
            self.__attrs__ |= {name}

    def __delattr__(self, name):
        if name in self.__attrs__:
            raise AttributeError('Attempt to delete immutable attribute "%s".' % name)
        else:
            raise AttributeError(name)

class A(Immutable):
    def __init__(self, val):
        super().__init__()
        self.val = val
