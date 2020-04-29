from immutable import Immutable
from order_item import OrderItem
from functools import lru_cache
from customer import Customer
from collections import Iterable

def get_update_seq(it, predicate, func):
    return (
        func(i) if predicate(i) else i
            for i in it
    )

class Order(Immutable):
    __slots__ = ('orderid', 'shipping_address','expedited', 
                 'shipped', 'customer', 'order_items')
    # class attribute
    orders = ()

    def __init__(self, orderid, shipping_address, expedited, shipped, customer, order_items):
        super().__init__()
        if not isinstance(orderid, int):
            raise ValueError('Invalid order id.')
        if not isinstance(shipping_address, str) or shipping_address == '':
            raise ValueError('Invalid shipping address.')
        if not isinstance(expedited, bool):
            raise ValueError('Invalid expedited indicator')
        if not isinstance(shipped, bool):
            raise ValueError('Invalid shipped indicator')
        if not isinstance(customer, Customer):
            raise ValueError('Invalid customer reference.')
        if not isinstance(order_items, Iterable):
            raise ValueError('Invalid order items collection. Not iterable')
        if not all(isinstance(i, OrderItem) for i in order_items):
            raise ValueError('Invalid order items collection. Not all order items')
        
        self.orderid = orderid
        self.shipping_address = shipping_address
        self.expedited = expedited
        self.shipped = shipped
        self.customer = customer
        self.order_items = order_items
        # self.total_price = sum(i.total_price for i in self.order_items)
        
    @staticmethod
    def count_expedited_orders_with_backordered_items_tramp(orders, acc=0):
        """ 
            Sample call using tramp function:
                tramp(count_expedited_orders_with_backordered_items_tramp, orders)
        """
        if len(orders) == 0:    # also: if not orders:
            yield acc
        else:
            h = orders[0]
            add = 1 if any(i.backordered for i in h.order_items if h.expedited) else 0
            yield Order.count_expedited_orders_with_backordered_items_tramp(orders[1:], acc + add)  

    @staticmethod
    def count_expedited_orders_with_backordered_items_comp(orders):
        return sum(1 for o in orders if o.expedited and
                any(i.backordered for i in o.order_items))

    @property
    @lru_cache(maxsize=1)
    def total_price(self):
        return sum(i.total_price for i in self.order_items)
        # return reduce(lambda acc, i: acc  i.total_price, self.order_items, 0)

    @staticmethod
    def mark_backordered(orders, orderid, itemnumber):
        return tuple(
            get_update_seq(orders,
                lambda o: o.orderid == orderid,
                lambda o: 
                    Order(o.orderid, o.shipping_address, o.expedited, o.shipped, o.customer,
                        Order.mark_backordered_items(o.order_items, itemnumber)
                    )   
            )
        )

    @staticmethod
    def mark_backordered_items(items, itemnumber):
        return tuple(
            get_update_seq(items,
                lambda i: i.itemnumber == itemnumber,
                lambda i: OrderItem(i.name, i.itemnumber, i.quantity, i.price, True)
            )
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
