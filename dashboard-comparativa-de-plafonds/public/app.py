import streamlit as st
import pandas as pd

# Main entry point
def main():
    # Top layout with three columns: left spacer, centered title, and right-aligned login
    col_left, col_center, col_right = st.columns([1, 3, 1])
    with col_left:
        st.write("")  # spacer
    with col_center:
        st.markdown(
            "<h1 style='text-align: center; margin-bottom: 0;'>TELEPLAN</h1>",
            unsafe_allow_html=True
        )
    with col_right:
        st.markdown(
            "<div style='text-align: right; margin-top: 0.5rem;'><a href='#'>Login</a></div>",
            unsafe_allow_html=True
        )

    # Subtitle above uploader
    st.markdown(
        "<h3 style='text-align: center; color: gray;'>Stop overpaying, find the perfect plan</h3>",
        unsafe_allow_html=True
    )

    # File uploader component
    uploaded_file = st.file_uploader("Upload your CSV invoice", type="csv")

    # Submit button and processing logic
    if st.button("Submit"):
        if uploaded_file is not None:
            try:
                data = pd.read_csv(uploaded_file)
                st.success("File uploaded successfully!")
                st.write("Preview of your invoice data:")
                st.dataframe(data.head())
            except Exception as e:
                st.error(f"An error occurred while reading the file: {e}")
        else:
            st.error("Please upload a CSV file before submitting.")

if __name__ == "__main__":
    main()