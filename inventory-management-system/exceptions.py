# exceptions.py
class DuplicateProductIDError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class InvalidProductDataError(Exception):
    pass
