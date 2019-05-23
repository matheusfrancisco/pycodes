from collections import UserList

class MyList(UserList):
    def __add__(self, value):
        if isinstance(value, list):
            return super().__add__(value)
        else:
            self.append(value)

    def __sub__(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            pass

