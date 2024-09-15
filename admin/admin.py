import streamlit as st

# Default prompt
default_prompt = "You are an invoice extractor expert. We will upload an invoice image and you will answer all the questions based on the uploaded image."

# Initialize session state for prompt if it doesn't exist
if "invoice_prompt" not in st.session_state:
    st.session_state.invoice_prompt = default_prompt

st.header("Admin Page - Update Prompt")

# Display the current prompt
st.subheader("Current Prompt")
st.write(st.session_state.invoice_prompt)

# Text input for new prompt
updated_prompt = st.text_input("Enter new prompt for extracting invoice", type="default")

# Button to update the prompt
if st.button("Save Changes"):
    if updated_prompt:
        st.session_state.invoice_prompt = updated_prompt
        st.success("Prompt updated successfully!")
    else:
        st.error("Prompt cannot be empty.")
