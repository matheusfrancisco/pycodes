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
    def get_filtered_info(predicate, func):
        output = []
        for order in Order.orders:
            if predicate(order):
                output.append(func(order))
        return output
  
    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_info(
            lambda order: order.expedited,
            lambda order: order.customer.name
        )

    @staticmethod
    def get_expedited_orders_customer_addresses():
        return Order.get_filtered_info(
            lambda order: order.expedited,
            lambda order: order.customer.address
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses():
        return Order.get_filtered_info(
            lambda order: order.expedited,
            lambda order: order.shipping_address)        

    @staticmethod
    def get_not_expedited_orders_customer_names():
        return Order.get_filtered_info(
            lambda order: not order.expedited,
            lambda order: order.customer.name
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses():
        return Order.get_filtered_info(
            lambda order: not order.expedited,
            lambda order: order.customer.address
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses():
        return Order.get_filtered_info(
            lambda order: not order.expedited,
            lambda order: order.shipping_address) 