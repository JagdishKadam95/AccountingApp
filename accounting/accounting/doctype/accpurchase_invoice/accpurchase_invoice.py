# -*- coding: utf-8 -*-
# Copyright (c) 2021, jack and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from datetime import date
from frappe.model.document import Document
class AccPurchase_invoice(Document):
	def on_submit(self):
		""" Saving data/ entry for purchase in AccPayment_entry doctype"""
		payment_entry = frappe.new_doc('AccPayment_entry')
		payment_entry.party_name=self.suplier_name 
		payment_entry.party_type = self.payment_type
		payment_entry.account_no = self.account_no
		payment_entry.payment_mode = self.payment_mode
		payment_entry.salespurchase_invoice_no = self.purchase_unique_no
		payment_entry.date = self.date
		payment_entry.save()
		payment_entry.submit()
		journal_entry = frappe.new_doc('AccJournal_entry')
		journal_entry.journal_entry_unique_no = self.purchase_unique_no
		journal_entry.account = self.account_no
		journal_entry.posting_date = self.date
		journal_entry.total_amount = self.total_amount
		journal_entry.save()
		journal_entry.submit()

		""" Saving data/ entry for purchase in general ledger"""
		general_ledger = frappe.new_doc('General Ledger')
		general_ledger.transaction_date = self.date
		general_ledger.account = self.account_no
		general_ledger.voucher_type = "AccPurchase_invoice"
		general_ledger.debit = self.total_amount
		general_ledger.credit = 0.00
		general_ledger.fiscal_year = self.date
		general_ledger.created_at = date.today()
		general_ledger.save()
		general_ledger.submit()