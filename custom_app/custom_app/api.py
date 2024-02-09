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




# from frappe.utils.file_manager import save_file


# @frappe.whitelist(allow_guest=True)
# def jobapply(form_data):

#     try:
#         title = frappe.form_dict.get("title")
#         name = frappe.form_dict.get("name")
#         email = frappe.form_dict.get("email")
#         phone_no = frappe.form_dict.get("phone")
#         resume = frappe.form_dict.get("resume")
#         cover_letter = frappe.form_dict.get("cover_letter")

#         # Debugging: Print the values to check if they are correct
#         # frappe.msgprint("field1 ==> " + str(name1) + " and field2 = " + str(email))
#         # pass
#         # frappe.msgprint(form_data)
#         parsed_data = urllib.parse.parse_qs(form_data)
#         # frappe.msgprint(parsed_data)

#         # Extract values
#         # csrf_token = parsed_data.get("csrf_token", [None])[0]
#         title = parsed_data.get("title", [None])[0]
#         name = parsed_data.get("name", [None])[0]
#         email = parsed_data.get("email", [None])[0]
#         phone_no = parsed_data.get("phone", [None])[0]
#         resume = parsed_data.get("resume", [None])[0]
#         cover_letter = parsed_data.get("cover_letter", [None])[0]

#         # frappe.msgprint("field1 ==> "+name1+" and field2 = "+ email + phone_no+requirement)
#         # pass


#         # frappe.msgprint("Form data ==> "+form_data)
        
#         # field1_value = frappe.form_dict.get("field1")
#         # field2_value = frappe.form_dict.get("field2")
#         # field3_value = frappe.form_dict.get("csrf_token")
#         # frappe.msgprint(field1)

#         # Replace "YourCustomDoctype" with the actual name of your Doctype
#         custom_data_doc = frappe.new_doc("Job Applicant")
#         custom_data_doc.job_title = title
#         custom_data_doc.applicant_name = name
#         custom_data_doc.email_id = email
#         custom_data_doc.phone_number = phone_no
#         custom_data_doc.cover_letter = cover_letter
#         # custom_data_doc.resume_attachment = resume
#         # custom_data_doc.cover_letter = cover_letter
#         # frappe.msgprint("Form data ==> "+custom_data_doc)

#         # Save the document to persist the changes
#         custom_data_doc.insert()

#         # Get the saved document
#         # job_applicant = frappe.get_doc("Job Applicant", job_applicant.name)

        
#         # Check if resume file is attached in the form data
#         if "resume" in frappe.request.files:
#             uploaded_file = frappe.request.files.get("resume")
#             resume_file = save_file(uploaded_file.name, uploaded_file.content, None, None, custom_data_doc.name,decode=True)

#             # Update the resume_attachment field with the file URL
#             custom_data_doc.resume_attachment = resume_file.file_url
#             custom_data_doc.save()

#         return "Data inserted successfully."
#     except Exception as e:
#         frappe.log_error(str(e))
#         return "Error inserting data: " + str(e)



import frappe
import urllib.parse
from frappe.utils.file_manager import save_file

@frappe.whitelist(allow_guest=True)
def jobapply(form_data):
    try:
        # Parse form data
        parsed_data = urllib.parse.parse_qs(form_data)

        title = parsed_data.get("title", [None])[0]
        name = parsed_data.get("name", [None])[0]
        email = parsed_data.get("email", [None])[0]
        phone_no = parsed_data.get("phone", [None])[0]
        cover_letter = parsed_data.get("cover_letter", [None])[0]

        # Create a new Job Applicant document
        job_applicant = frappe.new_doc("Job Applicant")
        job_applicant.job_title = title
        job_applicant.applicant_name = name
        job_applicant.email_id = email
        job_applicant.phone_number = phone_no
        job_applicant.cover_letter = cover_letter

        # Save the document to persist the changes
        job_applicant.insert()

        # Check if resume file is attached in the form data
        if "resume" in frappe.request.files:
            uploaded_file = frappe.request.files.get("resume")

            # Save the uploaded file
            file_doc = save_file(uploaded_file.name, uploaded_file.content, job_applicant.doctype, job_applicant.name)

            # Update the resume_attachment field with the file URL
            job_applicant.resume_attachment = file_doc.file_url
            job_applicant.save()

            return "Data inserted successfully with file upload."
        else:
            return "Data inserted successfully without file upload."

    except Exception as e:
        frappe.log_error(str(e))
        return "Error inserting data: " + str(e)
