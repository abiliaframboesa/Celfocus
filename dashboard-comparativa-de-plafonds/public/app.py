import streamlit as st
import pandas as pd

def main():
    # Estilo moderno e limpo
    st.markdown("""
        <style>
            .stApp {
                background-color: #f4f6f9;
                font-family: 'Segoe UI', sans-serif;
            }
            h1, h3 {
                font-weight: 600;
            }
            h1 {
                color: #0A66C2;
                font-size: 2.8em;
                margin-bottom: 0.2em;
                text-align: center;
            }
            h3 {
                color: #555;
                text-align: center;
                margin-top: -10px;
                margin-bottom: 30px;
            }
            .stButton>button {
                background-color: #0A66C2;
                color: white;
                font-size: 1.1em;
                border-radius: 8px;
                padding: 0.75em;
                width: 100%;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #004a99;
                transform: scale(1.01);
            }
            .stFileUploader {
                border: none !important;
            }
            .upload-box {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                max-width: 600px;
                margin: auto;
            }
            .login-link {
                text-align: right;
                margin-top: -30px;
                margin-bottom: 20px;
                padding-right: 20px;
            }
            .login-link a {
                color: #0A66C2;
                font-weight: bold;
                text-decoration: none;
            }
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho
    st.markdown("<h1>TELEPLAN 📱</h1>", unsafe_allow_html=True)
    st.markdown("<div class='login-link'><a href='#'>🔑 Login</a></div>", unsafe_allow_html=True)
    st.markdown("<h3>Stop overpaying, find the perfect plan</h3>", unsafe_allow_html=True)

    # Caixa centralizada para upload
    st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📄 Upload your CSV invoice", type="csv")
    submit = st.button("🚀 Submit")
    st.markdown("</div>", unsafe_allow_html=True)

    # Processamento do ficheiro
    if submit:
        if uploaded_file is not None:
            try:
                data = pd.read_csv(uploaded_file)
                st.success("✅ File uploaded successfully!")
                st.write("Preview of your invoice data:")
                st.dataframe(data.head())
            except Exception as e:
                st.error(f"❌ An error occurred while reading the file: {e}")
        else:
            st.error("⚠️ Please upload a CSV file before submitting.")

if __name__ == "__main__":
    main()
