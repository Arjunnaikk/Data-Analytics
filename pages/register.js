// Get a reference to the registration form
const registrationForm = document.getElementById('registration-form');

// Add an event listener for form submission
registrationForm.addEventListener('submit', async (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the input values from the form
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // Construct the data object with name, email, and password
  const data = {
    name: name,
    email: email,
    password: password
  };

  try {
    // Send a POST request to the backend server
    const response = await fetch('http://localhost:6001/api/auth/createuser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    // Parse the JSON response
    const responseData = await response.json();

    // Check if the request was successful
    if (response.ok) {
      // Display a success message
      const successMessage = document.querySelector('.message');
      successMessage.classList.remove('hidden');
    } else {
      // Display an error message
      const errorMessage = document.querySelector('.error-message');
      errorMessage.textContent = responseData.error;
    }
  } catch (error) {
    // Handle network errors or other exceptions
    console.error('An error occurred:', error);
  }
});
