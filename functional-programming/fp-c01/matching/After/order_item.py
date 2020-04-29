from immutable import Immutable

class OrderItem(Immutable):
    __slots__ = ('name', 'itemnumber', 'quantity', 'price', 'backordered')

    def __init__(self, name, itemnumber, quantity, price, backordered):
        super().__init__()
        self.name = name
        self.itemnumber = itemnumber
        self.quantity = quantity
        self.price = price
        self.backordered = backordered

    @property
    def total_price(self):
        return self.quantity * self.price
    