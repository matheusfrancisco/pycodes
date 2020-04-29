from immutable import Immutable
from order_item_1 import OrderItem
from functools import lru_cache, reduce

def get_updated_tuple(predicate, func, it):
    return tuple(
        func(i) if predicate(i) else i
        for i in it
    )

class Order(Immutable):
    __slots__ = ('orderid', 'shipping_address','expedited', 
                'shipped', 'customer', 'order_items') #, 'total_price')
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
        #self.total_price = sum(i.total_price for i in self.order_items)

    @property
    # @lru_cache(maxsize=1)
    def total_price(self):
        return sum(i.total_price for i in self.order_items)
        # return reduce(lambda acc, i: acc + i.total_price, self.order_items, 0)

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
                )
            ),
            orders
        )

    @staticmethod
    def notify_backordered(orders, msg):
        # Imperative, explicit iteration
        for o in orders:
            for i in o.order_items:
                if i.backordered:
                    o.customer.notify(o.customer, msg)

    @staticmethod
    def notify_backordered(orders, msg):
        # Functional, implicit iteration
        Order.map(lambda o: o.customer.notify(o.customer, msg),
            Order.filter(lambda o: Order.filter(
                    lambda i: i.backordered, o.order_items),
                orders
                )
            )

    @staticmethod
    def notify_backordered(orders, msg):
        # Functional version, using previously-written function
        Order.get_filtered_info(
            lambda o: any(i.backordered for i in o.order_items),
            lambda o: o.customer.notify(o.customer, msg),
            orders
        )
    
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
        return list(filter(predicate, it))

    @staticmethod
    def map(func, it):
        return list(map(func, it))  

    @staticmethod
    def get_filtered_info(predicate, func, orders):
        return Order.map(func, Order.filter(predicate, orders))
  
    @staticmethod
    def get_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_address
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_shipping_address)        

    @staticmethod
    def get_not_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_address
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_shipping_address) 
