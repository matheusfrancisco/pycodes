from immutable import Immutable
from order_item import OrderItem

def get_updated_tuple(predicate, func, it):
    return tuple(
        func(i) if predicate(i) else i
        for i in it
    )

def get_filtered_tuple(predicate, func, it):
    return tuple(
        func(i) for i in it if predicate(i)
    )

def consume(it):
    collections.deque(it, maxlen=0)    

class Order(Immutable):
    __slots__ = ('orderid', 'shipping_address','expedited', 
                'shipped', 'customer', 'order_items')
    # class attribute
    orders = ()

    def __init__(self, orderid, shipping_address, expedited, shipped, customer, order_items):
        super().__init__()
        self.orderid = orderid
        self.shipping_address = shipping_address
        self.expedited = expedited
        self.shipped = shipped
        self.customer = customer
        self.order_items = order_items

    @staticmethod
    def mark_backordered(orders, orderid, itemnumber):
        return get_updated_tuple(
            lambda o: o.orderid == orderid,
            lambda o: 
                Order(o.orderid, o.shipping_address, o.expedited, o.shipped, o.customer,
                get_updated_tuple(
                    lambda i: i.itemnumber == itemnumber,
                    lambda i: OrderItem(i.name, i.itemnumber, i.quantity, i.price, True),
                    o.order_items
                ),
             ),
            orders
        )

    @staticmethod
    def notify_backordered(orders, msg):
        # Functional version, using previously-written function
        consume(get_filtered_tuple(
            lambda o: any(i.backordered for i in o.order_items),
            lambda o: o.customer.notify(o.customer, msg),
            orders
        ))
    
    @staticmethod
    def test_expedited(order):
        return order.expedited

    @staticmethod
    def test_not_expedited(order):
        return not order.expedited

    @staticmethod
    def get_customer_name(order):
        return order.customer.name

    @staticmethod
    def get_customer_address(order):
        return order.customer.address

    @staticmethod
    def get_shipping_address(order):
        return order.shipping_address     

    @staticmethod
    def filter(predicate, it):
        return tuple(filter(predicate, it))

    @staticmethod
    def map(func, it):
        return tuple(map(func, it))  

    @staticmethod
    def get_expedited_orders_customer_names(orders):
        return Order.get_filtered_tuple(
            Order.test_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_expedited_orders_customer_addresses(orders):
        return get_filtered_tuple(
            Order.test_expedited,
            Order.get_customer_address,
            orders
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses(orders):
        return get_filtered_tuple(
            Order.test_expedited,
            Order.get_shipping_address,
            orders
        )        

    @staticmethod
    def get_not_expedited_orders_customer_names(orders):
        return get_filtered_tuple(
            Order.test_not_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses(orders):
        return get_filtered_tuple(
            Order.test_not_expedited,
            Order.get_customer_address,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses(orders):
        return get_filtered_tuple(
            Order.test_not_expedited,
            Order.get_shipping_address,
            orders
            ) 