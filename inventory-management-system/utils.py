class DuplicateProductIDError(Exception):
    """Raised when a product with duplicate ID is added to inventory."""
    def __init__(self, product_id):
        message = f"Product with ID '{product_id}' already exists in inventory."
        super().__init__(message)


class InsufficientStockError(Exception):
    """Raised when trying to sell more than available stock."""
    def __init__(self, requested, available):
        message = f"Insufficient stock. Requested: {requested}, Available: {available}"
        super().__init__(message)


class InvalidProductDataError(Exception):
    """Raised when loaded product data is invalid or missing required fields."""
    def __init__(self, message="Invalid product data found in file."):
        super().__init__(message)


from datetime import datetime

def parse_date(date_str):
    """
    Converts a string in 'YYYY-MM-DD' format to a date object.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date format must be YYYY-MM-DD")  