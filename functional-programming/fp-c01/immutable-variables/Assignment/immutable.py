import abc

class Immutable(metaclass=abc.ABCMeta):
    """Any class that wants to be immutable can
    inherit from this. Let me walk tou through

    __slots__ : no new attributes can be created after
    instancianted 
    """
    __slots__ = ('__attrs__',)

    def __init__(self, *args, **kwargs):
        """call super class and initialize attrs
          in fronzenset
        """
        super().__init__(*args, **kwargs)
        self.__attrs__ = frozenset()

    def __setattr__(self, name, value):
        if name == '__attrs__':
            super().__setattr__(name, value)
            return

        "if attrs exist I raise a error"
        if name in self.__attrs__:
            raise AttributeError('Attempt to modify immutable attribute "%s".' % name)
        else:
            super().__setattr__(name, value)
            self.__attrs__ |= {name}

    """
      We don't want deleted
    """
    def __delattr__(self, name):
        if name in self.__attrs__:
            raise AttributeError('Attempt to delete immutable attribute "%s".' % name)
        else:
            raise AttributeError(name)

class A(Immutable):
    def __init__(self, val):
        super().__init__()
        self.val = val
