from order1 import Order
from customer import Customer

def main():
    cust1 = Customer()
    cust1.name = 'Heart of Gold'
    cust1.address = 'The Milky Way Galaxy'
    cust1.enterprise = False
    cust2 = Customer()
    cust2.name = 'Milliways Restaurant'
    cust2.address = 'Magrathea'
    cust2.enterprise = True

    ord1 = Order()
    ord1.orderid = 1
    ord1.customer = cust1
    ord1.expedited = False
    ord1.shipping_address = 'Infinitely Improbable'

    ord2 = (Order())
    ord2.orderid = 2
    ord2.customer = cust2
    ord2.expedited = True
    ord2.shipping_address = 'Magrathea'

    Order.orders = [ord1, ord2]
    for name in ord1.get_expedited_orders_customer_names(Order.orders):
        print(name)
    for address in ord1.get_expedited_orders_customer_addresses(Order.orders):
        print(address)
    for address in ord1.get_expedited_orders_shipping_addresses(Order.orders):
        print(address)

    Order.set_order_expedited(1, Order.orders)

main()
