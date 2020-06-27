from __future__ import annotations
from . import InvoiceItem

class Invoice:
    line_items = []
    invoice_date = None
    due_date = None
    total_due = 0.0
    invoice_number = ''
    po_number = ''

    def __init__(self, invoice_number: string = '', due_date: string = '', ) -> None:
        pass

    def add_item(self, new_item: InvoiceItem) -> None:
    	self.line_items.append(new_item)
    	self.compute_total()

    def compute_total(self) -> None:
    	new_total = 0.0
    	for item in self.line_items:
    		new_total = new_total + item.amount

    def get_num_line_items(self) -> int:
    	return len(self.line_items)

    def get_total_due(self) -> float:
    	return self.total_due

    def get_invoice_number(self) -> str:
        return self.invoice_number

    def get_po_number(self) -> str:
        return self.po_number

    def get_item_by_index(self, index: int) -> InvoiceItem:
        return self.line_items[index]


