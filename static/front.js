 // Function to handle the creation of list items for nested JSON
 function clearResults(){
    const jsonResultsDiv = document.getElementById('jsonResults');
    jsonResultsDiv.innerHTML = ''; // Clear any existing content
 }
 function createListItems(obj, parentElement) {
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            if (typeof obj[key] === 'object' && obj[key] !== null) {
                // Create a sublist for nested objects
                const subList = document.createElement('ul');
                const li = document.createElement('li');
                li.classList.add('list-group-item'); // Add Bootstrap class
                li.innerHTML = `<a href="#" class="list-group-item list-group-item-action list-group-item-primary">${key}:</a>`;
                li.appendChild(subList);
                parentElement.appendChild(li);
                createListItems(obj[key], subList); // Recursive call for nested objects
            } else {
                // Create list item for non-object values
                const li = document.createElement('li');
                li.classList.add('list-group-item'); // Add Bootstrap class
                li.innerHTML = `
                <a href="#" class="list-group-item list-group-item-action list-group-item-primary">${key}:</a>
                <a href="#" class="list-group-item list-group-item-action list-group-item-info">${obj[key]}</a>
              `;
                parentElement.appendChild(li);
            }
        }
    }
}

function confirmUpload() {
    // Validate file selection (you can add additional validation here)
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert('Please select a file.');
        return;
    }
    // Send an HTTP request to the specified endpoint (adjust the URL as needed)
    const formData = new FormData(document.getElementById('uploadForm'));
    fetch('/infer/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            //alert('File uploaded successfully!');
            return response.json(); // Parse the response as JSON
            // Handle any additional actions (e.g., redirect, display success message)
        } else {
            alert('Error uploading file. Please try again.');
        }
    })
    .then(jsonData => {
        const jsonResultsDiv = document.getElementById('jsonResults');
        jsonResultsDiv.innerHTML = ''; // Clear any existing content
        // Create an unordered list to display the keys and values
        const ul = document.createElement('div');
        ul.classList.add('list-group')
        createListItems(jsonData, ul); // Start the recursive function call
    
        // Append the list to the div
        jsonResultsDiv.appendChild(ul);
    })         
    .catch(error => {
        console.error('Error:', error);
    });
}