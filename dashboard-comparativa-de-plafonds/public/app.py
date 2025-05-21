import streamlit as st
import pandas as pd

def main():
    st.title("Home Page")
    st.write("Simple UI with clean design")

    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV invoice", type="csv")

    # Submit button
    if st.button("Submit"):
        if uploaded_file is not None:
            try:
                # Read the uploaded CSV file
                data = pd.read_csv(uploaded_file)
                st.success("File uploaded successfully!")
                st.write("Preview of your invoice data:")
                st.dataframe(data.head())  # Display the first few rows of the CSV
            except Exception as e:
                st.error(f"An error occurred while reading the file: {e}")
        else:
            st.error("Please upload a CSV file before submitting.")

if __name__ == "__main__":
    main()