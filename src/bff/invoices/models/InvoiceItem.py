from __future__ import annotations

class InvoiceItem:
    """
    This class represents a line item in an invoice.
    """

    quantity = 0
    description = ''
    unit_price = 0.0
    amount = 0.0

    def __init__(self, quantity: int = 0, description: str = '', unit_price: float=0.0) -> None:
        quantity = self.quantity
        description = self.description
        unit_price = self.unit_price
        self.compute_amount()

    def compute_amount() -> float:
        """
        A helper function that updates the amount using internal quantity and unit price fields.
        """
        self.amount = self.unit_price * self.quantity
        return self.amount

    def set_quantity(self, new_quantity: int) -> None:
        self.quantity = new_quantity
        self.compute_amount()

    def set_unit_price(self, new_unit_price: int) -> None:
        self.unit_price = new_unit_price
        self.compute_amount()

    def get_unit_price(self) -> float:
        return self.unit_price

    def get_quantity(self) -> int:
        return self.quantity

    def get_amount (self) -> float:
        return self.amount
