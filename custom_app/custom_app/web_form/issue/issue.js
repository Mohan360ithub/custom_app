// frappe.ready(function() {
// 	// Example: Set the session user to the user field when the page is ready
// 	var sessionUser = "{{ user }}";
// 	$('input[data-fieldname="user"]').val(sessionUser);

// 	var project_name = "{{ project_name }}";
// 	alert(project_name);
// 	$('input[data-fieldname="project"]').val(project_name);
// 	// $('select[data-fieldname="project"]').val(project_name);
// 	// $('select[data-fieldname="project"]').trigger('change');


// 	// Example: Alert the session user when the page is ready
// 	// alert("Hello, " + sessionUser + "! The page is ready.");

// 	// You can bind events, manipulate the DOM, or perform other actions here
// });


frappe.ready(function() {
    // Example: Set the session user to the user field when the page is ready
    var sessionUser = "{{ user }}";
    $('input[data-fieldname="user"]').val(sessionUser);

    var projectNames = "{{ project_name }}".split(','); // Split the project names by comma
    var customerNames = "{{ customer_name }}".split(','); // Split the project names by comma
	// alert(projectNames)
    var projectDropdown = $('select[data-fieldname="project"]');
    var customerDropdown = $('select[data-fieldname="customer"]');
	// alert(projectDropdown)
    // Clear existing options in the dropdown
    projectDropdown.empty();
    customerDropdown.empty();

    // Add each project name as an option to the dropdown
    for (var i = 0; i < projectNames.length; i++) {
        var projectName = projectNames[i].trim(); // Remove leading/trailing whitespaces
        projectDropdown.append('<option value="' + projectName + '">' + projectName + '</option>');
    }
    for (var i = 0; i < customerNames.length; i++) {
        var customerName = customerNames[i].trim(); // Remove leading/trailing whitespaces
        customerDropdown.append('<option value="' + customerName + '">' + customerName + '</option>');
    }
    // You can bind events, manipulate the DOM, or perform other actions here
});
