import collections
import functools

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

class Order:
    # class attribute
    orders = []

    # instance attributes
    orderid = 0
    shipping_address = ''
    expedited = False
    shipped = False
    customer = None

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
    def filter(predicate,it):
        return list(filter(predicate, it))

    @staticmethod
    def map(func, it):
        return list(map(func, it))

    @staticmethod
    def get_filtered_info(predicate, func, orders):
        return Order.map(func, Order.filter(predicate, orders))

    @staticmethod
    def get_filtered_info_lc(predicate, func, it):
        return [func(x) for x in it if predicate(x)]

    @staticmethod
    def get_filtered_info_curried(predicate, func, orders):
        return Order.map(func, Order.filter(predicate, orders))

    @staticmethod
    def get_order_by_id(orderid, orders):
        return list(Order.filter(lambda order: order.orderid == orderid, orders))

    @staticmethod
    def get_order_by_id_lc(orderid, orders):
        return [x for x in orders if x.orderid == orderid]

    @staticmethod
    def set_order_expedited(orderid, orders):
        for order in Order.get_order_by_id(orderid, orders):
            order.expedited = True

    @staticmethod
    def set_expedited(order):
        order.expedited = True

    @staticmethod
    def set_order_expedited_map(orderid, orders):
        consume(Order.map(Order.set_expedited, 
            Order.filter(lambda x: x.orderid == orderid, orders)))

    @staticmethod
    def get_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_address,
            orders
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_shipping_address,
            orders
        )        

    @staticmethod
    def get_not_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_address,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_shipping_address,
            orders
        ) 
