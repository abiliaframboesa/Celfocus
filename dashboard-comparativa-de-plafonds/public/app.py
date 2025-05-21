import streamlit as st
import pandas as pd

def main():
    # CSS para design moderno, slogan destacado e correção do file uploader
    st.markdown("""
        <style>
            .stApp {
                background-color: #f4f6f9;
                font-family: 'Segoe UI', sans-serif;
            }
            h1 {
                color: #0A66C2;
                font-size: 2.8em;
                text-align: center;
                margin-bottom: 0.2em;
                font-weight: 700;
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
                font-size: 1em;
            }
            .slogan {
                text-align: center;
                color: #333;
                font-size: 1.4em;
                font-weight: 500;
                margin-bottom: 10px;
            }
            .divider {
                width: 80px;
                height: 4px;
                background-color: #0A66C2;
                margin: 0 auto 30px auto;
                border-radius: 2px;
            }
            .upload-box {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                max-width: 600px;
                margin: auto;
            }
            .stFileUploader label {
                display: none !important;
            }
            .stFileUploader > div {
                margin-top: 0 !important;
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
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho
    st.markdown("<h1>TELEPLAN 📱</h1>", unsafe_allow_html=True)
    st.markdown("<div class='login-link'><a href='#'>🔑 Login</a></div>", unsafe_allow_html=True)

    # Slogan com destaque visual
    st.markdown("<div class='slogan'>Stop overpaying, find the perfect plan</div>", unsafe_allow_html=True)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Caixa de upload centralizada e com estilo
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
