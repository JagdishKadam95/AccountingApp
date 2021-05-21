// Copyright (c) 2016, jack and contributors
// For license information, please see license.txt
/* eslint-disable */

// frappe.query_reports["GL Report"] = {
// 	"filters": [

// 	]
// };


frappe.query_reports["GL Report"] = {
	"filters": [
		{
			"fieldname": "transaction_date",
			"fieldtype": "Datetime",
			"in_list_view": 1,
			"label": "Transaction Date"
		   },
		   {
			"fieldname": "account",
			"fieldtype": "Data",
			"label": "Account"
		   },
		   {
			"fieldname": "fiscal_year",
			"fieldtype": "Data",
			"label": "Fiscal Year",
			"options": "Fiscal Year"
		   },
		   {
			"fieldname": "voucher_type",
			"default": "All",
			"fieldtype": "Select",
			"label": "Voucher Type",
			"options": "AccPurchase_invoice\nAccSales_invoice"
		   },
		   {
			"fieldname": "created_at",
			"fieldtype": "Date",
			"label": "Created At"
		   }
	]
};