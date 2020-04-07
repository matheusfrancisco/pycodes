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
    """
      Start refactoring function

      but this functions looks like map function
    """
        return list(filter(predicate, it))

    @staticmethod
    def map(func, it):
    """
      look in iteertools (python)
    """
        return list(map(func, it))

    @staticmethod
    def get_filter_info(predicate, func, orders):
        return Order.map(func, Order.filter(predicate, orders))

    @staticmethod
    def get_order_by_id(orderid, orders):
        return list(filter(lambda order: order.orderid == orderid, orders))

    @staticmethod
    def set_order_expedited(order, orders):
        for order in Order.get_order_by_id(orderid, orders):
            order.expedited = True
    
    """
      Need refactoring filtered info to single responsability principles

    """
    @staticmethod
    def get_filtered_info(predicate, func):
        output = []
        for order in Order.orders:
            if predicate(order):
                output.append(func(order))
        return output

  
    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_expedited_orders_customer_addresses():
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_address
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses():
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_shipping_address)        

    @staticmethod
    def get_not_expedited_orders_customer_names():
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses():
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_address
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses():
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_shipping_address) 

    @staticmethod
    def set_order_expedited(orderid):
        for order in Order.orders:
            if order.orderid == orderid:
                order.expedited = True

    @staticmethod
    def get_order_by_id(orderid):
        for order in Order.orders:
            if order.orderid == orderid:
                return order

    @staticmethod
    def get_order_by_id(orderid):
        return Order.get_filtered_info(
            lambda order: order.orderid == orderid,
            lambda order: order
        )

    @staticmethod
    def set_order_expedited(orderid):
        for order in Order.get_order_by_id(orderid):
            order.expedited = True
