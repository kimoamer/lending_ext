import frappe
import frappe.utils


def fix_Loan_Repayment_Schedule():
    loans = frappe.db.get_list("Loan",{"docstatus":1},pluck="name",ignore_permissions=True)
    for loan in loans:
        lrse = frappe.db.exists("Loan Repayment Schedule",{"loan":loan})
        if lrse:
            try:
                # Fetch the parent document
                parent_doc = frappe.get_doc("Loan Repayment Schedule", lrse)  # Replace with actual parent document name
                updated_data = frappe.db.get_list("Repayment Schedule",filters={"parent":loan},fields=["modified","modified_by","owner","docstatus","idx","payment_date","principal_amount","interest_amount","total_payment","balance_loan_amount","is_accrued"],ignore_permissions=True)
                # Loop through the updated data and append to the child table
                if len(parent_doc.repayment_schedule) = 0:
                    for entry in updated_data:
                        parent_doc.append("repayment_schedule", {
                            "modified": entry.get("modified"),
                            "modified_by": entry.get("modified_by"),
                            "owner": entry.get("owner"),
                            "docstatus": entry.get("docstatus"),
                            "idx": entry.get("idx"),
                            "payment_date": entry.get("payment_date"),
                            "principal_amount": entry.get("principal_amount"),
                            "interest_amount": entry.get("interest_amount"),
                            "total_payment": entry.get("total_payment"),
                            "balance_loan_amount": entry.get("balance_loan_amount"),
                            "is_accrued": entry.get("is_accrued"),
                        })

                    # Save the parent document to persist changes
                    parent_doc.save()
                    frappe.db.commit()
            except Exception as e:
                frappe.db.rollback()
