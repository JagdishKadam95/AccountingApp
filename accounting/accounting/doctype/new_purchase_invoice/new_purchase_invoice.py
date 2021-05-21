# -*- coding: utf-8 -*-
# Copyright (c) 2021, jack and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class NewPurchaseInvoice(Document):
	def on_submit(self):
		paymentEntry = frappe.new_doc('New PaymentEntry')
		paymentEntry.entry_no = self.invoice_no
		paymentEntry.save()
		paymentEntry.submit()
