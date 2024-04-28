// Get a reference to the login form
const loginForm = document.getElementById('login-form');

// Add an event listener for form submission
loginForm.addEventListener('submit', async (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the input values from the form
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // Construct the data object with email and password
  const data = {
    email: email,
    password: password
  };

  try {
    // Send a POST request to the backend server
    const response = await fetch('http://localhost:6001/api/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    // Parse the JSON response
    const responseData = await response.json();

    // Check if the login was successful
    if (response.ok) {
      // Redirect to the dashboard page
      window.location.href = 'http://localhost:8501/';
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
