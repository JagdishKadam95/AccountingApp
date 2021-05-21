# -*- coding: utf-8 -*-
# Copyright (c) 2021, jack and contributors
# For license information, please see license.txt

# from __future__ import unicode_literals
# # import frappe
# from frappe.utils.nestedset import NestedSet

# class account(NestedSet):
# 	pass


from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet
#from random import randint
#from datetime import datetime


class account(NestedSet):
	nsm_parent_field = "parent_account"