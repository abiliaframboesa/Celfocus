import streamlit as st

def main():
    st.title("Home Page")
    st.write("Simple UI with clean design")

    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV invoice", type="csv")

    # Submit button
    if st.button("Submit"):
        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            # Add data processing logic here
        else:
            st.error("Please upload a CSV file before submitting.")

if __name__ == "__main__":
    main()