#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items = None):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    self.quantity = quantity
    self.last_transaction = price * quantity

  def apply_discount(self):
    if self.discount > 0:
      discounted = self.total * self.discount / 100
      self.total -= discounted
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
      if hasattr(self, "last_transaction"):
        self.total -= self.last_transaction
        self.last_transaction = 0
      else:
        print("no valid transaction")

  pass
