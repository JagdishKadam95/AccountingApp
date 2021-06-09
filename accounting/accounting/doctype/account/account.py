# -*- coding: utf-8 -*-
# Copyright (c) 2021, jack and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import datetime
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet
class account(NestedSet):
	#pass
	nsm_parent_field = "parent_account"
	def before_save(self):
		self.created_at = datetime.datetime.now()
		"""
			to validate the entered account with or without account number.
		"""
		
		if not self.account_no:
			frappe.throw("account withount account number is unacceptable")

		self.created_at = datetime.datetime.now()	