# -*- coding: utf-8 -*-
# Copyright (c) 2021, jack and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
class Purchase_invoice(Document):
    def on_submit(self):
		Payment_entry = frappe.new_doc('AccPayment_entry')
        Payment_entry.party_name = self.suplier_name
		payment_entry.party_type = self.payment_type
		payment_entry.account_details = self.account_no
		payment_entry.payment_mode = self.payment_mode
		payment_entry.salespurchase_invoice_no = self.purchase_unique_no
		payment_entry.date = self.datesuplier_invoice_date
		payment_entry.save()
		payment_entry.submit()
 