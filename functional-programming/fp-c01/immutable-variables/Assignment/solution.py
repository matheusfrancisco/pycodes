from immutable import Immutable
from order_item import OrderItem

def get_updated_tuple(it, predicate, func):
    return tuple(
        func(i) if predicate(i) else i
        for i in it
    )

def get_filtered_tuple(it, predicate, func):
    return tuple(
        func(i) for i in it if predicate(i)
    )

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
        return Order.map(lambda o:

            # copy all orders that do not match the orderid
            o if o.orderid != orderid
                
            # otherwise build a new order with a new order item list
            else (Order(o.orderid, o.shipping_address, o.expedited, o.shipped, o.customer,
                        Order.map(lambda i:
                            # copy the items that don't match
                            item if i.itemnumber != itemnumber
    
                            # otherwise build a new order item setting backordered to True
                            else OrderItem(i.name, i.itemnumber, i.quantity, i.price, True),
    
                            # iterate over all order items
                            o.order_items)
                        )),
                # iterate over all orders
                orders
            )

    @staticmethod
    def mark_backordered(orders, orderid, itemnumber):
        return get_updated_tuple(
            orders,
            lambda o: o.orderid == orderid,
            lambda o: 
                Order(o.orderid, o.shipping_address, o.expedited, o.shipped, o.customer,
                get_updated_tuple(
                    o.order_items, 
                    lambda i: i.itemnumber == itemnumber,
                    lambda i: OrderItem(i.name, i.itemnumber, i.quantity, i.price, True)
                )
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
        get_filtered_tuple(orders,
            lambda o: any(i.backordered for i in o.order_items),
            lambda o: o.customer.notify(o.customer, msg)
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
        return tuple(filter(predicate, it))

    @staticmethod
    def map(func, it):
        return tuple(map(func, it))  

    # @staticmethod
    # def get_filtered_tuple(predicate, func, orders):
    #     return Order.map(func, Order.filter(predicate, orders))
  
    @staticmethod
    def get_expedited_orders_customer_names(orders):
        return Order.get_filtered_tuple(orders,
            Order.test_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_expedited_orders_customer_addresses(orders):
        get_filtered_tuple(orders,
            Order.test_expedited,
            Order.get_customer_address
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses(orders):
        get_filtered_tuple(orders,
            Order.test_expedited,
            Order.get_shipping_address)        

    @staticmethod
    def get_not_expedited_orders_customer_names(orders):
        get_filtered_tuple(orders,
            Order.test_not_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses(orders):
        get_filtered_tuple(orders,
            Order.test_not_expedited,
            Order.get_customer_address
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses(orders):
        get_filtered_tuple(orders,
            Order.test_not_expedited,
            Order.get_shipping_address) 