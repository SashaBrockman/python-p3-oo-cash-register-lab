#!/usr/bin/env python3

class CashRegister:
	def __init__(self, discount = 0):
		self.discount = discount
		self.total = 0
		self.items = []
		self.last_total = 0

	@property
	def discount(self):
		"""The discount property"""
		return self._discount
	
	@discount.setter
	def discount(self, discount):
		"""The discount setter"""
		self._discount = discount

	@property
	def total(self):
		"""The total property"""
		return self._total
	
	@total.setter
	def total(self, total):
		"""The total setter"""
		self._total = total

	@property
	def items(self):
		"""The items property"""
		return self._items
	
	@items.setter
	def items(self, items):
		"""The items setter"""
		self._items = items

	@property
	def last_total(self):
		"""The total property"""
		return self._last_total
	
	@last_total.setter
	def last_total(self, last_total):
		"""The total setter"""
		self._last_total = last_total

	def add_item(self, item, cost, quantity = 1):
		new_items = [item] * quantity
		self._items.extend(new_items)
		self._last_total = cost * quantity
		self._total = float(self.total + self._last_total)

	def apply_discount(self, discount = 20):
		if self._total != 0:
			self._total = float(self._total) * ((100 - discount) / 100)
			print(f"After the discount, the total comes to ${int(self.total)}.")
		else:
			print("There is no discount to apply.")

	def void_last_transaction(self):
		self._total -= self._last_total