# inventory.py
from utils import DuplicateProductIDError, InsufficientStockError, InvalidProductDataError, parse_date

from product import Electronics, Grocery, Clothing
from exceptions import DuplicateProductIDError, OutOfStockError
import json

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product._product_id in self._products:
            raise DuplicateProductIDError("Product ID already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        self._products.pop(product_id, None)

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p._name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.__class__.__name__.lower() == product_type.lower()]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id not in self._products:
            raise KeyError("Product ID not found.")
        try:
            self._products[product_id].sell(quantity)
        except ValueError:
            raise OutOfStockError("Not enough stock to sell.")

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        expired_ids = [pid for pid, p in self._products.items() if isinstance(p, Grocery) and p.is_expired()]
        for pid in expired_ids:
            del self._products[pid]

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump([p.to_dict() for p in self._products.values()], f)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                type_ = item.pop("type")
                if type_ == "Electronics":
                    product = Electronics(**item)
                elif type_ == "Grocery":
                    product = Grocery(**item)
                elif type_ == "Clothing":
                    product = Clothing(**item)
                else:
                    raise ValueError("Unknown product type")
                self._products[product._product_id] = product
