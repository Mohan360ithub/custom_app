import frappe
from frappe import _

def get_context(context):
    # Get the ID from the URL
    job_opening_id = frappe.form_dict.get('id')

    # Example: Retrieve job opening details by ID
    if job_opening_id:
        job_opening = frappe.get_doc("Job Opening", job_opening_id)

        # Now you can access the properties of the job_opening document
        context.designation = job_opening.get("designation")
        context.job_title = job_opening.get("job_title")
        context.description = job_opening.get("description")
        context.location = job_opening.get("location")
        # context.description = job_opening.get("description")

        # You can add more properties as needed
        # context.some_other_property = job_opening.get("some_other_property")
