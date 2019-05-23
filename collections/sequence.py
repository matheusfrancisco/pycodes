from collections.abc import Container, Iterable, Sized
from collections.abc import Sequence

class MySequence(Container, Iterable, Sized):
    def __init__(self, *seq):
        self.seq = seq

    def __contains__(self, val):
        return val in self.seq

    def __iter__(self):
        return iter(self.seq)

    def __len__(self):
        return len(self.seq)


class MySeq(Sequence):
    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, pos):
        return self.seq[pos]



