"""

Order processing system
Order
Order Items
Customer

Indicators
  - Expedited
  - Shipped
  - Enterprise customer
  - Item backordered

State information
  - Order id
  - Shipping address
"""

class Order:
  orders = []
  orderid = 0
  shipping_address = ''
  expedited = False
  shipped = False
  customer = None


  """
    Some problems methods looks like igual.. (DRY)
    each code create a empty list uses an if statement to check the
    condidtion, appends the itens in the list if condition is true

    DRY - don't repeat yourself
  """
  def get_expedited_orders__custormers_names(self):
    output = []
    for oder in Order.orders:
        if order.expredited:
              output.append(order.customer.name)
    return output


  def get_expedited_orders_custormers_addresses(self):
    output = []
    for oder in Order.orders:
        if order.expredited:
              output.append(order.customer.address)
    return output

  def get_expedited_orders_shipping_addresses(self):
    output = []
    for oder in Order.orders:
        if order.expredited:
              output.append(order.shipping_address)
    return output


"""
Higher Order Functions in python (HOF)

A higher order function is one that takes a function as a
parameter or returns a function as a result, or both

Example
"""

def f(x):
    return x + 2

def g(h, x):
    return h(x) * 2

# Function composition
print(g(f,42))



#Closure
def addx(x):
    def _(y):
        return x + y
    return _

add2 = addx(3)
add3 = addx(2)


print(add2(2), add3(3))


def f(x, y):
    return x*y

def f2(x):
    def _y(y):
        return f(x, y)
    return _

# Take function many arguments and reduce step by step
#Currying
print(f2(2))
print(f2(2)(3))


"""
Refactoring OrderClass

"""
class Order:
  orders = []
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
