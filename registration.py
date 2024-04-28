import streamlit as st
from pymongo import MongoClient
import hashlib

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Connect to MongoDB
@st.cache(allow_output_mutation=True)
def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017")  # Update with your MongoDB connection string
        streamlit_auth = client['test_database']  # Update with your database name
        user_collection = streamlit_auth['users']  # Update with your collection name
        return user_collection, True  # Return the user collection and a flag indicating success
    except Exception as e:
        st.error(f"Failed to connect to MongoDB: {e}")
        return None, False  # Return None and False flag indicating failure

# Streamlit UI
st.title("Login to Dashboard")

# Get the user collection and connection status
user_collection, connected = connect_to_mongodb()

# Print connection status
if connected:
    st.write("Connected to MongoDB successfully!")
else:
    st.error("Failed to connect to MongoDB.")

# Registration form
st.header("Register")
register_email = st.text_input("Email:")
register_username = st.text_input("Username:")
register_password = st.text_input("Password:", type="password")
register_confirm_password = st.text_input("Confirm Password:", type="password")

if st.button("Register"):
    if register_password != register_confirm_password:
        st.error("Passwords do not match. Please try again.")
    else:
        hashed_password = hash_password(register_password)
        # Check if the email already exists in the database
        existing_user = user_collection.find_one({"email": register_email})
        if existing_user:
            st.error("Email already exists. Please use a different email.")
        else:
            # Insert new user into the database
            new_user = {
                "email": register_email,
                "username": register_username,
                "password": hashed_password
            }
            user_collection.insert_one(new_user)
            st.success("Registration successful!")
            st.write("You can now login to the Dashboard.")
            # Reset the app to the initial state (login page)
            st.experimental_rerun()
