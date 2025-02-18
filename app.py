# app.py
import streamlit as st
import home  # Assuming home.py contains the home page functions
import form  # Assuming form.py contains the form functions
import about  # Assuming about.py contains the about page functions

# Set Page Title
st.set_page_config(page_title="Track Your Care Cost", layout="wide")

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

# Sidebar Navigation
st.sidebar.title("Navigation")

# Debugging: Print current page
st.sidebar.write(f"Current Page: {st.session_state['current_page']}")

# Create buttons for each page
if st.sidebar.button("🏠 Home"):
    st.session_state['current_page'] = 'home'

if st.sidebar.button("📝 Fill Form"):
    st.session_state['current_page'] = 'form'

if st.sidebar.button("ℹ️ About"):
    st.session_state['current_page'] = 'about'

# Display the selected page based on session state
if st.session_state['current_page'] == 'home':
    home.show()
elif st.session_state['current_page'] == 'form':
    form.show()
elif st.session_state['current_page'] == 'about':
    about.show()