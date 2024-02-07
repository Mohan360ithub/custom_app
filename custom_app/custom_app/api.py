from frappe import _
import frappe
import urllib.parse

@frappe.whitelist(allow_guest=True)
def process_form_data(form_data):

    try:
        
        name = frappe.form_dict.get("name")
        email = frappe.form_dict.get("email")
        phone_no = frappe.form_dict.get("phone")
        subject = frappe.form_dict.get("subject")
        message = frappe.form_dict.get("message")

        # Debugging: Print the values to check if they are correct
        # frappe.msgprint("field1 ==> " + str(name1) + " and field2 = " + str(email))
        # pass
        # frappe.msgprint(form_data)
        parsed_data = urllib.parse.parse_qs(form_data)
        # frappe.msgprint(parsed_data)

        # Extract values
        # csrf_token = parsed_data.get("csrf_token", [None])[0]
        name = parsed_data.get("name", [None])[0]
        email = parsed_data.get("email", [None])[0]
        phone_no = parsed_data.get("phone", [None])[0]
        subject = parsed_data.get("subject", [None])[0]
        message = parsed_data.get("message", [None])[0]

        # frappe.msgprint("field1 ==> "+name1+" and field2 = "+ email + phone_no+requirement)
        # pass


        # frappe.msgprint("Form data ==> "+form_data)
        
        # field1_value = frappe.form_dict.get("field1")
        # field2_value = frappe.form_dict.get("field2")
        # field3_value = frappe.form_dict.get("csrf_token")
        # frappe.msgprint(field1)

        # Replace "YourCustomDoctype" with the actual name of your Doctype
        custom_data_doc = frappe.new_doc("Contact Form")
        custom_data_doc.name1 = name
        custom_data_doc.email = email
        custom_data_doc.phone_no = phone_no
        custom_data_doc.subject = subject
        custom_data_doc.message = message
        # frappe.msgprint("Form data ==> "+custom_data_doc)

        # Save the document to persist the changes
        custom_data_doc.insert()

        return ("Data inserted successfully.")
    except Exception as e:
        frappe.log_error(str(e))
        return "Error inserting data: " + str(e)