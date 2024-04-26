import os
import streamlit as st
from pymongo import MongoClient
import hashlib
import subprocess

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Connect to MongoDB
@st.cache(allow_output_mutation=True)
def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017")  # Update with your MongoDB connection string
        streamlit_auth = client['test_database']  # Update with your database name
        user = streamlit_auth['users']  # Update with your collection name
        return user, True  # Return a tuple with the database connection and a flag indicating success
    except Exception as e:
        st.error(f"Failed to connect to MongoDB: {e}")
        return None, False  # Return None and False flag indicating failure

# Streamlit UI
st.title("Login to Dashboard")

# Get the collection and connection status
collection, connected = connect_to_mongodb()

# Print connection status
if connected:
    st.write("Connected to MongoDB successfully!")
else:
    st.error("Failed to connect to MongoDB.")

# Login form
email = st.text_input("Email:")
password = st.text_input("Password:", type="password")

if st.button("Login"):
    hashed_password = hash_password(password)
    user = collection.find_one({"email": email, "password": hashed_password})
    if user:
        st.success("Login successful!")
        st.write("Opening Homepage...")
        # Get the full path to the streamlit executable
        streamlit_path = os.path.join(os.path.dirname(st.__file__), "..", "bin", "streamlit")
        # Open the Homepage.py script using subprocess
        subprocess.Popen(["python","-m","streamlit", "run", "Homepage.py"])
    else:
        st.error("Invalid email or password. Please try again.")

# Registration button
if st.button("Register"):
    st.markdown("[Click here to register](./pages/registration.py)")
