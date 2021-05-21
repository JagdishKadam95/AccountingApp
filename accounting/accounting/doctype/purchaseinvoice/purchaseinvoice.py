from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
class PurchaseInvoice(Document):
	print('**************hello')
    def on_submit(self):
		print('***********hi')
        payment_entry = frappe.new_doc('accpayment_entry')
        payment_entry.party_name = self.suplier_name
		payment_entry.payment_type = self.payment_type
		payment_entry.account_no = self.account_no
		payment_entry.payment_mode = self.payment_mode
		payment_entry.salespurchase_invoice_no = self.purchase_unique_no
		payment_entry.date = self.datesuplier_invoice_date
		payment_entry.save()
		payment_entry.submit()