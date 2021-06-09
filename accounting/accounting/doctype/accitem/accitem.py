# -*- coding: utf-8 -*-
# Copyright (c) 2021, jack and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime 

class AccItem(Document):
	def before_save(self):
		self.created_at = datetime.datetime.now()
		"""
			validating price 
		"""
		if self.price == 0 or not self.price :
			frappe.throw("Amount/Price cannot set to 0 or less than 0")
			
		self.created_at = datetime.datetime.now()